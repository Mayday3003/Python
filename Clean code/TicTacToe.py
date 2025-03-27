from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class TrikiSimple(App):
    jugador = "X"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ganador = None  # Asegura que siempre exista el atributo

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Crear el tablero 3x3
        self.botones = []
        for fila in range(3):
            fila_layout = BoxLayout()
            for col in range(3):
                boton = Button(font_size=60, on_press=self.jugar)
                self.botones.append(boton)
                fila_layout.add_widget(boton)
            self.layout.add_widget(fila_layout)

        return self.layout

    def jugar(self, boton):
        # Si la casilla está vacía y no hay ganador
        if boton.text == "" and self.ganador is None:
            boton.text = self.jugador

            # Verificar si hay ganador
            if self.verificar_ganador():
                self.mostrar_ganador()
            else:
                # Cambiar jugador
                self.jugador = "O" if self.jugador == "X" else "X"

    def show_popup(self, instance):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text="¡Hola! Soy una ventana flotante."))
        btn_close = Button(text="Cerrar", size_hint=(None, None), size=(100, 50))

        popup = Popup(title="Ventana Flotante",
                      content=content,
                      size_hint=(None, None),
                      size=(300, 200),
                      auto_dismiss=False)

        btn_close.bind(on_press=popup.dismiss)
        content.add_widget(btn_close)

        popup.open()  # Muestra la ventana emergente

    def verificar_ganador(self):
        # Obtener el estado del tablero
        tablero = [elemento.text for elemento in self.botones]

        # Combinaciones ganadoras
        lineas = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]

        for a, b, c in lineas:
            if tablero[a] == tablero[b] == tablero[c] != "":
                self.ganador = tablero[a]
                return True
        return False

    def mostrar_ganador(self):
        # Bloquea el tablero cuando hay un ganador
        for boton in self.botones:
            boton.disabled = True
            if boton.text == "":
                boton.background_color = [0.8, 0.8, 0.8, 1]

        # Mostrar el popup con el ganador
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=f"¡El ganador es {self.ganador}!"))
        btn_close = Button(text="Cerrar", size_hint=(None, None), size=(100, 50))

        popup = Popup(title="Juego terminado",
                      content=content,
                      size_hint=(None, None),
                      size=(300, 200),
                      auto_dismiss=False)

        btn_close.bind(on_press=popup.dismiss)
        content.add_widget(btn_close)

        popup.open()  # Muestra el mensaje del ganador

TrikiSimple().run()
