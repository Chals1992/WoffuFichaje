from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el WebDriver (en este caso, Chrome)
options = Options()
options.add_argument("--headless")  # Ejecución en modo headless (sin ventana)
driver = webdriver.Chrome(options=options)

# Abre la URL de Woffu
driver.get("https://volkswagen-groupservices.woffu.com/v2/personal/dashboard/user")

# Maximiza la ventana (no es necesario si se está ejecutando en modo headless)
# driver.maximize_window()

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
