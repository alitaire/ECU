import tkinter
import os
from tkinter.filedialog import askopenfilename

from reliavision.gui.views.common import ViewBase
from reliavision.gui.views.tooltips import CreateToolTip



class ConfigWindow(ViewBase, tkinter.Frame):
    def __init__(self, model, controller, master, width=30):
        tkinter.Frame.__init__(self, master)
        ViewBase.__init__(
            self, model, controller, "ConfigWindow", parent=master, width=width
        )

    def _setupView_notAvail(self, model, controller, **kwargs):
        self.__window = self.winfo_toplevel()
        self.__window.title("Config")

        text = [
            " ",
            "    This function is currently not available :(    ",
            " ",
        ]

        for i, text_label in enumerate(text):
            tkinter.Label(self.__window, text=text_label).grid(row=i, column=0, sticky="nw")

    def _setupView(self, model, controller, **kwargs):
        width = kwargs["width"]
        entryWidth = 50
        buttonWidth = 10
        self.__window = self.winfo_toplevel()
        self.__window.title("Config")

        self.__sections = ["skillbridge", "spectre"]

        self.__skill_labels = (
            "Library",
            "Cell name",
            "Layout view type",
            "Schematic view type",
        )
        self.__spectre_labels = (
            "Devices",
            "Netlist",
            "Age",
            "Age levels",
            "Aging model",
            "URI library",
            "Reliability data",
            "PDK path",
            "PDK replace",
        )

        self._ttpDict = {
            "Library": "Name of Virtuoso library ",
            "Cell name": "Name of Virtuoso cell",
            "Layout view type": "typically 'layout'",
            "Schematic view type": "typically 'schematic'",
            "Devices": "Devices to degrade separated by ',', e.g., 'ne5mod,pe5mod'",
            "Netlist": "Simulation netlist (*.scs) written by ADE",
            "Age": "target age in years, e.g. '10y'",
            "Age levels": "typically '303,304'",
            "Aging model": "typically 'agemodel'",
            "URI library": "Shared object (*.so) file which is included in Spectre (absolute path)",
            "Reliability data": "XML (*.xml) file which contains ageing information for Spectre (absolute path)",
            "PDK path": "Path to modified models (absolute path)",
            "PDK replace": "(absolute paths)",
            "Original mos.scs": "mos.scs file installed in PDK (absolute paths)",
            "Modified mos.scs": "mos.scs file linking to modified models (absolute paths)",
        }

        self.mapDict = {
            "Library": "library",
            "Cell name": "cell_name",
            "Layout view type": "view_type_layout",
            "Schematic view type": "view_type_schematic",
            "Devices": "devices",
            "Netlist": "netlist",
            "Age": "age",
            "Age levels": "agelevels",
            "Aging model": "agemodel_name",
            "URI library": "uri_lib",
            "Reliability data": "xml_file",
            "PDK path": "pdk_path",
            "PDK replace": "pdk_replace",
            "Original mos.scs": "",
            "Modified mos.scs": "",
        }

        self.defaults = {
            "library": "virtuoso_library_name",
            "cell_name": "virtuoso_cell_name",
            "view_type_layout": "layout",
            "view_type_schematic": "schematic",
            "id": "reliavision",
            "devices": "ne5mod,pe5mod",
            "netlist": "input.scs",
            "age": "10y",
            "agelevels": "303,304",
            "agemodel_name": "agemodel",
            "uri_lib": os.getcwd() + "/liburi_xfab.so",
            "xml_file": os.getcwd() + "/xt018_reliability_data.xml",
            "pdk_path": "",
            "pdk_replace": "",
            "pdk_add": "",
            "regex": "(\w+[^mod])",
            "": "",
        }

        self._configure_input_fields(entryWidth, buttonWidth)

        self.__saveButton = tkinter.Button(
            self.__window, text="Save and open config file", width=20
        )
        self.__saveButton.pack(side=tkinter.LEFT, padx=10, pady=10)

        self.__quitButton = tkinter.Button(
            self.__window, text="Quit", width=buttonWidth
        )
        self.__quitButton.pack(side=tkinter.LEFT, padx=10, pady=10)

    def _configure_input_fields(self, entryWidth, buttonWidth):
        self.__entries = {}

        lab, row = self._setup_label("Skillbridge section")
        for label in self.__skill_labels:
            ent, but = self._setup_entry(label, entryWidth=entryWidth)
            self.__entries[label] = (ent, but)

        lab, row = self._setup_label("Spectre section")
        for label in self.__spectre_labels:
            if label in ["Netlist", "Reliability data", "URI library", "PDK path"]:
                ent, but = self._setup_button(label, entryWidth=entryWidth, buttonWidth=buttonWidth)
                self.__entries[label] = (ent, but)
            elif label == "PDK replace":
                lab, row = self._setup_label(label)
                ent, but = self._setup_button("Original mos.scs", entryWidth, buttonWidth)
                self.__entries["Original mos.scs"] = (ent, but)
                ent, but = self._setup_button("Modified mos.scs", entryWidth, buttonWidth)
                self.__entries["Modified mos.scs"] = (ent, but)
            else:
                ent, but = self._setup_entry(label, entryWidth=entryWidth)
                self.__entries[label] = (ent, but)

    def _get_file(self, filetypes, entry):
        initialdir = os.getenv("VIRTUOSO_PATH")
        filepath = askopenfilename(filetypes=filetypes, initialdir=initialdir)
        if not filepath:
            return
        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, filepath)

    def _setup_label(self, label):
        row = tkinter.Frame(self.__window)
        lab = tkinter.Label(row, width=20, text=(label + ":"), anchor="w")
        row.pack(side=tkinter.TOP, fill=tkinter.X, padx=2, pady=2)
        lab.pack(side=tkinter.LEFT)

        return lab, row

    def _setup_entry(self, label, entryWidth):

        lab, row = self._setup_label(label)

        ent = tkinter.Entry(row, width=entryWidth)
        ent.pack(side=tkinter.LEFT)
        CreateToolTip(ent, self._ttpDict[label])

        but = None

        default = self.defaults[self.mapDict[label]]
        ent.insert(tkinter.END, default)

        return ent, but

    def _setup_button(self, label, entryWidth, buttonWidth):

        lab, row = self._setup_label(label)

        ent = tkinter.Entry(row, width=entryWidth)
        but = tkinter.Button(
            row,
            text="Browse",
            command=lambda: self._get_file(
                filetypes=[("All Files", "*.*")], entry=ent
            ),
            width=buttonWidth,
        )

        ent.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.X)
        but.pack(side=tkinter.LEFT, padx=5)
        CreateToolTip(ent, self._ttpDict[label])
        CreateToolTip(but, self._ttpDict[label])

        default = self.defaults[self.mapDict[label]]
        ent.insert(tkinter.END, default)

        return ent, but

    def setup_controller(self):
        self.__quitButton.configure(
            command=self._controller.get_callback("quit_window", view=self)
        )

        self.__saveButton.configure(
            command=self._controller.get_callback(
                "save_config",
                # entries_needed=self.__entries_needed,
                entries=self.__entries,
                view=self,
            )
        )

    def update(self):
        pass

# def _setupView_2(self, model, controller, **kwargs):
    #     width = kwargs["width"]
    #     entryWidth = 50
    #     buttonWidth = 10
    #     self.__window = self.winfo_toplevel()
    #     self.__window.title("Config")
    #
    #     self.__labels = (
    #         "Netlist",
    #         "Script",
    #         "Output file",
    #         "Time series",
    #         "Age",
    #         "Stress time",
    #         "Schematic",
    #         "Layout",
    #         "bboxes",
    #         "svg title",
    #     )
    #
    #     self._ttpDict = {
    #         "Netlist": "Enter or choose netlist file (*.scs) for simulation with spectre.",
    #         "Script": "Enter or choose script (*.ssh) to run simulation.",
    #         "Output file": "spectre output, e.g. degradation.txt",
    #         "Time series": "spectre output, e.g. 'time_series.json'",
    #         "Age": "target age in years",
    #         "Stress time": "e.g. 1000n",
    #         "Layout": "layout design (*.gds)",
    #         "bboxes": "skill output, e.g. 'transistor_bboxes.txt'",
    #         "svg title": "title",
    #         "Schematic": "Schematic file, e.g. 'center.xml'.",
    #     }
    #
    #     self.__entries_needed = [
    #         "Netlist",
    #         "Script",
    #         "Age",
    #         "Stress time",
    #         "Output file",
    #         "Time series",
    #         "Schematic",
    #         "bboxes",
    #         "Layout",
    #         "svg title",
    #     ]
    #
    #     self._configure_input_fields(entryWidth, buttonWidth)
    #
    #     self.__saveButton = tkinter.Button(
    #         self.__window, text="Save config file", width=15
    #     )
    #     self.__saveButton.pack(side=tkinter.LEFT, padx=10, pady=10)
    #
    #     self.__quitButton = tkinter.Button(
    #         self.__window, text="Quit", width=buttonWidth
    #     )
    #     self.__quitButton.pack(side=tkinter.LEFT, padx=10, pady=10)

    # def _configure_input_fields(self, entryWidth, buttonWidth):
    #     self.__entries = {}
    #
    #     for label in self.__labels:
    #
    #         if label == "Age":
    #             ent, but = self._setup_age(label)
    #
    #         elif label == "Stress time":
    #
    #             ent, but = self._setup_stress_time(label)
    #
    #         elif label == "svg title":
    #
    #             ent, but = self._setup_svg_title(label)
    #
    #         else:
    #
    #             ent, but = self._setup_button(
    #                 label, entryWidth=entryWidth, buttonWidth=buttonWidth
    #             )
    #
    #         self.__entries[label] = (ent, but)

    # def _setup_age(self, label):
    #
    #     lab, row = self._setup_label(label)
    #
    #     ent = tkinter.Entry(row, width=8)
    #     unt = tkinter.Label(row, text=" ys")
    #     ent.pack(side=tkinter.LEFT)
    #     unt.pack(side=tkinter.LEFT)
    #     CreateToolTip(ent, self._ttpDict[label])
    #
    #     but = None
    #
    #     return ent, but

    # def _setup_stress_time(self, label):
    #     lab, row = self._setup_label(label)
    #
    #     ent = tkinter.Entry(row, width=8)
    #     unt = tkinter.Label(row, text=" s")
    #     spacer = tkinter.Label(self.__window, text=" ")
    #     ent.pack(side=tkinter.LEFT)
    #     unt.pack(side=tkinter.LEFT)
    #     spacer.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.X)
    #     CreateToolTip(ent, self._ttpDict[label])
    #
    #     but = None
    #
    #     return ent, but

    # def _setup_svg_title(self, label, width=50):
    #
    #     lab, row = self._setup_label(label)
    #
    #     ent = tkinter.Entry(row, width=width)
    #     spacer = tkinter.Label(self.__window, text=" ")
    #     ent.pack(side=tkinter.LEFT)
    #     spacer.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.X)
    #     CreateToolTip(ent, self._ttpDict[label])
    #
    #     but = None
    #
    #     return ent, but
