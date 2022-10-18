import random
import languages as get

class Tauler(object):
    tIDs = 0
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"
    def __init__(self, mida, vaixells=[], nomJugador='', vides=0, lang='ca'):
        self.__class__.tIDs +=1
        self.tID = self.__class__.tIDs
        self.nomJugador = nomJugador
        self.lang = lang
        self.mida = mida
        self.matriu = self.iniciarTauler(self.mida)
        self.llVaixells = vaixells
        self.vaixellsActius = 0
        self.colocarVaixells()
        self.vides = vides
        self.videsActivades = (vides > 0)
        self.jocAcabat = False
    
    def __str__(self):
        return get.text('playground/info', self.lang, self.getID(), self.getName())


    #Metodes per obtenir atributs:
    def getID(self):
        return str(self.tID)

    def getCasella(self, coords):
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

    def getName(self):
        return self.nomJugador

    def partidaGuanyada(self):
        return self.jocAcabat

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
        try:
            if orientacio == 'v':
                topLeft = (coords[0]-1,coords[1]-1)
                bottomRight = (coords[0]+tamany+1,coords[1]+1)
            else:
                topLeft = (coords[0]-1,coords[1]-1)
                bottomRight = (coords[0]+1,coords[1]+tamany+1)

            return self.comprovarAigua(topLeft, bottomRight)
                
        except IndexError:
            return False
    
    def comprovarAigua(self, topLeft, bottomRight):
        aigua = True
        for i in range(topLeft[0],bottomRight[0]+1):
                for j in range(topLeft[1],bottomRight[1]+1):
                    if self.matriu[i][j].getCasella() != "~":
                        aigua = False #Si hi ha alguna coordenada que no sigui aigua, el valor és fals.
        return aigua
    
    def colocarVaixells(self):
        for vaixell in self.llVaixells:
            for i in range(vaixell['quantitat']):
                vaixellColocat = False
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
                self.vaixellsActius += 1

    def vaixellEnfonsat(self):
        if self.vaixellsActius > 0:
            self.vaixellsActius -= 1

        if self.vaixellsActius == 0:
            self.jocAcabat = True
        
    def tret(self, coords):
        coords = tuple([int(coords[0]), self.abc.index(coords[1])])

        casella = self.getCasella(coords)
        if not(casella.casellaOberta()):
            if casella.teVaixell():
                vaixell = casella.getCasella()
                vaixellMort = vaixell.tocat()
                if vaixellMort:
                    self.vaixellEnfonsat()
                    get.text('playground/sink', self.lang, vaixell.getName().upper(), mostrar=True)
                else:
                    get.text('playground/touched', self.lang, mostrar=True)
            else:
                get.text('playground/water', self.lang, mostrar=True)
                self.restarVida()
        else:
            get.text('errors/cordOpened', self.lang, mostrar=True)

    def comprovarCoordenades(self, coord):
        mida = self.mida
        cCorrecte = True

        if len(coord) > 1:
            for el in coord[:-1]:
                if el not in self.nums:
                    cCorrecte = False
            if coord[-1] not in self.abc[:mida]:
                cCorrecte = False
        return cCorrecte
    
    def jugar(self):
        partidaActiva = True
        
        get.text('playground/info', self.lang, self.getID(), self.getName(), mostrar=True)
        get.text('playground/exitPlaygroundInfo', self.lang, mostrar=True)

        while partidaActiva:
            if self.partidaGuanyada():
                get.text('playground/winMessage', self.lang, mostrar=True)
                self.mostraTauler(True)
                return True
            if not(self.jugadorViu()):
                print(get.text('playground/deathMessage', self.lang)+'\n')
                self.mostraTauler(True)
                return True
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
    



class Vaixell(object):
    def __init__(self, mida, nom=''):
        self.mida = mida
        self.vides = mida-1
        self.visual = 'X'
        self.name = nom 
    
    def generarVaixell(self, tauler, orientacio, coord):
        if orientacio == 'h':
            for c in range(self.mida):
                tauler.getCasella((coord[0],coord[1]+c)).setCasella(self)
        else:
            for c in range(self.mida):
                tauler.getCasella((coord[0]+c,coord[1])).setCasella(self)
    
    def getVisual(self):
        return self.visual

    def getName(self):
        return self.name

    def tocat(self):
        if self.vides > 0:
            self.vides -= 1
            return False
        else:
            self.visual = "#"
            return True

class Casella(object):
    def __init__(self):
        self.content = '~'
        self.visible = False
    
    def __str__(self):
        if self.visible:
            if isinstance(self.content, Vaixell):
                return self.content.getVisual()
            else:
                return "~"
        else:
            return "·"

    def __getitem__(self, items):
        return str(self)

    def printDev(self):
        if isinstance(self.content, Vaixell):
            return self.content.getVisual()
        else:
            return self.content

    def setCasella(self, content):
        self.content = content
    
    def getCasella(self):
        return self.content

    def teVaixell(self):
        return isinstance(self.content, Vaixell)

    def casellaOberta(self):
        if not(self.visible):
            self.visible = True
            return False
        else:
            return True