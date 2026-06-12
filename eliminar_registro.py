# ./RegistroLaboral/eliminar_registro.py

from tkinter import messagebox

import database

def eliminar_registro_seleccionado(tabla):

    seleccion = tabla.selection()

    if not seleccion:
        return

    registro_id = seleccion[0]

    if (
        str(registro_id).startswith("virtual_")
    or
        str(registro_id).startswith("vacaciones_")
    ):


        messagebox.showinfo(
            "Registro protegido",
            "Las faltas virtuales y las cacaciones no pueden editarse ni eliminarse"
        )


        return

    tabla.winfo_toplevel().lift()
    tabla.winfo_toplevel().focus_force()

    confirmar = messagebox.askyesno(
        "Eliminar registro",
        "¿Desea eliminar este registro?"
    )
    tabla.winfo_toplevel().lift()
    tabla.winfo_toplevel().focus_force()

    if not confirmar:
        return

    valores = list(
        tabla.item(registro_id)["values"]
    )

    fecha_texto = valores[1]

    fecha_virtual = (
        fecha_texto.split(" ")[1]
    )

    dia, mes, anio = (
        fecha_virtual.split("/")
    )

    iid_virtual = (
        f"virtual_{anio}-{mes}-{dia}"
    )

    indice = tabla.index(
        registro_id
    )

    database.eliminar_registro(
        registro_id
    )

    tabla.delete(registro_id)

    tabla.insert(
        "",
        indice,
        iid=iid_virtual,
        tags=("rojo",),
        values=(
            valores[0],
            valores[1],
            0,
            "00'00\":00",
            "No disponible",
            "$0.00",
            "No disponible",
            "No registrado"
        )
    )

    tabla.winfo_toplevel().lift()
    tabla.winfo_toplevel().focus_force()

    messagebox.showinfo(
        "Registro eliminado",
        "El registro fue eliminado correctamente."
    )

    tabla.winfo_toplevel().lift()
    tabla.winfo_toplevel().focus_force()
