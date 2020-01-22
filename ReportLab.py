from reportlab.pdfgen import canvas

#Se crea o soporte deo documento
aux = canvas.Canvas("Proba de.pdf")

#Sobre este documento se pueden emplear una gran serie de elementos diferentes
#Con este de pasan coordenadas y un texto normal
#Esto escribe en una documento en las coordenadas que se le pasan el texto que tenemos escritos entre comillas dobles
aux.drawString(0, 0, "Posicion (x,y) = (0,0)")
aux.drawString(50, 100, "Posicion (x,y) = (50,100)")
aux.drawString(150, 50, "Posicion (x,y) = (150,50)")

#Esto permite introducir una imagen en nuestro doc
#Se le debe pasar le path de la imagen y la dimension de la imagen
aux.drawImage("/home/dam2/Imágenes/bed14325-5a43-48d4-a1d9-8c1b3541a5d3-profile_image-300x300.jpeg", 150, 300)






aux.showPage()
aux.save()
