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
import os
import pandas as pd
import numpy as np

class Data():
    
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
        
        output_data = 'dadosAr.json'
        
        if ext.upper() == 'JSON':
            if os.path.isfile('dadosAr.json'):
                data.to_json('dadosAr.json')
                print('Data overwritten to dadosAr.json')
            else:
                data.to_json('dadosAr.json')
                print('New file dadosAr.json created with data')
        elif ext.upper() == 'CSV':
            data.to_csv('dadosAr.csv')
            print("Exported to .CSV")
        else:
            return data

    getdata('csv')