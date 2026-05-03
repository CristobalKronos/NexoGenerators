# Generador de estrellas
import random

'''
# Reglas de generación de estrellas
# Código ID
# Color
    # Azul
    # Amarilla
    # Roja
# Tamaño
    # Enana
    # Normal
    # Gigante
# Número
    # Simple
    # Binaria
    # Ternaria
'''
import random

from seeds import seeds

def SelectColor():
    print()

def generate_Star():
    print("Generating star")

#seed = hash((coord_x, coord_y)) % (2**32)
seed = random.seed()
rng = random.randrange(100)
print(rng)