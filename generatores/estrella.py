# Generador de estrellas
import random

'''
Reglas de generación de estrellas
'''
import random

from seeds import seeds

#seed = hash((coord_x, coord_y)) % (2**32)
seed = random.seed()
rng = random.randrange(100)
print(rng)