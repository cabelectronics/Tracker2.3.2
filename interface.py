from PyQt5 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets, QtPrintSupport
import subprocess
import os
import sys
import time
from threading import Thread

#Home page of the index.html
file_homepage = open('homepage/homepage.html', 'r')
welcome_text = file_homepage.read()
file_homepage.close()

file_html = open('index.html', 'w')
file_html.write(str(welcome_text))
file_html.close()

file_finish_loop = open('finish/end.txt', 'w')
file_finish_loop.write('')
file_finish_loop.close()

def refresh_html(self):
    a = os.getcwd()
    b = a.replace('\\', '/')
    file_html_dir = str(b + '/index.html')
    self.browser.setUrl(QtCore.QUrl(file_html_dir))

class AboutDialog(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QtWidgets.QDialogButtonBox.Ok
        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.rejected)

        layout = QtWidgets.QVBoxLayout()
        

        title = QtWidgets.QLabel("CAB Tracker")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QtWidgets.QLabel()
        logo.setPixmap(QtGui.QPixmap(os.path.join('images', 'ma-icon-128.png'))) #Image logo
        layout.addWidget(logo)

        layout.addWidget(QtWidgets.QLabel("Version 2.1.397"))
        layout.addWidget(QtWidgets.QLabel("Copyright 2019 CAB ELECTRONICS Inc."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

class MainWindow(QtWidgets.QMainWindow):
    
    #Defining the configuration bottom
    def configuration_menu(self):
        subprocess.run('Python configuration.py', shell=True)


    def moto_center(self):
        file_map_center = open('map/center.txt', 'w')
        file_map_center.write('mainmoto')
        file_map_center.close()


    def airplane_center(self):
        file_map_center = open('map/center.txt', 'w')
        file_map_center.write('airplane')
        file_map_center.close()


    def helicopter_center(self):
        file_map_center = open('map/center.txt', 'w')
        file_map_center.write('helicopter')
        file_map_center.close()


    def delete_configuration(self):
        #Restore moto 1 latitude
        file_moto1_la = open('latitude/moto1.txt', 'w')
        file_moto1_la.write('')
        file_moto1_la.close()
        
        #Restore moto 1 longitude
        file_moto1_l0 = open('longitude/moto1.txt', 'w')
        file_moto1_l0.write('')
        file_moto1_l0.close()

        #Restore moto 2 latitude
        file_moto2_la = open('latitude/moto2.txt', 'w')
        file_moto2_la.write('')
        file_moto2_la.close

        #Restore moto 2 longitude
        file_moto2_lo = open('longitude/moto2.txt', 'w')
        file_moto2_lo.write('')
        file_moto2_lo.close()

        #Restore moto 3 latitude
        file_moto3_la = open('latitude/moto3.txt', 'w')
        file_moto3_la.write('')
        file_moto3_la.close()

        #Restore moto 3 longitude
        file_moto3_lo = open('longitude/moto3.txt', 'w')
        file_moto3_lo.write('')
        file_moto3_lo.close()

        #Restore moto 4 latitude
        file_moto4_la = open('latitude/moto4.txt', 'w')
        file_moto4_la.write('')
        file_moto4_la.close()

        #Restore moto 4 longitude
        file_moto4_lo = open('longitude/moto4.txt', 'w')
        file_moto4_lo.write('')
        file_moto4_lo.close()

        #Restore airplane latitude
        file_airplane_la = open('latitude/airplane.txt', 'w')
        file_airplane_la.write('')
        file_airplane_la.close()

        #Restore airplane longitude
        file_airplane_lo = open('longitude/airplane.txt', 'w')
        file_airplane_lo.write('')
        file_airplane_lo.close()

        #Restore helicopter latitude
        file_helicopter_la = open('latitude/helicopter.txt', 'w')
        file_helicopter_la.write('')
        file_helicopter_la.close

        #Restore helicopter longitude
        file_helicopter_lo = open('longitude/helicopter.txt', 'w')
        file_helicopter_lo.write('')
        file_helicopter_lo.close()

        #Restore GPX file
        file_gpx = open('gpx/gpxfile.txt', 'w')
        file_gpx.write('')
        file_gpx.close()

        #Restore Moto 1 COM Port
        file_moto1_com = open('com/moto_1.txt', 'w')
        file_moto1_com.write('')
        file_moto1_com.close()

        #Restore Moto 2 COM Port
        file_moto2_com = open('com/moto_2.txt', 'w')
        file_moto2_com.write('')
        file_moto2_com.close()

        #Restore Moto 3 COM Port
        file_moto3_com = open('com/moto_3.txt', 'w')
        file_moto3_com.write('')
        file_moto3_com.close()

        #Restore Moto 4 COM Port
        file_moto4_com = open('com/moto_4.txt', 'w')
        file_moto4_com.write('')
        file_moto4_com.close()

        #Restore Aireplane COM Port
        file_airplane_com = open('com/airplane.txt', 'w')
        file_airplane_com.write('')
        file_airplane_com.close()

        #Restore Helicopter COM Port
        file_helicopter_com = open('com/helicopter.txt', 'w')
        file_helicopter_com.write('')
        file_helicopter_com.close()

        #Delete all the data from the html file
        file_index_html = open('index.html', 'w')
        file_index_html.write('')
        file_index_html.close()

        #Restore the center of the map
        file_map_center = open('map/center.txt', 'w')
        file_map_center.write('NONE')
        file_map_center.close()

        #Restore the main moto
        file_mainmoto_center = open('map/mainmoto.txt' ,'w')
        file_mainmoto_center.write('NONE')
        file_mainmoto_center.close()

        #Restore kill loop
        file_finish_loop = open('finish/end.txt', 'w')
        file_finish_loop.write('KILL')
        file_finish_loop.close()

        #RESTART THE PROGRAM
        python = sys.executable
        os.execl(python, python, *sys.argv)

        
    
    def start_action(self):
        
        def func1():
            subprocess.run('python loop.py', shell=True)
    
        try: 
            my_thread = Thread(target= func1)
            my_thread.start()
        except:
            subprocess.run('python error/cmn_error.py')

        #KILL THE LOOP
        
        file_finish_loop = open('finish/end.txt', 'r')
        for line in file_finish_loop:
            if line == 'KILL':
                my_thread._stop()
            else:
                pass
        file_finish_loop.close()
        
        a = os.getcwd()
        b = a.replace('\\', '/')
        c = str(b + '/index.html')
        self.browser.setUrl(QtCore.QUrl(c))
    

    def finish_action(self):
        file_finish_loop = open('finish/end.txt', 'w')
        file_finish_loop.write('KILL')
        file_finish_loop.close()


    def auto_center(self):
        file_auto_center = open('map/center.txt', 'w')
        file_auto_center.write('auto')
        file_auto_center.close()

    
    def plus_zoom_action(self):
        file_zoom = open('map/zoom.txt', 'r')
        for line in file_zoom:
            zoom_value = line
        file_zoom.close()

        file_zoom = open('map/zoom.txt', 'w')
        a = int(zoom_value)
        b = a + 1
        ZOOM = str(b)
        file_zoom.write(ZOOM)
        file_zoom.close()


    def minus_zoom_action(self):
        file_zoom = open('map/zoom.txt', 'r')
        for line in file_zoom:
            zoom_value = line
        file_zoom.close()

        file_zoom = open('map/zoom.txt', 'w')
        a = int(zoom_value)
        b = a - 1
        ZOOM = str(b)
        file_zoom.write(ZOOM)
        file_zoom.close()
    
    def restart_html_action(self):
        refresh_html(self)
        

    def __init__(self, *args, **kwargs):
        
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QtWebEngineWidgets.QWebEngineView()
        
        refresh_html(self)

        self.setCentralWidget(self.browser)


        self.status = QtWidgets.QStatusBar()
        self.setStatusBar(self.status)

        #The toolbar is where all the buttoms go.
        navtb = QtWidgets.QToolBar("Navigation")
        navtb.setIconSize(QtCore.QSize(22, 22))
        self.addToolBar(navtb)

        next_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'configuration-icon.PNG')), "Configuration", self)
        next_btn.setStatusTip("configuration to next page")
        next_btn.triggered.connect(self.configuration_menu)
        navtb.addAction(next_btn)

        moto_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'moto-icon.png')), "Moto", self)
        moto_btn.setStatusTip("Center View to Moto")
        moto_btn.triggered.connect(self.moto_center)
        navtb.addAction(moto_btn)

        airplane_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'airplane-icon.png')), "Airplane", self)
        airplane_btn.setStatusTip("Center View to Airplane") 
        airplane_btn.triggered.connect(self.airplane_center)
        navtb.addAction(airplane_btn)

        helicopter_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'helicopter-icon.png')), "Helicopter", self)
        helicopter_btn.setStatusTip("Center View  to Helicopter")
        helicopter_btn.triggered.connect(self.helicopter_center)
        navtb.addAction(helicopter_btn)

        auto_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'auto-icon.png')), "Auto", self)
        auto_btn.setStatusTip("Move automatically")
        auto_btn.triggered.connect(self.auto_center)
        navtb.addAction(auto_btn)

        start_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'start-icon.png')), "Start", self)
        start_btn.setStatusTip("Resume")  
        start_btn.triggered.connect(self.start_action)
        navtb.addAction(start_btn)

        pause_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'pause-icon.png')), "Pause", self)
        pause_btn.setStatusTip("Pause")
        pause_btn.triggered.connect(self.finish_action)
        navtb.addAction(pause_btn)

        bin_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'bin-icon.png')), "Bin", self)
        bin_btn.setStatusTip("Delete the configuration")
        bin_btn.triggered.connect(self.delete_configuration)
        navtb.addAction(bin_btn)

        plus_zoom_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'plus-icon.png')), "+ Zoom", self)
        plus_zoom_btn.setStatusTip("More zoom")
        plus_zoom_btn.triggered.connect(self.plus_zoom_action)
        navtb.addAction(plus_zoom_btn)

        minus_zoom_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'minus-icon.png')), "- Zoom", self)
        minus_zoom_btn.setStatusTip("Less zoom")
        minus_zoom_btn.triggered.connect(self.minus_zoom_action)
        navtb.addAction(minus_zoom_btn)

        
        restart_html_btn = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'restart-icon.png')), "Refresh", self)
        restart_html_btn.setStatusTip("Refresh")
        restart_html_btn.triggered.connect(self.restart_html_action)
        navtb.addAction(restart_html_btn)

        navtb.addSeparator()

        #File menu

        file_menu = self.menuBar().addMenu("&File")
       

        #Edit menu

        edit_menu = self.menuBar().addMenu("&Edit")

        #View menu 

        view_menu = self.menuBar().addMenu("&View")

        #Help menu

        help_menu = self.menuBar().addMenu("&Help")

        self.setWindowIcon(QtGui.QIcon(os.path.join('images/icon', 'tracker-icon.png'))) #Here will go the logo
        
        #self.show()

        
        refresh_html(self)
        
            

        

        
        

    


app = QtWidgets.QApplication(sys.argv)
app.setApplicationName("CAB Tracker")
app.setOrganizationName("CAB Electronics")
app.setOrganizationDomain("cab-electronics.com")

window = MainWindow()
window.show()


app.exec_()

file_finish_loop = open('finish/end.txt', 'w')
file_finish_loop.write('KILL')
file_finish_loop.close()
