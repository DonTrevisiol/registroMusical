# ./RegistroLaboral/estadisticas_anuales/mpp_anual.py

import database

from resumenes.mpp import (
    obtener_mpp
)


def obtener_mpp_anual(anio):

    registros = (
        database.obtener_registros_anio(
            anio
        )
    )

    return obtener_mpp(
        registros
    )
