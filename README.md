# Proyecto_Final
 Toma y envío de datos a un portal Web (Adafruit IO) desde un sistema embebido (Raspberry Pi)
 
 En la carpeta "Toma_de_datos", se ubican los códigos utilizados para leer los sensores BME280 (temperatura, humedad y presión atmosférica) y BH1750 (luz).
 
 El archivo "main.py" se encarga de enviar los datos a la API REST de Adafruit. Para ejecutar sin errores este script debe utilizar python3.
 
 Debe descargar en su máquina (Raspberry Pi), la libreria "Adafruit_IO" antes de correr los script. Esto lo puede hacer usando el siguiente comando:
 
 sudo pip3 install adafruit-io
 
 Recuerde cambiar la llave y el usuario por las que Adafruit le otorga
