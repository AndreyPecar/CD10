import network
import time
import math

# =================== CONFIGURACIÓN ===================
SSID = "vivo Y51"        # Nombre exacto del hotspot (celular)
PASSWORD = "12345678"     # Contraseña
MUESTRAS = 10             # Cantidad de mediciones
CSV_FILE = "rssi_distance.csv"

# Parámetros del modelo de propagación
RSSI_1M = -40   # Valor de RSSI medido a 1 metro
N = 2.2         # Exponente de pérdida (ajústalo según el entorno)

# =================== INICIALIZACIÓN ===================
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print("Conectando a", SSID, "...")
    wlan.connect(SSID, PASSWORD)
    for _ in range(10):
        if wlan.isconnected():
            break
        print(".", end="")
        time.sleep(1)
    if wlan.isconnected():
        print("\n✅ Conectado a", SSID)
    else:
        print("\n❌ No se pudo conectar al AP.")
        raise SystemExit
else:
    print("Ya conectado a", SSID)

# =================== FUNCIONES ========================
def medir_rssi(ssid_objetivo):
    """Escanea redes y devuelve el RSSI del SSID objetivo."""
    redes = wlan.scan()
    for r in redes:
        ssid = r[0].decode()
        rssi = r[3]
        if ssid == ssid_objetivo:
            return rssi
    return None

def estimar_distancia(rssi):
    """Calcula distancia aproximada en metros a partir del RSSI."""
    exp = (RSSI_1M - rssi) / (10 * N)
    return round(pow(10, exp), 2)

# =================== MEDICIÓN =========================
print("\nIniciando mediciones RSSI y distancia estimada...\n")

valores = []

with open(CSV_FILE, "w") as f:
    f.write("Muestra,RSSI (dBm),Distancia estimada (m)\n")

    for i in range(MUESTRAS):
        rssi = medir_rssi(SSID)
        if rssi is not None:
            distancia = estimar_distancia(rssi)
            valores.append((rssi, distancia))
            f.write("{},{},{}\n".format(i + 1, rssi, distancia))
            print("Medición {} → RSSI: {} dBm → Distancia ≈ {} m".format(i + 1, rssi, distancia))
        else:
            f.write("{},NA,NA\n".format(i + 1))
            print("Medición {}: SSID no detectado".format(i + 1))
        time.sleep(1)

# =================== RESULTADOS =======================
if valores:
    prom_rssi = sum(r for r, _ in valores) / len(valores)
    prom_dist = sum(d for _, d in valores) / len(valores)
    print("\n📊 Promedio RSSI: {:.2f} dBm".format(prom_rssi))
    print("📏 Distancia estimada promedio: {:.2f} m".format(prom_dist))

    with open(CSV_FILE, "a") as f:
        f.write("\nPromedio,{:.2f},{:.2f}\n".format(prom_rssi, prom_dist))
else:
    print("⚠ No se obtuvieron mediciones válidas.")