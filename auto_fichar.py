import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.common.exceptions import TimeoutException

# Configuración de las opciones del navegador Edge
options = EdgeOptions()
options.use_chromium = True  # Usar el nuevo Microsoft Edge (Chromium)
options.add_argument("--headless")  # Ejecutar en modo headless (sin ventana)
options.add_argument("--disable-gpu")  # Deshabilitar GPU para evitar problemas

# Ruta al ejecutable del Microsoft Edge WebDriver
msedgedriver_path = "/usr/local/bin/msedgedriver"

# Crear una instancia del controlador de Edge
driver = Edge(executable_path=msedgedriver_path, options=options)

try:
    # Navegar a la página de inicio de sesión de Woffu
    url_woffu = "https://app.woffu.com/es/login"
    driver.get(url_woffu)

    # Esperar a que el campo de email esté presente y visible
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "login-email")))

    # Introducir el correo electrónico y la contraseña
    campo_email = driver.find_element(By.ID, "login-email")
    campo_email.send_keys("carles.casajuana1@volkswagen-groupservices.com")

    campo_password = driver.find_element(By.ID, "login-password")
    campo_password.send_keys("Holamundo1992&")

    # Hacer clic en el botón de inicio de sesión
    boton_login = driver.find_element(By.XPATH, "//button[@type='submit']")
    boton_login.click()

    # Esperar a que se complete el inicio de sesión y aparezca el botón de fichaje
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Fichar')]")))

    # Encontrar y hacer clic en el botón de fichaje
    boton_fichar = driver.find_element(By.XPATH, "//button[contains(text(), 'Fichar')]")
    boton_fichar.click()

    # Esperar a que se complete el fichaje
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='success']")))

    print("Fichaje realizado con éxito.")

except TimeoutException:
    print("Tiempo de espera excedido. No se pudo completar la acción.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {str(e)}")
finally:
    # Cerrar el navegador al finalizar
    driver.quit()
