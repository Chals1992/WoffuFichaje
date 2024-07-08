from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura el WebDriver para Edge
options = Options()
options.use_chromium = True  # Utiliza el motor Chromium de Edge

# Puedes configurar opciones adicionales según sea necesario

# Inicia el servicio del WebDriver de Edge
driver = webdriver.Edge(options=options)

# Abre la URL de Woffu
driver.get("https://volkswagen-groupservices.woffu.com")

# Maximiza la ventana (si es necesario)
driver.maximize_window()

# Espera a que el elemento se cargue antes de hacer clic
try:
    element = WebDriverWait(driver, 10).until(
        EC.eleme
