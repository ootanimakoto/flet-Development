import flet as ft


def main(page: ft.Page):
    # Text Control 生成
    t = ft.Text(value="Hello, world!", color="green")
    # ページのコントロールリストに Control を追加
    page.controls.append(t)
    # ページを更新
    page.update()


ft.app(target=main)
