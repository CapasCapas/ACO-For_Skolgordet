import random
from tkinter import NE

from numpy import var
def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

def PrintMap():
    row = 0
    for x in Gride:
        idx = 0
        for y in x:
            if row == GoalX and idx == GoalY:
                print("*", end=" ")
            else:
                print(y,end = " ")
            idx += 1
        print()
        row += 1
    print()


from array import *
Xa = 10
Ya = 20
#max x och y
MXaxel = Xa - 1 
MYaxel = Ya - 1
X = 1
Y = 1
GoalX = 1
GoalY = 1
GoalMod = 10
Nertramp = 1
rep = 0
TilpacaVext = 0.5

Gride = [[0 for i in range(Ya)]for j in range(Xa)] 
def new_func(Gride, X, Y, GoalX, GoalY,rep):
    rep = 0
    while (X != GoalX) or (Y != GoalY):
    #genererar vilket värde sam den ska till 
        Up = random.randrange(1,101)
        Ner = random.randrange(1,101)
        Hor = random.randrange(1,101)
        Ver = random.randrange(1,101)
    #Här legs det till ma vägen är trampad 
        Gride[X][Y] += Nertramp
        
        Up = Up + Gride[X][Y+1]
        Ner = Ner + Gride[X][Y-1]
        Hor = Hor + Gride[X+1][Y]
        Ver = Ver + Gride[X-1][Y]
 
    
        if X > GoalX:
            Ver += GoalMod
        elif X < GoalX:
            Hor += GoalMod
        if Y > GoalY:
            Ner += GoalMod
        elif Y < GoalY:
            Up += GoalMod



        if (Up >= Ner) and (Up >= Hor) and (Up >= Ver):
        #Up är stölst 
            Y +=1
        elif (Ner >= Hor) and (Ner >= Ver):
        #Ner är störst
            Y -= 1
        elif (Hor >= Ver):
        #Hor är störst
            X += 1
        else:
        #Ver är störst
            X -= 1

        X = clamp(X, 1, MXaxel-1)
        Y = clamp(Y, 1, MYaxel-1)
        rep += 1
        print (rep)

l = 0
while l < 10: 
    new_func( Gride, X, Y, GoalX, GoalY,rep)
    print(l)
    print(rep)
    l += 1

