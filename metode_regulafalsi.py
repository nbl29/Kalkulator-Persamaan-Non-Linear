import os
from helper import (evaluasi, input_fungsi, input_toleransi,
                    input_maks_iter, input_interval)

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.rule import Rule
from rich.align import Align
from rich import box

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def metode_regulafalsi():
    clear_screen()
    console.print()
    console.print(Align.center(
        Text("📐  METODE REGULA FALSI", style="bold white")
    ))
    console.print(Rule(style="magenta"))
    console.print(Panel(
        "[dim]Menggunakan interpolasi linear antara titik [bold magenta]a[/bold magenta] dan [bold magenta]b[/bold magenta]\n"
        "untuk menghampiri akar secara lebih cepat dari Bisection.[/dim]",
        border_style="dim magenta", padding=(0, 2), width=60,
    ))
    console.print()

    # Input
    expr      = input_fungsi()
    console.print()
    a, b      = input_interval()
    tol       = input_toleransi(default=1e-7)
    maks_iter = input_maks_iter(default=100)

    # Cek syarat tanda
    fa = evaluasi(expr, a)
    fb = evaluasi(expr, b)

    if fa is None or fb is None:
        console.input("\n  Tekan Enter untuk kembali...")
        return

    if fa * fb > 0:
        console.print(Panel(
            f"[bold red][ERROR][/bold red] f(a) dan f(b) harus berbeda tanda!\n\n"
            f"  f({a}) = [bold]{fa:.8f}[/bold]\n"
            f"  f({b}) = [bold]{fb:.8f}[/bold]",
            border_style="red", padding=(0, 2), width=60,
        ))
        console.input("\n  Tekan Enter untuk kembali...")
        return

    # Info awal
    console.print()
    console.print(Panel(
        f"[bold]f(x)[/bold]      = [magenta]{expr}[/magenta]\n"
        f"[bold]Interval[/bold]  = [[magenta]{a}[/magenta], [magenta]{b}[/magenta]]\n"
        f"[bold]Toleransi[/bold] = [yellow]{tol:.2e}[/yellow]   │   [bold]Maks Iter[/bold] = [yellow]{maks_iter}[/yellow]",
        title="[bold white]📋  Parameter[/bold white]",
        border_style="blue", padding=(0, 2), width=60,
    ))
    console.print()

    # Buat tabel rich
    tabel = Table(
        title="📊  Tabel Iterasi Regula Falsi",
        box=box.ROUNDED,
        border_style="magenta",
        header_style="bold magenta",
        show_lines=True,
        width=80,
    )
    tabel.add_column("Iter", justify="right", style="bold white", min_width=4)
    tabel.add_column("a", justify="right", style="green", min_width=14)
    tabel.add_column("b", justify="right", style="green", min_width=14)
    tabel.add_column("x (RF)", justify="right", style="bold yellow", min_width=14)
    tabel.add_column("f(x)", justify="right", style="cyan", min_width=13)
    tabel.add_column("|f(x)|", justify="right", style="dim white", min_width=10)

    # Iterasi pertama
    x  = (fb * a - fa * b) / (fb - fa)
    fx = evaluasi(expr, x)
    iterasi = 1

    tabel.add_row(
        str(iterasi),
        f"{a:.8f}",
        f"{b:.8f}",
        f"{x:.8f}",
        f"{fx:.8f}",
        f"{abs(fx):.2e}",
    )

    # Iterasi berikutnya
    while abs(fx) > tol:
        iterasi += 1
        if iterasi > maks_iter:
            console.print("[bold yellow]⚠️   Maksimum iterasi tercapai![/bold yellow]")
            break

        if fa * fx > 0:
            a  = x
            fa = fx
        else:
            b  = x
            fb = fx

        x  = (fb * a - fa * b) / (fb - fa)
        fx = evaluasi(expr, x)

        fx_style = "bold green" if abs(fx) < tol * 100 else "cyan"

        tabel.add_row(
            str(iterasi),
            f"{a:.8f}",
            f"{b:.8f}",
            f"{x:.8f}",
            Text(f"{fx:.8f}", style=fx_style),
            f"{abs(fx):.2e}",
        )

        if fx == 0:
            break

    console.print(tabel)

    # Hasil akhir
    console.print()
    console.print(Panel(
        f"[bold green]✅  Akar ditemukan   :[/bold green]  x = [bold white]{x:.10f}[/bold white]\n"
        f"[bold cyan]📊  Total iterasi    :[/bold cyan]  {iterasi}\n"
        f"[bold yellow]📉  f(root)          :[/bold yellow]  {fx:.4e}\n"
        f"[bold magenta]📏  Error akhir      :[/bold magenta]  {abs(fx):.4e}",
        title="[bold white]🏁  HASIL[/bold white]",
        border_style="green",
        padding=(1, 4),
        width=60,
    ))
    console.print()
    console.input("  Tekan [bold]Enter[/bold] untuk kembali...")
