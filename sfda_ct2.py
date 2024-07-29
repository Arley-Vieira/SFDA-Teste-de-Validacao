from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Inicia o webdriver
driver = webdriver.Chrome()
driver.maximize_window()

#Abre a página do Site
driver.get("https://www.saofranciscodeassis.edu.br/")

try:
    #Abre a página de contato pela página inicial
    contaco_link = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div[2]/div/div[2]/div/div/div/ul/li[6]/a")
    contaco_link.click()

    #espera até o formulário estiver carregado/disponível
    wait = WebDriverWait(driver, 5)
    result = wait.until(EC.visibility_of_element_located((By.ID,"form-field-name")))
    result_2 = wait.until(EC.visibility_of_element_located((By.ID,"form-field-email")))
    result_3 = wait.until(EC.visibility_of_element_located((By.ID, "form-field-message")))

    #CT1 - 2 - Tentar enviar formulário campo de mensagem em branco

    botao_enviar = driver.find_element(By.XPATH, "/html/body/div[2]/section[3]/div/div[3]/div/div/div/form/div/div[5]/button/span/span[2]")
    userinput1 = driver.find_element(By.XPATH, "/html/body/div[2]/section[3]/div/div[3]/div/div/div/form/div/div[2]/input")
    userinput1.send_keys("Emaildeexemplo")
    userinput2 = driver.find_element(By.XPATH, "/html/body/div[2]/section[3]/div/div[3]/div/div/div/form/div/div[1]/input")
    userinput2.send_keys("Textodeexemplo")
    

    
    botao_enviar.click()
    WebDriverWait(driver, 10).until(driver.save_screenshot("CT1-2_result.png"))

    #Importante - indentifica  se o código ocorreu como esperado
    if result and result_2 and result_3:
        print("Teste bem sucedido. Resultado(s) encontrado")
    else:
        print("Test falhou: sem resultados.")

except Exception as e:
    #captura o screenshot do erro, caso ocorra
    driver.save_screenshot("erro.png")
    print(f"Ocorreu um erro com {e}")

finally:
    # Fechar o navegador
    driver.quit()


