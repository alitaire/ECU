import usb.core

# Vendor ID et Product ID du périphérique USB
# Utiliser la commande "lsusb" pour trouver les IDs
VENDOR_ID = 0x1234
PRODUCT_ID = 0x5678

# Recherche du périphérique USB avec le Vendor ID et Product ID spécifiés
device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

# Vérifier si le périphérique a été trouvé
if device is None:
    raise ValueError("Périphérique USB non trouvé.")

# Ouvrir une interface avec le périphérique
try:
    device.set_configuration()
    endpoint = device[0][(0,0)][0]
except usb.core.USBError as e:
    print("Erreur lors de la configuration du périphérique:", str(e))
    exit()

# Recevoir des données depuis le périphérique
try:
    data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
    print("Données reçues depuis le périphérique:", data)
except usb.core.USBError as e:
    print("Erreur lors de la réception des données:", str(e))
