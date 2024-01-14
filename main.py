from FilaCircularInternet import MyCircularQueue
import turtle
import time


def desenharNomes(quant, nomes):
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    parteCirculo = 360 / quant
    turtle.goto(0, -20*quant)
    for nome in nomes:
        turtle.write(nome, font=("Verdana", 8, "normal"))
        turtle.circle(20*quant,parteCirculo)
    turtle.goto(0, -80 - 20*quant)
    for nome in nomes:
        turtle.fillcolor("Yellow")
        turtle.circle(80 + 20*quant, parteCirculo)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(10)
        turtle.penup()
        turtle.right(90)
        turtle.pendown()
        turtle.fd(5)
        turtle.left(90)
        turtle.fd(10)
        turtle.backward(10)
        turtle.right(180)
        turtle.fd(10)
        turtle.backward(10)
        turtle.left(90)
        turtle.fd(10)
        turtle.left(45)
        turtle.fd(10)
        turtle.backward(10)
        turtle.right(90)
        turtle.fd(10)
        turtle.backward(10)
        turtle.left(45)
        turtle.penup()
        turtle.backward(15)
        turtle.left(90)
        turtle.backward(10)
    if quant == 1:
        turtle.goto(0,0)
        turtle.showturtle()
        turtle.speed(1)
        turtle.shape("turtle")
        turtle.color("green")
        turtle.fd(50)
        turtle.backward(100)
        turtle.fd(100)
        turtle.backward(100)
        turtle.fd(50)
        turtle.color("Yellow")
        turtle.left(450)
        turtle.color("green")
        turtle.backward(80 + 20*quant)
        turtle.color("blue")
        for x in range(3):
            time.sleep(1)
            turtle.speed(2)
            turtle.fd(50)
            turtle.speed(1)
            turtle.backward(50)


def andarBomba(quant, passar):
    parteCirculo = 360 / quant
    turtle.speed(0)
    turtle.goto(0, -20*quant)
    turtle.speed(3)
    turtle.showturtle()
    for i in range(passar):
        turtle.shape("turtle")
        turtle.color("green")
        turtle.circle(20*quant,parteCirculo)
    turtle.color("Yellow")
    turtle.speed(1)
    turtle.left(720)
    turtle.reset()

nomes = []
while True:
    nome = turtle.textinput("Batata Quente","Digite o nome do participante ou digite 0 para continuar: ")
    if nome == '0':
        break
    else:
        nomes.append(nome)

fila = MyCircularQueue(len(nomes))
for nome in nomes:  
    fila.enqueue(nome)


desenharNomes(fila.size,nomes)

num = 0
numAnt = 0
somar = 0

while True:
    if fila.size > 1:
        #print("Participantes restantes: ")
        #fila.printCQueue()
        print(fila.lista())
        num = int(turtle.numinput("Batata Quente","Digite o número de vezes que a batata quente será passada: "))
        andarBomba(fila.size, num)
        for j in range(num):
            fila.mudarLugar()
        
        

        perdedor = fila.dequeue()
        nomes = fila.lista()
        turtle.TK.messagebox.showinfo(title="Batata Quente:", message=f"{perdedor} foi eliminado")
        #print(f"{perdedor} foi eliminado")
        turtle.clear()
        desenharNomes(fila.size,nomes)
        print("")
    else:
        ganhador = fila.dequeue()
        turtle.TK.messagebox.showinfo(title="Batata Quente:", message=f"{ganhador} ganhou")
        #print(f"{ganhador} ganhou")
        break