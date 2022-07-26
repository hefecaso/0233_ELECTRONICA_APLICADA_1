import time
import turtle
from turtle import *
import numpy as np
from math import atan2, degrees
import board
import adafruit_lsm303dlh_mag
import busio

i2c = busio.I2C(board.SCL,board.SDA)  # uses board.SCL and board.SDA
sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)
screen=turtle.Screen

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle

def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    return vector_2_degrees(magnet_x, magnet_y)

def vector_22_degrees(x, z):
    angle2 = degrees(atan2(x, z))
    if angle2 <= 0:
        angle2 += 90
    return angle2

def get2_heading(_sensor):
    magnet_x, magnet_z, _ = _sensor.magnetic
    return vector_22_degrees(magnet_x, magnet_z)

def pos():
    posicion = get2_heading(sensor)
    return posicion

posicion = get2_heading(sensor)
