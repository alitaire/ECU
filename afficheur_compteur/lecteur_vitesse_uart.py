import serial

port = '/dev/ttyACM0'
baud_rate = 115200
conversion_factor = 150 / 4000

try:
    ser = serial.Serial(port, baud_rate, timeout=1)

    while True:
        data = ser.readline().decode('utf-8').strip()
        if data:
            speeds_kmph = [float(speed) for speed in data.split()]  # Split data by spaces
            for speed_kmph in speeds_kmph:
                speed_analog = speed_kmph * conversion_factor
                # Assuming window.speedWidget.set_speed() takes a numeric argument
                print(f"{speed_analog} .2 km/h")

except serial.SerialException:
    print("Une erreur s'est produite. Assurez-vous que le port série est correct et que le dispositif est connecté.")
except KeyboardInterrupt:
    print("Arrêt de la lecture du port série.")
finally:
    if ser.is_open:
        ser.close()

