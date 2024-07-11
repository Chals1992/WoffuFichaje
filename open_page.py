# main.py
from msedge.selenium_tools import Edge, EdgeOptions
import time

# Configurar las opciones del navegador Edge
options = EdgeOptions()
options.use_chromium = True

# Iniciar el navegador Edge
driver = Edge(options=options)

# Abrir una página web
url = "https://www.ejemplo.com"  # Reemplaza con la URL que deseas abrir
driver.get(url)

# Esperar unos segundos (opcional)
time.sleep(5)

# Cerrar el navegador al finalizar
driver.quit()
