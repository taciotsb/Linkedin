# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 19:33:11 2021

@author: tacio
"""

#importações dos pacotes
from selenium import webdriver
from time import sleep


# Parametros, variaveis e constantes





#Funcoes e classes
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://br.linkedin.com/jobs/cientista-de-dados-vagas?position=1&pageNum=0')
    resultados= driver.find_elements_by_class_name('result-card')
    
    lista_descricao=[]
    while True:    
        for r in resultados[len(lista_descricao):]:
            r.click()
            sleep(1)
            try:
                descricao = driver.find_element_by_class_name("description")
                lista_descricao.append(descricao.text)
            except:
                print("erro")
                pass
        resultados= driver.find_elements_by_class_name('result-card')
        
        print(f'numeros de resultados {len(resultados)}')
        print(f'quantidade de coleta {len(lista_descricao)}')
        
        if len(lista_descricao)==len(resultados):
            break
     
    print(len(lista_descricao))
    print(lista_descricao)
    descricao_salvar= '\n'.join(lista_descricao)
    with open ("descricoesvagas.txt",'w',encoding='utf-8') as f:
        f.write(descricao_salvar)
    driver.quit()     