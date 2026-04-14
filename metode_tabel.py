import os
from helper import evaluasi, input_fungsi, input_toleransi

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

def metode_tabel():
    clear_screen()
    console.print()
    console.print(Align.center(
        Text("📋  METODE TABEL", style="bold white")
    ))
    console.print(Rule(style="green"))
    console.print(Panel(
        "[dim]Menghitung f(x) pada N titik dalam interval [bold green][a, b][/bold green]\n"
        "dan mendeteksi pergantian tanda sebagai indikator akar.[/dim]",
        border_style="dim green", padding=(0, 2), width=60,
    ))
    console.print()

    # Input
    expr = input_fungsi()
    console.print()

    try:
        a     = float(console.input("  [bold yellow]Batas bawah[/bold yellow]  a = "))
        b     = float(console.input("  [bold yellow]Batas atas [/bold yellow]  b = "))
        if a >= b:
            console.print(Panel(
                "[bold red][ERROR][/bold red] Batas bawah harus lebih kecil dari batas atas!",
                border_style="red", padding=(0, 2), width=60,
            ))
            console.input("\n  Tekan Enter untuk kembali...")
            return
        raw_N = console.input("  [bold yellow]Jumlah subinterval[/bold yellow] N (Enter = 20): ").strip()
        N = int(raw_N) if raw_N else 20
        if N <= 0:
            raise ValueError
    except ValueError:
        console.print(Panel(
            "[bold red][ERROR][/bold red] Input tidak valid!",
            border_style="red", padding=(0, 2), width=60,
        ))
        console.input("\n  Tekan Enter untuk kembali...")
        return

    # Hitung
    h      = abs((b - a) / N)
    x_list = [a + i * h for i in range(N + 1)]

    fx_list = []
    for x in x_list:
        fx = evaluasi(expr, x)
        if fx is None:
            console.input("\n  Tekan Enter untuk kembali...")
            return
        fx_list.append(fx)

    # Info awal
    console.print()
    console.print(Panel(
        f"[bold]f(x)[/bold]      = [green]{expr}[/green]\n"
        f"[bold]Interval[/bold]  = [[green]{a}[/green], [green]{b}[/green]]\n"
        f"[bold]N[/bold]         = [yellow]{N}[/yellow]   │   [bold]h[/bold] = [yellow]{h:.6f}[/yellow]",
        title="[bold white]📋  Parameter[/bold white]",
        border_style="blue", padding=(0, 2), width=60,
    ))
    console.print()

    # Buat tabel rich
    tabel = Table(
        title="📊  Tabel Evaluasi f(x)",
        box=box.ROUNDED,
        border_style="green",
        header_style="bold green",
        show_lines=False,
        width=60,
    )
    tabel.add_column("No", justify="right", style="dim white", min_width=4)
    tabel.add_column("x", justify="right", style="cyan", min_width=14)
    tabel.add_column("f(x)", justify="right", style="yellow", min_width=16)
    tabel.add_column("Tanda", justify="center", min_width=6)

    # Isi tabel + deteksi akar
    akar_kandidat = []
    for i in range(N + 1):
        tanda_val = "+" if fx_list[i] >= 0 else "-"
        tanda_style = "bold green" if fx_list[i] >= 0 else "bold red"

        # Tandai baris pergantian tanda
        row_style = None
        if i > 0 and fx_list[i - 1] * fx_list[i] < 0:
            akar_kandidat.append((x_list[i - 1], x_list[i]))
            row_style = "on dark_orange3"

        tabel.add_row(
            str(i),
            f"{x_list[i]:.8f}",
            f"{fx_list[i]:.8f}",
            Text(tanda_val, style=tanda_style),
            style=row_style,
        )

    console.print(tabel)
    console.print()

    # Ringkasan akar
    if akar_kandidat:
        kandidat_text = Text()
        kandidat_text.append("🔍  Kemungkinan akar ditemukan di interval:\n\n", style="bold white")
        for idx, (ka, kb) in enumerate(akar_kandidat, 1):
            kandidat_text.append(f"  [{idx}]  ", style="bold cyan")
            kandidat_text.append(f"({ka:.8f}",  style="yellow")
            kandidat_text.append(" , ", style="dim")
            kandidat_text.append(f"{kb:.8f})", style="yellow")
            kandidat_text.append("\n")
        kandidat_text.append("\n💡  Gunakan interval di atas sebagai input Bisection / Regula Falsi!", style="bold green")

        console.print(Panel(
            kandidat_text,
            border_style="green",
            padding=(1, 2),
            width=60,
        ))
    else:
        console.print(Panel(
            "[bold yellow]⚠️   Tidak ditemukan pergantian tanda.\n\n"
            "[dim]💡  Coba perbesar N atau ubah interval.[/dim]",
            border_style="yellow", padding=(1, 2), width=60,
        ))

    console.print()
    console.input("  Tekan [bold]Enter[/bold] untuk kembali...")
