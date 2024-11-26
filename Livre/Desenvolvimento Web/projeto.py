from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import randint

navegador = webdriver.Chrome()

navegador.get('https://www.google.com.br/?hl=pt-BR')

abrir = navegador.find_element(By.XPATH, '//*[@id="APjFqb"]')

abrir.send_keys("Marcos")
abrir.submit()

navegador.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a/h3').click()
time.sleep(3)

navegador.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/article/ul/li[7]/a').click()
time.sleep(4)

txt = navegador.find_elements(By. CLASS_NAME, "t")[randint(1, len(navegador.find_elements(By. CLASS_NAME, "t")) - 1)].text

print(txt)