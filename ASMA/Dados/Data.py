#from bs4 import BeautifulSoup 
#import requests
#Alternative method
#def beautifulsoup():
    #url = "https://sistemasinter.cetesb.sp.gov.br/Ar/php/ar_resumo_hora.php"
    #html = requests.get(url).content
    #soup = BeautifulSoup(html, "lxml")
    #print(soup.prettify())
    #table = soup.find("table", class_ = "font01")
    #print(table.prettify())

import json
import pandas as pd
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db as firebase_db
from datetime import datetime 

#-------------------------------------------------------------------------------------------------------


#chave pra acessar o Banco de dados
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://asma-85af3-default-rtdb.firebaseio.com/'
})

#requisição Rest para puchar os dados da Cetesb
class Data():
    @staticmethod
    def getdata(ext):
        df = pd.read_html('https://sistemasinter.cetesb.sp.gov.br/Ar/php/ar_resumo_hora.php')
        data = pd.DataFrame(df[4])
    
        del data['Unnamed: 1']
        data.rename(columns={'Unnamed: 0':'Região', 'Unnamed: 2': 'Índice', 'Unnamed: 3': 'Poluente'}, inplace=True)
    
        conditions = [
            (data['Índice'] <=40),
            (data['Índice'] >40) & (data['Índice'] <=80),
            (data['Índice'] >80) & (data['Índice'] <=120),
            (data['Índice'] >120) & (data['Índice'] <=200),
            (data['Índice'] >200)
        ]
        values = ['Boa', 'Moderada', 'Ruim', 'Muito Ruim', 'Péssima']
        data['Qualidade'] = np.select(conditions, values)

        now = datetime.now()
        data['Data e Hora'] = now.strftime("%d-%m-%Y %H:%M")
        
#---------------------------------------------------------------
        
        #Salvando os dados em um arquivo JSON temporário
        dados_hora= 'dadosHora.json'
        data.to_json(dados_hora, orient='records')
        
        if ext.upper() == 'FIREBASE':
            with open(dados_hora, 'r') as f:
                data_dict = json.load(f)

            #Substituituidno os dados existentes
            firebase_db.reference('dadosHora').set(data_dict)
            print('Dados da hora corrente atualizados')

#----------------------------------------------------------------

            #Add no Geral padrão
            for entry in data_dict:
                firebase_db.reference('DadosGerais').push(entry)
            print('Dados coletados e salvos no Geral')
                
        elif ext.upper() == 'CSV':
            data.to_csv('dadosHora.csv')
            print("Exported to .CSV")
        else:
            return data

# Uso da função
Data.getdata('firebase')

