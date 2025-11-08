# Análisis de Redes WiFi con Raspberry Pi Pico W

Este repositorio contiene el código fuente y los resultados de un proyecto de laboratorio enfocado en el análisis y la manipulación de redes WiFi utilizando la placa de desarrollo **Raspberry Pi Pico W** con **MicroPython**.

El proyecto explora desde conceptos básicos, como la obtención de la dirección MAC y el escaneo de redes, hasta aplicaciones prácticas de IoT, como la creación de un punto de acceso (AP) con un servidor web para controlar hardware de forma remota y la caracterización de la señal WiFi (RSSI) en función de la distancia.

---

## 🚀 Funcionalidades Implementadas

-   **Creación de un Punto de Acceso (AP):** Configuración del Pico W para actuar como un AP WiFi independiente.
-   **Servidor Web Integrado:** Un servidor web simple que sirve una página HTML para interactuar con el microcontrolador.
-   **Control Remoto de Hardware:** Control del LED integrado en la placa a través de botones en la interfaz web.
-   **Lectura de Sensores (ADC):** Modificación del servidor para leer y mostrar en tiempo real el valor del conversor analógico-digital (ADC).
-   **Escaneo y Análisis de Redes:** Scripts para conectar el Pico W a redes existentes.
-   **Caracterización de la Señal (RSSI):** Un script para medir sistemáticamente la potencia de la señal WiFi (RSSI) a diferentes distancias y exportar los datos a un archivo CSV para su posterior análisis.

---

## 📂 Descripción de Archivos

Aquí se detalla el propósito de cada archivo en el repositorio:

-   `main.py`
    -   **Propósito:** Script principal para configurar el Raspberry Pi Pico W como un **Punto de Acceso (AP)** y levantar un servidor web.
    -   **Funcionalidad:** Sirve el archivo `index.html` y permite controlar el LED integrado de la placa a través de peticiones HTTP. Esta es la versión base del AP.

-   `main.py ADC.txt` y `index.html ADC.txt`
    -   **Propósito:** Son las versiones modificadas del script principal y la página web que incluyen la funcionalidad de **leer y mostrar el valor del conversor ADC**.
    -   **Nota:** Se proporcionan como `.txt` para mostrar el código. Para usarlos, deben ser renombrados a `main.py` y `index.html` y cargados en el Pico W.

-   `conectar AP.py`
    -   **Propósito:** Un script simple que configura el Pico W en modo estación (cliente) para conectarse a un punto de acceso WiFi existente. Es el paso previo para realizar mediciones de RSSI.

-   `GenerarCSV y medidas.py`
    -   **Propósito:** El script principal para el experimento de **análisis de RSSI vs. distancia**.
    -   **Funcionalidad:** Se conecta a un AP, realiza múltiples mediciones de RSSI a intervalos definidos, calcula promedios y guarda los resultados en un archivo CSV.

-   `rssi_distance.csv`
    -   **Propósito:** Es el **archivo de salida** generado por `GenerarCSV y medidas.py`.
    -   **Contenido:** Contiene los datos tabulados de las mediciones de RSSI a diferentes distancias, listos para ser analizados o graficados.

---

## 🛠️ Requisitos

### Hardware
-   Raspberry Pi Pico W
-   Cable Micro-USB

### Software
-   Firmware de **MicroPython** para la Raspberry Pi Pico W.
-   Un IDE compatible como **Thonny** para cargar y ejecutar los scripts.
-   Cualquier navegador web moderno para interactuar con el servidor.

---

## 🚀 Cómo Empezar

1.  **Configurar el Pico W:** Asegúrate de tener MicroPython instalado en tu Raspberry Pi Pico W.
2.  **Crear el Punto de Acceso:**
    -   Renombra `main.py ADC.txt` a `main.py` y `index.html ADC.txt` a `index.html`.
    -   Carga ambos archivos a la raíz de tu Pico W usando Thonny.
    -   Reinicia el dispositivo. El Pico W creará una red WiFi (ej. "Grupo dinamita").
    -   Conéctate a esa red desde tu PC o celular y navega a `http://192.168.4.1` para ver la interfaz.
3.  **Realizar Mediciones de RSSI:**
    -   Modifica el SSID y la contraseña dentro de `GenerarCSV y medidas.py` para que coincidan con tu red WiFi.
    -   Ejecuta el script en el Pico W. Sigue las instrucciones para tomar las mediciones.
    -   Una vez finalizado, el archivo `rssi_distance.csv` estará en el sistema de archivos del Pico W con los resultados.

---

## 👤 Autor

-   **Miguel Andrey Peña Cárdenas**
