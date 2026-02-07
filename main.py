import flet as ft
from scripts.send_email import send_email


def main(page: ft.Page):
    page.title = "Городские жалобы"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    theme_field = ft.TextField(
        label="Тема жалобы",
        multiline=True,
        min_lines=5,
        max_lines=10,
        width=400,
        border_color=ft.Colors.BLUE_GREY_400,
    )

    complaint_field = ft.TextField(
        label="Опишите проблему",
        multiline=True,
        min_lines=5,
        max_lines=10,
        width=400,
        border_color=ft.Colors.BLUE_GREY_400,
    )

    def send(e):
        nonlocal complaint_field
        nonlocal theme_field
        nonlocal send_button
        text = complaint_field.value
        theme = theme_field.value
        page.update()
        send_button.content = 'Отправляем...'
        page.update()
        send_email(theme, text)
        theme_field.value = ''
        complaint_field.value = ''
        send_button.content = 'Отправить'
        page.update()

    send_button = ft.Button(
        content="Отправить",
        icon=ft.Icons.SEND,
        width=400,
        height=50,
        on_click=send
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Жалобы о состоянии городской среды",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Опишите проблему, которую вы заметили в городе",
                    size=14,
                    color=ft.Colors.GREY_700,
                    text_align=ft.TextAlign.CENTER,
                ),
                theme_field,
                complaint_field,
                send_button,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(
    target=main,
    view=ft.AppView.FLET_APP,
    assets_dir="assets"
)
