from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.searchencrypt.com/home")

search_bar = driver.find_element(By.CLASS_NAME, "search-bar__search")
search_bar.send_keys("Isabele Araújo Amaro")

search_button = driver.find_element(By.CLASS_NAME, "search-bar__submit")
search_button.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "serp__web-result__container"))
)

all_results = driver.find_elements(By.CLASS_NAME, "serp__web-result__container")
total_results = len(all_results)

exact_matches = 0
for result in all_results:
    description = result.find_element(By.CSS_SELECTOR, ".web-result__description").text
    if "Isabele Araújo Amaro" in description:
        exact_matches += 1

print("Resultados encontrados:", total_results)
print("Resultados exatos:", exact_matches)

# Fechar o navegador
driver.quit()
