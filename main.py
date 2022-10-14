from classes import *
from functions import *

MIDATAULELL = 10
FLOTA = [{'nom':'un portaavions','mida':4,'quantitat':1},
        {'nom':'un cuirassat','mida':3,'quantitat':2},
        {'nom':'una fragata','mida':2,'quantitat':3},
        {'nom':'una patrullera','mida':1,'quantitat':4}]
VIDES = 3
lang = ''
accio = 0

jocsActius = {}
taulerActual = 0

#Funcions:
def mostraMenu():
    accio = 0
    print("""
=>Què vols fer?

1. Començar nova partida.
2. Recuperar partida anterior.
3. Sortir del joc.
    """)
    while accio == 0:
        accio = input("Tria una opció: ")
        if int(accio) not in range(1,4):
            accio = 0
    return int(accio)

def nouTauler(MIDATAULELL, FLOTA, VIDES):
    global jocsActius

    sortir = False
    while not(sortir):
        vides = input("Vols jugar amb vides? [S/n]: ")
        if vides.upper() in "SN":
            sortir = True
    nomTauler = input("Introdueix un nom pel tauler: ")
    tauler = Tauler(MIDATAULELL,FLOTA,nomTauler,(VIDES if vides == 'S' else 0))
    jocsActius[tauler.getID()] = tauler
    return str(tauler.getID())



#- Programa principal: -#ca
while lang == '':
    lang = input('\nSelect a language [ca, es, en]: ')
    if lang not in ('ca'):
        lang = ''

#print(instruccions[lang]['banner-motd'])

while accio != 3:
    accio = mostraMenu()
    
    if accio == 1:

        taulerActual = nouTauler(MIDATAULELL, FLOTA, VIDES)

        resultat = jocsActius[taulerActual].jugar()
        if resultat == 1:
            print('El jugador ha mort!')
        elif resultat == 2:
            print("FELICITATS! HAS GUANYAT!")
            

    if accio == 2:
        taulers = []
        for tauler in jocsActius.keys():
            taulers += jocsActius[tauler].getMatriu()

        for i in range(2):
            for k in range(len(taulers)):
                for j in range(3):
                    #print(str(taulers[k][i][j]), end=' ')
                    print(k,i,j, end=' ')
                print('   ', end='')
            print()