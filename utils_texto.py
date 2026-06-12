# ./RegistroLaboral/utils_texto.py

from constantes import MESES

def nombre_mes(numero_mes):
    return MESES[
        str(numero_mes).zfill(2)
        ]
