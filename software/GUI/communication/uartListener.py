import threading
import serial
import time

class UartListener(threading.Thread):
    def __init__(self, controller, port="COM3", baudrate="115200"):
        super().__init__()
        self._controller = controller
        self.port = port
        self.baudrate = baudrate
        self.connected = False


    def run(self):
        ser = serial.Serial(self.port, self.baudrate)
        self.connected = True
        print(f"UART port : {self.port} started")
        while self.connected:
            data = ser.readline().decode('utf-8')
            # Mettez à jour l'interface graphique avec les données reçues
            self._controller.update_label(data)
        ser.close()
        print(f"UART port : {self.port} stopped")


    def stop(self):
        if self.connected:
            self.connected = False