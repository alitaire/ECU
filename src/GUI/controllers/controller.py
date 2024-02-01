'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''

from models import Model
from views import MainWindow


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

    def leds_blink(self):
        self.model.leds_blink()

    def incr(self):
        self.model.incr("Speed", 10)

    def update_label(self, text):
        self.model.update_label(text)

    def callbacks(args):
        pass
