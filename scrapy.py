from ast import Pass
from gettext import find
import string
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import support
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import pandas as pd
import re

from datetime import datetime

from sqlalchemy import null, true

import funcoes as f

import key as k

key_email = k.email
key_senha = k.senha

def chamapaginas():
    
    browser.get('https://www.orulo.com.br/customers/sign_in')
    
    
    WebDriverWait(browser, 50).until(lambda browser: browser.execute_script('return document.readyState') == 'complete')
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'email'))).send_keys(key_email)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(key_senha)
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/div/form/button'))).click()
    
    #WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'submit_sign_in'))).click()
    WebDriverWait(browser, 50).until(lambda browser: browser.execute_script('return document.readyState') == 'complete')


def filtro(fil):
    #val = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[7]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/a/div/fieldset/div/div[2]/div/div[2]/div[2]/div/b[2]'))).text
    #val = f.convert(val)
    #old_page = val
    if fil == 1:
        try:
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]'))).click()
        except:
            pass
        
        #maior menor
        try:
            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sort_order"]'))).click()
        except:
            pass                                                                
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[7]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/fieldset/div/div[2]/select/option[7]'))).click()
        sleep(3)         
        #definindo cidade
        #WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'SearchFilter__InputText-sc-149rnbh-3 lfSufU'))).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[7]/div/div/div[1]/div/div/div[1]/div/form/input'))).click()
        #WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'BtnOutlineStyles__Button-sc-15zkphd-0 jpSwUG'))).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/button[3]'))).click()
                                                                                
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[7]/div/div/div[1]/div/div/div[1]/div/form/input'))).send_keys("São Paulo")
        #WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'SearchFilter__InputText-sc-149rnbh-3 lfSufU'))).send_keys("São Paulo")
                                                                                
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/a[2]'))).click()
                                                                                
        # em construção
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="status_popover_button_id"]'))).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="status_under_construction"]'))).click()

        #preço 200-300
        #abre
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_popover_button_id"]'))).click()

        #checkbox de apartamento                                               
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[7]/div/div[2]/div[1]/div/div/div[1]'))).click()

        # seta os preços                                                               
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[9]/div/select[1]/option[2]'))).click()
                                                                          
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[9]/div/select[2]/option[3]'))).click()
        #fecha
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_popover_button_id"]'))).click()
    
    elif fil == 2:
        #preço 300-400
        #abre
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_popover_button_id"]'))).click()
                                                                                
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[9]/div/select[1]/option[3]'))).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[9]/div/select[2]/option[4]'))).click()
        #fecha
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_popover_button_id"]'))).click()
    
    elif fil == 3:
        #preço 400-500
        #abre
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_popover_button_id"]'))).click()
                                                                                
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[9]/div/select[1]/option[4]'))).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[9]/div/select[2]/option[5]'))).click()
        #fecha
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_popover_button_id"]'))).click()

    elif fil == 4:
        #preço 500-1000
        #abre
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_popover_button_id"]'))).click()
                                                                                
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[9]/div/select[1]/option[5]'))).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[9]/div/select[2]/option[10]'))).click()
        #fecha
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_popover_button_id"]'))).click()
    
    elif fil == 5:
        #preço 1000-max
        #abre
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_popover_button_id"]'))).click()
                                                                                
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[9]/div/select[1]/option[10]'))).click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[9]/div/select[2]/option[1]'))).click()
        #fecha
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="more_popover_button_id"]'))).click()
    
    #carrega nao esta funcionando repensar
    #carrega_pagina(old_page)

    

def contador():
    parent = browser.find_element_by_xpath('/html/body/div[4]/div[7]/div/div/div[2]/div[2]/div[1]/div/div')
    contador_anuncios = len(parent.find_elements_by_xpath('./div'))
    contador_anuncios1 = int(contador_anuncios)
    #print(contador_anuncios1)
    return contador_anuncios1


def proxima():
    try:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'next-page-button'))).click()
    except:
        print("acabou!!") 
    

def cookies():
    #cookeis e alertr
    sleep(3)
    try:
       #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]'))).click()
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))).click()
    except:
        pass
    try:
                                                                                
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pushActionRefuse"]'))).click()
    except:
        pass


#troca a aba, para assim conseguir navegar
def trocar():
    sleep(1)
    filho = browser.window_handles[1]
    browser.switch_to.window(filho)

# fecha todas abas menos a aba 0
def fechar_abas():
    pai = browser.window_handles[0]
    for window_handle in browser.window_handles:
        if window_handle != pai:
            browser.switch_to.window(window_handle)
            browser.close()   
    browser.switch_to.window(pai) 


def carrega_pagina(old_page):
      
      while True:
            sleep(1)
            val = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[7]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/a/div/fieldset/div/div[2]/div/div[2]/div[2]/div/b[2]'))).text
            new_page = f.convert(val)
            if new_page == old_page:
                  old_page = new_page
            else:                     
                  #print("pagina totalmente carregada")
                  break 


def ver_anun(item,fil):
    # pega valor
    val = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[4]/div[7]/div/div/div[2]/div[2]/div[1]/div/div/div[{item}]/a/div/fieldset/div/div[2]/div/div[2]/div[2]/div/b[2]'))).text
    val = f.convert(val)
    # como o site mostra valores alem do  filtro, precisamos definir alguma variavel de controle, para nao repetiri anuncio
    if fil == 2:
        if val <= 300000:
            fil +=1
             # sair do loop para começar novo filtro
    elif fil == 3:
        if val <= 400000:
            fil +=1       
    elif fil == 4:
        if val <= 500000:
            fil +=1         
    elif fil == 5:
        if val <= 1000000:
            fil +=1
    return fil

#conta quantos tipos disponiveis
def cont_tipo():
    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="info_typologies"]')))
    #sleep(2)
    parent = browser.find_element_by_xpath('//*[@id="info_typologies"]')
    contador_anuncios = len(parent.find_elements_by_xpath('./table'))
    contador_anuncios1 = int(contador_anuncios)
    #print('quantidade de tipologias')
    #print(contador_anuncios1)
    return contador_anuncios1

# conta quantidade dentro de cada tipo
def cont_dif(a):
    #parent = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="info_typologies"]')))
    #sleep(2)
    parent = browser.find_element_by_xpath(f'/html/body/div[3]/div[7]/main/div[1]/div[4]/div[2]/section/table[{a}]/tbody')
    
    contador_anuncios = len(parent.find_elements_by_xpath('./tr'))
    contador_anuncios1 = int(contador_anuncios)
    #print('quantidade de anuncios por tipologia')
    #print(contador_anuncios1)
    return contador_anuncios1

# conta quantidade de lazer do anuncio
def cont_lazer():
    #parent = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="info_typologies"]')))
    #sleep(2)
    try:
        parent = browser.find_element_by_xpath(f'/html/body/div[3]/div[7]/main/div[1]/div[4]/div[1]/fieldset/div[2]/div/ul')
        contador_anuncios = len(parent.find_elements_by_xpath('./li'))
        c = int(contador_anuncios)
    except:
        c = 0
    #print('quantidade de anuncios por tipologia')
    #print(contador_anuncios1)
    a = 1
    lazer = []
    while a <= c:
        la = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[3]/div[7]/main/div[1]/div[4]/div[1]/fieldset/div[2]/div/ul/li[{a}]'))).text   
        lazer.append(la)
        #print("nome = ", end='')                                                           
        #print(nome)
        a +=1
    return lazer


def veri_cod():
    cod = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[3]/div[2]/div/div[1]'))).text
    cod = f.pegar_num(cod)
    return cod



#dar tab daqui pra baixo e retirar o comentario do primeiro while
#browser = webdriver.Firefox(options=options)
browser = webdriver.Firefox()
chamapaginas()
WebDriverWait(browser, 50).until(lambda browser: browser.execute_script('return document.readyState') == 'complete')
sleep(3)
cookies()
WebDriverWait(browser, 50).until(lambda browser: browser.execute_script('return document.readyState') == 'complete')


fil = 1

# variavel de pagina csv
#pag = 1
# usar essa para caso travar
pag = 716

# tilt = 2 qnd for começar a fazer o crawler# agora eu entendi pq do tilt = 1, o tilt ele é necessario pois
# precisa rodar o primeiro filtro pra setar cidade, ordenar, entre outros filtro
# depois q setou, colocar o fil desejado para assim rodar onde parou
tilt = 1

# variavel q armazena os codigo de cada predio
list_cod = []

# variavel de controle do filtro para manter ou mudar o filtro

while fil <=5:
    
    filtro(fil)
    WebDriverWait(browser, 50).until(lambda browser: browser.execute_script('return document.readyState') == 'complete')
    sleep(3)
    var_fil = fil
    if tilt == 1:
        # aqui vc seta o fil desejado, no caso de agora preciso do 5
        fil = 5
        tilt = 2
    while fil == var_fil:
        #retorna qnt de anuncios na pagina, normal retornar 11, se tiver menos ai pode passar para o proximo filtro
        anum = contador()
        item = 2
        while item <= anum:
            dados_anuncios = []                                                          
            fil2 = ver_anun(item,fil)
            if  fil2 == fil:
                # usar um try, pq se tiver menos q 11 o numero de anun, ele tem q faz o q tem e começar o proximo filtro
                try:
                    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[4]/div[7]/div/div/div[2]/div[2]/div[1]/div/div/div[{item}]/a/div/fieldset/div/div[1]/div'))).click()
                except:
                    var_fil +=1
                    break
                trocar()


                
                # /html/body/div[3]/div[7]/main/div[1]/div[3]/div[2]/div/div[1]

                # aqui começa a pegar as informações

                #WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[4]/div[2]/section/h1')))
                #sleep(3)
                
                while true:
                    WebDriverWait(browser, 50).until(lambda browser: browser.execute_script('return document.readyState') == 'complete') 
                    browser.execute_script("window.scrollTo(0, 600)")
                    try:
                        WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[4]/div[2]/section/p[1]')))
                        break
                    except:
                        browser.refresh()
                #sleep(2)


                # verifica se o codigo ja foi adicionado, para nao repetir o anuncio
                cod = veri_cod()
                if cod in list_cod:
                    print("ja tem na lista")
                    fechar_abas()
                    item += 1
                    continue
                else:
                    list_cod.append(cod)


                #chama a função q retorna a quantidade de tipos( os tipos podem ser apartamento, garden, cobertura, entre outros)
                var_cont_tipo = cont_tipo()
                lazer = cont_lazer()
                # informaçoes
                estagio = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[4]/fieldset[2]/div[2]/div[1]/span[2]'))).text
                lancamento = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[4]/fieldset[2]/div[2]/div[4]/span[2]'))).text
                #                                                                                        /html/body/div[3]/div[7]/main/div[1]/div[4]/fieldset[2]/div[2]/div[6]/span[2]
                try:
                    entrega = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[4]/fieldset[2]/div[2]/div[5]/span[2]'))).text
                except:
                    entrega = '00/00/0000'

                                                                                                          
                total_uni = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[4]/fieldset[2]/div[2]/div[8]/span[2]'))).text
                try:                                                                                        
                    estoque = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[4]/fieldset[2]/div[2]/div[9]/span[2]'))).text
                except:
                    estoque = 0

                try:    
                    uni_por_andar = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[4]/fieldset[2]/div[2]/div[10]/span[2]'))).text
                except:
                    uni_por_andar = 0                                                                                          
                try:
                    num_andar = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[4]/fieldset[2]/div[2]/div[11]/span[2]'))).text
                except:
                    num_andar = 0
                atualizado = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[4]/fieldset[2]/div[2]/div[12]/span[2]'))).text
                href = browser.current_url 
                

                # a é variavel de controle q vai ser a iteração
                a = 1
                while a <= var_cont_tipo:
                    
                    #print("tipologia = ", end='')                                                           
                    #print(tipologia) 
                    #variavel de qntidade de anuncios por tipo, por exemplo pode ter 1 a 3 ou ate mais valroes diferentes por tipos
                    var_cont_dif = cont_dif(a)
                    # b é outra variavel de controle de iteração
                    b=1
                    while b <= var_cont_dif:
                        nome = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[3]/div[1]/div/h2'))).text   
                        
                        #print("nome = ", end='')                                                           
                        #print(nome) 
                        end = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[7]/main/div[1]/div[3]/div[1]/div/h1'))).text   
                        nun_end = f.pegar_num(end)
                        end, bairro = f.nome_rua(end)
                        #print("endereço = ", end='')                                                         
                        #print(end)
                        #print("bairro = ", end='')                                                         
                        #print(bairro)
                        #print("numero = ", end='')                                                         
                        #print(nun_end)
                        tipologia = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[3]/div[7]/main/div[1]/div[4]/div[2]/section/p[{a}]'))).text   
                        #print("tipologia = ", end='')                                                           
                        #print(tipologia) 
                        preco = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[3]/div[7]/main/div[1]/div[4]/div[2]/section/table[{a}]/tbody/tr[{b}]/td[1]/div'))).text   
                        preco = f.convert(preco)
                        #print("preço = ", end='')                                                           
                        #print(preco)
                        metragem = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[3]/div[7]/main/div[1]/div[4]/div[2]/section/table[{a}]/tbody/tr[{b}]/td[2]'))).text   
                        metragem = f.transforma(metragem)
                        #metragem = int(metragem)
                        #print("metragem = ", end='')                                                           
                        #print(metragem)
                        faixa = f.faixametragem(metragem)
                        #print("faixa de metragem = ", end='')                                                           
                        #print(faixa)
                        quartos = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[3]/div[7]/main/div[1]/div[4]/div[2]/section/table[{a}]/tbody/tr[{b}]/td[3]'))).text   
                        #print("quartos = ", end='')                                                           
                        #print(quartos)
                        banheiros = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[3]/div[7]/main/div[1]/div[4]/div[2]/section/table[{a}]/tbody/tr[{b}]/td[4]'))).text   
                        #print("banheiros = ", end='')                                                           
                        #print(banheiros)
                        garagem = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[3]/div[7]/main/div[1]/div[4]/div[2]/section/table[{a}]/tbody/tr[{b}]/td[5]'))).text   
                        #print("garagem = ", end='')                                                           
                        #print(garagem)

                        #print("lazer = ", end='')                                                           
                        #print(lazer)

                        #print("estagio = ", end='')                                                           
                        #print(estagio)
                        #print("lançamento = ", end='')                                                           
                        #print(lancamento)
                        #print("entrega = ", end='')                                                           
                        #print(entrega)
                        #print("total unidade = ", end='')                                                           
                        #print(total_uni)
                        #print("estoque = ", end='')                                                           
                        #print(estoque)
                        #print("unidades por andar = ", end='')                                                           
                        #print(uni_por_andar)
                        #print("numero de andares = ", end='')                                                           
                        #print(num_andar)
                        #print("atualizado = ", end='')                                                           
                        #print(atualizado)
                        now = datetime.now()
                        horario = now.strftime("%d/%m/%Y")
                        

                        dados_anuncios.append([cod,nome,end,nun_end,bairro,tipologia,preco,metragem,faixa,quartos,banheiros,garagem,lazer,estagio,lancamento,entrega,total_uni,estoque,uni_por_andar,num_andar,atualizado,horario,href])
     

                        b +=1 
                        #print("==================================================")
                    a +=1 
                    
                    #sleep(10)
                


                #sleep(500)
                
                
                #sleep(500)
                fechar_abas()
                item += 1
            
            else:
                fil += 1
                break
            
        
            dados = pd.DataFrame(dados_anuncios, columns=['codigo','nome','endereco','numero','bairro','tipologia','preco','metragem','faixa','quartos','banheiros','garagem','lazer','estagio','lancamento','entrega','total_unidades','estoque','unidades_por_andar','numero_andares','atualizado','data_scraping','url'])
            dados.to_csv(f'anuncios_orulo{pag}.csv', index=False)
            pag += 1

        if anum < 11:
            fil +=1
            break

        if fil == var_fil:
            #chama proxima pagina
            proxima()
            sleep(3)
        #proximo filtro de preço
    
print("pronto")
#login()                                                                /html/body/div[4]/div[7]/div/div/div[2]/div[2]/div[1]/div/div/div[4]
                                                                            