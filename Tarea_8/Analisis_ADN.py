import os

referencia = "ATGCTAGCTAAT"

def detectar_mutaciones(ref, muestra):
    mutaciones = []
    for i, (r, m) in enumerate(zip(ref, muestra)):
        if r != m:
            mutaciones.append(i)
    return mutaciones

directorio_actual = os.path.dirname(os.path.abspath(__file__))

nombre_archivo = "secuencias_adn.txt"
ruta_archivo = os.path.join(directorio_actual, nombre_archivo)

with open(ruta_archivo, "r") as archivo:
    for num_linea, linea in enumerate(archivo, start=1):
        secuencia = linea.strip().upper()
        if len(secuencia) != len(referencia):
            print(f"Línea {num_linea}: Longitud incorrecta ({len(secuencia)} en vez de {len(referencia)}). Se omite.")
            continue
        mutaciones = detectar_mutaciones(referencia, secuencia)
        if mutaciones:
            print(f"Línea {num_linea}: Mutaciones en posiciones: {mutaciones}")
        else:
            print(f"Línea {num_linea}: Sin mutaciones.")
