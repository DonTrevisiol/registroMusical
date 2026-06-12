# ./RegistroLaboral/resumenes/mejor_dia.py
from .mensual import es_dia_trabajado
# ===============================
# MEJOR DÍA
# ===============================

def obtener_mejor_dia(registros):

    mejor = None

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

        # Ignorar faltas
        if not es_dia_trabajado(
            canciones,
            tiempo_seg,
            dinero,
            detalles,
        ):
            continue

        if mejor is None:

            mejor = registro
            continue

        (
            _,
            fecha_mejor,
            canciones_mejor,
            tiempo_mejor,
            dinero_mejor,
            detalles_mejor,
            tipo_registro_mejor
        ) = mejor

        # 1) Más dinero total
        if dinero > dinero_mejor:

            mejor = registro
            continue

        if dinero < dinero_mejor:
            continue

        # 2) Dinero promedio por canción
        prom_actual = (
            dinero / canciones
            if canciones > 0
            else -1
        )

        prom_mejor = (
            dinero_mejor / canciones_mejor
            if canciones_mejor > 0
            else -1
        )

        if prom_actual > prom_mejor:

            mejor = registro
            continue

        if prom_actual < prom_mejor:
            continue

        # 3) Tiempo promedio por canción
        tiempo_prom_actual = (
            tiempo_seg / canciones
            if canciones > 0 and tiempo_seg > 0
            else float("inf")
        )

        tiempo_prom_mejor = (
            tiempo_mejor / canciones_mejor
            if canciones_mejor > 0 and tiempo_mejor > 0
            else float("inf")
        )

        if tiempo_prom_actual < tiempo_prom_mejor:

            mejor = registro
            continue

    return mejor
