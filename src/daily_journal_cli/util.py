from datetime import datetime, date

import typer


def format_date(date: date) -> str:
    date_proper = date.strftime("%b %d, %Y")
    day_of_week = date.strftime("%A")
    return f"[bold blue]{date_proper}[/] [italic dim]({day_of_week})[/]"


def string_to_date(date_string: str) -> date:
    try:
        return datetime.strptime(date_string, "%m/%d/%Y").date()
    except:
        print("[red bold]Please provide date in valid format[/] (example: 05/26/1994).")
        raise typer.Exit()
