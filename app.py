import PyPDF3
import os
import re
import pandas as pd
import io
import csv
from flask import Flask, make_response, render_template, request, jsonify, redirect, url_for, session, send_file


app = Flask(__name__, template_folder='html', static_folder='css')
app.secret_key = 'sua_chave_secreta'


def extract_data_from_pdf(pdf_file):
    pdf_reader = PyPDF3.PdfFileReader(pdf_file)
    receita_pattern = r'(\d{4}-\d{2}\s-\s\w+-SEGUR.|\d{4}-\d{2}\s-\s\w+-PATRONAL|\d{4}-\d{2}\s-\s\w+-TERCEIROS|\d{4}-\d{2}\s-\s\w+)'
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


@app.route('/extrair_info', methods=['POST', 'GET'])
def extract_info():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    pdf_file = request.files['file']

    if pdf_file.filename.endswith('.pdf'):
        dados = extract_data_from_pdf(pdf_file)
        session['dados'] = dados
        return render_template('index.html', dados=dados)
       
    else:
        return jsonify({'error': 'O arquivo enviado não é um PDF'}), 400


@app.route('/export_csv', methods=['POST'])
def export_csv():
    try:
        dados = session.get('dados')
        if dados:
            # Criar um buffer de memória
            csv_buffer = io.StringIO()
            
            # Escrever os dados no buffer
            csv_writer = csv.writer(csv_buffer)
            csv_writer.writerow(['Receita', 'Pa Exerc', 'Dt Vcto', 'Vl Original', 'Sdo Devedor', 'Situação'])
            csv_writer.writerows(dados)
            
            # Criar uma resposta Flask com o conteúdo do buffer
            response = make_response(csv_buffer.getvalue())
            
            # Configurar os cabeçalhos da resposta para download do arquivo CSV
            response.headers['Content-Disposition'] = 'attachment; filename=dados.csv'
            response.headers['Content-Type'] = 'text/csv'
            
            # Limpar os dados da sessão após o download do CSV
            session.pop('dados', None)
            
            return response, 200
        else:
            return jsonify({'error': 'Nenhum dado para exportar em CSV'}), 400
    
    except Exception as e:
        print(f"Erro ao baixar arquivo CSV: {e}")
        return jsonify({'error': 'Erro ao baixar arquivo CSV'}), 500
            


@app.route('/')
def index():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True)