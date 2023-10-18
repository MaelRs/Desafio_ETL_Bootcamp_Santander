#import pandas as pd
# Projeto realizado integralmente com extração de dados de arquivo CSV, devido a indisponibilidade das aplicações sugeridas pelo Professor durante a aula como Swagger, e API da SDW-2023.
#Repositório da API: https://github.com/digitalinovationone/santander-dev-week-2023-api
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app/api/users'


# Arquivo CSV para geração de lista de clientes.
df_client=pd.read_csv('SDW2023 (1).csv')
users_ids = df_client['Name'].tolist()
print(users_ids)
#df.head()
