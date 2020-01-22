from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

# Lista de objetos
guion = []

# Similar al anterior ejercicio, introducir una imagen
# Se le pasa en este orden
# Posicion x, posicion y , ancho y alto de la imagen y path de la imagen
imaxe = Image(0, 00, 300, 300, "/home/dam2/Imágenes/bed14325-5a43-48d4-a1d9-8c1b3541a5d3-profile_image-300x300.jpeg")

# Ahora a partir de la imagen se crea el dibujo
debuxo = Drawing(30, 30)
# Al dibujo se le ha añadido la imagen
debuxo.add(imaxe)
debuxo.translate(0, 600)
# A nuestra lista de objetos se le ha añadido un nuevo objeto
guion.append(debuxo)

debuxo = Drawing(30, 30)
debuxo.add(imaxe)
# Esto rota la imagen 45 grados
debuxo.rotate(45)
guion.append(debuxo)
# Escala para X e Y
debuxo.scale(1.5, 0.5)
guion.append(debuxo)
# Se mueve de sitio la imagen
debuxo.translate(-90, 300)
guion.append(debuxo)

debuxo = Drawing(0, 0)
debuxo.add(imaxe)
debuxo.rotate(90)
debuxo.translate(-20, -100)
guion.append(debuxo)


# Ancho y alto de un documento A4
debuxo = Drawing(A4[0], A4[1])
# Recorremos el guion y se van añadiendo al deb todos los dibujos que se crearon
for deb in guion:
    debuxo.add(deb)

# Se crea un nuevo documento PDF donde se mostrará todos los dibujos
renderPDF.drawToFile(debuxo, "probaPDF2.pdf")
