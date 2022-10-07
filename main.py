from classes import *
from functions import *

MIDATAULELL = 10
FLOTA = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
VIDES = 3
lang = ''
accio = 0

jocsActius = {}
taulerActual = 0

#- Programa principal: -#ca
while lang == '':
    lang = input('\nSelect a language [ca, es, en]: ')
    if lang not in ('ca'):
        lang = ''

#print(instruccions[lang]['banner-motd'])

while accio != 3:
    accio = mostraMenu()
    
    if accio == 1:
        sortirPartida = False

        taulerActual = nouTauler(jocsActius, MIDATAULELL, FLOTA, VIDES)
        resultat = partida(jocsActius[taulerActual])
        if resultat == 1:
            print("FELICITATS! HAS GUANYAT!")
        elif resultat == 0:
            print('El jugador ha mort!')
            
            