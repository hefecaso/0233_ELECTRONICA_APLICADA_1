import ISS_Info
import turtle
import time
import threading
import math
#from mpl_toolkits.basemap import Basemap
#librerias predicciones
import urllib.request as url
import json
#import folium

import urllib.request as url
import json
import ephem
from datetime import datetime, timezone

screen = turtle.Screen()
screen.title("ISS TRACKER")
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("world.png")
screen.register_shape("iss.gif")
#screen.register_shape("gt.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.penup()

gt = turtle.Turtle()
#gt.shape("gt.gif")
gt.penup()
cerco = turtle.Turtle()

# Latitud y Logitud de Guatemala
latitud=15.783471
longitud=-90.230759
n=6 #número de veces que pasará la ISS
Pass=url.Request('http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n={}'.format(latitud,longitud,n))
response_Pass= url.urlopen(Pass)

def pasoISS():
    Pass_obj = json.loads(response_Pass.read())
    #print (Pass_obj)
    pass_list=[]
    for count,item in enumerate(Pass_obj["response"], start=0):
        pass_list.append(Pass_obj['response'][count]['risetime'])
        print("Proximos pases sobre Guatemala")
        print(datetime.fromtimestamp(pass_list[count]).strftime('%d-%m-%Y %H:%M:%S'))



def tracker():
    pasoISS()
    while True:

        try:

            location = ISS_Info.iss_current_loc()
            lat = location['iss_position']['latitude']
            lon = location['iss_position']['longitude']
            screen.title("ISS TRACKER: (Latitude: {},  Longitude: {})".format(lat,lon))
            iss.goto(float(lon),float(lat))
            iss.pencolor("red")
            iss.dot(iss.goto(float(lon),float(lat)))
            gt.pencolor("orange")
            gt.dot(gt.goto(float(longitud),float(latitud)))
            cerco.pencolor("magenta")
            cerco.dot(cerco.goto(float(-107.324236),float(19.819178)))
            cerco.dot(cerco.goto(float(-76.671761),float(20.143828)))
            cerco.dot(cerco.goto(float(-76.671761),float(10.808493)))
            cerco.dot(cerco.goto(float(-109.107194),float(6.09958)))
            degrees_per_radian = 180.0 / math.pi
            home = ephem.Observer()
            home.lon = '-90.51327'
            home.lat = '14.64072'
            home.elevation = 1729
            iss_1 = ephem.readtle('ISS',
                '1 25544U 98067A   22162.52439360  .00005833  00000+0  11028-3 0  9998',
                '2 25544  51.6455   4.6361 0004468 222.6641 220.6469 15.49954017344301'
            )
            home.date = datetime.utcnow()
            iss_1.compute(home)
            Angulo_Elevacion = '%4.1f' % (iss_1.alt * degrees_per_radian)
            Azimut =  '%5.1f' % (iss_1.az * degrees_per_radian)
            print('Elevacion:', Angulo_Elevacion ,', Azimut:', Azimut)
            time.sleep(5)

        except Exception as e:
            print(str(e))
            break
t = threading.Thread(target=tracker())
t.start()
#pasoISS()


def elevacion():
    Angulo_Elevacion = '%4.1f' % (iss_1.alt * degrees_per_radian)
    return Angulo_Elevacion

def azimut():
    Azimut =  '%5.1f' % (iss_1.az * degrees_per_radian)
    return Azimut
