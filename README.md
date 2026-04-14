# 🧮 Kalkulator Persamaan Non-Linear

Aplikasi kalkulator akar persamaan non-linear berbasis terminal dengan tampilan berwarna menggunakan library **rich**.

Mendukung tiga metode numerik:
- 📋 Metode Tabel
- ✂️ Metode Bisection
- 📐 Metode Regula Falsi

---

## 🪟 Windows — Command Prompt

### 1. Install Python
Jika belum punya Python, unduh di [python.org/downloads](https://www.python.org/downloads/) lalu install.
Pastikan centang ✅ **"Add Python to PATH"** saat proses instalasi.

Cek apakah Python sudah terinstall:
```cmd
python --version
```

### 2. Pindah ke folder proyek
```cmd
cd C:\Users\NamaKamu\Downloads\output
```
> Sesuaikan path di atas dengan lokasi folder hasil ekstrak ZIP.

### 3. Install dependensi
```cmd
pip install rich
```

### 4. Jalankan program
```cmd
python main.py
```

---

## 🐧 Linux — Terminal

### 1. Pastikan Python sudah terinstall
Sebagian besar distro Linux sudah menyertakan Python. Cek versinya:
```bash
python3 --version
```

Jika belum ada, install lewat package manager:
```bash
# Ubuntu / Debian
sudo apt update && sudo apt install python3 python3-pip -y

# Arch Linux
sudo pacman -S python python-pip

# Fedora
sudo dnf install python3 python3-pip
```

### 2. Pindah ke folder proyek
```bash
cd ~/Downloads/output
```
> Sesuaikan path dengan lokasi folder hasil ekstrak ZIP.

### 3. Install dependensi
```bash
pip3 install rich
```

### 4. Jalankan program
```bash
python3 main.py
```

---

## 📱 Termux (Android)

### 1. Install Termux
Unduh Termux dari [F-Droid](https://f-droid.org/packages/com.termux/) (disarankan, bukan dari Play Store).

### 2. Update & install Python
Buka Termux lalu jalankan:
```bash
pkg update && pkg upgrade -y
pkg install python -y
```

### 3. Pindah ke folder proyek
Jika file ZIP sudah diunduh ke penyimpanan internal:
```bash
# Izinkan akses penyimpanan terlebih dahulu
termux-setup-storage

# Masuk ke folder Download
cd ~/storage/downloads/output
```

### 4. Install dependensi
```bash
pip install rich
```

### 5. Jalankan program
```bash
python main.py
```

> **Catatan:** Fitur hitung mundur dengan deteksi tombol Backspace (`msvcrt`) hanya berfungsi di Windows. Di Linux, Termux, dan platform lain, fitur tersebut dilewati secara otomatis dan program tetap berjalan normal.

---

## ✨ Fitur Tampilan

- Banner ASCII art berwarna di menu utama
- Panel berwarna dengan border rounded per metode
- Tabel iterasi otomatis berwarna
- Baris pergantian tanda di-highlight oranye (Metode Tabel)
- Nilai f(x) berubah hijau saat mendekati nol
- Panel hasil akhir dengan ikon ✅ 📊 📉 📏
- Input prompt berwarna dengan ikon `›`
- Pesan error & peringatan dalam panel merah/kuning
