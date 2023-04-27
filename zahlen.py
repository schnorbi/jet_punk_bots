from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()
driver.get("https://www.jetpunk.com/user-quizzes/1357024/zahlen-1-50-in-15-sekunden")

time.sleep(8)
driver.switch_to.frame("gdpr-consent-notice")
driver.find_element(By.XPATH, '//*[@id="save"]').click()

time.sleep(2)
driver.switch_to.default_content()

time.sleep(2)
bt = driver.find_element(By.XPATH, '//*[@id="start-button"]').click()

time.sleep(0.25)
bo = driver.find_element(By.XPATH, '//*[@id="txt-answer-box"]')

i = 1
while i < 51:
    bo.send_keys(i)
    i += 1

time.sleep(600)

driver.quit()