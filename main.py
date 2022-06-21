#criação da janela
from PyQt5.QtWidgets import QApplication,QWidget
#configuração dos atributos da janela
from PyQt5.QtGui import QIcon
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

#criação da aplicação e da janela
app=QApplication(sys.argv)
#janela
window=Window()
window.show()
sys.exit(app.exec_())
