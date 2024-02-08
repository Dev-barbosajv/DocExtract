import PyPDF3

def separar_paginas(pdf_path, paginas_para_separar, output_path_prefix):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF3.PdfFileReader(pdf_file)
        for pagina_numero in paginas_para_separar:
            if 0 < pagina_numero <= pdf_reader.numPages:
                output_pdf_path = f"{output_path_prefix}_pagina_{pagina_numero}.pdf"
                pdf_writer = PyPDF3.PdfFileWriter()
                pdf_writer.addPage(pdf_reader.getPage(pagina_numero - 1))
                with open(output_pdf_path, 'wb') as output_pdf_file:
                    pdf_writer.write(output_pdf_file)
                print(f"Página {pagina_numero} separada com sucesso em {output_pdf_path}")
            else:
                print(f"Erro: A página {pagina_numero} não existe no PDF.")

# Exemplo de uso:
pdf_path = 'pdfs_para_analise.pdf'
paginas_para_separar = list(range(1, 19))  # Lista de 1 a 18
output_path_prefix = 'pdfs'
separar_paginas(pdf_path, paginas_para_separar, output_path_prefix)
