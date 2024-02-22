'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


from models import ModelInterface


class Model(ModelInterface):
    '''
    classdocs
    '''

    def __init__(self):
        super().__init__()
        self.value = ''


    def calculate(self, caption):
        print(f'calculating for {caption}')
        if caption == 'C':
            self.value = ''
        elif isinstance(caption, int):
            self.value += str(caption)
        self.setState("View", "Calculate")
        self.notify()
        self.delState("View")
        return self.value

    def incr(self, cpt, value):
        self.setState(cpt, value)
        self.notify()
        self.delState(cpt)

    def leds_blink(self):
        self.setState("Injector-1", "blink")
        self.notify()
        self.delState("Injector-1")

    def update_label(self, text):
        self.setState("Test", text)
        self.notify()
        self.delState("Test")

    def update_connection(self, status):
        if status:
            txt = "Connected"
        else:
            txt = "Disconnected"
        self.setState("Com", txt)
        self.notify()
        self.delState("Com")
