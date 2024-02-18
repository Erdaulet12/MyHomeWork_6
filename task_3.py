"""task_3.py"""

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    """main method"""

    url = "https://finance.kapital.kz/"

    driver = webdriver.Chrome()
    driver.get(url)

    currency_element = driver.find_element(
        By.CSS_SELECTOR, "table.currencies-table")

    usd_rate = currency_element.text
    driver.quit()
    return usd_rate


if __name__ == "__main__":
    usd_rate = main()
    print(usd_rate)
