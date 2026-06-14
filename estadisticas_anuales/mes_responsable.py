# ./RegistroLaboral/estadisticas_anuales/mes_responsable.py

import database

from registros_virtuales import (
    generar_registros_mes
)

from resumenes.mensual import (
    calcular_resumen_mensual
)


def obtener_mes_responsable(anio):

    mejor_mes = None
    mejor_resumen = None

    for mes in range(1, 13):

        registros = generar_registros_mes(
            anio,
            str(mes).zfill(2)
        )

        resumen = (
            calcular_resumen_mensual(
                registros
            )
        )

        if (
            resumen["dias_trabajados"] == 0
            and
            resumen["faltas_injustificadas"] == 0
        ):
            continue

        if mejor_resumen is None:

            mejor_mes = mes
            mejor_resumen = resumen
            continue

        # 1) Más días trabajados

        if (
            resumen["dias_trabajados"]
            >
            mejor_resumen["dias_trabajados"]
        ):

            mejor_mes = mes
            mejor_resumen = resumen
            continue

        if (
            resumen["dias_trabajados"]
            <
            mejor_resumen["dias_trabajados"]
        ):
            continue

        # 2) Menos faltas

        if (
            resumen["faltas_injustificadas"]
            <
            mejor_resumen["faltas_injustificadas"]
        ):

            mejor_mes = mes
            mejor_resumen = resumen
            continue

        if (
            resumen["faltas_injustificadas"]
            >
            mejor_resumen["faltas_injustificadas"]
        ):
            continue

        # 3) Más canciones

        if (
            resumen["canciones_totales"]
            >
            mejor_resumen["canciones_totales"]
        ):

            mejor_mes = mes
            mejor_resumen = resumen
            continue

        # 4) Más tiempo

        if (
            resumen["tiempo_total"]
            >
            mejor_resumen["tiempo_total"]
        ):

            mejor_mes = mes
            mejor_resumen = resumen

    return (
        mejor_mes,
        mejor_resumen["dias_trabajados"]
    )

