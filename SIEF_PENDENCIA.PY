"""
Pendência - Processo Fiscal (SIEF)

"""


import PyPDF3
import re
import pandas as pd
import os

def extract_data_from_pdf(pdf_file, pattern):
    pdf_reader = PyPDF3.PdfFileReader(pdf_file)

    data = []

    for pagina_numero in range(pdf_reader.numPages):
        texto_da_pagina = pdf_reader.getPage(pagina_numero).extractText()

        for match in re.finditer(pattern, texto_da_pagina):
            processo, situacao, localizacao = match.groups()
            data.append((processo, situacao, localizacao))

    return data

# Diretório onde estão localizados os arquivos PDF
diretorio = 'PDF_SIEF_PENDENCIA'

# Lista para armazenar os dados de todos os arquivos PDF
todos_os_dados = []

# Regex fornecido
pattern = r'(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})\s+(DEVEDOR)\s+(.+)\n'


# Iterar sobre os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith('.pdf'):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        dados_pdf = extract_data_from_pdf(caminho_arquivo, pattern)
        todos_os_dados.extend(dados_pdf)

# Criando um DataFrame com os dados coletados de todos os arquivos PDF
df = pd.DataFrame(todos_os_dados, columns=['Processo', 'Situação', 'Localização'])

# Imprimindo o DataFrame
print(df)