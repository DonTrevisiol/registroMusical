# ./RegistroLaboral/resumenes/peor_dia.py


from .mensual import es_dia_trabajado
# ===============================
# PEOR DÍA
# ===============================

def obtener_peor_dia(registros):

    peor = None

    for registro in registros:

        (
            registro_id,
            fecha,
            canciones,
            tiempo_seg,
            dinero,
            detalles,
            tipo_registro
        ) = registro

        # Ignorar faltas y días no trabajados
        if not es_dia_trabajado(
            canciones,
            tiempo_seg,
            dinero,
            detalles
        ):
            continue

        if peor is None:

            peor = registro
            continue

        (
            _,
            fecha_peor,
            canciones_peor,
            tiempo_peor,
            dinero_peor,
            detalles_peor,
            tipo_registro_peor
        ) = peor

        # 1) Menor dinero total
        if dinero < dinero_peor:

            peor = registro
            continue

        if dinero > dinero_peor:
            continue

        # 2) Menor dinero promedio por canción

        prom_actual = (
            dinero / canciones
            if canciones > 0
            else float("inf")
        )

        prom_peor = (
            dinero_peor / canciones_peor
            if canciones_peor > 0
            else float("inf")
        )

        if prom_actual < prom_peor:

            peor = registro
            continue

        if prom_actual > prom_peor:
            continue

        # 3) Mayor tiempo promedio por canción

        tiempo_prom_actual = (
            tiempo_seg / canciones
            if canciones > 0 and tiempo_seg > 0
            else 0
        )

        tiempo_prom_peor = (
            tiempo_peor / canciones_peor
            if canciones_peor > 0 and tiempo_peor > 0
            else 0
        )

        if tiempo_prom_actual > tiempo_prom_peor:

            peor = registro
            continue

    return peor
