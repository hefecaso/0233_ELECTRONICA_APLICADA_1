# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

""" Display compass heading data five times per second """
import time
from math import atan2, degrees
import board
import adafruit_lsm303dlh_mag
import busio
i2c = busio.I2C(board.SCL,board.SDA)  # uses board.SCL and board.SDA
sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    return vector_2_degrees(magnet_x, magnet_y)

def pos():
    posicion = get_heading(sensor)
    return posicion

posicion = get_heading(sensor)

'''while True:
    posicion = get_heading(sensor)
    #print("heading: {:.2f} degrees".format(posicion))
    print(posicion)
    time.sleep(0.2)'''
