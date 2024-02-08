import os
import pandas as pd

# Nome da pasta onde os arquivos CSV estão localizados
pasta_origem = 'arquivos_csv'

# Lista para armazenar os DataFrames de cada arquivo CSV
dfs = []

# Iterar sobre os arquivos na pasta
for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
        # Ler o arquivo CSV e adicionar ao DataFrame
        df = pd.read_csv(caminho_arquivo)
        dfs.append(df)

# Concatenar todos os DataFrames em um único DataFrame
df_final = pd.concat(dfs, ignore_index=True)

# Caminho para o arquivo CSV consolidado
arquivo_consolidado = 'consolidado.csv'

# Salvar o DataFrame consolidado em um arquivo CSV
df_final.to_csv(arquivo_consolidado, index=False)

print(f"Arquivo CSV consolidado salvo com sucesso em '{arquivo_consolidado}'.")
