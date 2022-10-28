from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from anticaptchaofficial.hcaptchaproxyless import *
navegador = webdriver.Chrome()

link = 'https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/Emitir'

navegador.get(link)

CNPJ= input('Digite seu CNPJ : ')

navegador.find_element(By.ID, "NI").send_keys(CNPJ)

navegador.find_element(By.ID, "validar").click()


time.sleep(100)