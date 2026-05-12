# Generador de Hex
import random

'''
# Reglas de generación de Hex
    # Código ID
    # Coordenadas X
    # Coordenadas Y
    # Coordenadas Z

# Un hex puede contener uno de los siguientes:
    - 40% Vacío
    - 30% Un sistema solar
    - 15% Nube de materia (nebulosa)
    - 10% Cementerio estelar
    - 5% Anomalía
'''

seed = random.seed()
def verificar():
    # Primero, verificar si el Hex está en la base de datos.
    print("Verificando...")
    print("Hex no registrado, procediendo a generar uno...")
    generateHex(1,2,3)

def generateSolarSystem():
    rngSS = random.randrange(100)

    # Primero se define la estrella, identificando el número, color y tamaño.
    # Segundo se identifica el número de circulos planetarios y la zona habitable.
    # Tercero se identifica el contenido de cada circulo planetario

    if rngSS <= 100:
        print("")

def generateNebulosa():
    print("")

def generateCementerioEstelar():
    print("")

def generateAnomalía():
    print("")

def generateHex(codX, codY, codZ):    
    # Segundo, en caso de no haber un Hex creado, se genera uno nuevo.

    rng1 = random.randrange(100)
    print (rng1)
    
    if rng1 <= 60:
        print("En las coordenadas" + codX + codY + codZ + "Se encuentra: " + "Vacío")
    elif rng1 <= 80:
        print("En las coordenadas" + codX + codY + codZ + "Se encuentra: " + "Sistema solar")
        generateSolarSystem()
    elif rng1 <= 90:
        print("En las coordenadas" + codX + codY + codZ + "Se encuentra: " + "Nube de materia / Nebulosa")
    elif rng1 <= 95:
        print("En las coordenadas" + codX + codY + codZ + "Se encuentra: " + "Cementerio estelar")
    else:
        print("En las coordenadas" + codX + codY + codZ + "Se encuentra: " + "Anomalía")
    
    # Tercero, se guarda el Hex en la base de datos.
        
verificar()