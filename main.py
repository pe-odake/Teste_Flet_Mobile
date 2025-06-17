import flet as ft
import random

def main(page: ft.Page):
    page.title = "Contador Interativo 🎯"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    contador = ft.Text(value="0", size=40, weight="bold", color=ft.colors.BLUE_800)
    msg = ft.Text("", size=20)
    confete = ft.Text("🎉", size=50, visible=False)

    def atualizar_contador(e):
        valor = int(contador.value) + 1
        contador.value = str(valor)
        msg.value = random.choice(["Boa!", "Mais um!", "Você consegue!", "👏", "Top!"])
        confete.visible = valor % 10 == 0
        page.update()

    def resetar(e):
        contador.value = "0"
        confete.visible = False
        msg.value = ""
        page.update()

    def alternar_tema(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.BRIGHTNESS_6_OUTLINED, on_click=alternar_tema),
                ft.Text("Modo Claro/Escuro", size=16)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Column(
            [
                contador,
                confete,
                msg,
                ft.Row(
                    [
                        ft.ElevatedButton("Contar +1", icon=ft.icons.ADD, on_click=atualizar_contador),
                        ft.OutlinedButton("Resetar", icon=ft.icons.RESTART_ALT, on_click=resetar),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
