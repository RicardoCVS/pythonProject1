from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# Configura el driver
driver_path = os.environ.get('WEBDRIVER_PATH', None)
if driver_path is None:
    raise Exception("No se encontró el path del driver. Asegúrate de configurar la variable de entorno 'WEBDRIVER_PATH'")
driver = webdriver.Chrome(driver_path)

# Busca en Google
driver.get("https://www.google.com")
try:
    accept_cookies_button = driver.find_element_by_css_selector(".consent-bump__actions > button")
    accept_cookies_button.click()
except Exception as e:
    print("No se encontró el botón de aceptar cookies:", e)

search_box = driver.find_element_by_name("q")
search_box.send_keys("automatización")
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# Encuentra el enlace de Wikipedia
search_results = driver.find_elements_by_css_selector(".g .tF2Cxc")
wikipedia_link = None
for result in search_results:
    link = result.find_element_by_css_selector(".yuRUbf > a")
    if "wikipedia.org" in link.get_attribute("href"):
        wikipedia_link = link
        break

if wikipedia_link is not None:
    # Navega a la página de Wikipedia y obtén el año del primer proceso automático
    wikipedia_link.click()
    time.sleep(2)
    year_element = driver.find_element_by_css_selector(".infobox tr:nth-child(3) td")
    year = year_element.text
    print(f"El primer proceso automático fue en el año {year}.")

    # Realiza un screenshot de la página de la Wikipedia
    driver.save_screenshot("wikipedia_page.png")
else:
    print("No se encontró el enlace de Wikipedia en los resultados de búsqueda.")

driver.quit()

