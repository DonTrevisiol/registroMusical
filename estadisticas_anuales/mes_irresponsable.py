# ./RegistroLaboral/estadisticas_anuales/mes_irresponsable.py

import database

from registros_virtuales import (
    generar_registros_mes
)

from resumenes.mensual import (
    calcular_resumen_mensual
)


def obtener_mes_irresponsable(anio):

    peor_mes = None
    peor_resumen = None

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

        if peor_resumen is None:

            peor_mes = mes
            peor_resumen = resumen
            continue

        # 1) Más faltas

        if (
            resumen["faltas_injustificadas"]
            >
            peor_resumen["faltas_injustificadas"]
        ):

            peor_mes = mes
            peor_resumen = resumen
            continue

        if (
            resumen["faltas_injustificadas"]
            <
            peor_resumen["faltas_injustificadas"]
        ):
            continue

        # 2) Menos días trabajados

        if (
            resumen["dias_trabajados"]
            <
            peor_resumen["dias_trabajados"]
        ):

            peor_mes = mes
            peor_resumen = resumen
            continue

        if (
            resumen["dias_trabajados"]
            >
            peor_resumen["dias_trabajados"]
        ):
            continue

        # 3) Menos canciones

        if (
            resumen["canciones_totales"]
            <
            peor_resumen["canciones_totales"]
        ):

            peor_mes = mes
            peor_resumen = resumen
            continue

        # 4) Menos tiempo

        if (
            resumen["tiempo_total"]
            <
            peor_resumen["tiempo_total"]
        ):

            peor_mes = mes
            peor_resumen = resumen

    return (
        peor_mes,
        peor_resumen["faltas_injustificadas"]
    )
