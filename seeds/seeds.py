def generar_sistema(coord_x, coord_y):
    seed = hash((coord_x, coord_y)) % (2**32)
    rng = random.Random(seed)