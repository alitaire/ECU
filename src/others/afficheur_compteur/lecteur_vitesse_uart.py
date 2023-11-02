import serial
import time  # Ajout de l'importation du module time
import afficheur
# ... Définir les paramètres UART et conversion_factor comme vous l'avez fait
port = "COM6"
baud_rate = 115200
conversion_factor = 2

speedWidget = afficheur.SpeedWidget()  # Créez une instance du widget SpeedWidget
while True:
    pass
'''
try:
    ser = serial.Serial(port, baud_rate, timeout=1)
    speedWidget = afficheur.SpeedWidget()  # Créez une instance du widget SpeedWidget

    while True:
        data = ser.readline().decode('utf-8').strip()
        if data:
            speeds_kmph = [float(speed) for speed in data.split()]  # Split data by spaces
            for speed_kmph in speeds_kmph:
                speed_analog = speed_kmph * conversion_factor
                speedWidget.set_speed(speed_analog)  # Mettez à jour la valeur de vitesse dans le widget
                time.sleep(0.1)  # Facultatif : pour éviter d'afficher des valeurs trop rapidement

except serial.SerialException:
    print("Une erreur s'est produite. Assurez-vous que le port série est correct et que le dispositif est connecté.")
except KeyboardInterrupt:
    print("Arrêt de la lecture du port série.")
finally:
    if ser.is_open:
        ser.close()
'''