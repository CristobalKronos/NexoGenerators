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

def generateHex(codX, codY, codZ):    
    # Segundo, en caso de no haber un Hex creado, se genera uno nuevo.

    rng1 = random.randrange(100)
    print (rng1)
    
    if rng1 <= 40:
        print("Vacío")
    elif rng1 <= 70:
        print("Sistema solar")
    elif rng1 <= 85:
        print("Nube de materia / Nebulosa")
    elif rng1 <= 95:
        print("Cementerio estelar")
    else:
        print("Anomalía")
    
    # Tercero, se guarda el Hex en la base de datos.
        
verificar()