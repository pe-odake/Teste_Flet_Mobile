import flet as ft
import os

def main(page: ft.Page):
    page.title = "Meu App Móvel"
    page.add(ft.Text("Teste do Drone com o Tablet - BANANA"))

ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8501)))

# TESTE COMMIT - oi
