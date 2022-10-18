#Fitxer per afegir suport pels idiomes.

#Funció que retorna o printa una string segons idioma, nom i paràmetres.
def text(text, idioma, *p, mostrar=False):
        strPrint = "Text not found"
        text = text.split("/")
        if idioma in ('ca', 'es', 'en'):
                if len(text) == 1:
                        strPrint = lang[idioma][text[0]]
                elif len(text) == 2:
                        strPrint = lang[idioma][text[0]][text[1]]
        if len(p) == 1:
                strPrint = strPrint.format(p[0])
        elif len(p) == 2:
                strPrint = strPrint.format(p[0],p[1])
        if mostrar:
                print(strPrint)
        else:
                return(strPrint)

lang = {
        
        #IDIOMA CATALÀ:
        'ca' : {
        'menu': {
                'welcome' : """
# ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ # ~ X ~
#                                                         #
#    BENVINGUT A BATTLESHIP! - Fet per David Perelló      #
#                                                         #
# ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ # ~ X ~
""",
        'options' : """
=>Què vols fer?

1. Començar nova partida.
2. Recuperar partida anterior.
3. Canviar idioma.
4. Sortir del joc.
    """,        
                'select-option' : 'Tria una opció: ',
                'activePlaygrounds' : 'Partides actives:',
                'insertID' : 'Introdueix ID: ',
        },



        'playground': {
                'info' : 'Tauler {0}: {1}',
                'exitPlaygroundInfo' : 'Recorda! Per sortir del tauler, envia una coordenada buida!',
                'playWLives' : 'Vols jugar amb vides? [S/n]: ',
                'enterName' : 'Introdueix un nom pel identificar el tauler: ',
                'selectLang' : 'Selecciona un idioma {1} [{0}]: ',
                'time-to-shot': 'A disparar un tret!',
                'remaining' : "Vides restants: {0}",
                'insertCord' : 'Introdueix la coordenada (ej. 3J): ',
                'touched' : 'TOCAT!',
                'water' : 'AIGUA!',
                'sink' : 'HAS ENFONSAT {0}!',
                'winMessage' : 'FELICITATS! HAS GUANYAT!',
                'deathMessage' : 'Quina pena! El jugador ha mort!',

        },


        'fleet': {
                'four': 'un portaavions',
                'three': 'un cuirassat',
                'two' : 'una fragata',
                'one' : 'una patrullera'
        },

        'errors' : {
                'cordOpened' : 'Ja has descobert la coordenada!', 
                'playgroundsNotFound' : 'ERROR: No hi han partides actives! Comença una partida amb l\'opció 1.'
        }
        
        #IDIOMA CASTELLÀ:
        },'es':{
        'menu': {
                'welcome' : """
# ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ # ~ X ~ # ~
#                                                             #
#      BIENVENIDO A BATTLESHIP! - Hecho por David Perelló     #
#                                                             #
# ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ # ~ X ~ # ~
""",           
                'options' : """
=>¿Qué deseas hacer?

1. Empezar una nueva partida.
2. Recuperar una partida anterior.
3. Cambiar el idioma.
4. Salir del juego.
    """,        
                'select-option' : 'Elige una opción: ',
                'activePlaygrounds' : 'Partidas activas:',
                'insertID' : 'Introduce una ID: ',
        },



        'playground': {
                'info' : 'Tablero {0}: {1}',
                'exitPlaygroundInfo' : '¡Recuerda! Para salir del tablero, ¡escribe una coordenada vacía!',
                'playWLives' : '¿Deseas jugar con vidas? [S/n]: ',
                'enterName' : 'Introduce un nombre para identificar el tablero: ',
                'selectLang' : 'Selecciona un idioma {1} [{0}]: ',
                'time-to-shot': '¡A disparar!',
                'remaining' : "Vidas restantes: {0}",
                'insertCord' : 'Introduce una coordenada (ej. 3J): ',
                'touched' : '¡TOCADO!',
                'water' : '¡AGUA!',
                'sink' : '¡HAS HUNDIDO {0}!',
                'winMessage' : '¡FELICIDADES! ¡HAS GANADO!',
                'deathMessage' : '¡Qué pena! El jugador ha muerto!',

        },


        'fleet': {
                'four': 'un portaviones',
                'three': 'un acorazado',
                'two' : 'una fragata',
                'one' : 'una patrullera'
        },

        'errors' : {
                'cordOpened' : '¡Ya has descubierto esta coordenada!', 
                'playgroundsNotFound' : 'ERROR: ¡No se encuentran partidas activas! Empieza una partida seleccionando la opción 1.'
        }

        #IDIOMA ANGLÈS:
        },'en':{
        'menu': {
                'welcome' : """
# ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ #
#                                                   #
#    WELCOME TO BATTLESHIP! - By David Perelló      #
#                                                   #
# ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ X ~ # ~ #
""",            'options' : """
=>Choose an option:

1. Start a new game.
2. Recover an old game.
3. Change the language.
4. Exit.
    """,        
                'select-option' : 'Choose an option: ',
                'activePlaygrounds' : 'Active games:',
                'insertID' : 'Enter an ID: ',
        },



        'playground': {
                'info' : 'Playground {0}: {1}',
                'exitPlaygroundInfo' : 'Remember! To exit the playground, write an empty coordinate!',
                'playWLives' : 'Do you want to play with lives? [Y/n]: ',
                'enterName' : 'Enter a name for the playground: ',
                'selectLang' : 'Choose a language {1} [{0}]: ',
                'time-to-shot': '¡Time to shot!',
                'remaining' : "Remaining lives: {0}",
                'insertCord' : 'Enter a coordinate (ex. 3J): ',
                'touched' : 'REACHED!',
                'water' : 'WATER!',
                'sink' : '¡YOU\'VE SUNKED {0}!',
                'winMessage' : 'CONGRATULATIONS! YOU HAVE WIN!',
                'deathMessage' : 'What a pitty! The player has died!',

        },


        'fleet': {
                'four': 'an aircraft carrier',
                'three': 'a battleship',
                'two' : 'a frigate',
                'one' : 'a patrol boat'
        },

        'errors' : {
                'cordOpened' : '¡You\'ve already discovered this coordinate!', 
                'playgroundsNotFound' : 'ERROR: ¡No active games found! Start a new game choosing option 1.'
        }
}}



