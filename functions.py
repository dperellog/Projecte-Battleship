from classes import *
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

def tuplaCoords(coord, mida):
    nums = "0123456789"
    cCorrecte = True
    coords = (0,"")
    if len(coord) > 1:
        for el in coord[:-1]:
            if el not in nums:
                cCorrecte = False
        if coord[-1] not in abc:
            cCorrecte = False
        if cCorrecte:
            if int(coord[:-1]) in list(range(mida)) and coord[-1] in abc[:mida]:
                coords = (coord[:-1],coord[-1])
    return coords

def tret(tauler, coords):
    coords = tuple([int(coords[0]), abc.index(coords[1])])
    casella = tauler.getCasella(coords)
    if not(casella.casellaOberta()):
        if casella.teVaixell():
            resultat = casella.getCasella().tocat()
            if resultat:
                nomVaixell = casella.getCasella().getNom()
                return 2
            else:
                return 1
        else:
            return 0
    else:
        return -1

def partida(tauler):
    print(f"Tauler (ID {tauler.getID()}): {tauler.getName()}.")
    print("Recorda! Per sortir del tauler, envia una coordenada buida!")
    casella = '00'
    while casella != '':
        if tauler.jugadorViu():
            if tauler.partidaGuanyada():
                return 1
            if tauler.videsActives():
                print(f'\nVides restants: {tauler.videsRestants()}')
            print('A disparar un tret!\n')
            tauler.mostraTauler()

            casella = input("Introdueix la coordenada (ej. 3J): ").upper()
            if casella != '':
                coords = tuplaCoords(casella, tauler.mida)
                if coords != (0,''):
                    resultat = tret(tauler, coords)
                    if resultat == 1:
                        print("TOCAT!")
                    elif resultat == 2:
                        print("TOCAT I ENFONSAT!")
                    elif resultat == 0:
                        print("AIGUA!")
                        tauler.restarVida()
                    elif resultat == -1:
                        print("Ja has descobert la coordenada!")
                else:
                    print("Coordenada incorrecte!")
        else:
            return 0
    return -1
    
