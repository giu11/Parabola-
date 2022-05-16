import math
import numpy as np

class Parabola_asse_x():
    def __init__(self):
        pass
        
    def Disegno(self):
        vertice = 0
        v = 0
        print("y = ax**2 +bx +c")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        x = 0
        if b== 0 and c == 0:
            vertice = "l'origine degli assi"
            intx = f"l'intersezione con l'asse delle x è ({c},0)"
            delta = float((pow(b, 2)-(4*a*c)))
            inty1 = float(((-1*b)- delta)/(2*a))
            inty2 = float(((1*b)- delta)/(2*a))
            inty = f"le interezioni conl'asse delle y sono ({inty1}, 0) e ({inty2}, 0)"

            return f'Il vertice è {vertice},{intx} e {inty} '
        elif c == 0:
            x_vertice = float(-1*(pow(b, 2))/ 4 / a)
            y_vertice = float(-1*(b/2*a))
            intx = f"l'intersezione con l'asse delle x è ({c},0)"
            delta = float(pow(b, 2)-(4*a*c))
            inty1 = float((-1*b)- delta)/(2*a)
            inty2 = float((1*b)- delta)/(2*a)
            inty = f"le interezioni conl'asse delle y sono (0,{inty1}) e (0,{inty2})"
            return f'Il vertice ha coordinate ({x_vertice}, {y_vertice}), {intx} e {inty}'
        else:
            delta = float(pow(b, 2)-(4*a*c))
            x_vertice = float(-1* delta / 4/ a)
            y_vertice = float(-1*(b/2*a))
            intx = f"L'intersezione con l'asse delle x è ({c},0)"
            inty1 = float((-1*b)- delta)/(2*a)
            inty2 = float((1*b)- delta)/(2*a)
            inty = f"le interezioni conl'asse delle y sono (0,{inty1}) e (0,{inty2})"
            return f'Il vertice ha coordinate ({x_vertice}, {y_vertice}), {intx} e {inty}'

    def notevoli():
        print("y = ax**2 +bx +c")
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
    
        
#Intersezione con gli assi --> Risolutore equazioni di secondo gardo 
#Fuoco
#X vertice 
# ASSe
#Stesse cose per asse x

            


        

         
pa = Parabola_asse_x()  
print(pa.Disegno())


        