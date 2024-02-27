'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''

from models import Model
from views import MainWindow
from communication import UartListener


class Controller:
    '''
    classdocs
    '''

    def __init__(self):
        self.model = Model()
        self.view = MainWindow(controller=self, model=self.model)
        self.model.attach(self.view)
        self.uart_listener = None


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

    def connect_uart(self, port, baudrate):
        if self.uart_listener is None:
            self.uart_listener = UartListener(self, port, baudrate)
            self.uart_listener.start()
            self.model.update_connection(True)

    def disconnect_uart(self):
        if self.uart_listener:
            self.uart_listener.stop()
            self.uart_listener = None
            self.model.update_connection(False)

    def callbacks(args):
        pass
