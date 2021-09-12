import pdfkit

# Converte o HTML em PDF utilizando o pdfkit
pdfkit.from_file(
    input='src/index.htm',
    output_path='saida.pdf',
    css='src/estilo.css',
    options={
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': 'UTF-8'
    }
)