import threading
import time

class UartListener(threading.Thread):
    def __init__(self, controller, port="COM3", baudrate="115200"):
        super().__init__()
        self._controller = controller
        self.port = port
        self.baudrate = baudrate

    def run(self):
        import serial

        ser = serial.Serial(self.port, self.baudrate)
        try:
            while True:
                data = ser.readline().decode('utf-8')
                # Mettez à jour l'interface graphique avec les données reçues
                self._controller.update_label(data)
        except KeyboardInterrupt:
            ser.close()