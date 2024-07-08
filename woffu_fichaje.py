from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura el WebDriver para Edge (Microsoft Edge)
options = Options()
options.add_argument("--headless")  # Ejecución en modo headless (sin ventana)

# Reemplaza 'path_to_msedgedriver' con la ruta correcta a msedgedriver.exe en tu sistema
driver_path = '/path_to_msedgedriver/msedgedriver.exe'

# Inicializa el driver de Edge
driver = webdriver.Edge(executable_path=driver_path, options=options)

try:
    # Abre la URL de Woffu
    driver.get("https://volkswagen-groupservices.woffu.com")

    # Maximiza la ventana (si es necesario)
    driver.maximize_window()

    # Espera a que el elemento 'Entrar' sea clickable y luego haz clic en él
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Entrar')]"))
    )
    element.click()
    print("Clic en 'Entrar' realizado con éxito.")

except Exception as e:
    print(f"No se pudo hacer clic en 'Entrar': {e}")

finally:
    # Cierra el navegador al finalizar
    driver.quit()
