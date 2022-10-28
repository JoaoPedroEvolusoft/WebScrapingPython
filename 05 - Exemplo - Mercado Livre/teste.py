from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# #defining anticaptcha function
# def acp_api_send_request(navegador, message_type, data={}):
#     message = {
# 		# this receiver has to be always set as antiCaptchaPlugin
#         'receiver': 'antiCaptchaPlugin',
#         # request type, for example setOptions
#         'type': message_type,
#         # merge with additional data
#         **data
#     }
#     # run JS code in the web page context
#     # preceicely we send a standard window.postMessage method
#     return navegador.execute_script("""
#     return window.postMessage({});
#     """.format(json.dumps(message)))
# # Init the chrome options object for connection the extension
# options = webnavegador.ChromeOptions()
# # A full path to CRX or ZIP or XPI file which was downloaded earlier 
# options.add_extension('/home/jospiado/Desktop')
# # Run the browser (Chrome Webnavegador) with passing the full path to the downloaded Webnavegador file
# navegador = webnavegador.Chrome('chromenavegador', options=options)

# # Go to the empty page for setting the API key through the plugin API request
# navegador.get('https://antcpt.com/blank.html')

# # Setting up the anti-captcha.com API key 
# # replace YOUR-ANTI-CAPTCHA-API-KEY to your actual API key, which you can get from here:
# # https://anti-captcha.com/clients/settings/apisetup
# acp_api_send_request(
#     navegador,
#     'setOptions',
#     {'options': {'antiCaptchaApiKey': '32ead22866b6ea13aad860f83183dfad'}}
# )

# # 3 seconds pause
# time.sleep(3)
# navegador.get(url)
# # replace the url with the URL you want to scrap

# navegador.maximize_window()
# # Test input
# navegador.find_element_by_css_selector('span[role=checkbox]').send_keys(Keys.ENTER)

# # Most important part: we wait upto 120 seconds until the AntiCaptcha plugin indicator with antigate_solver class
# # gets the solved class, which means that the captcha was successfully solved
# WebnavegadorWait(browser, 120).until(lambda x: x.find_element_by_css_selector('.antigate_solver.solved'))

# # Sending form
# navegador.find_element_by_css_selector('input[type=submit]').click()
# def solve():
#     import sys
#     from twocaptcha import TwoCaptcha
#     result = None

#     sitekey = 'https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp'
#     api_key = '<your_api_key_from_two_captcha>'
#     solver = TwoCaptcha(api_key)
#     try:
#         result = solver.recaptcha(
#             sitekey=sitekey,
#             url='https://www.deezer.com/en/login'
#         )

#     except Exception as e:
#         sys.exit(e)

#     return result

# textarea = navegador.find_element_by_id('g-recaptcha-response')
# solution = solve()
# code = solution['code']
# navegador.execute_script(f"var ele=arguments[0]; ele.innerHTML = '{code}';", textarea)
# time.sleep(1) # waiting is mandatory
# textarea = navegador.find_element_by_xpath('//*[@id="login-btn"]/button').click()

navegador = webdriver.Chrome()

navegador.get('https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp')


time.sleep(100)
# cpf = input('Digite seu cpf')
# datanasci= input('Digite sua data nascimento')

# elemento = navegador.find_element(By.ID, 'txtCPF')
# elemento2 = navegador.find_element(By.ID, 'txtDataNascimento')

# elemento.send_keys(cpf)
# elemento2.send_keys(datanasci)
