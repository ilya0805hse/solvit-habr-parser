from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://habr.com/ru/articles/top/daily/")

headers = driver.find_elements(By.CLASS_NAME, "tm-title__link")
views = driver.find_elements(By.CLASS_NAME, "tm-icon-counter__value")

for i in range(len(headers)):
    print(" ".join(headers[i].text.split()[:5]) + "...", "|", "Просмотры:", views[i].text)

driver.quit()
