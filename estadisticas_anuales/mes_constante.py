# ./RegistroLaboral/estadisticas_anuales/mes_constante.py

import database

def obtener_mes_constante(anio):

    mejor_mes = None

    mejor_diferencia = None

    for mes in range(1, 13):

        registros = database.obtener_registros_mes(
            anio,
            str(mes).zfill(2)
        )

        registros_validos = [
            r
            for r in registros
            if r[4] > 0
        ]

        if len(registros_validos) < 2:
            continue

        if not registros_validos:
            continue

        mejor_dia = max(
            registros_validos,
            key=lambda r: r[4]
        )

        peor_dia = min(
            registros_validos,
            key=lambda r: r[4]
        )

        diferencia = (
            mejor_dia[4]
            - peor_dia[4]
        )

        dias_trabajados = len(
            registros_validos
        )

        canciones = sum(
            r[2]
            for r in registros_validos
        )

        dinero_total = sum(
            r[4]
            for r in registros_validos
        )

        if mejor_mes is None:

            mejor_mes = (
                mes,
                diferencia,
                dias_trabajados,
                canciones,
                dinero_total
            )

            mejor_diferencia = diferencia

            continue

        (
            _mes_actual,
            diferencia_actual,
            dias_actuales,
            canciones_actuales,
            dinero_actual
        ) = mejor_mes

        # Menor diferencia
        if diferencia < diferencia_actual:

            mejor_mes = (
                mes,
                diferencia,
                dias_trabajados,
                canciones,
                dinero_total
            )

            continue

        if diferencia > diferencia_actual:
            continue

        # Más días trabajados
        if dias_trabajados > dias_actuales:

            mejor_mes = (
                mes,
                diferencia,
                dias_trabajados,
                canciones,
                dinero_total
            )

            continue

        if dias_trabajados < dias_actuales:
            continue

        # Más canciones
        if canciones > canciones_actuales:

            mejor_mes = (
                mes,
                diferencia,
                dias_trabajados,
                canciones,
                dinero_total
            )

            continue

        if canciones < canciones_actuales:
            continue

        # Más dinero
        if dinero_total > dinero_actual:

            mejor_mes = (
                mes,
                diferencia,
                dias_trabajados,
                canciones,
                dinero_total
            )

    return mejor_mes
