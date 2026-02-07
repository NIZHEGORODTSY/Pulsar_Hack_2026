import flet as ft


def main(page: ft.Page):
    page.title = "Мое Android приложение"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Элементы интерфейса
    txt_name = ft.TextField(label="Ваше имя")
    txt_greeting = ft.Text()

    def say_hello(e):
        txt_greeting.value = f"Привет, {txt_name.value}!"
        page.update()

    page.add(
        ft.Column([
            ft.Text("Добро пожаловать!", size=30),
            txt_name,
            ft.ElevatedButton("Поздороваться", on_click=say_hello),
            txt_greeting
        ])
    )




