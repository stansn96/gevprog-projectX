#!/usr/bin/python3

from PyQt4 import QtCore, QtGui
from heroclass import *
from wumpusclass import *
from grottengenerator import *
import sys
from time import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

"""Class voor de grafische interface"""
class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    """Class voor het doorgeven van de richting aan de heldstap functie """
    def koppelFunctie(self, beurt):
            if beurt == "links":
                self.heldstap("links")
            if beurt == "rechts":
                self.heldstap("rechts")
            if beurt == "omhoog":
                self.heldstap("omhoog")
            if beurt == "omlaag":
                self.heldstap("omlaag")
            if beurt == "schiet":
                self.speelbord.beweging = "schiet"
            if beurt == "beweeg":
                self.speelbord.beweging = "beweeg"
                
    """Class voor het opzetten van de grafische interface. Deze class en de retranslate class zijn gegenereerd met het programma QT Designer"""
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(969, 674)
        
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.scene = QtGui.QGraphicsScene(Form)
        self.graphicsView.setStyleSheet("border: 0px")
        self.rooms = QtGui.QGraphicsPixmapItem()
        self.rooms.setPixmap(QtGui.QPixmap("kamers.png"))
        self.scene.addItem(self.rooms)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView.setScene(self.scene)
        self.info = QtGui.QLabel(Form)
        self.info.setText(_fromUtf8(""))
        self.info.setObjectName(_fromUtf8("info"))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.gridLayout.addWidget(self.info, 2, 0, 3, 4)
        spacerItem1 = QtGui.QSpacerItem(20, 200, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.ArrowLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ArrowLabel.setFont(font)
        self.ArrowLabel.setObjectName(_fromUtf8("ArrowLabel"))
        self.verticalLayout.addWidget(self.ArrowLabel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.ArrowAmount = QtGui.QLCDNumber(Form)
        self.ArrowAmount.setObjectName(_fromUtf8("ArrowAmount"))
        self.verticalLayout.addWidget(self.ArrowAmount)
        self.GoldLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.GoldLabel.setFont(font)
        self.GoldLabel.setObjectName(_fromUtf8("GoldLabel"))
        self.verticalLayout.addWidget(self.GoldLabel)
        self.GoldAmount = QtGui.QLCDNumber(Form)
        self.GoldAmount.setObjectName(_fromUtf8("GoldAmount"))
        self.verticalLayout.addWidget(self.GoldAmount)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.BtnMove = QtGui.QPushButton(Form)
        self.BtnMove.setObjectName(_fromUtf8("BtnMove"))
        self.verticalLayout.addWidget(self.BtnMove)
        self.BtnShoot = QtGui.QPushButton(Form)
        self.BtnShoot.setObjectName(_fromUtf8("BtnShoot"))
        self.verticalLayout.addWidget(self.BtnShoot)
        self.BtnUp = QtGui.QPushButton(Form)
        self.BtnUp.setObjectName(_fromUtf8("BtnUp"))
        self.verticalLayout.addWidget(self.BtnUp, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.BtnLeft = QtGui.QPushButton(Form)
        self.BtnLeft.setObjectName(_fromUtf8("BtnLeft"))
        self.horizontalLayout_2.addWidget(self.BtnLeft)
        self.BtnDown = QtGui.QPushButton(Form)
        self.BtnDown.setObjectName(_fromUtf8("BtnDown"))
        self.horizontalLayout_2.addWidget(self.BtnDown)
        self.BtnRight = QtGui.QPushButton(Form)
        self.BtnRight.setObjectName(_fromUtf8("BtnRight"))
        self.horizontalLayout_2.addWidget(self.BtnRight)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 5, 2, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 6, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Hunt the Wumpus", None))
        
        self.BtnLeft.setText(_translate("Form", "Links", None))
        self.BtnRight.setText(_translate("Form", "Rechts", None))
        self.BtnUp.setText(_translate("Form", "Omhoog", None))
        self.BtnDown.setText(_translate("Form", "Omlaag", None))
        self.BtnMove.setText(_translate("Form", "Bewegen", None))
        self.BtnShoot.setText(_translate("Form", "Schieten", None))
        
        self.ArrowLabel.setText(_translate("Form", "Pijlen", None))
        self.GoldLabel.setText(_translate("Form", "Goud", None))

        """Aanmaken van de Hero"""
        self.hero = Hero("Held")

        self.setinfobericht("Welkom bij Hunt the Wumpus, Held\nWe hebben je nodig om de wumpus te verslaan!")
		
		"""Aanmaken van de Wumpus en grottenstelsel wordt gegenereerd. Pixels van Hero worden berekend en Hero wordt op juiste plek geplaatst."""
        self.wumpus = Wumpus(self.hero.updatepositie())
        self.kamerplan = Grottengenerator(self.hero.updatepositie(), self.wumpus.updatepositie())
        positievandehero = self.hero.updatepositie()
        herox, heroy = self.coordsberekenen(positievandehero)
        self.sethero(herox, heroy)

        self.speelbord = Afhandelen()
        self.speelbord.start()

        self.connect(self.speelbord, QtCore.SIGNAL("goud"), self.verandergoud, QtCore.Qt.DirectConnection)
        self.connect(self.speelbord, QtCore.SIGNAL("pijl"), self.veranderpijlen, QtCore.Qt.DirectConnection)
        self.connect(self.speelbord, QtCore.SIGNAL("beweging"), self.opnieuwbeurt, QtCore.Qt.DirectConnection)
        
        """Koppel de buttons aan de koppelfunctie, die vervolgende de juiste waarden doorgeeft aan de daarvoor geschikte functie"""
        self.BtnLeft.clicked.connect(self.koppelFunctieLinks)
        self.BtnRight.clicked.connect(self.koppelFunctieRechts)
        self.BtnUp.clicked.connect(self.koppelFunctieOmhoog)
        self.BtnDown.clicked.connect(self.koppelFunctieOmlaag)
        self.BtnMove.clicked.connect(self.koppelFunctieBeweeg)
        self.BtnShoot.clicked.connect(self.koppelFunctieSchiet)

    """Class voor het tonen van een bericht in de UI"""
    def setinfobericht(self, bericht):
        self.info.setText(_translate("Form", bericht, None))

    def veranderpijlen(self):
        arrows = self.hero.pijlaantal()
        self.ArrowAmount.display(arrows)
        
    def verandergoud(self):
        self.hero.goudgevonden()
        goud = self.hero.goudaantal()
        self.GoldAmount.display(goud)          

    """Maak een Pixmapitem voor de hero, schaal deze en voeg deze toe aan de map"""
    def sethero(self, herox, heroy):
        self.heldfoto = QtGui.QGraphicsPixmapItem()
        self.heldfoto.setPixmap(QtGui.QPixmap("face.png"))
        self.heldfoto.setPos(herox,heroy)
        self.heldfoto.scale(0.5,0.5)
        self.scene.addItem(self.heldfoto)
    
    """Zet coordinaten om in coordinaten in pixels"""
    def coordsberekenen(self, coord):
        return (coord[0] - 1) * 120 + 20, (coord[1] - 1) * 100 + 10

    def heldstap(self, richting): #bewegingssysteem van Matthijs Bonnema
        if self.stappen == True:
            self.plek = self.hero.updatepositie()
            if richting == "links":
                if self.plek[0] == 1:
                    self.speelbord.richting = "links"
                    self.heldfoto.setPixmap(QtGui.QPixmap('left.png'))
                    self.heldfoto.moveBy(480 , 0)
                else:
                    self.speelbord.richting = "links"
                    self.heldfoto.setPixmap(QtGui.QPixmap('left.png'))
                    self.heldfoto.moveBy(-120, 0)
                self.hero.moveleft()
            if richting == "rechts":
                if self.plek[0] == 5:
                    self.speelbord.richting = "rechts"
                    self.heldfoto.setPixmap(QtGui.QPixmap('right.png'))
                    self.heldfoto.moveBy(-480 , 0)
                else:
                    self.speelbord.richting = "rechts"
                    self.heldfoto.setPixmap(QtGui.QPixmap('right.png'))
                    self.heldfoto.moveBy(120, 0)
                self.hero.moveright()
            if richting == "omhoog":
                if self.plek[1] == 1:
                    self.speelbord.richting = "omhoog"
                    self.heldfoto.setPixmap(QtGui.QPixmap('up.png'))
                    self.heldfoto.moveBy(0, 300)
                else:
                    self.speelbord.richting = "omhoog"
                    self.heldfoto.setPixmap(QtGui.QPixmap('up.png'))
                    self.heldfoto.moveBy(00, -100)
                self.hero.moveup()
            if richting == "omlaag":
                if self.plek[1] == 4:
                    self.speelbord.richting = "omlaag"
                    self.heldfoto.setPixmap(QtGui.QPixmap('face.png'))
                    self.heldfoto.moveBy(0, -300)
                else:
                    self.speelbord.richting = "omlaag"
                    self.heldfoto.setPixmap(QtGui.QPixmap('face.png'))
                    self.heldfoto.moveBy(0, 100)
                self.hero.movedown()
    
    def setstappen(self):
        self.stappen = True

    def schieten(self):
        self.schieten = True
    
    def opnieuwstappen(self):
        self.stappen = False
        
    def koppelFunctieLinks(self):
        self.koppelFunctie("links")
        
    def koppelFunctieRechts(self):
        self.koppelFunctie("rechts")

    def koppelFunctieOmhoog(self):
        self.koppelFunctie("omhoog")

    def koppelFunctieOmlaag(self):
        self.koppelFunctie("omlaag")

    def koppelFunctieBeweeg(self):
        self.koppelFunctie("beweeg")

    def koppelFunctieSchiet(self):
        self.koppelFunctie("schiet") 
    
    def respawn(self):
        ui.hero.herplaatsen()
        xCor, yCor = self.coordsberekenen(self.hero.updatepositie())
        self.heldfoto.setPos(xCor, yCor)
    
    def win(self):
        self.setinfobericht("Gefelciteerd je hebt de wumpus verslagen!\n")
        sleep(1)
        self.setinfobericht("Je vond {} goud en had {} pijlen over".format(self.hero.goudaantal(),(self.hero.pijlaantal())))
        self.speelbord.quit()
        
    def dood(self, won):
        self.setinfobericht("Helaas, je bent dood!\nJe vond {} goud en had {} pijlen over".format(self.hero.goudaantal(),(self.hero.pijlaantal())))
        self.speelbord.quit()
	
    def returnkamerplan(self):
        return self.kamerplan

    def opnieuwbeurt(self):
        self.speelbord.beweging = None

"""Thread aangemaakt zodat stappen uitgevoerd kunnen worden zonder lang te wachten & zonder dat programma crasht"""
class Afhandelen(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        

    def run(self):
        sleep(1)
        ui.opnieuwstappen()
        levend = True
        self.beweging = None
        self.richting = None
        self.emit(QtCore.SIGNAL("goud"))
        self.emit(QtCore.SIGNAL("pijl"))
         
        kamerplanvariabele = ui.kamerplan.returngrotten()
        
        """Checken of er items rondom de hero zijn"""
        while levend:
            items = []

            xcoor, ycoor = ui.hero.updatepositie()

            if ycoor == 1:
                omliggendeposities = [(xcoor, ycoor + 1), (xcoor, 4), (xcoor + 1, ycoor), (xcoor - 1, ycoor)]
                omliggendepositieswumpus = [(xcoor, ycoor + 1), (xcoor, 4), (xcoor + 1, ycoor), (xcoor - 1, ycoor)]            
            elif xcoor == 1:
                omliggendeposities = [(xcoor, ycoor + 1), (xcoor, 5), (xcoor + 1, ycoor), (xcoor - 1, ycoor)]
                omliggendepositieswumpus = [(xcoor, ycoor + 1), (xcoor, 5), (xcoor + 1, ycoor), (xcoor - 1, ycoor)]
            elif ycoor == 4:
                omliggendeposities = [(xcoor, 1), (xcoor, ycoor - 1), (xcoor + 1, ycoor), (xcoor - 1, ycoor)]
                omliggendepositieswumpus = [(xcoor, 1), (xcoor, ycoor - 1), (xcoor + 1, ycoor), (xcoor - 1, ycoor)]            
            elif xcoor == 5:
                omliggendeposities = [(xcoor, ycoor + 1), (xcoor, ycoor - 1), (1, ycoor), (xcoor - 1, ycoor)]
                omliggendepositieswumpus = [(xcoor, ycoor + 1), (xcoor, ycoor - 1), (1, ycoor), (xcoor - 1, ycoor)]
            else:
                omliggendeposities = [(xcoor, ycoor + 1), (xcoor, ycoor - 1), (xcoor + 1, ycoor), (xcoor - 1, ycoor)]
                omliggendepositieswumpus = [(xcoor, ycoor + 1), (xcoor, ycoor - 1), (xcoor + 1, ycoor), (xcoor - 1, ycoor)]
			
            for coordinaten in kamerplanvariabele:
                for kamers in omliggendeposities:
                    if str(coordinaten[0]) == str(kamers):
                        items.append(coordinaten[1])
              
            if "Goud" in items:
                ui.setinfobericht("Er ligt goud naast je!")
                sleep(2)
            if "Vleermuis" in items:
                ui.setinfobericht("Er is een vleermuis in de buurt")
                sleep(2)
            if "Put" in items:
                ui.setinfobericht("Ik voel de tocht van een put...")
                sleep(2)
            
            for coordinaten in kamerplanvariabele:
                for kamers in omliggendeposities:
                    if str(coordinaten[0]) == str(kamers):
                        if str(kamers) == str(ui.wumpus.updatepositie()):
                            ui.setinfobericht("Ik ruik de Wumpus...")

            if levend:
                if ui.hero.updatepositie() == ui.wumpus.updatepositie():
                    ui.setinfobericht("De Wumpus heeft je opgegeten!")
                    levend = False
                    ui.dood(False)
                if levend:
                    ui.wumpus.jagen(ui.hero.updatepositie())

                    if ui.hero.updatepositie() == ui.wumpus.updatepositie():
                        ui.setinfobericht("De Wumpus heeft je opgegeten!")
                        levend = False
                        ui.dood(False)

            ui.setinfobericht("Wil je bewegen of schieten?")
            self.emit(QtCore.SIGNAL("beweging"))
            self.beweging = None
            while self.beweging == None:
                sleep(1)
            
            """Code voor schieten proberen te maken, werkt niet"""
            self.schietpositie=[]
            if self.beweging == "beweeg":
                ui.setstappen()
                ui.setinfobericht("\nWil je naar onder, boven, links of rechts bewegen?\n")
                self.richting = None
                while self.richting == None:
                    sleep(1)
                ui.opnieuwstappen()
                if ui.speelbord.richting == "omlaag" or ui.speelbord.richting == "omhoog":
                    ui.setinfobericht("Je bent {} verplaatst!\n".format(self.richting))
                else:
                    ui.setinfobericht("Je bent naar {} verplaatst!\n".format(self.richting))
                sleep(1)

                for room in kamerplanvariabele:
                    if ui.hero.updatepositie() == room[0]:
                        if room[1] == "Goud":
                            ui.setinfobericht("Je hebt goud gevonden!")
                            room[1] = None
                            sleep(1)
                            self.emit(QtCore.SIGNAL("goud"))
                        elif room[1] == "Vleermuis":
                            ui.setinfobericht("Je stapte op een vleermuis\nDe vleermuis nam je mee, en bracht je naar een andere kamer!")
                            sleep(1)
                            nieuwexcor, nieuweycor = ui.hero.herplaatsen1(ui.wumpus.updatepositie())
                            herplaatsherox, herplaatsheroy = ui.coordsberekenen((nieuwexcor, nieuweycor))
                            ui.heldfoto.setPos(herplaatsherox,herplaatsheroy)
                        elif room[1] == "Put":
                            ui.setinfobericht("Je viel in een put")
                            sleep(1)
                            ui.setinfobericht("En dat overleefde je niet!\n")
                            levend = False
                            
            """Code voor schieten, werkt niet"""                            
            elif self.beweging == "schiet":
                self.xarrow,self.yarrow= ui.hero.updatepositie()
                ui.schieten()
                ui.setinfobericht("\nKlik 4 keer op de richting waar de pijl heenmoet!\n")
                self.richting = None
                while self.richting == None:
                    sleep(1)
                for i in range(5):
                    if ui.speelbord.richting == "omlaag":
                        ui.setinfobericht("Je hebt {} geschoten!\n".format(self.richting))
                        self.yarrow=self.yarrow+1
                        self.schietpositie.append((self.xarrow,self.yarrow))
                        sleep(1)

                    elif ui.speelbord.richting == "omhoog":
                        ui.setinfobericht("Je hebt {} geschoten!\n".format(self.richting))
                        self.yarrow=self.yarrow=-1
                        self.schietpositie.append((self.xarrow,self.yarrow))
                        sleep(1)
                        
                    elif ui.speelbord.richting == "rechts":
                        ui.setinfobericht("Je hebt naar {} geschoten!\n".format(self.richting))
                        self.yarrow=self.xarrow=+1
                        self.schietpositie.append((self.xarrow,self.yarrow))
                        sleep(1)
                        
                    elif ui.speelbord.richting == "links":
                        ui.setinfobericht("Je hebt naar {} geschoten!\n".format(self.richting))
                        self.yarrow=self.xarrow=-1
                        self.schietpositie.append((self.xarrow,self.yarrow))
                        sleep(1)
                    
                if ui.wumpus.updatepositie() in self.schietpositie:
                    levend=False
                    sleep(1)
                self.emit(QtCore.SIGNAL("pijl"))

            self.beweging = None
        if not ui.wumpus.updatepositie() in self.schietpositie:
            ui.dood(False)
        else:
            ui.win()

    def actionMove(self):
        self.beweging = "beweeg"

    def actionShoot(self):
        self.beweging = "shoot"

def run():
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())

