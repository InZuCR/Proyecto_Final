#!/usr/bin/env python3


import BME280read as BME280
import BH1750 as ls

import time
from Adafruit_IO import Client, Feed, RequestError

IO_KEY = "aio_nBXP73dp8faqApgrkO1G5SPAtuUL"
IO_USERNAME = "IngridCR"

# Instancia un cliente REST
aio = Client(IO_USERNAME,IO_KEY)
# Configura  `humedad` feed

humedad_feed = aio.feeds('hidroponico.humedad')
temperatura_feed = aio.feeds('hidroponico.temperatura')
presion_feed = aio.feeds('hidroponico.presionatmosferica')
luminosidad_feed = aio.feeds('hidroponico.luminosidad')


while True:
    humedad=BME280.readHumidity()
    temperatura=BME280.readTemperature()
    presion=BME280.readPressure()
    luz=ls.leeLux(0x23)

    print("Nivel de humedad: [%]".format(humedad))
    aio.send(humedad_feed.key, humedad)
    aio.send(temperatura_feed.key, temperatura)
    aio.send(presion_feed.key, presion)
    aio.send(luminosidad_feed.key, luz)

    time.sleep (10)
