# ./RegistroLaboral/estadisticas_anuales/promedios.py

import database

from registros_virtuales import (
    generar_registros_mes
)


def obtener_promedios_anuales(anio):

    canciones_totales = 0
    tiempo_total = 0
    dinero_total = 0

    dias_trabajados = 0

    for mes in range(1, 13):

        registros = generar_registros_mes(
            anio,
            str(mes).zfill(2)
        )

        for registro in registros:

            (
                _id,
                fecha,
                canciones,
                tiempo_seg,
                dinero,
                detalles,
                tipo_registro
            ) = registro

            if (
                canciones > 0
                or tiempo_seg > 0
                or dinero > 0
            ):

                dias_trabajados += 1

            canciones_totales += canciones
            tiempo_total += tiempo_seg
            dinero_total += dinero

    promedio_diario = (
        dinero_total / dias_trabajados
        if dias_trabajados > 0
        else 0
    )

    promedio_cancion = (
        dinero_total / canciones_totales
        if canciones_totales > 0
        else 0
    )

    promedio_tiempo_cancion = (
        tiempo_total / canciones_totales
        if canciones_totales > 0
        else 0
    )

    return (
        promedio_diario,
        promedio_cancion,
        promedio_tiempo_cancion
    )
