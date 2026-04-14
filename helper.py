import math
import re
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def konversi_ekspresi(expr):
    """
    Auto-konversi notasi matematika umum ke sintaks Python:
    - x^2        → x**2
    - 2x         → 2*x
    - 2(x+1)     → 2*(x+1)
    - (x+1)(x-1) → (x+1)*(x-1)
    """
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d)([a-zA-Z(])', r'\1*\2', expr)
    expr = re.sub(r'(\))([a-zA-Z0-9(])', r'\1*\2', expr)
    return expr


def evaluasi(expr, x):
    """Evaluasi f(x) dari string ekspresi."""
    try:
        expr_converted = konversi_ekspresi(expr)
        return eval(expr_converted, {"x": x, "math": math, **vars(math)})
    except Exception as e:
        console.print(f"  [bold red][ERROR][/bold red] Gagal evaluasi f({x}): {e}")
        console.print(f"  [dim][INFO]  Ekspresi setelah konversi: {konversi_ekspresi(expr)}[/dim]")
        return None


def input_fungsi():
    """Input ekspresi fungsi f(x) dengan contoh format."""
    contoh = Text()
    contoh.append("Contoh fungsi yang valid:\n\n", style="dim")
    contoh.append("  x**3 - x - 2", style="cyan")
    contoh.append("  atau  ", style="dim")
    contoh.append("x^3 - x - 2\n", style="cyan")
    contoh.append("  sin(x) - x/2\n", style="cyan")
    contoh.append("  x*exp(-x) + 1\n", style="cyan")
    contoh.append("  2x + 1", style="cyan")
    contoh.append("         atau  ", style="dim")
    contoh.append("2*x + 1\n", style="cyan")
    contoh.append("  2x^2 - 3x + 1\n", style="cyan")
    contoh.append("  log(x) - 1\n", style="cyan")
    contoh.append("  (x+1)(x-1)", style="cyan")

    console.print(Panel(contoh, title="[bold white]📝  Input Fungsi[/bold white]",
                        border_style="cyan", padding=(0, 2), width=56))
    console.print()

    expr = console.input("  [bold cyan]f(x) =[/bold cyan]  ").strip()

    converted = konversi_ekspresi(expr)
    if converted != expr:
        console.print(f"  [dim]→ Dibaca sebagai : [bold white]{converted}[/bold white][/dim]")

    return expr


def input_toleransi(default=1e-7):
    """Terima input toleransi dalam berbagai format."""
    while True:
        raw = console.input(
            f"  [bold yellow]Toleransi[/bold yellow] (contoh: 10^-5, Enter = {default}): "
        ).strip()

        if raw == "":
            return default

        try:
            if "^" in raw:
                basis, eksponen = raw.split("^")
                hasil = float(basis.strip()) ** float(eksponen.strip())
                console.print(f"  [dim]→ Toleransi = [bold white]{hasil:.2e}[/bold white][/dim]")
                return hasil

            hasil = float(raw)
            if hasil <= 0:
                console.print("  [bold red]⚠️   Toleransi harus lebih dari 0![/bold red]\n")
                continue
            console.print(f"  [dim]→ Toleransi = [bold white]{hasil:.2e}[/bold white][/dim]")
            return hasil

        except Exception:
            console.print("  [bold red]⚠️   Format tidak valid! Coba lagi. (contoh: 10^-5 atau 1e-5)[/bold red]\n")


def input_maks_iter(default=100):
    """Input maksimum iterasi dengan nilai default."""
    while True:
        raw = console.input(
            f"  [bold yellow]Maks iterasi[/bold yellow] (Enter = {default}): "
        ).strip()

        if raw == "":
            return default

        try:
            nilai = int(raw)
            if nilai <= 0:
                console.print("  [bold red]⚠️   Harus lebih dari 0![/bold red]\n")
                continue
            return nilai
        except ValueError:
            console.print("  [bold red]⚠️   Input tidak valid, masukkan bilangan bulat![/bold red]\n")


def input_interval():
    """Input batas bawah dan batas atas interval."""
    while True:
        try:
            a = float(console.input("  [bold yellow]Batas bawah[/bold yellow]  a = "))
            b = float(console.input("  [bold yellow]Batas atas [/bold yellow]  b = "))
            if a >= b:
                console.print("  [bold red]⚠️   Batas bawah harus lebih kecil dari batas atas![/bold red]\n")
                continue
            return a, b
        except ValueError:
            console.print("  [bold red]⚠️   Input tidak valid, masukkan angka![/bold red]\n")
