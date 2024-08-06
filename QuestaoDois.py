from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.searchencrypt.com/home")

search_bar = driver.find_element(By.ID, "search-input")  # Assumindo que o ID do campo de pesquisa é "search-input".
search_bar.send_keys("Isabele Araújo Amaro")

search_button = driver.find_element(By.ID, "search-button")  # Assumindo que o ID do botão de pesquisa é "search-button"
search_button.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".result-item"))
)

all_results = driver.find_elements(By.CSS_SELECTOR, ".result-item")
total_results = len(all_results)

exact_results = driver.find_elements(By.CSS_SELECTOR, ".result-item:contains('Isabele Araújo Amaro')")
exact_matches = len(exact_results)

print("Resultados encontrados:", total_results)
print("Resultados exatos:", exact_matches)

# Fechar o navegador
driver.quit()
