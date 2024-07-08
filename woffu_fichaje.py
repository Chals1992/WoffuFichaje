from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar el navegador (asegúrate de tener chromedriver instalado)
driver = webdriver.Chrome()

# Ir a la página de Woffu
driver.get("https://volkswagen-groupservices.woffu.com/v2/personal/dashboard/user")

# Maximizar la ventana
driver.maximize_window()

# Aquí añadirías el código para iniciar sesión si es necesario
# Ejemplo:
# username = driver.find_element(By.ID, "username")
# password = driver.find_element(By.ID, "password")
# username.send_keys("tu_usuario")
# password.send_keys("tu_contraseña")
# password.send_keys(Keys.RETURN)

# Hacer clic en el botón de fichar
time.sleep(5)  # Esperar a que la página cargue
fichar_button = driver.find_element(By.CSS_SELECTOR, ".sc-llcuoN")
fichar_button.click()

# Cerrar el navegador
time.sleep(5)
driver.quit()

