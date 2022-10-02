import RPi.GPIO as GPIO
import time
import os
import math
import ephem
from datetime import datetime, timezone




GPIO.setmode(GPIO.BOARD) # Use Board numerotation mode
GPIO.setwarnings(False) # Disable warnings

# Use pin 11 for PWM signal
servo = 11
frequence = 50
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequence)


#C onvirtiendo ángulos a ciclos de trabajo
def angulo_giro(angulo):

    #angulo = -1*Angulo_Elevacion
    giro = (angulo)/18 +2
    return giro

def movimiento():
    pwm.start(angulo_giro(angulo))

# Iniciando pwm en 0
pwm.start(0)

#Limpiando terminal
#os.system ("clear")

# Iniciando loop
#while True:

while True:
    time.sleep(10)
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
    Angulo_Elevacion = int(iss_1.alt * degrees_per_radian)
    print('Elevacion:' , Angulo_Elevacion)
    time.sleep(1)

    #angulo = float(-1*Angulo_Elevacion)
    angulo = float(Angulo_Elevacion)
    #angulo = float(input("Ingrese un águlo: "))

    if 180 >= angulo >= 0:
        movimiento()
        #time.sleep(1.5)
        time.sleep(1)

    else:
        print("\nÁngulo fuera de los parámetros permitidos. \n")

    pwm.stop()
    GPIO.cleanup()



''''
        DC 7% | neut | 90°
        DC 2% | min  | 0°
        DC 12%| max  | 180°
'''

#################
#   Referencias #
#################

# Tutorial: https://raspberrypi-espana.es/servo-frambuesa-pi/

# Referencias importantes
# Teória y cálculos: https://www.learnrobotics.org/blog/raspberry-pi-servo-motor/?utm_source=youtube&utm_medium=description&utm_campaign=link_in_description_FYb7Pr2XNxE#Step-3-Calculate-duty-cycle-to-degrees-formula-for-the-Servo-Motor
# Teoría youtube: https://www.youtube.com/watch?v=ddlDgUymbxc&ab_channel=GavenMacDonald

#Chekpoin menú, falta target ISS
