# Enganharia-de-dados-python1

## Buscando dados do ANAC (Agência Nacional de Aviação Civil), tratando e subindo para o POSTGRE.

- Neste pequeno projeto, utilizamos o Python para fazer o carregamento dos dados, de uma pasta local para o Postgre.
- Utilizamos algumas bibliotecas como PANDAS, PSYCOPG2 e PYTHON-DOTENV.
- O Pandas tem várias funções, neste projeto o papel dele foi realizar toda a ingestão, tratamento e inserção dos dados no Banco de Destino.
- Já o Psycopg2 teve o papel de realizar a conexão com o Postgre e através do cursor executar consultas SQL.
- O Python-dotenv achei interessante, pois nele, criamos uma variável de ambiente, com os "requisitos" necessários para a conexão com o Banco de destino. Um dos pontos positivos do arquivo .env é armazenar informações sensíveis como senhas, chaves de API e credenciais de banco de dados, sem precisar expor esses dados diretamente no código, realizando apenas o carregamento dessas variáveis.

<h2 align="center">Segue Imagens do projeto com cada trecho de código:</h2>

<h3 align="center">Import</h3>
<div align="center">
<img src = "https://github.com/user-attachments/assets/5e0efe0a-0a46-4e61-84df-d6989599b40f"/>
</div>
<div align="center">Imports realizados para a execução das tarefas.</div>



<h3 align="center">Buscando os Dados na Origem</h3>
<div align="center">
<img src = "https://github.com/user-attachments/assets/fe8c8d46-2519-4680-993e-cce11a5313ef"/>
</div>
<div align="center">Neste projeto básico, buscamos dados de uma pasta local.</div>



<h3 align="center">Realizando a conexão com o Banco utilizando a Variável de Ambiente</h3>
<div align="center">
<img src = "https://github.com/user-attachments/assets/e3fb5ac4-9c9e-478b-ba4a-fe446e19bdda"/>
</div>
<div align="center">Utilizamos o python-dotenv para conectar ao banco usando variavel de ambiente, chamando as credenciais usando os.getenv.</div>



<h3 align="center">Habilitando o Cursor e Executando comandos SQL</h3>
<div align="center">
<img src = "https://github.com/user-attachments/assets/935c3808-bbdd-4fe1-bab6-be344001a8a0"/> 
</div>
<div align="center">Habilitar cursor, Deletar dados existentes na tabela, Inserir dados no banco de dados, Confirmar alterações, Fechar cursor e conexão.</div>



<h3 align="center">Script completo</h3>
<div align="center">
<img src = "https://github.com/user-attachments/assets/4a5261bf-53c9-4485-bfe0-3175b5f6d931"/>   
</div>
<div align="center">Fim!</div>
