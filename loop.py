import gpxpy
import gpxpy.gpx
import folium
import serial
import time
import serial
import pandas as pd
from decimal import Decimal
import base64
import sys
import subprocess

################################################################################Read The configuration########################################################################################
baud_rate = open('baudrate/baudrate.txt', 'r')
for line in baud_rate:
    BAUDRATE = line
baud_rate.close()

moto1_com = open('com/moto_1.txt', 'r')
for line in moto1_com:
    MOTO1COM = line
moto1_com.close()

moto2_com = open('com/moto_2.txt', 'r')
for line in moto2_com:
    MOTO2COM = line
moto2_com.close()

moto3_com = open('com/moto_3.txt', 'r')
for line in moto3_com:
    MOTO3COM = line
moto3_com.close()

moto4_com = open('com/moto_4.txt', 'r')
for line in moto4_com:
    MOTO4COM = line
moto4_com.close()

airplane_com = open('com/airplane.txt', 'r')
for line in airplane_com:
    AIRPLANECOM = line
airplane_com.close()

helicopter_com = open('com/helicopter.txt', 'r')
for line in helicopter_com:
    HELICOPTERCOM = line
helicopter_com.close()


############################################################################Read the GPX file##########################################################################################

format_type = open('gpx/format.txt', 'r')
for line in format_type:
    if 'GPX' in line:
        try:
            #Read the location of the gpx file
            gpx_file = open('gpx/gpxfile.txt', 'r')
            for line in gpx_file:
                my_gpx = line
            gpx_file.close() 

            my_gpx_file = open(my_gpx, 'r') 

            gpx = gpxpy.parse(my_gpx_file)

            points = []
            for track in gpx.tracks:
                for segment in track.segments:        
                    for point in segment.points:
                        points.append(tuple([point.latitude, point.longitude]))

            ave_lat = sum(p[0] for p in points)/len(points)
            ave_lon = sum(p[1] for p in points)/len(points)
        except:
            subprocess.run('python error/file_format_error.py')
    elif 'KMZ' in line:
        subprocess.run('python error/file_format_error.py')
    else:
        subprocess.run('python error/file_format_error.py')


########################################################################CHECKING FOR KILL DEFINITION##############################################################################
def check_kill():
    file_finish_loop = open('finish/end.txt', 'r')
    for line in file_finish_loop:
        if 'KILL' in line:
            sys.exit()
        else:
            pass




########################################################################READ LATITUDE & LONGITUDE####################################################################################

#Get de latitude of moto 1
def LatitudeM1():
    if MOTO1COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate =  BAUDRATE
            ser.port = MOTO1COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if ave_lat > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto1_latitude = aM7
                        
                elif ave_lat < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto1_latitude = aM8
                    
                return moto1_latitude    
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the longitude of moto 1
def LongitudeM1():  
    if MOTO1COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = MOTO1COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[5])
                if ave_lon > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto1_longitude = aM7

                elif ave_lon < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto1_longitude = aM8

                return moto1_longitude
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the latitude of moto 1
def LatitudeM2():
    if MOTO2COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = MOTO2COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if ave_lat > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto2_latitude = aM7
                elif ave_lat < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto2_latitude = aM8

                return moto2_latitude
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the longitude of Moto 2
def LongitudeM2():
    if MOTO2COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = MOTO2COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[5])
                if ave_lon > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto2_longitude = aM7

                elif ave_lon < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto2_longitude = aM8

                return moto2_longitude
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the latitude of Moto3
def LatitudeM3():
    if MOTO3COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = MOTO3COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if ave_lat > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto3_latitude = aM7
                    
                elif ave_lat < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto3_latitude = aM8

                return moto3_latitude    
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the longitude of Moto 3
def LongitudeM3():
    if MOTO3COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = MOTO3COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[5])
                if ave_lon > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto3_longitude = aM7

                elif ave_lon < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto3_longitude = aM8

                return moto3_longitude
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the latitude of Moto 4
def LatitudeM4():
    if MOTO4COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate =  BAUDRATE
            ser.port = MOTO4COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if ave_lat > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto4_latitude = aM7
                    
                elif ave_lat < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto4_latitude = aM8

                return moto4_latitude    
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the longitude of Moto 4
def LongitudeM4():
    if MOTO4COM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate =  BAUDRATE
            ser.port = MOTO4COM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if ave_lat > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    moto4_latitude = aM7
                    
                elif ave_lat < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    moto4_latitude = aM8

                return moto4_latitude    
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the latitude of the Airplane
def LatitudeAir():
    if AIRPLANECOM =="NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate =  BAUDRATE
            ser.port = AIRPLANECOM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if ave_lat > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    airplane_latitude = aM7
                    
                elif ave_lat < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    airplane_latitude = aM8

                return airplane_latitude    
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the longitude of the Airplane
def  LongitudeAir():
    if AIRPLANECOM == "NO":
        pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = AIRPLANECOM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[5])
                if ave_lon > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    airplane_longitude = aM7

                elif ave_lon < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    airplane_longitude = aM8

                return airplane_longitude
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the latitude of the Helicopter
def LatitudeHel():
    if HELICOPTERCOM == "NO":
        pass 
    else:
        try:
            ser = serial.Serial()
            ser.baudrate =  BAUDRATE
            ser.port = HELICOPTERCOM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[3])
                if ave_lat > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    helicopter_latitude  = aM7
                    
                elif ave_lat < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    helicopter_latitude  = aM8

                return helicopter_latitude    
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')

#Get the longitude of the Helicopter
def LongitudeHel():
    if HELICOPTERCOM == "NO":
            pass
    else:
        try:
            ser = serial.Serial()
            ser.baudrate = BAUDRATE
            ser.port = HELICOPTERCOM
            ser.open()

            search = ser.readline()
            line = str(search)
            if "RMC" in line:
                line = line.split(",")
                aM1 = Decimal(line[5])
                if ave_lon > 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6

                    helicopter_longitude = aM7

                elif ave_lon < 0:
                    aM2 = aM1 / 100
                    aM3 = int(aM2)
                    aM4 = aM3 * 100
                    aM5 = aM1 - aM4
                    aM6 = aM5 / 60
                    aM7 = aM3 + aM6
                    aM8 = aM7 * -1

                    helicopter_longitude = aM8

                return helicopter_longitude
            ser.close()
        except:
            subprocess.run('python error/serial_error.py')


###########################################################################ESTABLISHING THE DEFAULT ZOOM = 11########################################################################

file_zoom = open('map/zoom.txt', 'w')
file_zoom.write('11') #Seting [11] as the zoom standard
file_zoom.close()

#####################################################################################################################################################################################



#EL LOOP DE LA MUERTE tan tan tannn
while True:
    
    ####################################################################################################################################################################
    check_kill()
    ####################################################################################################################################################################

    ###########################################################################READ LATITUDE & LONGITUDE##################################################################

    #Latitude Moto 1
    try:
        M1LA = LatitudeM1()
    except:
        pass
    
    #Longitude Moto 1
    try: 
        M1LO = LongitudeM1()
    except:
        pass

    #Latitude Moto 2
    try:
        M2LA = LatitudeM2()
    except:
        pass

    #Longitude Moto 2
    try:
        M2LO = LongitudeM2()
    except:
        pass

    #Latitude Moto 3
    try:
        M3LA = LatitudeM3()
    except:
        pass

    #Longitude Moto 3
    try:
        M3LO = LongitudeM3()
    except:
        pass

    #Latitude Moto 4
    try:
        M4LA = LatitudeM4()
    except:
        pass

    #Longitude Moto 4
    try:
        M4LO = LongitudeM4()
    except:
        pass

    #Latitude Airplane
    try:
        AIRLA = LatitudeAir()
    except:
        pass

    #Longitude Airplane
    try:
        AIRLO = LongitudeAir()
    except:
        pass

    #Latitude Helicopter
    try:
        HELLA = LatitudeHel()
    except:
        pass

    #Longitude Helicopter
    try:
        HELLO = LongitudeHel()
    except:
        pass
    
    
    ####################################################################################################################################################################
    check_kill()
    ####################################################################################################################################################################


    ###########################################################################CREATION OF THE MAP######################################################################

    #Reading the ZOOM value
    file_zoom = open('map/zoom.txt', 'r')
    for line in file_zoom:
        ZOOM = line
    file_zoom.close()    

    #Function for reading the object that mus be at the center of the map
    def read_center_map():
        file_center_map = open('map/center.txt', 'r')
        for line in file_center_map:
            if 'NONE' in line:
                center_key = 0
            elif 'airplane' in line:
                center_key = 1
            elif 'helicopter' in line:
                center_key = 2
            elif 'mainmoto' in line:
                file_mainmoto_center = open('map/mainmoto.txt', 'r')
                for line in file_mainmoto_center:
                    if 'Moto1' in line:
                        center_key = 3
                    elif 'Moto2' in line:
                        center_key = 4
                    elif 'Moto3' in line:
                        center_key = 5
                    elif 'Moto4' in line:
                        center_key = 6
                    else:
                        center_key = 0
            elif 'auto' in line:
                center_key = 0

            else:
                center_key = 0
        return center_key          

    a = read_center_map()
    

    ####################################################################################################################################################################
    check_kill()
    ####################################################################################################################################################################


    #ESTABLISHING THE CENTER OBJECT

    

    if a == 0:
        try:
            my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=ZOOM, zoom_control=False, scrollWheelZoom=False, dragging=False)
        except:
            subprocess.run('python error/cmn_error.py')

    elif a == 1:
        try:
            my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=ZOOM, zoom_control=False, scrollWheelZoom=False, dragging=False)
        except:
            subprocess.run('python error/cmn_error.py')
             

    elif a == 2:
        try:
            my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=ZOOM, zoom_control=False, scrollWheelZoom=False, dragging=False)
        except:
            subprocess.run('python error/cmn_error.py')
            a = 0

    elif a == 3:
        try:
            my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=ZOOM, zoom_control=False, scrollWheelZoom=False, dragging=False)
        except:
            subprocess.run('python error/cmn_error.py')
            a = 0

    elif a == 4:
        try:
            my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=ZOOM, zoom_control=False, scrollWheelZoom=False, dragging=False)
        except:
            subprocess.run('python error/cmn_error.py')
            a = 0

    elif a == 5:
        try:
            my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=ZOOM, zoom_control=False, scrollWheelZoom=False, dragging=False)
        except:
            subprocess.run('python error/cmn_error.py')
            a = 0

    elif a == 6:
        try:
            my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=ZOOM, zoom_control=False, scrollWheelZoom=False, dragging=False)
        except:
            subprocess.run('python error/cmn_error.py')
            a = 0
    else:   
        my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=ZOOM, zoom_control=False, scrollWheelZoom=False, dragging=False)
        
            


    #Guide to follow:
    #my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=13)

    ############CENTER_KEY########################################################
    # 0 = Free center
    # 1 = Airplane center
    # 2 = Helicopter center
    # 3 = Moto 1 center
    # 4 = Moto 2 center
    # 5 = Moto 3 center
    # 6 = Moto 4 center

    ###########################################################################CREATION OF THE MAP############################################################################
    

    ####################################################################################################################################################################
    check_kill()
    ####################################################################################################################################################################

    #fade lines
    folium.PolyLine(points, color="red", weight=4, opacity=1).add_to(my_map)
    
    #Moto 1 in map
    moto1_logo = 'images/moto1-map.png'
    moto1_icon = folium.features.CustomIcon(moto1_logo, icon_size=(40, 40))
    try:
        folium.Marker([M1LA, M1LO], icon=moto1_icon).add_to(my_map)
    except:
        pass

    #Moto 2 in map
    moto2_logo = 'images/moto2-map.png'
    moto2_icon = folium.features.CustomIcon(moto2_logo, icon_size=(40, 40))
    try:
        folium.Marker([M2LA, M2LO], icon=moto2_icon).add_to(my_map)
    except:
        pass

    #Moto 3 in map
    moto3_logo = 'images/moto3-map.png'
    moto3_icon = folium.features.CustomIcon(moto3_logo, icon_size=(40, 40))
    try:
        folium.Marker([M3LA, M3LO], icon=moto3_icon).add_to(my_map)
    except:
        pass

    #Moto 4 in map
    moto4_logo = 'images/moto4-map.png'
    moto4_icon = folium.features.CustomIcon(moto4_logo, icon_size=(40, 50))
    try:
        folium.Marker([M4LA, M4LO], icon=moto4_icon).add_to(my_map)
    except:
        pass

    #Helicopter in map
    helicopter_logo = 'images/helicopter-icon.png'
    helicopter_icon = folium.features.CustomIcon(helicopter_logo, icon_size=(40, 40))
    try:
        folium.Marker([HELLA, HELLO], icon=helicopter_icon).add_to(my_map)
    except:
        pass

    #Airplane in map
    airplane_logo = 'images/airplane-map.png'
    airplane_icon = folium.features.CustomIcon(airplane_logo, icon_size=(40,40))
    try:
        folium.Marker([AIRLA, AIRLO], icon=airplane_icon).add_to(my_map)
    except:
        pass


    ####################################################################################################################################################################
    check_kill()
    ####################################################################################################################################################################


    # Save map
    my_map.save("./index.html")
    '''
    a_file = open("./index.html", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[3] = '\t<meta http-equiv="refresh" content="3" />\n'

    a_file = open("./index.html", "w")
    a_file.writelines(list_of_lines)
    a_file.close()
    '''

    ####################################################################################################################################################################
    check_kill()
    ####################################################################################################################################################################
    
    

    