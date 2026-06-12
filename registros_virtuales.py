# ./RegistroLaboral/registros_virtuales.py

# ==============================
# GENERAR REGISTROS DEL MES
# (REALES + FALTAS VIRTUALES)
# ==============================
import database
from datetime import (
    datetime,
    timedelta
)

def generar_registros_mes(anio, mes):

    registros_reales = (
        database.obtener_registros_mes(
            anio,
            mes
        )
    )

    fecha_inicio = (
        database.obtener_fecha_primer_registro()
    )

    if not fecha_inicio:
        return []

    fecha_inicio = datetime.strptime(
        fecha_inicio,
        "%Y-%m-%d"
    ).date()

    registros_por_fecha = {}

    for registro in registros_reales:

        fecha = registro[1]

        registros_por_fecha[
            fecha
        ] = registro

    fecha_mes = datetime(
        int(anio),
        int(mes),
        1
    ).date()

    hoy = datetime.now().date()

    if (
        fecha_mes.year == hoy.year
        and
        fecha_mes.month == hoy.month
    ):

        ultimo_dia = hoy

    else:

        if int(mes) == 12:

            ultimo_dia = datetime(
                int(anio) + 1,
                1,
                1
            ).date() - timedelta(days=1)

        else:

            ultimo_dia = datetime(
                int(anio),
                int(mes) + 1,
                1
            ).date() - timedelta(days=1)

    registros_finales = []

    fecha_actual = fecha_mes

    while fecha_actual <= ultimo_dia:

        if fecha_actual < fecha_inicio:

            fecha_actual += timedelta(days=1)
            continue

        # 0=Lunes ... 6=Domingo
        if fecha_actual.weekday() >= 5:

            fecha_actual += timedelta(days=1)
            continue

        fecha_str = fecha_actual.strftime(
            "%Y-%m-%d"
        )

        if fecha_str in registros_por_fecha:

            registros_finales.append(
                registros_por_fecha[
                    fecha_str
                ]
            )

        else:

            if database.fecha_es_vacaciones(
                fecha_str
            ):

                registros_finales.append(
                    (
                        f"vacaciones_{fecha_str}",
                        fecha_str,
                        0,
                        0,
                        0,
                        "VACACIONES",
                        "vacaciones"
                    )
                )

            else:

                registros_finales.append(
                    (
                        f"virtual_{fecha_str}",
                        fecha_str,
                        0,
                        0,
                        0,
                        "No registrado",
                        "injustificada"
                    )
                )

        fecha_actual += timedelta(days=1)

    return registros_finales
