import re
import functools

import tkinter
import tkinter.ttk as ttk

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

        self._choices_tree = None

    def _setupView(self, model, controller, **kwargs):
        self.__parent = kwargs["parent"]
        self.__width = kwargs["width"]
        self.__height = kwargs["height"]

        self.__parent.grid_columnconfigure(10)

    def _set_image(
        self,
        filepath,
        row=0,
        column=1,
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


    def __setup_tree(self, choices):

        if self._choices_tree is not None:
            self._choices_tree.destroy()

        self._choices_tree = ttk.Treeview(self.__parent)
        self._choices_tree.column("#0", width=200, minwidth=50, anchor=tkinter.W)
        self._choices_tree.heading("#0", text="EXPLORER", anchor=tkinter.W)
        
        for idx, choice in enumerate(choices):
            if re.match("I\d+", choice):
                if idx > 0:
                    self._choices_tree.insert(parent=f"{idx_p}", index="end", iid=idx, text=choice)
                else:
                    idx_p = idx
                    self._choices_tree.insert(parent="", index="end", iid=idx, text=choice)
            else:
                idx_p = idx
                self._choices_tree.insert(parent="", index="end", iid=idx, text=choice)
        
        self._choices_tree.bind("<Double-1>", lambda event: self.on_double_click(event))
        self._choices_tree.grid(row=0, rowspan=2, column=0, sticky="nw", pady=5, padx=5)
        
    def setup_controller(self):
        pass
    
    def on_double_click(self, event):
        item = self._choices_tree.selection()[0]
        scheme_name = self._choices_tree.item(item, "text")
        self._controller.update_schematic2(scheme_name)

    def update(self):
        # pass
        state = self._model.getState()

        if "schematic" in list(state.keys()):
            if "metadata" in state["schematic"]:
                self.__setup_tree(state["schematic"]["metadata"])

            if "image" in state["schematic"]:
                self._set_image(state["schematic"]["image"], padx=50)
