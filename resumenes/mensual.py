# ./RegistroLaboral/resumenes/mensual.py


def es_falta(detalles):

    return (
        detalles.strip().lower()
        == "no registrado"
    )


def es_dia_trabajado(
    canciones,
    tiempo_seg,
    dinero,
    detalles
):

    if es_falta(detalles):
        return False

    return (
        canciones > 0
        or tiempo_seg > 0
        or dinero > 0
    )


# ===============================
# RESUMEN MENSUAL
# ===============================

def calcular_resumen_mensual(registros):

    canciones_totales = 0
    tiempo_total = 0
    dinero_total = 0

    dias_trabajados = 0
    faltas_totales = 0
    faltas_justificadas = 0
    faltas_injustificadas = 0

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

        if tipo_registro == "justificada":

            faltas_totales += 1
            faltas_justificadas += 1
            continue

        if (
            canciones == 0
            and tiempo_seg == 0
            and dinero == 0
        ):
            faltas_totales += 1
            faltas_injustificadas += 1
            continue

        if es_dia_trabajado(
            canciones,
            tiempo_seg,
            dinero,
            detalles
        ):

            dias_trabajados += 1

            canciones_totales += canciones
            tiempo_total += tiempo_seg
            dinero_total += dinero

    return {
        "canciones_totales":
            canciones_totales,

        "tiempo_total":
            tiempo_total,

        "dinero_total":
            dinero_total,

        "dias_trabajados":
            dias_trabajados,

        "faltas_totales":
            faltas_totales,

        "faltas_justificadas":
            faltas_justificadas,

        "faltas_injustificadas":
            faltas_injustificadas
    }
