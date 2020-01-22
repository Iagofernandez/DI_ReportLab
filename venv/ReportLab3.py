from reportlab.pdfgen import canvas

# Escritura en un archivo de texto
# Se lamacena lo que se quiere escribir en un array y se almacena
frase = ["O patio da miña casa", "cando chove se molla", "como as demais"]

# Craecion del archivo en el que queremos escribir
aux = canvas.Canvas("probaTexto.pdf")

# Se posiciona donde se empieza a escribir las lineas de texto en nuestro archivo
# Tmabien se indica el tipo de letra que se usará
obxTexto = aux.beginText()
obxTexto.setTextOrigin(100, 300)
obxTexto.setFont("Courier", 14)
for linha in frase:
    obxTexto.textLine(linha)

obxTexto.setFillGray(0.5)

# Permite la visualizacion del archivo
aux.drawText(obxTexto)
aux.showPage()
aux.save()
