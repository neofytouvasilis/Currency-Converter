import flet as ft

from api import convert_currency
from utils import is_valid_amount


def main(page: ft.Page):
    page.title = "Currency Converter"
    page.window.width = 380
    page.window.height = 450
    page.padding = 20

    amount_input = ft.TextField(
        label="Amount",
        value="1",
        width=300,
    )

    from_input = ft.TextField(
        label="From Currency",
        value="USD",
        width=300,
    )

    to_input = ft.TextField(
        label="To Currency",
        value="EUR",
        width=300,
    )

    result_text = ft.Text(
        "",
        size=20,
        weight=ft.FontWeight.BOLD,
    )

    rate_text = ft.Text("", size=14)

    def convert_click(e):
        amount = amount_input.value

        if not is_valid_amount(amount):
            result_text.value = "Please enter a valid amount."
            rate_text.value = ""
            page.update()
            return

        try:
            amount = float(amount)

            from_currency = from_input.value.strip().upper()
            to_currency = to_input.value.strip().upper()

            converted, rate = convert_currency(
                amount,
                from_currency,
                to_currency,
            )

            result_text.value = (
                f"{amount:.2f} {from_currency} = "
                f"{converted:.2f} {to_currency}"
            )

            rate_text.value = (
                f"1 {from_currency} = "
                f"{rate:.4f} {to_currency}"
            )

        except Exception as ex:
            result_text.value = f"Error: {ex}"
            rate_text.value = ""

        page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "💱 Currency Converter",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                ),
                amount_input,
                from_input,
                to_input,
                ft.ElevatedButton(
                    "Convert",
                    width=300,
                    on_click=convert_click,
                ),
                result_text,
                rate_text,
            ],
            spacing=18,
        )
    )


ft.app(target=main)