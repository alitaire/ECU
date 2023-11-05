'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


class Model:
    '''
    classdocs
    '''

    def __init__(self):
        self.value = ''


    def calculate(self, caption):
        print(f'calculating for {caption}')
        if caption == 'C':
            self.value = ''
        elif isinstance(caption, int):
            self.value += str(caption)

        return self.value