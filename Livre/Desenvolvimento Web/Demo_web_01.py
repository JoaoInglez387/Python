from selenium import webdriver
from selenium.webdriver.common.by import By


navegador = webdriver.Edge()

navegador.get('https://www.google.com.br/')

abrir = navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
abrir.send_keys("Compressor de Ar")
abrir.submit()

navegador.find_element(By.XPATH, '//*[@id="bqHHPb"]/div/div/a[1]/div/span').click()
#------------------------------------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(5)
driver.quit()