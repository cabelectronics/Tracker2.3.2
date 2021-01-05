from PyQt5 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets, QtPrintSupport
import sys
import os

#path = QDir.current().filePath('plotly-latest.min.js') 
#local = QUrl.fromLocalFile(path).toString(


def refresh_html(self):
    path = QtCore.QDir.current().filePath('index.html')
    local = QtCore.QUrl.fromLocalFile(path).toString()
    self.browser.setUrl(QtCore.QUrl(local))

#Contorno/Ventana de la app
class AboutDialog(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QtWidgets.QDialogButtonBox.Ok
        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.rejected)

        layout = QtWidgets.QVBoxLayout()

        title = QtWidgets.QLabel("CAB Mission Software")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QtWidgets.QLabel()
        logo.setPixmap(QtGui.QPixmap(os.path.join('public/images', 'airplane-map.png'))) #LOGO image 
        layout.addWidget(logo)

        layout.addWidget(QtWidgets.QLabel('MS 1.0'))
        layout.addWidget(QtWidgets.QLabel("Copyright 2020 CAB ELECTRONICS"))

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class MainWindow(QtWidgets.QMainWindow):
    #All functions of the bottoms are defined here....
    #....
    #....

    #We define the Main Window Structure
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QtWebEngineWidgets.QWebEngineView()
        refresh_html(self)
        self.setCentralWidget(self.browser)





app = QtWidgets.QApplication(sys.argv)
app.setApplicationName('Mission Software')
app.setOrganizationName('CAB Electronics')

window = MainWindow()
window.show()

app.exec_()