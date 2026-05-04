# Generador de Hex
import random

'''
# Reglas de generación de Hex
    # Código ID
    # Coordenadas X
    # Coordenadas Y
    # Coordenadas Z

# Un hex puede contener uno de los siguientes:
    - Un sistema solar
    - Nube de materia (nebulosa)
    - Cementerio estelar
    - Anomalía
    - Vacío
'''

seed = random.seed()
def verificar():
    rng1 = random.randrange(100)
    if rng1 >= 50:
        print(rng1)
    else:
        print("Vacío")
verificar()