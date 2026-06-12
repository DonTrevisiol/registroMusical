# ./RegistroLaboral/estadisticas_anuales/mtp_anual.py

import database

from resumenes.mtp import (
    obtener_mtp
)


def obtener_mtp_anual(anio):

    registros = (
        database.obtener_registros_anio(
            anio
        )
    )

    return obtener_mtp(
        registros
    )
