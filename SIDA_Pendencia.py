"""
Pendencia SIDA_PENDENCIA.

"""

import PyPDF3
import re
import pandas as pd

def extract_data_from_pdf(pdf_file):
    pdf_reader = PyPDF3.PdfFileReader(pdf_file)
    receita_pattern = r'\d+-[A-Z]+'
    inscricao_pattern = r'\d{2}\.\d\.\d{2}\.\d{6}-\d{2}'
    dt_vcto_pattern = r'(\d{2}/\d{2}/\d{4})'
    vl_original_pattern = r'(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)'
    sdo_devedor_pattern = r'(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)'
    situacao_pattern = r'(DEVEDOR|PENDENTE|PAGO)'
    
    data = []
    
    for pagina_numero in range(pdf_reader.numPages):
        texto_da_pagina = pdf_reader.getPage(pagina_numero).extractText()
        print(f'TEXTO DA PAGINA: {texto_da_pagina}')
        for match in re.finditer(f"Receita: {receita_pattern}\s+{inscricao_pattern}\s+{dt_vcto_pattern}\s+{vl_original_pattern}\s+{sdo_devedor_pattern}\s+{situacao_pattern}", texto_da_pagina):
            receita, pa_exerc, dt_vcto, vl_original, sdo_devedor, situacao = match.groups()
            data.append((receita, pa_exerc, dt_vcto, vl_original, sdo_devedor, situacao))
    return data

# Caminho do arquivo PDF
caminho_arquivo_pdf = 'PDF_SIEF_PENDENCIA\pdfs_pagina_7.pdf'

# Extraindo dados do PDF
dados_pdf = extract_data_from_pdf(caminho_arquivo_pdf)
print(f'AQUI ESTÁ OS DADOS DO PDF: {dados_pdf}')
# Criando um DataFrame com os dados coletados do arquivo PDF
df = pd.DataFrame(dados_pdf, columns=['Receita', 'PA/Exerc', 'Dt. Vcto', 'Vl.Original', 'Sdo.Devedor', 'Situação'])

# Imprimindo o DataFrame
print(df)

