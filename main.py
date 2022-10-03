from classes import *
MIDATAULELL = 10
FLOTA = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
VIDES = 50
lang = ''
accio = 0


jocsActius = {}
taulerActual = 0

#- Funcions del programa -#

instruccions = {
    'ca' : {
        'banner-motd' : 
"""L\'objectiu és el seguent:
Busca i tomba tota la flota que hi ha amagada al taulell.

Per fer-ho, has d\'anar llançant trets a les coordenades que vulguis del taulell. Cada cop que llancis un tret, el joc et mostrarà el que hi havia amagat a aquella posició.
Pots jugar sense cap comptador de vides o, per fer-ho més entretingut, amb un comptador on cada vegada que trobis aigua et restarà una vida.

COMENÇEM!""",
        }
}


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
 
def nouTauler():
    global jocsActius
    global MIDATAULELL
    global FLOTA
    global VIDES



    sortir = False
    while not(sortir):
        vides = input("Vols jugar amb vides? [S/n]: ")
        if vides.upper() in "SN":
            sortir = True
    
    nomTauler = input("Introdueix un nom pel tauler: ")

    tauler = Tauler(MIDATAULELL,FLOTA,nomTauler,(VIDES if vides == 'S' else 0))
    jocsActius[tauler.getID] = tauler
    
    return tauler.getID

def jugada(tauler):
    global lang
    if tauler.jugadorViu():
        print(f"Tauler (ID {tauler.getID()}): {tauler.getName()}.")
        print(tauler.feedback('remaining',lang,tauler.videsRestants()))
        print(tauler.feedback('time-to-shot',lang))
        casella = ''
        while casella != '':
            casella = input()
    else:
        return True
"""
tauler = Tauler(MIDATAULELL,FLOTA)
tauler.colocarVaixells()
#tauler.mostraTauler()
tauler.feedback('banner-motd','ca','7')
"""


#- Programa principal: -#
print("""
# ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ #
#                                                   #
#    WELCOME TO BATTLESHIP! - By David Perelló      #
#                                                   #
# ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ #""")

while lang == '':
    lang = input('\nSelect a language [ca, es, en]: ')
    if lang not in ('ca'):
        lang = ''

print(instruccions[lang]['banner-motd'])

while lang == '':
    lang = input('\nSelect a language [ca, es, en]: ')
    if lang not in ('ca'):
        lang = ''

while accio != 3:
    accio = mostraMenu()
    
    if accio == 1:
        sortirPartida = False

        taulerActual = nouTauler()
        jugada(jocsActius[taulerActual])
            
            