import tkinter

from PIL import Image, ImageTk

from reliavision.gui.views.common import ViewBase


class Schematic(ViewBase, tkinter.Frame):
    def __init__(self, model, controller, parent=None, width=800, height=700):
        tkinter.Frame.__init__(self, parent)
        ViewBase.__init__(
            self,
            model,
            controller,
            "schematic",
            parent=parent,
            width=width,
            height=height,
        )

        self._choices_menu = None

    def _setupView(self, model, controller, **kwargs):
        self.__parent = kwargs["parent"]
        self.__width = kwargs["width"]
        self.__height = kwargs["height"]

        self.__parent.grid_columnconfigure(10)

    def _set_image(
        self,
        filepath,
        row=1,
        column=0,
        pady=5,
        padx=0,
    ):
        # print("creating logo")
        img = Image.open(filepath)

        scale = img.height / img.width

        # Resize the Image using resize method
        if scale < 1:
            resized_image = img.resize(
                (int(self.__width), int(scale * self.__width)), Image.Resampling.LANCZOS
            )
        else:
            resized_image = img.resize(
                (int(self.__height / scale), int(self.__height)), Image.Resampling.LANCZOS
            )
        self.img = ImageTk.PhotoImage(resized_image)

        self.image_label = tkinter.Label(self.__parent, image=self.img)
        self.image_label.grid(row=row, column=column, sticky="nw", pady=pady, padx=padx)

    def __setup_buttons(self, choices):

        self._var_choices = tkinter.StringVar(self.__parent)
        self._var_choices.set(choices[0])

        if self._choices_menu is not None:
            self._choices_menu.destroy()

        self._choices_menu = tkinter.OptionMenu(
            self.__parent,
            self._var_choices,
            *choices,
            command=self._controller.get_callback(
                "update_schematic", schematic_name=self._var_choices
            )
        )

        self._choices_menu.grid(row=0, column=0, sticky="nw", pady=5)

    def setup_controller(self):
        pass

    def update(self):
        # pass
        state = self._model.getState()

        if "schematic" in list(state.keys()):
            if "metadata" in state["schematic"]:
                self.__setup_buttons(state["schematic"]["metadata"])

            if "image" in state["schematic"]:
                self._set_image(state["schematic"]["image"], padx=50)
