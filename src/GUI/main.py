'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''

import platform

from controllers import Controller
from communication import UartListener

if __name__ == '__main__':
    controller = Controller()


    system_info = platform.system()

    if system_info == 'Windows':
        print("Le système d'exploitation est Windows.")
        port = 'COM3'
    elif system_info == 'Linux':
        print("Le système d'exploitation est Linux.")
        port = '/dev/ttyUSB0'
    else:
        print(f"Le système d'exploitation est {system_info}.")

    uart_listener = UartListener(controller, port, "115200")
    uart_listener.start()

    controller.main()
