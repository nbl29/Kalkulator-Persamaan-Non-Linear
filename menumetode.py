import os
import time
from metode_tabel import metode_tabel
from metode_bisection import metode_bisection
from metode_regulafalsi import metode_regulafalsi

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich.rule import Rule

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu_metode():
    clear_screen()

    console.print()
    console.print(Align.center(
        Text("⚙️   PILIH METODE NUMERIK", style="bold white")
    ))
    console.print(Rule(style="blue"))
    console.print()

    # Info kategori
    console.print(Panel(
        "[dim]Metode Tertutup (Closed Methods)[/dim]\n"
        "Membutuhkan interval [bold cyan][a, b][/bold cyan] dengan syarat [bold]f(a) · f(b) < 0[/bold]",
        border_style="dim blue",
        padding=(0, 2),
        width=56,
    ))
    console.print()

    # Daftar metode
    items = Text()
    items.append("  [1]", style="bold green")
    items.append("  Metode Tabel\n", style="white")
    items.append("       Tabulate f(x) pada interval untuk deteksi akar\n\n", style="dim")
    items.append("  [2]", style="bold cyan")
    items.append("  Metode Bisection\n", style="white")
    items.append("       Bagi dua interval secara rekursif hingga konvergen\n\n", style="dim")
    items.append("  [3]", style="bold magenta")
    items.append("  Metode Regula Falsi\n", style="white")
    items.append("       Interpolasi linear untuk perkiraan akar lebih cepat\n\n", style="dim")
    items.append("  [0]", style="bold red")
    items.append("  Kembali ke Menu Utama", style="white")

    console.print(Panel(
        items,
        title="[bold white]📐  METODE[/bold white]",
        border_style="blue",
        padding=(1, 2),
        width=56,
    ))
    console.print(Rule(style="dim blue"))

def menu_metode():
    while True:
        tampilkan_menu_metode()
        pilihan = console.input("\n  [bold blue]›[/bold blue]  Pilihan [[bold]0/1/2/3[/bold]]: ").strip()

        if pilihan == "1":
            metode_tabel()
        elif pilihan == "2":
            metode_bisection()
        elif pilihan == "3":
            metode_regulafalsi()
        elif pilihan == "0":
            clear_screen()
            break
        else:
            console.print(
                Panel("[bold red]⚠️   Pilihan tidak valid, coba lagi.[/bold red]",
                      border_style="red", padding=(0, 2), width=56)
            )
            time.sleep(1.2)
