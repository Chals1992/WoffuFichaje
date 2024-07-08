import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions

# Configuración de las opciones del navegador Edge
options = EdgeOptions()
options.use_chromium = True  # Usar el nuevo Microsoft Edge (Chromium)
options.add_argument("--headless")  # Ejecutar en modo headless (sin ventana)
options.add_argument("--disable-gpu")  # Deshabilitar GPU para evitar problemas

# Configurar la ruta del archivo msedgedriver.exe
msedgedriver_path = "C:\\Carles\\edgedriver_win64\\msedgedriver.exe"  # Ruta correcta del msedgedriver.exe

# Crear una instancia del controlador de Edge
driver = Edge(executable_path=msedgedriver_path, options=options)

try:
    # Navegar a la página de inicio de sesión de Woffu
    url_woffu = "https://app.woffu.com/es/login"
    driver.get(url_woffu)

    # Esperar a que la página se cargue completamente
    time.sleep(5)  # Puedes ajustar el tiempo de espera según sea necesario

    # Encontrar y completar los campos de inicio de sesión
    campo_email = driver.find_element(By.ID, "login-email")
    campo_email.send_keys("carles.casajuana1@volkswagen-groupservices.com")

    campo_password = driver.find_element(By.ID, "login-password")
    campo_password.send_keys("Holamundo1992&")

    # Hacer clic en el botón de inicio de sesión
    boton_login = driver.find_element(By.XPATH, "//button[@type='submit']")
    boton_login.click()

    # Esperar a que se complete el inicio de sesión
    time.sleep(5)  # Puedes ajustar el tiempo de espera según sea necesario

    # Encontrar y hacer clic en el botón de fichaje
    boton_fichar = driver.find_element(By.XPATH, "//button[contains(text(), 'Fichar')]")
    boton_fichar.click()

    # Esperar a que se complete el fichaje
    time.sleep(5)  # Puedes ajustar el tiempo de espera según sea necesario

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
