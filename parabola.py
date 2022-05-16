import math
import numpy as np

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
            delta = float((pow(b, 2)-(4*a*c)))
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
        elif a == 0 and b == 0 and c == 0:
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

    def notevoli():
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
        elif a == 0 and b == 0 and c == 0:
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

    def notevoli():
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
#Stesse cose per asse x

            


        

         
pa = Parabola_asse_x()  
print(pa.Disegno())


        
