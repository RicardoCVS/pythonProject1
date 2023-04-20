import time
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

time.sleep(10)  # Esperar a que se carguen los resultados

search_bar = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
search_bar.send_keys("automatización")
search_bar.send_keys(Keys.RETURN)

time.sleep(3)  # Esperar a que se carguen los resultados

wiki_link = driver.find_element(By.XPATH, "//a[contains(@href, 'https://es.wikipedia.org')]")
wiki_link.click()

time.sleep(3)  # Esperar a que se cargue la página de Wikipedia

year = driver.find_element(By.XPATH, "//*[contains(text(), 'primer proceso automático')]").text

print(f"Año en que se realizó el primer proceso automático: {year}")

driver.save_screenshot("wikipedia_page.png")
driver.quit()
