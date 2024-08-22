from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://hk.centanet.com/findproperty/list/transaction?q=96004b309c3")

rental_prices = []
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__layout']/div/div[5]/div[7]/div/div/div[4]/div/button[2]")))
for i in range(417):
    parent_elements = driver.find_elements(By.CSS_SELECTOR, "div.cv-structured-list-item.cv-structured-list-item--standard.bx--structured-list-row")
    for parent_element in parent_elements:
        date = parent_element.find_element(By.CSS_SELECTOR, "div.info-date span").text.strip()
        address = parent_element.find_element(By.XPATH, "div[2]").text.strip()
        rent = parent_element.find_element(By.CLASS_NAME, "tranRent").text.strip()
        area = parent_element.find_element(By.XPATH, "div[6]").text.strip()
        rate = parent_element.find_element(By.XPATH, "div[7]").text.strip()
        rental_prices.append((date, address, rent, area, rate))
    next_button.click()
    driver.implicitly_wait(1)

driver.close()

df = pd.DataFrame(rental_prices, columns = ["Date", "Address", "Rent", "Area", "Rate"])

df.to_csv("results.csv", index=False, encoding = "utf-8-sig")