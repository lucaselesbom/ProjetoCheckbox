import flet as ft
from flet_contrib.color_picker import ColorPicker

def main(page: ft.Page):
    page.title = "Teste Checkbox"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.adaptive = True

    def atualizar_checkbox(e):
        checkbox_container.content.label = texto_checkbox.value
        checkbox_container.width = largura_checkbox.value
        checkbox_container.height = altura_checkbox.value
        checkbox_container.bgcolor = color_picker.color

        if estilo_checkbox.value == "Stadium Border":
            checkbox_container.border_radius = 20
        elif estilo_checkbox.value == "Rounded Rectangle":
            checkbox_container.border_radius = 10
        elif estilo_checkbox.value == "Circle":
            checkbox_container.border_radius = 50

        dialogo_cor.open = False
        page.update()

    def abrir_color_picker(e):
        page.dialog = dialogo_cor
        dialogo_cor.open = True
        page.update()

    def fechar_color_picker(e):
        dialogo_cor.open = False
        page.update()

    texto_checkbox = ft.TextField(
        label="Texto do Checkbox",
        hint_text="Selecione aqui",
        value="Selecione aqui",
        on_change=atualizar_checkbox
    )

    largura_checkbox = ft.Slider(
        label="Largura: {value}",
        min=50,
        max=500,
        value=100,
        divisions=20,
        on_change=atualizar_checkbox
    )

    altura_checkbox = ft.Slider(
        label="Altura: {value}",
        min=50,
        max=500,
        value=100,
        divisions=20,
        on_change=atualizar_checkbox
    )

    estilo_checkbox = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(label="Stadium Border", value="Stadium Border"),
            ft.Radio(label="Rounded Rectangle", value="Rounded Rectangle"),
            ft.Radio(label="Circle", value="Circle"),
        ]),
        value="Stadium Border",
        on_change=atualizar_checkbox
    )

    color_picker = ColorPicker(
        color="#FF0000",
        width=300,
    )

    dialogo_cor = ft.AlertDialog(
        content=color_picker,
        actions=[
            ft.TextButton("OK", on_click=atualizar_checkbox),
            ft.TextButton("Cancelar", on_click=fechar_color_picker),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    cor_checkbox = ft.IconButton(
        icon=ft.icons.BRUSH,
        on_click=abrir_color_picker
    )

    checkbox_principal = ft.Checkbox(
        label="Selecione aqui",
    )

    checkbox_container = ft.Container(
        content=checkbox_principal,
        bgcolor="red",
        padding=10,
        border_radius=20,  # Define o raio das bordas
    )

    page.add(
        checkbox_container,
        texto_checkbox,
        ft.Row(controls=[ft.Text("Largura do Checkbox: "), largura_checkbox]),
        ft.Row(controls=[ft.Text("Altura do Checkbox: "), altura_checkbox]),
        ft.Row(controls=[ft.Text("Estilo do Checkbox: "), estilo_checkbox]),
        ft.Row(controls=[ft.Text("Cor de Fundo do Checkbox: "), cor_checkbox]),
    )

    atualizar_checkbox(None)

ft.app(target=main)
