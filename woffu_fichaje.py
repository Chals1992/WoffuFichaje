from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura el WebDriver (en este caso, Edge)
options = Options()
options.use_chromium = True  # Utilizar el motor Chromium en Edge
options.add_argument("--headless")  # Ejecución en modo headless (sin ventana)

# Reemplaza 'path/to/msedgedriver.exe' con la ruta correcta a msedgedriver.exe
driver_path = 'path/to/msedgedriver.exe'
driver = webdriver.Edge(executable_path=driver_path, options=options)

# Abre la URL de Woffu
driver.get("https://volkswagen-groupservices.woffu.com/v2/personal/dashboard/user")

# Ajusta el tamaño de la ventana
driver.maximize_window()

# Espera a que el botón "Entrar" sea clickeable
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Entrar')]"))
    )
    time.sleep(2)  # Espera adicional antes de hacer clic
    element.click()
    print("Clic en el botón 'Entrar' exitoso.")
except Exception as e:
    print(f"No se pudo hacer clic en el botón 'Entrar': {e}")

# Cierra el navegador al finalizar
driver.quit()
