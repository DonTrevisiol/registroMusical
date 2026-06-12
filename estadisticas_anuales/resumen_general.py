# ./RegistroLaboral/estadisticas_anuales/resumen_general.py

from resumenes.mensual import (
    calcular_resumen_mensual
)

def calcular_resumen_anual(registros):

    return calcular_resumen_mensual(
        registros
    )
