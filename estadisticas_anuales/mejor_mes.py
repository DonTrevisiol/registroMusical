# ./RegistroLaboral/estadisticas_anuales/mejor_mes.py

import database

from registros_virtuales import (
    generar_registros_mes
)

from resumenes.mensual import (
    calcular_resumen_mensual
)


def obtener_mejor_mes(anio):

    mejor_mes = None
    mejor_dinero = -1

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

        dinero = resumen[
            "dinero_total"
        ]

        if dinero > mejor_dinero:

            mejor_dinero = dinero
            mejor_mes = mes

    return (
        mejor_mes,
        mejor_dinero
    )




