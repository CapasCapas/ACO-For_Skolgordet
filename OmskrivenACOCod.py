import pygame
import random

KartaX = 100
KartaY = 200

#Kordinaten av spelaren
X = 0
Y = 0

#Variablar
MaxSlump = 100 
Nertramp = 2


Gride = [[1 for i in range(KartaY)]for j in range(KartaX)]
PersonligGride = [[1 for i in range(KartaY)]for j in range(KartaX)] 

#genererar ett slumpsesit numer 
Up = random.randrange(1,(MaxSlump+1))
Ner = random.randrange(1,(MaxSlump+1))
Hor = random.randrange(1,(MaxSlump+1))
Ver = random.randrange(1,(MaxSlump+1))
UpHor = random.randrange(1,(MaxSlump+1))
UpVer = random.randrange(1,(MaxSlump+1))
NerHor = random.randrange(1,(MaxSlump+1))
NerVer = random.randrange(1,(MaxSlump+1))


#Leger till rutpertierna som liger nära 
Up += (Gride[X][Y+1])
Ner += (Gride[X][Y-1])
Hor += (Gride[X+1][Y])
Ver += (Gride[X-1][Y])
UpHor += (Gride[X+1][Y+1])
UpVer += (Gride[X-1][Y+1])
NerHor += (Gride[X+1][Y-1])
NerVer += (Gride[X-1][Y-1])



