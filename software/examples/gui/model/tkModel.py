import configparser
from io import BytesIO
from typing import List, Tuple

import numpy as np

from reliavision import bbox, cadence, timeSeries
from reliavision.config import defs, section_checkers
from reliavision.dtypes import SchematicInfo, Spectre
from reliavision.gds.gdsSettings import gdsSettingsLoader
from reliavision.gui.model.common import ModelBaseClass
from reliavision.layout import Layout
from reliavision.skill.gds.gdsLoader import gdsLoader
from reliavision.skill.layout.deviceLoader import deviceLoader
from reliavision.skill.ops import alter_skillbridge_socket_name, check_vectors
from reliavision.skill.schematic.schematicLoader import load_schematic_devices
from reliavision.skill.spectre.spectreLoader import spectreLoader


class tkModel(ModelBaseClass):
    def __init__(self) -> None:
        super().__init__()

        self.__max_foms = {}
        self.__time_series_data = []
        self.__schematic_images = []
        self.__schematic_metadatas = []
        self.__devices_schematic = []
        self.__layout = None
        self.__config_file = None

    def run_spectre(self):

        # GET DATA FROM SPECTRE
        # if section_checkers.check_if_local(self.__config_file):
        #     # local
        #     self.__time_series_data = self.__init_time_series(self.__config_file)
        #
        #     self.__spectre = cadence.spectre.init_spectre_devices_from_file(
        #         filename=self.__config_file[defs.Local.section_name][defs.Local.spectre]
        #     )
        #
        # else:
        #     run_simulation_default()
        #     self.__time_series_data, self.__spectre = read_logger_output_test()

        self.__time_series_data, self.__spectre = spectreLoader(self.__config_file)

        # TIME SERIES
        self._state["time_series"] = self.__set_time_series_state(
            self.__time_series_data
        )

        # UPDATE SCHEMATIC
        self.__devices_schematic = load_schematic_devices(self.__config_file)

        assert len(self.__devices_schematic) > 0

        imageIOs, metadatas = bbox.draw_foms_bboxes(
            self.__devices_schematic, self.__spectre
        )

        schematic_metadatas = [
            "{}_".format(metadata["fom"])
            + (
                "{}_".format(metadata["instance"])
                if metadata["instance"] != "none"
                else ""
            )
            + "{}_{}".format(metadata["cell"], metadata["lib"])
            for metadata in metadatas
        ]

        self._state["schematic"] = {
            "image": imageIOs[0],
            "metadata": schematic_metadatas,
        }

        self.__schematic_images = imageIOs
        self.__schematic_metadatas = schematic_metadatas

        # config_user = {
        #                 "regex": "(.*?).([^.]+)_(\d+)_(\d+)$",
        #                 "library": "forFabio",
        #                 "cell_name": "ZEOTA_mpadc",
        #                 "view_type": "layout",
        #                 "id": "reliavision"
        #                 }

        # UPDATE LAYOUT
        # config_user = {
        #     "regex": "(.*?).([^.]+)_(\d+)_(\d+)$",
        #     "bboxes": "./input_files/ZEOTA/skill/transistor_bboxes.txt",
        #     "gds_design": "./input_files/ZEOTA/layout/ZEOTA_mpadc.gds",
        # }

        # if section_checkers.check_if_layout(self.__config_file):
        #     devices_layout = deviceLoader(self.__config_file)
        #     gds_file = gdsLoader(self.__config_file)
        #
        #     self.__layout.update(gds_file, devices_layout, self.__spectre)
        #
        #     self._state["layoutviewer"] = {}
        #     self._state["layoutviewer"]["cells"] = self.__layout.get_cells()
        #     self._state["layoutviewer"]["colors"] = self.__layout.get_colors()
        #     self._state["layoutviewer"][
        #         "hidden_types"
        #     ] = self.__layout.get_hidden_types()
        #     self._state["layoutviewer"]["patterns"] = self.__layout.get_patterns()

        self._state["max_foms"] = self.__get_max_foms(
            self.__spectre, self.__devices_schematic
        )

        self.notify()
        self.state_remove("schematic", "time_series", "max_foms")

        # if section_checkers.check_if_layout(self.__config_file):
        #     self.state_remove("layoutviewer")

        print("ageing update complete")

    def iv_plot(self, name, device, xvar, yvar):
        x, y = self.get_data_from_time_series(device, xvar, yvar)

        self._state[name] = {
            "x": x,
            "y": y,
            "label": device,
            "xlabel": xvar,
            "ylabel": yvar,
        }
        self.notify()
        self.state_remove(name)

    def get_data_from_time_series(self, device, xvar, yvar):
        xvar = timeSeries.plot_type_to_time_series_key(xvar)
        yvar = timeSeries.plot_type_to_time_series_key(yvar)

        x = 0
        y = 0

        for dev_type in list(self.__time_series_data.keys()):
            if device in self.__time_series_data[dev_type].keys():
                device_data = self.__time_series_data[dev_type][device]
                x = device_data[xvar]
                y = device_data[yvar]

        return x, y

    def get_device_aging(self, fom_name: str, name: str = "unknown") -> None:
        # print(fom_name)
        # print(name)

        self._state[name] = self.__max_foms[fom_name]
        self.notify()
        self.state_remove(name)

    # def update_plot(self, name: str) -> None:
    #     x = np.linspace(0, np.pi * 2, 201)
    #     y = np.sin(x) + 0.1 * np.random.random(len(x))
    #
    #     self._state[name] = {"data": {"x": x, "y": y}}
    #     self.notify()

    def state_remove(self, *args: str) -> None:
        for arg in args:
            self._state.pop(arg)

    def update_schematic(self, schematic_name: str) -> None:

        self._state["schematic"] = {
            "image": self.__schematic_images[
                self.__schematic_metadatas.index(schematic_name)
            ]
        }
        self.notify()
        self.state_remove("schematic")

    def __init_schematic(
        self,
    ) -> Tuple[List[BytesIO], List[str], List[SchematicInfo], dict]:

        self.__devices_schematic = load_schematic_devices(self.__config_file)

        # spectre = cadence.spectre.init_spectre_devices_from_file(
        #     filename=config_user["spectre"]["output_file"]
        # )

        # imageIOs, metadatas = bbox.draw_foms_bboxes(devices_schematic, spectre)

        imageIOs = []
        schematic_metadatas = []

        for device_schematic in self.__devices_schematic:
            imageIOs.append(device_schematic.get_image_data())
            schematic_metadatas.append(
                (
                    "{}".format(device_schematic.instance)
                    if device_schematic.instance != "none"
                    else ""
                )
                + "{}_{}".format(
                    device_schematic.cell,
                    device_schematic.lib,
                )
            )

        # schematic_metadatas = [
        #     "{}_{}_{}_{}".format(
        #         metadata["fom"], metadata["instance"], metadata["cell"], metadata["lib"]
        #     )
        #     for metadata in metadatas
        # ]

        state = {
            "image": imageIOs[0],
            "metadata": schematic_metadatas,
        }

        return imageIOs, schematic_metadatas, self.__devices_schematic, state

    def __set_time_series_state(self, data_time_series: dict) -> dict:
        devices = timeSeries.get_devices(data_time_series)

        state = {
            "xtypes": timeSeries.get_plot_x(),
            "ytypes": timeSeries.get_plot_y(),
            "xinit": timeSeries.PlotTypes.time,
            "yinit": timeSeries.PlotTypes.vgs,
            "devices": devices,
        }

        x, y = self.get_data_from_time_series(
            devices[0],
            state["xinit"],
            state["yinit"],
        )

        # set init data
        state["init_data"] = {
            "x": x,
            "y": y,
            "label": devices[0],
            "xlabel": state["xinit"],
            "ylabel": state["yinit"],
        }

        return state

    def __init_time_series(self, config_user: dict) -> dict:

        data_time_series = timeSeries.init_time_series_from_json(
            config_user[defs.Local.section_name][defs.Local.time_series]
        )

        self.__time_series_data = data_time_series

        return self.__set_time_series_state(data_time_series)

    def __get_max_foms(
        self,
        spectre: Spectre,
        devices_schematic: List[SchematicInfo],
        n_devices: int = 40,
    ) -> dict:

        devices_masked = []

        for device_schematic in devices_schematic:
            mask = cadence.device.get_device_indices(device_schematic, spectre.devices)
            devices_masked += [spectre.devices[i] for i in mask]

        for fom_name in spectre.fom_names:

            devices_sorted = sorted(
                devices_masked, key=lambda device: device.get_fom_value(fom_name)
            )[-n_devices:]

            self.__max_foms[fom_name] = {
                "devices": [device.name for device in devices_sorted],
                "values": [device.get_fom_value(fom_name) for device in devices_sorted],
                "fom": fom_name,
            }

        state = {
            "fom": [*spectre.fom_names],
            "data": self.__max_foms[spectre.fom_names[0]],
        }

        return state

    def __init_layout(self, config_user: dict) -> Layout:
        state = {}

        gds_file = gdsLoader(self.__config_file)
        hidden_types, color_map = gdsSettingsLoader(config_user)

        layout = Layout(
            gds_design=gds_file,
            hidden_types=hidden_types,
            color_map=color_map,
        )

        state["cells"] = layout.get_cells()
        state["colors"] = layout.get_colors()
        state["hidden_types"] = layout.get_hidden_types()
        state["patterns"] = layout.get_patterns()

        return layout

    def init_from_config_file(self, filename, name):
        self._state[name] = {"filename": filename}

        config_user = configparser.ConfigParser()
        config_user.read(filename)

        config_user = alter_skillbridge_socket_name(config_user)
        check_vectors(config_user)

        self.__config_file = config_user

        (
            self.__schematic_images,
            self.__schematic_metadatas,
            devices_schematic,
            self._state["schematic"],
        ) = self.__init_schematic()

        if "layout" in self.__config_file:
            self.__layout = self.__init_layout(self.__config_file)

            self._state["layoutviewer"] = {}
            self._state["layoutviewer"]["cells"] = self.__layout.get_cells()
            self._state["layoutviewer"]["colors"] = self.__layout.get_colors()
            self._state["layoutviewer"][
                "hidden_types"
            ] = self.__layout.get_hidden_types()
            self._state["layoutviewer"]["patterns"] = self.__layout.get_patterns()

        self.notify()
        self.state_remove("schematic")

        if "layout" in config_user:
            self.state_remove("layoutviewer")

    def generate_config_file(self, config_window, entries, file):

        _mapDict_inv = {v: k for (k, v) in config_window.mapDict.items()}
        _defaults = config_window.defaults

        # generate text
        text = []
        sections = [defs.SKILL, defs.Spectre]
        for sec in sections:
            text.append(f"[{sec.section_name}]")
            for key in sec.keywords:
                if not key == "pdk_replace":
                    if key in _mapDict_inv.keys() and not entries[_mapDict_inv[key]][0].get() == "":
                        label = _mapDict_inv[key]
                        text.append(key + f"={entries[label][0].get()}")
                    else:
                        text.append(key + f"={_defaults[key]}")
                else:
                    label1 = "Original mos.scs"
                    label2 = "Modified mos.scs"
                    text.append(key + f"={entries[label1][0].get()},{entries[label2][0].get()}")
            text.append("")

        config_text = "\n".join(text)

        # response?
        self._state["config_text"] = config_text

        with file:
            file.write(config_text)

        self.notify()
        self.state_remove("config_text")

        # def generate_config_file(self, entries, entries_needed, file):
        #
        # config_strings = []
        # for lab in entries_needed:
        #     try:
        #         config_strings.append(entries[lab][0].get())
        #     except KeyError:
        #         print(f"Warning: {lab} not found in entries from config window")
        #         config_strings.append("")
        #         exit(1)
        #
        # (
        #     netlist,
        #     script,
        #     age,
        #     stress_time,
        #     output_file,
        #     time_series,
        #     schematic,
        #     bboxes,
        #     gds_design,
        #     svg_title,
        # ) = config_strings
        #
        # # generate text
        # config_text = f"[spectre]\n\
        #     netlist={netlist}\n\
        #     script={script}\n\
        #     age={age}y\n\
        #     stress_time={stress_time}\n\
        #     output_file={output_file}\n\
        #     time_series={time_series}\n\
        #     \n\
        #     [schematic]\n\
        #     config={schematic}\n\
        #     \n\
        #     [layout]\n\
        #     bboxes={bboxes}\n\
        #     gds_design={gds_design}\n\
        #     svg_title={svg_title}"
        #
        # # response?
        # self._state["config_text"] = config_text
        #
        # with file:
        #     file.write(config_text)
        #
        # self.notify()
        # self.state_remove("config_text")

        # _mapDict_inv = {
        #     "library": "Library",
        #     "cell_name": "Cell name",
        #     "view_type_layout": "Layout view type",
        #     "view_type_schematic": "Schematic view type",
        #     "devices": "Devices",
        #     "netlist": "Netlist",
        #     "age": "Age",
        #     "agelevels": "Age levels",
        #     "agemodel_name": "Aging model",
        #     "uri_lib": "URI library",
        #     "xml_file": "Reliability data",
        #     "pdk_path": "PDK path",
        #     "pdk_replace": "PDK replace",
        #     "1": "Original PDK",
        #     "2": "Modified PDK",
        # }
