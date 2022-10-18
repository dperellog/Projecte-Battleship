#=== IMPORTS ===#
#Importar les classes i el diccionari de llenguatges.
from classes import *
import languages as get

#=== CONSTANTS ===#
MIDATAULELL = 10
FLOTA = [{'nom':'fleet/four','mida':4,'quantitat':1},
        {'nom':'fleet/three','mida':3,'quantitat':2},
        {'nom':'fleet/two','mida':2,'quantitat':3},
        {'nom':'fleet/one','mida':1,'quantitat':4}]
VIDES = 50
LLENGUATGES = ('ca', 'es', 'en')

#=== VARIABLES ===#
lang = ''
jocsActius = {}
taulerActual = 0

#=== FUNCIONS ===#

#Funció que mostra el menú i permet al jugador seleccionar.
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
    return accio

#Funció que recull propietats de la partida i inicialitza un objecte Taulell.
def nouTauler(MIDATAULELL, FLOTA, VIDES):
    global jocsActius

    #Obtenir l'idioma del taulell.
    sortir = False
    while not(sortir):
        langTauler = input(get.text('playground/selectLang', lang, lang.upper(), LLENGUATGES)).lower()
        if langTauler in LLENGUATGES:
            sortir = True
        elif langTauler == '':
            langTauler = lang
            sortir = True

    #Obtenir si el jugador vol jugar amb vides o sense.
    sortir = False
    while not(sortir):
        vides = input(get.text('playground/playWLives', langTauler))
        if (langTauler in ('ca','es')) and (vides.upper() in "SN"):
            sortir = True
        if (langTauler in ('en')) and (vides.upper() in "YN"):
            sortir = True

    #Inicialitzar el taulell.
    nomTauler = input(get.text('playground/enterName', langTauler))
    tauler = Tauler(MIDATAULELL,FLOTA,nomTauler,(0 if vides.upper() == 'N' else VIDES), langTauler)
    jocsActius[tauler.getID()] = tauler
    
    #Retornar l'ID del taulell
    return str(tauler.getID())

#Funció que permet cambiar l'idioma general del programa (el menú).
def canviarIdioma():
    global lang
    lang = ''
    while lang == '':
        lang = input(f'\nSelect a language {LLENGUATGES}: ').lower()
        if lang not in LLENGUATGES:
            lang = ''

#=== PROGRAMA PRINCIPAL ===#
#Permet al jugador establir un idioma pel menú.
canviarIdioma()

get.text('menu/welcome', lang, mostrar=True)

#Realitzar l'acció associada a l'opció del menú:
accio = '0'
while accio != '4':
    accio = mostraMenu()
    
    #1->Iniciar nova partida:
    if accio == '1':

        taulerActual = nouTauler(MIDATAULELL, FLOTA, VIDES)

        resultat = jocsActius[taulerActual].jugar()
        
        #Si s'ha acabat la partida, eliminar el taulell de la llista.
        if resultat:
            del jocsActius[taulerActual]
            
    #2->Llistar i recuperar partida anterior:
    if accio == '2':
        #Mostrar les partides actuals:
        if len(jocsActius) > 0:
            print("\n"+get.text('menu/activePlaygrounds', lang)+"\n")
            for tauler in jocsActius:
                get.text('playground/info', lang, tauler, jocsActius[tauler].getName(), mostrar=True)
            
            #Permetre al jugador seleccionar el taulell per ID:
            taulerCorrecte = False
            while not(taulerCorrecte):
                taulerID = input(get.text('menu/insertID', lang))
                if taulerID in jocsActius.keys():
                    taulerActual = taulerID #Actualitzar el taulell actual.
                    taulerCorrecte = True
            
            #Jugar al taulell actual:
            resultat = jocsActius[taulerActual].jugar()
            
            #Si s'ha acabat la partida, eliminar el taulell de la llista.
            if resultat:
                del jocsActius[taulerActual]
        else:
            get.text('errors/playgroundsNotFound', lang, mostrar=True)
    
    #3->Canviar l'idioma principal:
    if accio == '3':
        canviarIdioma()