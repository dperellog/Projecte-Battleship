from classes import *
import languages as get

MIDATAULELL = 10
FLOTA = [{'nom':'fleet/four','mida':4,'quantitat':1},
        {'nom':'fleet/three','mida':3,'quantitat':2},
        {'nom':'fleet/two','mida':2,'quantitat':3},
        {'nom':'fleet/one','mida':1,'quantitat':4}]
VIDES = 3
LLENGUATGES = ('ca', 'es', 'en')
lang = ''
accio = 0

jocsActius = {}
taulerActual = 0

#Funcions:
def mostraMenu():
    accio = 0
    get.text('menu/options',lang, mostrar=True)
    while accio == 0:
        accio = input(get.text('menu/select-option', lang))
        if accio.isnumeric():
            if int(accio) not in range(1,5):
                accio = 0
        else:
            accio = 0
    return int(accio)

def nouTauler(MIDATAULELL, FLOTA, VIDES):
    global jocsActius

    sortir = False
    while not(sortir):
        langTauler = input(get.text('playground/selectLang', lang, lang.upper(), LLENGUATGES)).lower()
        if langTauler in LLENGUATGES:
            sortir = True
        elif langTauler == '':
            langTauler = lang
            sortir = True

    sortir = False
    while not(sortir):
        vides = input(get.text('playground/playWLives', langTauler))
        if (langTauler in ('ca','es')) and (vides.upper() in "SN"):
            sortir = True
        if (langTauler in ('en')) and (vides.upper() in "YN"):
            sortir = True

    
    nomTauler = input(get.text('playground/enterName', langTauler))
    tauler = Tauler(MIDATAULELL,FLOTA,nomTauler,(0 if vides.upper() == 'N' else VIDES), langTauler)
    jocsActius[tauler.getID()] = tauler
    return str(tauler.getID())


def canviarIdioma():
    global lang
    lang = ''
    while lang == '':
        lang = input(f'\nSelect a language {LLENGUATGES}: ').lower()
        if lang not in LLENGUATGES:
            lang = ''

#- Programa principal: -#
canviarIdioma()

get.text('menu/welcome', lang, mostrar=True)

while accio != 4:
    accio = mostraMenu()
    
    if accio == 1:

        taulerActual = nouTauler(MIDATAULELL, FLOTA, VIDES)

        resultat = jocsActius[taulerActual].jugar()
        if resultat:
            del jocsActius[taulerActual]
            

    if accio == 2:
        if len(jocsActius) > 0:
            print("\n"+get.text('menu/activePlaygrounds', lang)+"\n")
            for tauler in jocsActius:
                get.text('playground/info', lang, tauler, jocsActius[tauler].getName(), mostrar=True)
            
            taulerCorrecte = False
            while not(taulerCorrecte):
                taulerID = input(get.text('menu/insertID', lang))
                if taulerID in jocsActius.keys():
                    taulerActual = taulerID
                    taulerCorrecte = True
                    
            resultat = jocsActius[taulerActual].jugar()
            if resultat:
                del jocsActius[taulerActual]
        else:
            get.text('errors/playgroundsNotFound', lang, mostrar=True)
    
    if accio == 3:
        canviarIdioma()