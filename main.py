import os
import time
import threading
import sys
from menumetode import menu_metode
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich import box
from rich.style import Style
from rich.rule import Rule

console = Console()

BANNER = r"""
  _  __     _ _         _       _
 | |/ /__ _| | | ___  _| | __ _| |_ ___  _ __
 | ' // _` | | |/ / | | | / _` | __/ _ \| '__|
 | . \ (_| | |   <| |_| | | (_| | || (_) | |
 |_|\_\__,_|_|_|\_\\__,_|_|\__,_|\__\___/|_|
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu_utama():
    try:
        nama_user = os.getlogin()
    except Exception:
        nama_user = "User"

    clear_screen()

    # Banner
    banner_text = Text(BANNER, style="bold cyan")
    console.print(Align.center(banner_text))

    console.print(Rule(style="cyan"))

    # Subtitle
    console.print(Align.center(
        Text("Kalkulator Persamaan Non-Linear", style="bold white on blue")
    ))
    console.print(Align.center(
        Text("Metode Numerik · Solusi Akar Fungsi", style="dim white")
    ))
    console.print()

    # Welcome
    console.print(Align.center(
        Text(f"👋  Selamat datang, {nama_user}!", style="bold yellow")
    ))
    console.print()

    # Menu items
    menu_content = Text()
    menu_content.append("  [1]", style="bold cyan")
    menu_content.append("  Pilih Metode\n", style="white")
    menu_content.append("  [2]", style="bold red")
    menu_content.append("  Keluar\n", style="white")

    console.print(Panel(
        menu_content,
        title="[bold white]☰  MENU UTAMA[/bold white]",
        border_style="cyan",
        padding=(1, 4),
        width=50,
    ))
    console.print(Rule(style="dim cyan"))

def konfirmasi_exit():
    batal = threading.Event()

    def hitung_mundur():
        for sisa in range(5, 0, -1):
            if batal.is_set():
                return
            sys.stdout.write(
                f"\r  ⏳  Keluar dalam [{sisa}] detik... (Backspace untuk batal)  "
            )
            sys.stdout.flush()
            time.sleep(1)

    def pantau_tombol():
        # Windows
        try:
            import msvcrt
            while not batal.is_set():
                if msvcrt.kbhit():
                    tombol = msvcrt.getch()
                    if tombol == b'\x08':
                        batal.set()
                        return
        except ImportError:
            pass

    clear_screen()
    console.print(Panel(
        "[bold yellow]⚠️   Apakah anda yakin ingin keluar?\n\n"
        "[dim]Tekan [bold white]Backspace[/bold white] untuk membatalkan.[/dim]",
        border_style="yellow",
        padding=(1, 4),
        width=50,
    ))
    console.print()

    t_hitung = threading.Thread(target=hitung_mundur)
    t_tombol = threading.Thread(target=pantau_tombol, daemon=True)

    t_hitung.start()
    t_tombol.start()
    t_hitung.join()

    print()  # newline setelah countdown

    if batal.is_set():
        batal.set()
        return False
    else:
        batal.set()
        return True

def main():
    while True:
        tampilkan_menu_utama()
        pilihan = console.input("\n  [bold cyan]›[/bold cyan]  Pilihan [[bold]1/2[/bold]]: ").strip()

        if pilihan == "1":
            menu_metode()
        elif pilihan == "2":
            if konfirmasi_exit():
                clear_screen()
                console.print(Panel(
                    "[bold green]✅  Terima kasih telah menggunakan kalkulator ini!\n"
                    "[dim white]   Sampai jumpa! 👋[/dim white]",
                    border_style="green",
                    padding=(1, 4),
                    width=50,
                ))
                console.print()
                break
        else:
            console.print(
                Panel("[bold red]⚠️   Pilihan tidak valid, coba lagi.[/bold red]",
                      border_style="red", padding=(0, 2), width=50)
            )
            time.sleep(1.2)

if __name__ == "__main__":
    main()
