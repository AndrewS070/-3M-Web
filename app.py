from flask import Flask, render_template
import turtle
import io
import base64
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    # Crear un canvas para turtle
    canvas = turtle.Screen()
    canvas.bgcolor("black")
    turtle.speed(0)
    turtle.hideturtle()

    # El código de dibujo con turtle
    turtle.goto(0, -40)

    # Dibujar hojas
    for i in range(16):
        for j in range(18):
            turtle.color('#FFA216')
            turtle.right(90)
            turtle.circle(150 - j * 6, 90)
            turtle.left(90)
            turtle.circle(150 - j * 6, 90)
            turtle.right(180)
        turtle.circle(40, 24)

    # Dibujar centro de la flor
    turtle.color('black')
    turtle.shape('circle')
    turtle.shapesize(0.5)
    turtle.fillcolor('#8B4513')
    golden_ang = 137.508
    phi = golden_ang * (3.141592653589793 / 180)

    for i in range(140):
        r = 4 * (i ** 0.5)
        theta = i * phi
        x = r * (cos(theta))
        y = r * (sin(theta))
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(i * golden_ang)
        turtle.pendown()
        turtle.stamp()

    # Definir puntos para dibujar letras
    def point(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color('black')
        turtle.fillcolor('#FFA216')
        turtle.begin_fill()
        turtle.circle(4)
        turtle.end_fill()

    # Función para dibujar 'T'
    def draw_T(x, y):
        positions_t = [(x, y + 30), (x + 6, y + 30), (x + 12, y + 30), (x + 18, y + 30), (x + 24, y + 30),
                       (x + 12, y + 30), (x + 12, y + 24), (x + 12, y + 18), (x + 12, y + 12), (x + 12, y + 6), (x + 12, y)]
        for pos in positions_t:
            point(*pos)

    # Función para dibujar 'Ú'
    def draw_U(x, y):
        positions_u = [(x, y + 30), (x, y + 24), (x, y + 18), (x, y + 12), (x, y + 6),
                       (x + 3, y + 3), (x + 6, y), (x + 12, y - 1), (x + 18, y), (x + 21, y + 3),
                       (x + 24, y + 6), (x + 24, y + 12), (x + 24, y + 18), (x + 24, y + 24), (x + 24, y + 30),
                       (x + 12, y + 36), (x + 16, y + 40)]
        for pos in positions_u:
            point(*pos)

    # Dibujar 'TÚ'
    draw_T(-27, -20)
    draw_U(7, -20)

    # Convertir el canvas de turtle en una imagen
    canvas.getcanvas().postscript(file='drawing.ps')
    img = Image.open('drawing.ps')
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    img_data = base64.b64encode(img_io.getvalue()).decode()

    # Devolver la plantilla HTML con la imagen
    return render_template('index.html', img_data=img_data)

if __name__ == '__main__':
    app.run(debug=True)
