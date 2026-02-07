import flet as ft

def main(page: ft.Page):
    # Настройки страницы
    page.title = "Простое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT  # или DARK, SYSTEM
    page.padding = 20
    page.window_full_screen = True  # Для мобильных устройств
    
    # Переменные состояния
    counter = 0
    
    # Элементы интерфейса
    title = ft.Text(
        "Добро пожаловать!",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    subtitle = ft.Text(
        "Простое приложение на Flet",
        size=16,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREY
    )
    
    counter_text = ft.Text(
        f"Счетчик: {counter}",
        size=24,
        weight=ft.FontWeight.W_500
    )
    
    # Кнопки
    def increment_counter(e):
        nonlocal counter
        counter += 1
        counter_text.value = f"Счетчик: {counter}"
        page.update()
    
    def reset_counter(e):
        nonlocal counter
        counter = 0
        counter_text.value = f"Счетчик: {counter}"
        page.update()
    
    def show_dialog(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Уведомление"),
            content=ft.Text("Вы нажали на кнопку!"),
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
    
    increment_btn = ft.ElevatedButton(
        "Увеличить",
        on_click=increment_counter,
        icon=ft.Icons.ADD,
        width=150
    )
    
    reset_btn = ft.ElevatedButton(
        "Сбросить",
        on_click=reset_counter,
        icon=ft.Icons.REFRESH,
        width=150,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.RED
    )
    
    action_btn = ft.ElevatedButton(
        "Показать диалог",
        on_click=show_dialog,
        icon=ft.Icons.INFO,
        width=200
    )
    
    # Контейнеры для группировки
    header = ft.Column(
        controls=[
            title,
            subtitle,
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    counter_section = ft.Column(
        controls=[
            counter_text,
            ft.Row(
                controls=[increment_btn, reset_btn],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )
    
    # Навигация (опционально)
    navigation_rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOME,
                selected_icon=ft.Icons.HOME,
                label="Главная"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS,
                selected_icon=ft.Icons.SETTINGS,
                label="Настройки"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.INFO,
                selected_icon=ft.Icons.INFO,
                label="О приложении"
            ),
        ],
    )
    
    # Основной контейнер с содержимым
    content = ft.Container(
        content=ft.Column(
            controls=[
                header,
                ft.Divider(),
                counter_section,
                ft.Divider(height=30),
                action_btn,
                ft.Divider(height=30),
                ft.Text("Дополнительные функции:", weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.PINK),
                    ft.IconButton(icon=ft.Icons.SHARE, icon_color=ft.Colors.BLUE),
                    ft.IconButton(icon=ft.Icons.DOWNLOAD, icon_color=ft.Colors.GREEN),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        expand=True
    )
    
    # Основной макет (с навигацией или без)
    if page.width > 600:  # Для планшетов/горизонтальной ориентации
        page.add(
            ft.Row(
                controls=[navigation_rail, ft.VerticalDivider(width=1), content],
                expand=True
            )
        )
    else:  # Для мобильных телефонов
        page.add(content)

# Запуск приложения
ft.app(
    target=main,
    view=ft.AppView.FLET_APP,  # Для запуска как нативного приложения
    assets_dir="assets"  # Папка для ресурсов (иконки, изображения)
)