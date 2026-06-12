# ./RegistroLaboral/tabla_utils.py

from datetime import datetime

from constantes import DIAS

from utils import (
    formatear_tiempo_total,
    formatear_tiempo_promedio
)
from utils_fechas import (
    numero_lunes_del_anio
)

def obtener_datos_fila(registro):

        (
            registro_id,
            fecha,
            canciones,
            tiempo_seg,
            dinero,
            detalles,
            tipo_registro
        ) = registro

        if tipo_registro == "vacaciones":

            fecha_dt = datetime.strptime(
                fecha,
                "%Y-%m-%d"
            )

            if fecha_dt.weekday() == 0:

                numero = numero_lunes_del_anio(
                    fecha_dt
                )

                semana = f"#{numero:02d}"

            else:

                semana = ""

            fecha_mostrar = (
                f"{DIAS[fecha_dt.weekday()]} "
                f"{fecha_dt.strftime('%d/%m/%Y')}"
            )

            return (
                "morado",
                (
                    semana,
                    fecha_mostrar,
                    "------",
                    "------",
                    "------",
                    "------",
                    "------",
                    detalles
                )
            )


        if tipo_registro == "justificada":

            fecha_dt = datetime.strptime(
                fecha,
                "%Y-%m-%d"
            )

            if fecha_dt.weekday() == 0:

                numero = numero_lunes_del_anio(
                    fecha_dt
                )

                semana = f"#{numero:02d}"

            else:

                semana = ""

            fecha_mostrar = (
                f"{DIAS[fecha_dt.weekday()]} "
                f"{fecha_dt.strftime('%d/%m/%Y')}"
            )

            return (
                "gris",
                (
                    semana,
                    fecha_mostrar,
                    "---",
                    "---",
                    "---",
                    "---",
                    "---",
                    detalles
                )
            )

        tiempo_total = formatear_tiempo_total(
            tiempo_seg
        )

        if canciones > 0 and tiempo_seg > 0:

            tiempo_promedio = (
                tiempo_seg / canciones
            )

            tiempo_promedio_texto = (
                formatear_tiempo_promedio(
                    tiempo_promedio
                )
            )

        else:

            tiempo_promedio_texto = (
                "No disponible"
            )

        if canciones > 0:

            dinero_promedio = (
                dinero / canciones
            )

            dinero_promedio_texto = (
                f"${dinero_promedio:.2f}"
            )

        else:

            dinero_promedio_texto = (
                "No disponible"
            )

        # ===========================
        # COLOR SEGÚN CANCIONES
        # ===========================

        if canciones >= 20:

            color = "verde"

        elif canciones >= 10:

            color = "azul"

        else:

            color = "rojo"

        fecha_dt = datetime.strptime(
            fecha,
            "%Y-%m-%d"
        )

        if fecha_dt.weekday() == 0:
            numero = numero_lunes_del_anio(
                fecha_dt
            )
            semana = f"#{numero:02d}"
        else:
            semana=""

        fecha_mostrar = (
            f"{DIAS[fecha_dt.weekday()]} "
            f"{fecha_dt.strftime('%d/%m/%Y')}"
        )

        return (
            color,
            (
                semana,
                fecha_mostrar,
                canciones,
                tiempo_total,
                tiempo_promedio_texto,
                f"${dinero:.2f}",
                dinero_promedio_texto,
                detalles
            )
        )
