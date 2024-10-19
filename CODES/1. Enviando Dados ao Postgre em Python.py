# IMPORTS
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

# Buscando Documento
caminho_do_arquivo = r"C:\Users\crist\Documents\Engenharia de dados com PYTHON\Arquivos\01. Postgree\Origem de dados\V_OCORRENCIA_AMPLA.json"
df=pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')

colunas = ['Numero_da_Ocorrencia', 'Classificacao_da_Ocorrência', 'Data_da_Ocorrencia','Municipio', 'UF', 'Regiao', 'Nome_do_Fabricante']
df = df[colunas]
df.rename(columns={'Classificacao_da_Ocorrência':'Classificacao_da_Ocorrencia'}, inplace = True)

# Criando Conexão com o Banco, usando Variável de ambiente .env
load_dotenv()

conn= psycopg2.connect(   
    dbname = os.getenv('dbname'),
    user = os.getenv('user'),
    password = os.getenv('password'),
    host = os.getenv('host'),
    port = os.getenv('port')
    )

#Habilitando cursor 
cur = conn.cursor()

#Deletando dados existentes
cur.execute(
    'delete from Anac'
)

#Subindo novos dados
for index,column in df.iterrows():
    cur.execute ("""INSERT INTO Anac 
    (     
                Numero_da_Ocorrencia, 
                Classificacao_da_Ocorrencia, 
                Data_da_Ocorrencia, 
                Municipio, 
                UF, 
                Regiao, 
                Nome_do_Fabricante
            ) VALUES (
                %s,%s,%s,%s,%s,%s,%s)""",
                (
                    column['Numero_da_Ocorrencia'],
                    column['Classificacao_da_Ocorrencia'],
                    column['Data_da_Ocorrencia'],
                    column['Municipio'],
                    column['UF'],
                    column['Regiao'],
                    column['Nome_do_Fabricante']
                )

                 )

conn.commit()
cur.close()
conn.close()



