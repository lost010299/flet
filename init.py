# Importamos Flet
import flet as ft
from fpdf import FPDF
# Creamos una clase para el formulario
class FormularioApp:
    def __init__(self):
        # Campos de texto para que el usuario ingrese datos
        # Campos de texto para que el usuario ingrese datos
        self.nombre = ft.TextField(label="Nombre", width=300)
        self.correo = ft.TextField(label="Correo", width=300)
        self.edad = ft.TextField(label="Edad", width=300)
        self.sangre = ft.TextField(label="Tipo de sangre", width=300)
        self.dni = ft.TextField(label="DNI", width=300)
        self.link_descarga = ft.Text() 
        # Texto donde se mostrará el resultado
        self.resultado = ft.Text(value="", size=16)

    # Función que se ejecuta cuando se presiona el botón "Enviar"
    def enviar_datos(self, e):     
        self.resultado.value = (
        f"Nombre: {self.nombre.value}\n"
        f"Correo: {self.correo.value}\n"
        f"Edad: {self.edad.value}\n"
        f"Tipo de sangre: {self.sangre.value}\n"
        f"DNI: {self.dni.value}"
    )
        self.page.update()
    # Función principal que crea la interfaz
    def main(self, page: ft.Page):
        self.page = page  # Guardamos la referencia a la página
        self.page.title = "Formulario Básico con Flet"
        self.page.bgcolor = "white"  # Fondo blanco
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        # Botones guardados en self
        self.boton_enviar = ft.ElevatedButton(text="Enviar", on_click=self.enviar_datos)
        self.boton_pdf = ft.ElevatedButton(text="Generar PDF", on_click=self.generar_pdf)

        # Agregamos todos los elementos a la página en una columna
        self.page.add(
            ft.Column(
                  controls=[
                    self.nombre,
                    self.correo,
                    self.edad,
                    self.sangre,
                    self.dni,
                    self.boton_enviar,
                    self.boton_pdf,
                    self.resultado
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

# Arrancamos la aplicación en el navegador
if __name__ == "__main__":
    app = FormularioApp()
    ft.app(target=app.main, view=ft.WEB_BROWSER)
