from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QRect, QCoreApplication
from program10ui import Ui_MainWindow


class MyActions(Ui_MainWindow):
    def __init__(self, title = ""):
        self.title = title
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.myactions()


    def myactions(self):
        self.button_buscar.clicked.connect(self.buscar)
        self.button_limpiar.clicked.connect(self.limpiar)
        self.button_salir.clicked.connect(self.salir)
    
    def buscar(self):
        p1 = float(self.text_p1.toPlainText())
        p2 = float(self.text_p2.toPlainText())
        p3 = float(self.text_p3.toPlainText())
        r = (p1*0.3 + p2*0.4 + p3*0.3)
        self.text_promedio.setText(str(r))
        if (r>=70):
            self.text_status.setText("aprobado")
        else:
            self.text_status.setText("Reprobado")
    def limpiar(self):
        self.text_p1.setText("")
        self.text_p2.setText("")
        self.text_p3.setText("")
        self.text_nombre.setText("")
        self.text_nc.setText("")
        self.text_semestre.setText("")
        self.text_materia.setText("")
        self.text_carrera.setText("")
        self.text_status.setText("")
        self.text_promedio.setText("")
    def salir(self):
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyActions("title of app")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())