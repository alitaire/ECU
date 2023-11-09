'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


from src.GUI.models.interface import ModelInterface


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
        return self.value