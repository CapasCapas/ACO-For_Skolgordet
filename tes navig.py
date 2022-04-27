import random
from time import sleep
from tkinter import NE
import pygame



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
            
            if Gride[Xt][Yt] > 140:
                Gride[Xt][Yt] = Gride[Xt][Yt] / (TilpacaVext*4)
            elif Gride[Xt][Yt] > 1:
                Gride[Xt][Yt] = Gride[Xt][Yt] / TilpacaVext 
            Yt += 1
        Xt += 1

def SjärmUpdaterare(Xa, Ya, pixAr, GoalX, GoalY):
    Xt = 0
    while Xt < Xa:
        Yt = 0
        while Yt < Ya: 
            F = (Gride[Xt][Yt]) * 10
            F = clamp(F, 0, 254)
            Ferg = (F, F, F)
            if Gride[Xt][Yt] > 1: 
                pixAr[Xt][Yt] = Ferg
            elif Xt == GoalX and Yt == GoalY:
                pixAr[Xt][Yt] = (250,0,0)
            Yt += 1
        Xt += 1
    pygame.display.update()





from array import *
Xa = 150
Ya = 300
#max x och y
MXaxel = Xa - 1 
MYaxel = Ya - 1
X = 1
Y = 1
GoalX = 0
GoalY = 0
GoalMod = 30
Nertramp = 4
rep = 0
Black = (0,0,0)
TilpacaVext = 1.05
SlumpMax = 50
#[StartX, StartY, SlufX, SlutY]
StartOchSlutStelen = [[2, 4, 70, 150], [2, 250, 70, 150], [130, 4, 70, 150], [130, 250, 2, 4]]
Gride = [[1 for i in range(Ya)]for j in range(Xa)] 

pygame.init()
gameDisplay = pygame.display.set_mode((Xa, Ya))
gameDisplay.fill(Black)
pixAr = pygame.PixelArray(gameDisplay)
#för att updatter


def new_func(Gride, X, Y, GoalX, GoalY,rep):
    rep = 0
    MaxF = 2000
    while ((X != GoalX) or (Y != GoalY)) and rep < MaxF:
    #genererar vilket värde sam den ska till 
        Up = random.randrange(1,(SlumpMax+1))
        Ner = random.randrange(1,(SlumpMax+1))
        Hor = random.randrange(1,(SlumpMax+1))
        Ver = random.randrange(1,(SlumpMax+1))
    #Här legs det till ma vägen är trampad 
        Gride[X][Y] += Nertramp
        
        Up = Up + (Gride[X][Y+1])
        Ner = Ner + (Gride[X][Y-1])
        Hor = Hor + (Gride[X+1][Y])
        Ver = Ver + (Gride[X-1][Y])
 
    
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
    if rep == MaxF:
        print( )
    else:
        print (rep)

l = 0
ValAvStartOchSlut = 0 
while l < 100: 
    for a in StartOchSlutStelen :
        X = a[0]
        Y = a[1]
        GoalX = a[2]
        GoalY = a[3]
        new_func( Gride, X, Y, GoalX, GoalY,rep)
        #PrintMap()
        TillbackaVextning(Xa, Ya, TilpacaVext)
        SjärmUpdaterare(Xa, Ya, pixAr, GoalX, GoalY)
    #gameDisplay.fill(Black)
    l += 1

gameDisplay.fill(Black)
SjärmUpdaterare(Xa, Ya, pixAr, GoalX, GoalY)
sleep(1000)


