from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://finance.kapital.kz/"

driver = webdriver.Chrome()
driver.get(url)


currency_element = driver.find_element(
    By.CSS_SELECTOR, "table.currencies-table")

usd_rate = currency_element.text

print(usd_rate)

driver.quit()
