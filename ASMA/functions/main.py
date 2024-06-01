import firebase_admin
from firebase_admin import credentials, db
import requests
import pandas as pd
import numpy as np
from datetime import datetime
import json
#from google.cloud import pubsub_v1

# Configuração do Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://asma-85af3-default-rtdb.firebaseio.com/'
})

def getdata(event, context):
    try:
        url = 'https://sistemasinter.cetesb.sp.gov.br/Ar/php/ar_resumo_hora.php'
        response = requests.get(url)
        df = pd.read_html(response.content)
        data = pd.DataFrame(df[4])

        del data['Unnamed: 1']
        data.rename(columns={'Unnamed: 0': 'Região', 'Unnamed: 2': 'Índice', 'Unnamed: 3': 'Poluente'}, inplace=True)

        conditions = [
            (data['Índice'] <= 40),
            (data['Índice'] > 40) & (data['Índice'] <= 80),
            (data['Índice'] > 80) & (data['Índice'] <= 120),
            (data['Índice'] > 120) & (data['Índice'] <= 200),
            (data['Índice'] > 200)
        ]
        values = ['Boa', 'Moderada', 'Ruim', 'Muito Ruim', 'Péssima']
        data['Qualidade'] = np.select(conditions, values)

        now = datetime.now()
        data['Data e Hora'] = now.strftime("%d-%m-%Y %H:%M")

        # Salvando os dados em um arquivo JSON temporário
        dados_hora = 'dadosHora.json'
        data.to_json(dados_hora, orient='records')

        with open(dados_hora, 'r') as f:
            data_dict = json.load(f)

        # Substituindo os dados existentes
        ref = db.reference('dadosHora')
        ref.set(data_dict)
        print('Dados da hora corrente atualizados')

        # Adicionando no Geral padrão
        geral_ref = db.reference('DadosGerais')
        for entry in data_dict:
            geral_ref.push(entry)
        print('Dados coletados e salvos no Geral')

        return "Dados atualizados com sucesso"
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return f"Ocorreu um erro: {e}", 500
