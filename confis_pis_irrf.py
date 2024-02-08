"""
EXTRAINDOS RECEITAS DE IRRF, PIS, COFINS
"""

import PyPDF3
import re
import pandas as pd
import os

def extract_data_from_pdf(pdf_file):
    pdf_reader = PyPDF3.PdfFileReader(pdf_file)
    receita_pattern = r'(\d{4}-\d{2}\s-\s\w+)'
    pa_exerc_pattern = r'(\d{2}/\d{4})'
    dt_vcto_pattern = r'(\d{2}/\d{2}/\d{4})'
    vl_original_pattern = r'(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)'
    sdo_devedor_pattern = r'(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)'
    # Adicionar parametros
    situacao_pattern = r'(DEVEDOR|PENDENTE|PAGO)' #
    
    
    data = []

    for pagina_numero in range(pdf_reader.numPages):
        texto_da_pagina = pdf_reader.getPage(pagina_numero).extractText()

        for match in re.finditer(f"{receita_pattern}\s+{pa_exerc_pattern}\s+{dt_vcto_pattern}\s+{vl_original_pattern}\s+{sdo_devedor_pattern}\s+{situacao_pattern}", texto_da_pagina):
            receita, pa_exerc, dt_vcto, vl_original, sdo_devedor, situacao = match.groups()
            data.append((receita, pa_exerc, dt_vcto, vl_original, sdo_devedor, situacao))

    return data

# Diretório onde estão localizados os arquivos PDF
diretorio = 'Pdfs_1'

# Lista para armazenar os dados de todos os arquivos PDF
todos_os_dados = []

# Iterar sobre os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith('.pdf'):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        dados_pdf = extract_data_from_pdf(caminho_arquivo)
        todos_os_dados.extend(dados_pdf)

# Criando um DataFrame com os dados coletados de todos os arquivos PDF
df = pd.DataFrame(todos_os_dados, columns=['Receita', 'PA/Exerc', 'Dt. Vcto', 'Vl.Original', 'Sdo.Devedor', 'Situação'])

# Nome da pasta para salvar os arquivos CSV
pasta_destino = 'arquivos_csv'

# Verificar se a pasta destino existe, caso contrário, criar
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Caminho completo para a pasta destino
caminho_pasta_destino = os.path.join(os.getcwd(), pasta_destino)

# Salvando o DataFrame em um arquivo CSV dentro da pasta destino
nome_arquivo_csv = 'receitas_pis.csv'
caminho_arquivo_csv = os.path.join(caminho_pasta_destino, nome_arquivo_csv)
df.to_csv(caminho_arquivo_csv, index=False)

print(f"Arquivo CSV salvo com sucesso em '{caminho_arquivo_csv}'.")
print(df)






df.to_csv('confis_pis_irrf.csv', index=False)
print("Arquivo CSV salvo com sucesso.")
print(df)
