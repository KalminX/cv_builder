from weasyprint import HTML
HTML('https://weasyprint.org/').write_pdf('test.pdf')
print("WeasyPrint test successful")