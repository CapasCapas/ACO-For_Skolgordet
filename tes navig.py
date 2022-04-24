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
            elif row == X and idx == Y:
                print("X", end=" ")
            else:
                print(y,end = " ")
            idx += 1
        print()
        row += 1
    print()

def TillbackaVextning(Xa, Ya, TilpacaVext):
    Xt = 0
    while Xt < Xa:
        Yt = 0
        while Yt < Ya: 
            if Gride[Xt][Yt] > 1:
                Gride[Xt][Yt] = Gride[Xt][Yt] / TilpacaVext 
            Yt += 1
        Xt += 1




from array import *
Xa = 15
Ya = 30
#max x och y
MXaxel = Xa - 1 
MYaxel = Ya - 1
X = 1
Y = 1
GoalX = 0
GoalY = 0
GoalMod = 20
Nertramp = 2
rep = 0
TilpacaVext = 2
#[StartX, StartY, SlufX, SlutY]
StartOchSlutStelen = [[2, 4, 13, 25], [2, 25, 4, 13], [13, 4, 2, 25], [13, 25, 2, 4]]

Gride = [[1 for i in range(Ya)]for j in range(Xa)] 
def new_func(Gride, X, Y, GoalX, GoalY,rep):
    rep = 0
    while ((X != GoalX) or (Y != GoalY)) and rep < 1000:
    #genererar vilket värde sam den ska till 
        Up = random.randrange(1,31)
        Ner = random.randrange(1,31)
        Hor = random.randrange(1,31)
        Ver = random.randrange(1,31)
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
ValAvStartOchSlut = 0 
while l < 20: 
    for a in StartOchSlutStelen :
        X = a[0]
        Y = a[1]
        GoalX = a[2]
        GoalY = a[3]
        new_func( Gride, X, Y, GoalX, GoalY,rep)
        #PrintMap()
        TillbackaVextning(Xa, Ya, TilpacaVext)
    l += 1
    


