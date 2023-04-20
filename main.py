import time
import re
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Asegúrate de tener instalado el ChromeDriver
driver = webdriver.Chrome()

driver.get("https://www.google.com")

# Aceptar cookies
try:
    cookies_accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='L2AGLb']/div"))
    )
    cookies_accept_button.click()
except Exception as e:
    print("No se encontró el botón para aceptar las cookies. Omitiendo...")

time.sleep(3)  # Esperar a que se carguen los resultados

search_bar = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
search_bar.send_keys("automatización")
search_bar.send_keys(Keys.RETURN)

time.sleep(3)  # Esperar a que se carguen los resultados

wiki_link = driver.find_element(By.XPATH, "//a[contains(@href, 'https://es.wikipedia.org')]")
wiki_link.click()

time.sleep(3)  # Esperar a que se cargue la página de Wikipedia

# Buscar el párrafo usando el XPath proporcionado
paragraph = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[28]")

# Hacer scroll hasta el elemento paragraph
driver.execute_script("arguments[0].scrollIntoView();", paragraph)

# Esperar un tiempo adicional para asegurar que la página esté completamente renderizada
time.sleep(3)

paragraph_text = paragraph.text

# Extraer los años (números de tres y cuatro dígitos) del párrafo
years_four_digits = re.findall(r'\b\d{4}\b', paragraph_text)
years_three_digits = re.findall(r'\b\d{3}\b', paragraph_text)

print(f"Años encontrados en el párrafo con 4 dígitos: {', '.join(years_four_digits)}")
print(f"Años encontrados en el párrafo con 3 dígitos: {', '.join(years_three_digits)}")

# Guardar screenshot completo
desktop_path = "C:\\Users\\vicar\\OneDrive\\Desktop"
with open(os.path.join(desktop_path, "wikipedia_page.png"), "wb") as f:
    f.write(driver.get_screenshot_as_png())

driver.quit()
