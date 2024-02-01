import tkinter

from reliavision.config import defs
from reliavision.gui.views.common import ViewBase
from reliavision.technology_parser.technology_parser import parse_technology


class TechnologyWindow(ViewBase, tkinter.Frame):
    def __init__(self, model, controller, master):
        tkinter.Frame.__init__(self, master)
        ViewBase.__init__(self, model, controller, "technology")

    def _setupView(self, model, controller, **kwargs):
        window = self.winfo_toplevel()

        # text = [
        #     "nmos: HCI (IDLIN, IDSAT)",
        #     "pmos: NBTI (VTH)",
        #     "pmos: NBTI (VTH)",
        #     "pmos5: NBTI (VTH); HCI (IDSAT)",
        #     "nmos_hv: HCI (IDLIN, IDSAT, IDANALOG)",
        #     "pmos_hv: NBTI (VTH)",
        #     "nmos_special: HCI (Sthslope)",
        # ]

        config = model._tkModel__config_file
        if config:
            degradation_lib = config[defs.Spectre.section_name][
                defs.Spectre.xml
            ]  # TODO: Ist das richtig?
            # degradation_lib = "../xml_converter/degradation.xml"

            text = parse_technology(degradation_lib)
        else:
            text = [
                " ",
                "    No technology information available.    ",
                "    Please create and/or load config file.    ",
                " ",
            ]

        for i, text_label in enumerate(text):
            tkinter.Label(window, text=text_label).grid(row=i, column=0, sticky="nw")

        self.okButton = tkinter.Button(window, text="OK", width=25)

        self.okButton.grid(row=len(text), column=0, sticky="swe")

        window.title("Technology")

    def update(self):
        print(self._name)
        self._state = self._model.getState()

    def setup_controller(self):
        self.okButton.configure(
            command=self._controller.get_callback("quit_window", view=self)
        )
