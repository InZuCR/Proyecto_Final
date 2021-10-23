#!/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:47:04 2021

@author: Ingrid y Carlos
"""

import BH1750 as ls
import time
from Adafruit_IO import Client, Feed, RequestError

IO_KEY = 'ADAKEY'
IO_USERNAME = 'ADAUSER'

# Instancia un cliente REST
aio = Client(IO_USERNAME,IO_KEY)
# Configura  `Iluminacion` feed
luz_feed = aio.feeds('hidroponico.iluminacion')
while True:
    luz=ls.leeLux(0x23)
    print("Nivel de luz: {:.2f} lx".format(luz))
    aio.send(luz_feed.key, luz)
    time.sleep (2)
    