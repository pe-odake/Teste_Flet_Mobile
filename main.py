
# main.py
import flet as ft

def main(page: ft.Page):
    page.title = "Meu App Móvel"
    page.add(ft.Text("Teste do Drone com o Tablet"))

ft.app(target=main, view=ft.WEB_BROWSER)

