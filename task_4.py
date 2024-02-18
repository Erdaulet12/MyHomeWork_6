"""task_4.py"""

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    """main method"""

    url = "https://www.olx.kz/zhivotnye/koshki/"

    driver = webdriver.Chrome()
    driver.get(url)

    cats_elements = driver.find_element(
        By.CSS_SELECTOR, "div.css-oukcj3")

    cats = cats_elements.text
    driver.quit()
    return cats


if __name__ == "__main__":
    cats = main()
    print(cats)
