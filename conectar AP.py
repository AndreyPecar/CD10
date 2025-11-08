import network
import time

SSID = "vivo Y51"       # Nombre del AP de tu celular
PASSWORD = "12345678"    # Contraseña del AP

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Conectando a", SSID, "...")

for i in range(10):
    if wlan.isconnected():
        break
    time.sleep(1)
    print(".", end="")

if wlan.isconnected():
    print("\n✅ Conectado exitosamente")
    print("IP asignada:", wlan.ifconfig()[0])
else:
    print("\n❌ No se pudo conectar al AP.")