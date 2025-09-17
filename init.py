# Importamos Flet
import flet as ft

# Creamos una clase para el formulario
class FormularioApp:
    def __init__(self):
        # Campos de texto para que el usuario ingrese datos
        self.nombre = ft.TextField(label="Nombre", width=300)
        self.correo = ft.TextField(label="Correo", width=300)
        
        # Texto donde se mostrará el resultado
        self.resultado = ft.Text(value="", size=16)

    # Función que se ejecuta cuando se presiona el botón "Enviar"
    def enviar_datos(self, e):
        # Tomamos los valores de los campos y los mostramos en self.resultado
        self.resultado.value = f"Nombre: {self.nombre.value}\nCorreo: {self.correo.value}"
        # Actualizamos la página para que se vea el cambio
        self.page.update()

    # Función principal que crea la interfaz
    def main(self, page: ft.Page):
        self.page = page  # Guardamos la referencia a la página
        self.page.title = "Formulario Básico con Flet"
        self.page.bgcolor = "white"  # Fondo blanco
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        # Botón que ejecuta enviar_datos cuando se hace clic
        boton = ft.ElevatedButton(text="Enviar", on_click=self.enviar_datos)

        # Agregamos todos los elementos a la página en una columna
        self.page.add(
            ft.Column(
                controls=[
                    self.nombre,
                    self.correo,
                    boton,
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
