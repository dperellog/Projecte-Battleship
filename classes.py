#=== IMPORTS ===#
import random
import languages as get

#=== CLASSE TAULER ===#
class Tauler(object):
    tIDs = 0 #Propietat global que compta el número de taulells que s'han creat.
    
    #Constants de classe ("helpers"):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"

    #Constructor:
    def __init__(self, mida, vaixells=[], nomJugador='', vides=0, lang='ca'):
        #Definir propietats base:
        self.__class__.tIDs +=1
        self.tID = self.__class__.tIDs
        self.nomJugador = nomJugador
        self.lang = lang
        self.mida = mida
        self.vides = vides
        self.videsActivades = (vides > 0)
        self.llVaixells = vaixells
        self.vaixellsActius = 0
        self.jocAcabat = False

        #Inicialitzar la matriu:
        self.matriu = self.iniciarTauler(self.mida)

        #Poblar la matriu:
        self.colocarVaixells()


    #Metodes per obtenir atributs des de l'exterior:
    def getID(self):
        return str(self.tID)

    def getName(self):
        return self.nomJugador

    def getCasella(self, coords):
        #Obtenir el contingut de la casella (retorna un objecte tipus Casella).
        return self.matriu[coords[0]][coords[1]]

    def getMatriu(self):
        return self.matriu

    def jugadorViu(self):
        if self.videsActivades:
            return self.vides > 0
        else:
            return True
    
    def videsRestants(self):
        return self.vides

    def videsActives(self):
        return self.videsActivades

    def restarVida(self):
        self.vides -= 1



    #Metodes del tauler:
    def iniciarTauler(self, mida):
        return [[Casella() for j in range(mida)] for i in range(mida)]

    def mostraTauler(self, dev=False):
        espais = len(str(self.mida))
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #Imprimir índex abecedari:
        print(" "*espais, end=" ")
        for lletra in abc[:self.mida]:
            print(f"{lletra} ", end="")
        print()

        #Imprimir files amb índex numeric.
        f = 0
        for fila in self.matriu:
            if len(str(f)) != espais:
                print(" "*(espais-1),end="")
                print(f, end=" ")
            else:
                print(f, end=" ")
            for columna in fila:
                if dev:
                    print(columna.printDev(), end=" ")
                else:
                        print(columna, end=" ")
            print()
            f+=1

    def submatriuBuida(self, coords, orientacio, tamany):
    #Aquesta funció comprova si l'àrea on s'ha de situar el vaixell està buida o no.
        #Funció que ajuda a comprovar si l'àrea seleccionada conté tot aigua.
        def comprovarAigua(topLeft, bottomRight):
            aigua = True
            for i in range(topLeft[0],bottomRight[0]+1):
                    for j in range(topLeft[1],bottomRight[1]+1):
                        if self.matriu[i][j].getCasella() != "~":
                            aigua = False #Si hi ha alguna coordenada que no sigui aigua, el valor és fals.
            return aigua

        #Codi principal de la funció:
        try:
            if orientacio == 'v':
                topLeft = (coords[0]-1,coords[1]-1)
                bottomRight = (coords[0]+tamany+1,coords[1]+1)
            else:
                topLeft = (coords[0]-1,coords[1]-1)
                bottomRight = (coords[0]+1,coords[1]+tamany+1)
            return comprovarAigua(topLeft, bottomRight)
                
        except IndexError:
            #Si el vaixell surt dels límits del tauler, retornar fals.
            return False
    
    
    #Funció que donada la llista de vaixells, els col·loca al taulell.
    def colocarVaixells(self):

        for vaixell in self.llVaixells:

            #Inserta tants vaixells iguals com la quantitat d'aquests.
            for q in range(vaixell['quantitat']):
                vaixellColocat = False

                #Intenta col·locar el vaixell fins que estigui col·locat
                while not(vaixellColocat):
                    #Generar coordenades aleatories:
                    orientacio = random.choice(['v','h'])
                    if orientacio == 'v':
                        coords = (random.randint(0,self.mida-vaixell['mida']-1), random.randint(0,self.mida-1))
                    else:
                        coords = (random.randint(0,self.mida-1), random.randint(0,self.mida-vaixell['mida']-1))

                    #Si hi ha espai, col·loca el vaixell:
                    if self.submatriuBuida(coords, orientacio, vaixell['mida']):
                        Vaixell(vaixell['mida'], get.text(vaixell['nom'], self.lang)).generarVaixell(self,orientacio,coords)
                        vaixellColocat = True

                #Comptabilitza el vaixell dins del comptador de vaixells no enfonsats.        
                self.vaixellsActius += 1

    #Funció que comptabilitza el nombre de vaixells que resten amb vida.
    def vaixellEnfonsat(self):
        if self.vaixellsActius > 0:
            self.vaixellsActius -= 1

        #Si s'ha enfonsat tota la flota, mostrar que s'ha guanyat.
        if self.vaixellsActius == 0:
            self.jocAcabat = True

    #Funció que valida que la coordenada entrada existeixi dins de tauler.
    def comprovarCoordenades(self, coord):
        mida = self.mida
        numCorrecte = False
        llCorrecte = False

        if len(coord) > 1:
            if coord[:-1].isnumeric():
                if int(coord[:-1]) < mida:
                    numCorrecte = True
            if coord[-1] in self.abc[:mida]:
                llCorrecte = True
        
        return numCorrecte and llCorrecte

    #Funció que llança un tret a una coordenada donada (prèviament verificada).    
    def tret(self, coords):
        coords = tuple([int(coords[0]), self.abc.index(coords[1])])

        #Obté l'objecte Casella de la coordenada.
        casella = self.getCasella(coords)

        if not(casella.casellaOberta()):
            if casella.teVaixell():

                #Obté l'objecte vaixell de la casella.
                vaixell = casella.getCasella()
                #Redueix la vida del vaixell.
                vaixellMort = vaixell.tocat()
                #Si la vida del vaixell és 0, s'ha enfonsat.
                if vaixellMort:
                    #Notifica l'objecte Tauler que s'ha enfonsat un vaixell.
                    self.vaixellEnfonsat()
                    get.text('playground/sink', self.lang, vaixell.getName().upper(), mostrar=True)
                else:
                    get.text('playground/touched', self.lang, mostrar=True)
            else:
                get.text('playground/water', self.lang, mostrar=True)
                self.restarVida()
        else:
            get.text('errors/cordOpened', self.lang, mostrar=True)
    
    #Funció que entra en bucle mentre la partida està en primer pla.
    def jugar(self):
        #Retorna True si la partida s'ha acabat (jugador ha guanyat o s'ha mort).
        #Retorna False si el jugador vol tornar al menú.

        partidaActiva = True
        
        get.text('playground/info', self.lang, self.tID, self.getName(), mostrar=True)
        get.text('playground/exitPlaygroundInfo', self.lang, mostrar=True)

        while partidaActiva:
            #Si el joc ha acabat, notifica-ho al jugador i al programa principal.
            if self.jocAcabat:
                get.text('playground/winMessage', self.lang, mostrar=True)
                self.mostraTauler(True)
                return True
            if not(self.jugadorViu()):
                print(get.text('playground/deathMessage', self.lang)+'\n')
                self.mostraTauler(True)
                return True

            #Si no s'ha acabat el joc, demana al jugador noves coordenades i fes el tret.
            else:
                if self.videsActives():
                    get.text('playground/remaining', self.lang, self.videsRestants(), mostrar=True)
                print(get.text('playground/time-to-shot', self.lang)+'\n')
                self.mostraTauler()
                cCorrecte = False
                while not(cCorrecte):
                    casella = input(get.text('playground/insertCord', self.lang)).upper()
                    if casella == '':
                        return False
                    if self.comprovarCoordenades(casella):
                        cCorrecte = True
                        self.tret(casella)
    

#=== CLASSE VAIXELL ===#
class Vaixell(object):
    def __init__(self, mida, nom=''):
        self.mida = mida
        self.vides = mida-1
        self.visual = 'X' #Retorna com s'ha de mostrar el vaixell.
        self.name = nom 
    
    #Funció que actualitza el contingut de les instànices Casella on ha d'anar el vaixell.
    def generarVaixell(self, tauler, orientacio, coord):
        if orientacio == 'h':
            for c in range(self.mida):
                tauler.getCasella((coord[0],coord[1]+c)).setCasella(self)
        else:
            for c in range(self.mida):
                tauler.getCasella((coord[0]+c,coord[1])).setCasella(self)
    
    #Retorna com s'ha de mostrar el vaixell.
    def getVisual(self):
        return self.visual

    def getName(self):
        return self.name

    #Si el jugador ha trobat el vaixell, actualitza les vides.
    def tocat(self):
        if self.vides > 0:
            self.vides -= 1
            return False
        else:
            #Si el vaixell s'ha enfonsat, actualitza la visual.
            self.visual = "#"
            return True

#=== CLASSE CASELLA ===#
class Casella(object):
    def __init__(self):
        self.content = '~'
        self.visible = False
    
    #Modifica el que ha de retornar l'objecte quan es printa.
    def __str__(self):
        if self.visible:
            if isinstance(self.content, Vaixell):
                return self.content.getVisual()
            else:
                return "~"
        else:
            return "·"

    #Funció utilitzada per mostrar el contingut de la casella encara que no s'hagi obert.
    def printDev(self):
        if isinstance(self.content, Vaixell):
            return self.content.getVisual()
        else:
            return self.content

    #Modificar el contingut de la casella.
    def setCasella(self, content):
        self.content = content
    
    #Retornar el contingut de la casella.
    def getCasella(self):
        return self.content

    #Retorna si la casella té un objecte vaixell o no.
    def teVaixell(self):
        return isinstance(self.content, Vaixell)

    #Comprova si la casella ja s'ha obert. Si no, l'obre.
    def casellaOberta(self):
        if not(self.visible):
            self.visible = True
            return False
        else:
            return True