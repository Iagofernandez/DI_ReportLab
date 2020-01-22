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
obxTexto.setFont("Helvetica", 14)

for linha in frase:
   #Este realiza salto de linea
    obxTexto.textLine(linha)


    #Este codigo no realiza salto de linea
    #obxTexto.textOut(linha)


# Esto permite poner un color negro a la frase
# Cuanto mas cerca del 0.0 se pone negro absoluto
obxTexto.setFillGray(0.5)

# Texto escrito en varias lineas
textoLongo = """
      Este e un texto mais longo,
      escrito en varias liñas
      onde se recolles nunha cadea,
      única"""
obxTexto.textLines(textoLongo)

# Esta parte del codigo te permite conocer todos los tipos de letra que existen
obxTexto.setFillGray(0.5)

texto = "Exemplo de tipos de letra de reportlab"

# Bucle for que emplea el metodo getAvaliableFonts para recoger y imprimir una frase con cada uno de los tipos de letras
for tipo_letra in aux.getAvailableFonts():
    obxTexto.setFont(tipo_letra, 14)
    obxTexto.textLine(tipo_letra + ": " + texto)
# Permite la visualizacion del archivo
aux.drawText(obxTexto)
aux.showPage()
aux.save()
