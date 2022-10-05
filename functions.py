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