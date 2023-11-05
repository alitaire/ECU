'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


from src.GUI.models.model import Model
from src.GUI.views.view import View


class Controller:
    '''
    classdocs
    '''

    def __init__(self):
        self.model = Model()
        self.view = View(self)


    def main(self):
        print("In main controller")
        self.view.main()

    def on_button_click(self, caption):
        result = self.model.calculate(caption)
        self.view.value_var.set(result)
