from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from anticaptchaofficial.hcaptchaproxyless import *
navegador = webdriver.Chrome()

link = 'https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PF/Emitir'

navegador.get(link)

cpf = input('Digite seu CPF: ')
navegador.find_element(By.ID, "NI").send_keys(cpf)

navegador.find_element(By.ID, "validar").click()

time.sleep(100)