'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


from src.GUI.models.model import Model
from src.GUI.views.view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)


    def main(self):
        print("In main controller")
        self.view.main()
