
from time import sleep
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =  webdriver.Chrome()

driver.get('https://www.pelando.com.br/cupons-de-descontos')

cupoms= driver.find_elements( By.XPATH,"//a[@class='sc-eqUAAy kzHRhw sc-a4b5c454-1 eyQTiv']")

for cupom in cupoms:
    cupom.click()
    sleep(10)
    tikets = driver.find_elements(By.XPATH,"//li[@class='sc-3047764d-0 ffXBnY']")
    for tiket in tikets:
        print(tiket.text)
        
#//span[@role='presentation']
driver.implicitly_wait(0.5)

