# 🧮 Kalkulator Persamaan Non-Linear

Aplikasi kalkulator akar persamaan non-linear berbasis terminal dengan tampilan berwarna menggunakan library **rich**.

Mendukung tiga metode numerik:
- 📋 Metode Tabel
- ✂️ Metode Bisection
- 📐 Metode Regula Falsi

---

## 📥 Cara Mendapatkan File (Git Clone)

Cara termudah untuk mendapatkan file proyek ini adalah lewat **git clone** — tersedia untuk semua platform di bawah.

### 🪟 Windows (Command Prompt)
Install Git terlebih dahulu di [git-scm.com](https://git-scm.com/download/win), lalu:
```cmd
git clone https://github.com/nbl29/Kalkulator-Persamaan-Non-Linear.git
cd Kalkulator-Persamaan-Non-Linear
```

### 🐧 Linux (Terminal)
```bash
# Install git jika belum ada
sudo apt install git -y       # Ubuntu / Debian
sudo pacman -S git            # Arch Linux
sudo dnf install git          # Fedora

git clone https://github.com/nbl29/Kalkulator-Persamaan-Non-Linear.git
cd Kalkulator-Persamaan-Non-Linear
```

### 📱 Termux (Android)
```bash
pkg install git -y
git clone https://github.com/nbl29/Kalkulator-Persamaan-Non-Linear.git
cd Kalkulator-Persamaan-Non-Linear
```

Setelah berhasil di-clone, lanjut ke langkah instalasi sesuai platform kamu di bawah.

---

## 🪟 Windows — Command Prompt

### 1. Install Python
Jika belum punya Python, unduh di [python.org/downloads](https://www.python.org/downloads/) lalu install.
Pastikan centang ✅ **"Add Python to PATH"** saat proses instalasi.

Cek apakah Python sudah terinstall:
```cmd
python --version
```

### 2. Masuk ke folder proyek
```cmd
cd Kalkulator-Persamaan-Non-Linear
```

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

### 2. Masuk ke folder proyek
```bash
cd Kalkulator-Persamaan-Non-Linear
```

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

### 3. Masuk ke folder proyek
```bash
cd Kalkulator-Persamaan-Non-Linear
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
