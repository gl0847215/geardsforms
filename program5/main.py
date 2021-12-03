from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QRect, QCoreApplication
from program5ui import Ui_MainWindow


class MyActions(Ui_MainWindow):
    def __init__(self, title = ""):
        self.title = title
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.myactions()


    def myactions(self):
        self.Button_calcular.clicked.connect(self.calcular)
        self.button_salir.clicked.connect(self.salir)
        self.button_limpiar.clicked.connect(self.limpiar)
    
    def calcular(self):
        x = float(self.text_x.toPlainText())
        y = float(self.text_y.toPlainText())
        z = float(self.text_z.toPlainText())
        result = ((3*x**4 + 2*x*z*y**2)**0.5 / (3 + x**2*y**2*z**2)) + 5*x**2*y
        self.text_resultado.setText(str(result))
    
    def salir(self):
        sys.exit(app.exec_())
    
    def limpiar(self):
        self.text_resultado.setText("")
        self.text_x.setText("")
        self.text_y.setText("")
        self.text_z.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyActions("title of app")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())