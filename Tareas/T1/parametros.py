import random
import csv

class Arena:
    def __init__(self, nombre, tipo, rareza, humedad, dureza, estatica):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza
        self.humedad = humedad
        self.dureza = dureza
        self.estatica = estatica
        

class Excavador:
    def __init__(self, nombre, tipo, edad, energia, fuerza, suerte, felicidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.energia = energia
        self.fuerza = fuerza
        self.suerte = suerte
        self.felicidad = felicidad

with open("T1/arenas.csv") as arenas:
    arenas = csv.reader(arenas, delimiter=",")

print(arenas)





        
