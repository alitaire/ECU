'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


from src.GUI.models.model import Model
from src.GUI.views.mainapplication import MainWindow


class Controller:
    '''
    classdocs
    '''

    def __init__(self):
        self.model = Model()
        self.view = MainWindow(controller=self, model=self.model)

        self.model.attach(self.view)


    def main(self):
        print("In main controller")
        self.view.mainloop()

    def on_button_click(self, caption):
        result = self.model.calculate(caption)
        self.view.value_var.set(result)
