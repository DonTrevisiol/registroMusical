# ./RegistroLaboral/estadisticas_anuales/peor_dia_anual.py

import database

from registros_virtuales import (
    generar_registros_mes
)

from resumenes.peor_dia import (
    obtener_peor_dia
)


def obtener_peor_dia_anual(anio):

    registros = (
        database.obtener_registros_anio(
            anio
        )
    )

    return obtener_peor_dia(
        registros
    )





