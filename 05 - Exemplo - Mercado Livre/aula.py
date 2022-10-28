from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from anticaptchaofficial.hcaptchaproxyless import *
navegador = webdriver.Chrome()

link = 'https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp'

navegador.get(link)

chave_captcha= navegador.find_element(By.ID ,'hcaptcha').get_attribute('data-sitekey')
solver = hCaptchaProxyless()
solver.set_verbose(1)
solver.set_key('8afa127dc6b03519a4a933c11ccf2b1f')
solver.set_website_url(link)
solver.set_website_key(chave_captcha)

cpf = input('Digite seu cpf')
datanasci= input('Digite sua data nascimento')

elemento = navegador.find_element(By.ID, 'txtCPF')
elemento2 = navegador.find_element(By.ID, 'txtDataNascimento')

elemento.send_keys(cpf)
elemento2.send_keys(datanasci)


solver.set_soft_id(0)

resposta = solver.solve_and_return_solution()

if resposta  != 0:
    print(resposta)
    #Preencher o campo
    #h-captcha-response-0pzojc4ad9na

     
    navegador.execute_script(f"document.querySelector('textarea').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, "id_submit").click()
else:
    print(solver.err_string)



time.sleep(100)