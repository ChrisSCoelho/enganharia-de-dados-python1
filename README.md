### enganharia-de-dados-python1

##Buscando dados do ANAC (Agência Nacional de Aviação Civil), tratando e subindo para o POSTGRE.

#- Neste pequeno projeto, utilizamos o Python para fazer o carregamento dos dados, de uma pasta local para o Postgre.
  
#- Utilizamos algumas bibliotecas como PANDAS, PSYCOPG2 e PYTHON-DOTENV.

#- O Pandas tem várias funções, neste projeto o papel dele foi realizar toda a ingestão, tratamento e inserção dos dados no Banco de Destino.

#- Já o Psycopg2 teve o papel de realizar a conexão com o Postgre e através do cursor executar consultas SQL.

#- O Python-dotenv achei interessante, pois nele, criamos uma variável de ambiente, com os "requisitos" necessários para a conexão com o Banco de destino.
Um dos pontos positivos do arquivo .env é armazenar informações sensíveis como senhas, chaves de API e credenciais de banco de dados,
 sem precisar expor esses dados diretamente no código, realizando apenas o carregamento dessas variáveis.
