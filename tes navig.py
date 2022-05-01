import random
from time import sleep
from tkinter import NE
import pygame
import multiprocessing


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

def TillbackaVextning(Xa, Ya, TilpacaVext, MaxNertramp):
    Xt = 0
    while Xt < Xa:
        Yt = 0
        while Yt < Ya: 
            #Max är maxtalet en ruta kan vara 
            
            #if Gride[Xt][Yt] > MaxNertramp:
            #    Gride[Xt][Yt] = MaxNertramp
            if Gride[Xt][Yt] > 1:
                Gride[Xt][Yt] = Gride[Xt][Yt] - TilpacaVext 
            Yt += 1
        Xt += 1

def SjärmUpdaterare(Xa, Ya, pixAr,pixArP,VisaKArta,VisaVargeVäg):
    gameDisplay.fill(Black)
    Xt = 0
    while Xt < Xa:
        Yt = 0
        while Yt < Ya: 
            F = (Gride[Xt][Yt]) * 30
            F = clamp(F, 0, 254)
            Ferg = (F, F, F)
            print(Gride[Xt][Yt])
            if Gride[Xt][Yt] > 1 and VisaKArta == 1: 
                pixAr[Xt][Yt] = Ferg
                print("tatta")

            if PGride[Xt][Yt] > 1 and VisaVargeVäg == 1: 
                pixArP[Xt][Yt] = (255,255,255)

            Yt += 1
        Xt += 1
    pygame.display.update()
    

#Överför den privata vägen till den glubala
def Hitarät(Xa, Ya,rep , PGride):
    
    Xt = 0
    while Xt < Xa:
        Yt = 0
        while Yt < Ya: 
            #Överför alla ruter till det glubala nätet  
            Gride[Xt][Yt] += (PGride[Xt][Yt])/ (rep+1)
            Yt += 1
        Xt += 1
    PGride = [[1 for i in range(Ya)]for j in range(Xa)]



from array import *
#spelyta och start och slut kordinater 
Xa = 150
Ya = 300
#start och slut kordinater 
#[StartX, StartY, SlufX, SlutY]
StartOchSlutStelen = [[6, 8, 70, 150], [6, 250, 70, 150], [130, 8, 70, 150], [130, 250, 6, 8]]



#Variablar som kan endras
GoalMod = 15
    #hur mycket den trampar ner 
Nertramp = 2
    #tilbackavexten efter varje gång
TilpacaVext = 1.5
    #maximala slumptalet
SlumpMax = 60
    #maximala antalet nertramp
MaxNertramp = 10000000
    #hur många steg myrena kan ta
MaxF = 900
    #hur många gånger den testar en väg
Försök = 1000

#Gui instelningar 
    #skriver ut försök
FörsökUt = 0
    #visar varje väg myran tar 
VisaVargeVäg = 1
    #visar Gride 
VisaKArta = 1
    #printar vilket försök den är på
PintFörsök = 0




#variablar som inte ska röras 
#max x och y
MXaxel = Xa - 1 
MYaxel = Ya - 1
X = 1
Y = 1
rep = 0
GoalX = 0
GoalY = 0
Black = (0,0,0)
#Rutnäten 
    #glubal Grid 
Gride = [[1 for i in range(Ya)]for j in range(Xa)] 
    #personlig grid
PGride = [[1 for i in range(Ya)]for j in range(Xa)] 


pygame.init()
gameDisplay = pygame.display.set_mode((Xa, Ya))
gameDisplay.fill(Black)
pixAr = pygame.PixelArray(gameDisplay)
#ektra sjärm
gameDisplayP = pygame.display.set_mode((Xa, Ya))
gameDisplayP.fill(Black)
pixArP = pygame.PixelArray(gameDisplayP)
#för att updatter


def new_func(Gride, X, Y, GoalX, GoalY, rep, MaxF,PGride, Xa, Ya, FörsökUt):
    rep = 0
    while ((X != GoalX) or (Y != GoalY)) and rep < MaxF:
    #genererar vilket värde sam den ska till 
        Up = random.randrange(1,(SlumpMax+1))
        Ner = random.randrange(1,(SlumpMax+1))
        Hor = random.randrange(1,(SlumpMax+1))
        Ver = random.randrange(1,(SlumpMax+1))
    #Här legs det till ma vägen är trampad 
        PGride[X][Y] += Nertramp
        
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
    if FörsökUt == 1:
        if rep == MaxF:
            print("[X]")
        else:
            print ("[*]",rep)  
    if rep < MaxF
        Hitarät(Xa, Ya,rep , PGride)

l = 0
ValAvStartOchSlut = 0 
while l < (Försök/4) or l == (Försök/4): 
    for a in StartOchSlutStelen :
        X = a[0]
        Y = a[1]
        GoalX = a[2]
        GoalY = a[3]
        PGride = [[1 for i in range(Ya)]for j in range(Xa)]
        new_func( Gride, X, Y, GoalX, GoalY, rep, MaxF,PGride, Xa, Ya, FörsökUt)
        #PrintMap()
        #gameDisplay.fill(Black)
        TillbackaVextning(Xa, Ya, TilpacaVext, MaxNertramp)
        SjärmUpdaterare(Xa, Ya, pixAr,pixArP,VisaKArta,VisaVargeVäg)
    if PintFörsök == 1:
        print(l*4)
    l += 1
print("Klar")
gameDisplay.fill(Black)
SjärmUpdaterare(Xa, Ya, pixAr,pixArP,VisaKArta,VisaVargeVäg)
sleep(1000)



