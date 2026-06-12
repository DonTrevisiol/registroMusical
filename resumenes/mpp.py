# ./RegistroLaboral/resumenes/mpp.py


# ===============================
# M.P.P.
# MEJOR PAGO PROMEDIO
# ===============================

def obtener_mpp(registros):

    mejor = None
    mejor_promedio = None

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

        if canciones <= 0:
            continue

        promedio = dinero / canciones

        if mejor is None:

            mejor = registro
            mejor_promedio = promedio
            continue

        if promedio > mejor_promedio:

            mejor = registro
            mejor_promedio = promedio
            continue

        if promedio < mejor_promedio:
            continue

        # ==========================
        # DESEMPATE 1:
        # MAYOR DINERO TOTAL
        # ==========================

        dinero_mejor = mejor[4]

        if dinero > dinero_mejor:

            mejor = registro
            mejor_promedio = promedio
            continue

        if dinero < dinero_mejor:
            continue

        # ==========================
        # DESEMPATE 2:
        # MENOR TIEMPO PROMEDIO
        # ==========================

        tiempo_prom_actual = (
            tiempo_seg / canciones
            if canciones > 0 and tiempo_seg > 0
            else float("inf")
        )

        tiempo_prom_mejor = (
            mejor[3] / mejor[2]
            if mejor[2] > 0 and mejor[3] > 0
            else float("inf")
        )

        if tiempo_prom_actual < tiempo_prom_mejor:

            mejor = registro
            mejor_promedio = promedio

    return mejor
