'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


import tkinter as tk
from views import ViewInterface

class Injecteur:
    '''
    classdocs
    '''

    def __init__(self, parent, model, controller, name, color="orange", size=30, border=2):
        super().__init__(parent, width=size, height=size)

        # Chargement de l'image
        image_pillow = Image.open("img/injector.png")
        image_pillow = image_pillow.resize((70, 150), Image.ANTIALIAS)
        self.inj_img = ImageTk.PhotoImage(image_pillow)

        # Injecteur 1
        inj1_text = tk.Label(self.outlayout, text="Injecteur 1")
        inj1_img = tk.Label(self.outlayout, image=self.inj_img)
        inj1_voy = Voyant(self.outlayout, self._model, self._controller, "Injector-1", size=35)


        inj1_text.pack(padx=5, pady=5)
        inj1_img.pack(padx=5, pady=5)
        inj1_voy.pack(padx=5, pady=5)