import RPi.GPIO as GPIO
import time
import math
import ephem
from datetime import datetime, timezone

##########
#def diferencia(xi, xf):
    #y = xf-xi
    #return y

xf = 0
xi = 0
##########

out1 = 24
out2 = 25
out3 = 8
out4 = 7

i=0
positive=0
negative=0
y=0


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # Disable warnings
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)

while True:
    time.sleep(10)
    GPIO.setwarnings(False) # Disable warnings
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)
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
    #Angulo_Elevacion = '%4.1f' % (iss_1.alt * degrees_per_radian)
    #Azimut =  '%5.1f' % (iss_1.az * degrees_per_radian)
    Azimut =  int(iss_1.az * degrees_per_radian)
    print('Azimut:', Azimut)
    time.sleep(1)

    ##############
    xf = Azimut
    y = xf-xi
    xi = xf
    ##############

    deg = y
    #print("ingrese un valor para rotar un angulo de 0 a 360")

    #deg = int(input())
    x = int(-1*(deg*4096)/(360))
    if x>0 and x<=4096:
        for y in range(x,0,-1):
            if negative==1:
                if i==7:
                    i=0
                else:
                    i=i+1
                y=y+2
                negative=0
            positive=1

            if i==0:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.003)
            elif i==1:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.003)
            elif i==2:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.003)
            elif i==3:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.003)
            elif i==4:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.003)
            elif i==5:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.003)
            elif i==6:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.003)
            elif i==7:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.003)
            if i==7:
                i=0
                continue
            i=i+1

    elif x<0 and x>=-4096:
        x=x*-1
        for y in range(x,0,-1):
            if positive==1:
                if i==0:
                    i=7
                else:
                    i=i-1
                y=y+3
                positive=0
            negative=1

            if i==0:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.003)
            elif i==1:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.003)
            elif i==2:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.003)
            elif i==3:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.003)
            elif i==4:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                time.sleep(0.003)
            elif i==5:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.003)
                #time.sleep(1)
            elif i==6:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.003)
                #time.sleep(1)
            elif i==7:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(0.003)
            if i==0:
                i=7
                continue
            i=i-1
    #break


#except KeyboardInterrupt:
    #GPIO.cleanup()


#Chekpoin menú, falta target ISS
