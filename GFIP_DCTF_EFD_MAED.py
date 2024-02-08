"""
EXTRAINDO VALORES DE RECEITA:
    GFIP - MULTA ATR - OK
    DCTF - MULTA ATR - OK
    EFD - PIS/COFINS - OK
    MAED - DCTFWEB - OK
"""


import PyPDF3
import re
import pandas as pd
import os

print("APENAS GFIP - MULTA ATR  /  DCTF - MULTA ATR / EFD - PIS/COFINS / MAED - DCTFWEB")

pdf_reader = PyPDF3.PdfFileReader('Pdfs_1\IRRF_PIS_COFINS_AND_OUTROS_PART2.pdf')

# Padrão regex para extrair linhas contendo as receitas específicas
pattern = r'(\d{4}-\d{2}\s-\s(?:GFIP\s-\sMULTA\sATR|DCTF\s-\sMULTA\sATR|EFD\s-\sPIS/COFINS|MAED\s-\sDCTFWEB))\s+(\d{2}/\d{2}/\d{4})\s+(\d{2}/\d{2}/\d{4})\s+(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)\s+(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)\s+(DEVEDOR|PENDENTE|PAGO)'

data = []

for pagina_numero in range(pdf_reader.numPages):
    texto_da_pagina = pdf_reader.getPage(pagina_numero).extractText()

    for match in re.finditer(pattern, texto_da_pagina):
        receita, pa_exerc, dt_vcto, vl_original, sdo_devedor, situacao = match.groups()
        data.append((receita, pa_exerc, dt_vcto, vl_original, sdo_devedor, situacao))

# Criando um DataFrame com os dados coletados
df = pd.DataFrame(data, columns=['Receita', 'PA/Exerc', 'Dt. Vcto', 'Vl.Original', 'Sdo.Devedor', 'Situação'])

pasta_destino = 'arquivos_csv'

# Verificar se a pasta destino existe, caso contrário, criar
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Caminho completo para a pasta destino
caminho_pasta_destino = os.path.join(os.getcwd(), pasta_destino)

# Salvando o DataFrame em um arquivo CSV dentro da pasta destino
nome_arquivo_csv = 'gfip.csv'
caminho_arquivo_csv = os.path.join(caminho_pasta_destino, nome_arquivo_csv)
df.to_csv(caminho_arquivo_csv, index=False)

print(f"Arquivo CSV salvo com sucesso em '{caminho_arquivo_csv}'.")
print(df)