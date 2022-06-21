from PyQt5.QtWidgets import QApplication,QWidget
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()

#criação da aplicação e da janela
app=QApplication(sys.argv)
#janela
window=Window()
window.show()
sys.exit(app.exec_())
