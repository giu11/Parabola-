import math
import numpy as np1


class Parabola_asse_x():
    def __init__(self):
        pass
        
    def Disegno(self):
        vertice = 0
        v = 0
        
        print("x = ay**2 +by +c")
        print("NOTA BENE: Se a<0 la concavità è rivolta vero sinistra ")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        x = 0
        if b== 0 and c == 0:
            vertice = "l'origine degli assi"
            delta = float((pow(b, 2)-(4*a)))
            inty1 = float(((-1*b)- math.sqrt(delta))/(2*a))
            inty2 = float((b- math.sqrt(delta))/(2*a))
            inty = f"le interezioni conl'asse delle y sono (0,{inty1}) e (0,{inty2} e l' intersezione con l'asse delle x è (0,0) )"

            return f'Il vertice è {vertice}, e {inty} '
        elif c == 0:
            x_vertice = float(-1*(pow(b, 2))/ 4 * a)
            y_vertice = float(-1*(b/2*a))
            intx = f"l'intersezione con l'asse delle x è (0,0)"
            delta = float(pow(b, 2)-(4*a*c))
            inty1 = float((-1*b)- math.sqrt(delta))/(2*a)
            inty2 = float((1*b)- math.sqrt(delta))/(2*a)
            inty = f"le interezioni conl'asse delle y sono (0,{inty1}) e (0,{inty2})"
            return f'Il vertice ha coordinate ({x_vertice}, {y_vertice}), {intx} e {inty}'
        elif a == 0:
            return f"L'equazione è inesistente prova a inserire dei numeri corretti"
        else:
            delta = float(pow(b, 2)-(4*a*c))
            x_vertice = float(-1* delta / 4* a)
            y_vertice = float(-1*(b/2*a))
            intx = f"L'intersezione con l'asse delle x è ({c},0)"
            inty1 = float((-1*b)- math.sqrt(delta))/(2*a)
            inty2 = float((1*b)- math.sqrt(delta))/(2*a)
            inty = f"le interezioni conl'asse delle y sono (0,{inty1}) e (0,{inty2})"
            return f'Il vertice ha coordinate ({x_vertice}, {y_vertice}), {intx} e {inty}'

    def notevoli(self):
        print("x = ay**2 +by +c")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        delta = float(pow(b, 2)-(4*a*c))
        yfuoco = float(-1*(b/2*a))
        xfuoco = float(1-delta)/ (4*a)
        asse = float(-1*(b/2*a))
        direttrice = float(-1*((1+delta)/(4*a)))
        return f"Il fuoco ha coordinate ({xfuoco}; {yfuoco}), l'asse di simmetria ha equazione y={asse}, la direttrice ha equzione x= {direttrice}  "
    def parametro():
        pass
class Parabola_asse_y():
    def __init__(self):
        pass
        
    def Disegno(self):
        vertice = 0
        v = 0
        
        print("y = ax**2 +bx +c")
        print("NOTA BENE: Se a<0 la concavità è vero rivolta verso il basso ")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        x = 0
        if b== 0 and c == 0:
            vertice = "l'origine degli assi"
            delta = float((pow(b, 2)-(4*a*c)))
            intx1 = float(((-1*b)- math.sqrt(delta))/(2*a))
            intx2 = float((b- math.sqrt(delta))/(2*a))
            inty = f"le interezioni conl'asse delle x sono ({intx1},0) e ({intx2},0) e l' intersezione con l'asse delle y è (0,0) )"

            return f'Il vertice è {vertice}, e {inty} '
        elif c == 0:
            y_vertice = float(-1*(pow(b, 2))/ 4 * a)
            x_vertice = float(-1*(b/2*a))
            inty = f"l'intersezione con l'asse delle y è (0,0)"
            delta = float(pow(b, 2)-(4*a*c))
            intx1 = float((-1*b)- math.sqrt(delta))/(2*a)
            intx2 = float((1*b)- math.sqrt(delta))/(2*a)
            intx = f"le interezioni conl'asse delle y sono (0,{intx1}) e (0,{intx2})"
            return f'Il vertice ha coordinate ({x_vertice}, {y_vertice}), {intx} e {inty}'
        elif a == 0:
            return f"L'equazione è inesistente prova a inserire dei numeri corretti"
        else:
            delta = float(pow(b, 2)-(4*a*c))
            y_vertice = float(-1* delta / 4* a)
            x_vertice = float(-1*(b/2*a))
            inty = f"L'intersezione con l'asse delle y è (0,{c})"
            intx1 = float((-1*b)- math.sqrt(delta))/(2*a)
            intx2 = float((1*b)- math.sqrt(delta))/(2*a)
            inty = f"le interezioni conl'asse delle y sono (0,{intx1}) e (0,{intx2})"
            return f'Il vertice ha coordinate ({x_vertice}, {y_vertice}), {intx} e {inty}'

    def notevoli(self):
        print("y = ax**2 +bx +c")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        delta = float(pow(b, 2)-(4*a*c))
        xfuoco = float(-1*(b/2*a))
        yfuoco = float(1-delta)/ (4*a)
        asse = float(-1*(b/2*a))
        direttrice = float(-1*((1+delta)/(4*a)))
        return f"Il fuoco ha coordinate ({xfuoco}; {yfuoco}), l'asse di simmetria ha equazione x={asse}, la direttrice ha equzione y= {direttrice}  "
    def parametro():
        pass

    
        
#Intersezione con gli assi --> Risolutore equazioni di secondo gardo 
#Fuoco
#X vertice 
# ASSe
#Stesse cose per asse xs       
    
print("Ciao benvenuto nel risolutore di paarbole ricorda che la PARABOLA è il luogo geometrico dei punti equidistanti da un punto fisso detto fucoe da una retta detta direttrice")         
tipo = int(input("Per risolvere la parabola con asse // all'asse delle y inserisci 1 sennò inserisci 0 per risolvere la parabola con asse // all'asse delle x "))
if tipo == 1:
        y = Parabola_asse_y()
        cosa = int(input("Se vuoi disegnare la parabola inserisci 1 se invece vuoi conoscere il fuoco, l'asse e la direttrice inserisci 0 "))
        if cosa == 1:
            print(y.Disegno())
        elif cosa == 0:
            print(y.notevoli())
        else: 
            print("VALORE ERRATO")
elif tipo == 0:
        x = Parabola_asse_x()
        cosa = int(input("Se vuoi disegnare la parabola inserisci 1 se invece vuoi conoscere il fuoco, l'asse e la direttrice inserisci 0 )"))
        if cosa == 1:
            print(x.Disegno())
        elif cosa == 0:
            print(x.notevoli())
        else: 
            print("VALORE ERRATO")

        



        


        
