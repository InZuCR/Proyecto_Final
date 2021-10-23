#!/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:19:45 2021

Este script lee el sensor de luz BH1750 por bus I2C.

@author: Ingrid y Carlos 
"""

import smbus

# Constantes para el sensor
DEVICE     = 0x23 # Dirección I2C por defecto
POWER_DOWN = 0x00 # Estado no activo
POWER_ON   = 0x01 # Encendido
RESET      = 0x07 # Registor de reset
HR_MODE_1  = 0x20 # modo 1 resolucion 1 lx

i2c = smbus.SMBus(1) 

def convertToNumber(data):
    """
    Convierte 2 bytes en un numero decimal
    ----------
    data : list
        Bloque de datos 
    Returns
    -------
    float
        Luxes leidos
    """
    result=(data[1] + (256 * data[0])) / 1.2
    return (result)

def leeLux(DEVICE):
    """
    Toma la lectura del sensor en lux 
    Parameters
    ----------
    DEVICE : int
        Dirección del dispositivo

    Returns
    -------
    float
        Luz ambiente en lux
    """
    data = i2c.read_i2c_block_data(DEVICE,HR_MODE_1,2)
    return convertToNumber(data)
