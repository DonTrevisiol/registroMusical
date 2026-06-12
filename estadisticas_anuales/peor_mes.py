# ./RegistroLaboral/estadisticas_anuales/peor_mes.py

import database

from registros_virtuales import (
    generar_registros_mes
)

from resumenes.mensual import (
    calcular_resumen_mensual
)


def obtener_peor_mes(anio):

    peor_mes = None
    peor_dinero = None

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

        if peor_dinero is None:

            peor_dinero = dinero
            peor_mes = mes
            continue

        if dinero < peor_dinero:

            peor_dinero = dinero
            peor_mes = mes

    return (
        peor_mes,
        peor_dinero
    )
