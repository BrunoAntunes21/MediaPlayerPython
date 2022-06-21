#criação da janela
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout
#configuração dos atributos da janela
from PyQt5.QtGui import QIcon,QPalette
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        #configuração de um icone e configuração do mesmo
        self.setWindowIcon(QIcon("botoes.ico"))
        #configuração do texto da janela
        self.setWindowTitle("prototipo de aplicativo de multimidia feito em Python")
        #configuração do eixo x e y(posicionamento da tela)
        self.setGeometry(350,100,700,500)

        # configuração da paletta de cores
        p = self.palette()
        # configuração da paleta de cores da janela
        p.setColor(QPalette.Window, Qt.GlobalColor.red)

        self.create_player()

    #criação do player
    def create_player(self):
        self.mediaPlayer=QMediaPlayer(None,QMediaPlayer.VideoSurface)
        videowidget= QVideoWidget()

        self.openBtn=QPushButton()

        self.openBtn=QPushButton('Open video')
        #configuração da posição horizontal da tela
        hbox=QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(self.openBtn)

        #configuração da posição vertical da tela
        vbox=QVBoxLayout()
        vbox.setContentsMargins(0,0,0,0)

        self.setLayout(vbox)




#criação da aplicação e da janela
app=QApplication(sys.argv)
#janela
window=Window()
window.show()
sys.exit(app.exec_())



