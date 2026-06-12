# ./RegistroLaboral/estadisticas_anuales/mejor_dia_anual.py

import database

from resumenes.mejor_dia import (
    obtener_mejor_dia
)


def obtener_mejor_dia_anual(anio):

    registros = (
        database.obtener_registros_anio(
            anio
        )
    )

    return obtener_mejor_dia(
        registros
    )
