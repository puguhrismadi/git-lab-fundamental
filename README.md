# 📘 Panduan Instalasi & Penggunaan Aplikasi Buku Tamu

Aplikasi **Buku Tamu** ini dibuat menggunakan **Python (Flask)**, **SQLite**, dan **Tailwind CSS**. Aplikasi digunakan untuk mencatat data tamu secara digital melalui form web dan menampilkan data tamu dalam bentuk tabel dengan pagination.

---

## 🧩 Teknologi yang Digunakan

* Python 3.9+
* Flask
* SQLite (Database lokal)
* HTML + Tailwind CSS (CDN)

---

## 📁 Struktur Folder Aplikasi

```
guestbook/
│
├── main.py                # File utama aplikasi Flask
├── database.db            # Database SQLite (auto-generate)
├── requirements.txt       # Daftar library Python
│
├── templates/
│   ├── index.html         # Form input buku tamu
│   └── tamu_list.html     # Tabel data tamu + pagination
```

---

## ⚙️ 1. Persiapan Lingkungan

### 1.1 Pastikan Python Terinstal

Cek versi Python:

```bash
python --version
```

Disarankan menggunakan **Python 3.9 atau lebih baru**.

---

### 1.2 Membuat Virtual Environment (Disarankan)

```bash
python -m venv venv
```

Aktifkan virtual environment:

* **Windows**

```bash
venv\Scripts\activate
```

* **Linux / macOS**

```bash
source venv/bin/activate
```

---

## 📦 2. Instalasi Library

Pastikan file `requirements.txt` berisi:

```txt
Flask==3.0.0
```

Install semua dependency:

```bash
pip install -r requirements.txt
```

---

## ▶️ 3. Menjalankan Aplikasi

Jalankan aplikasi Flask dengan perintah:

```bash
python main.py
```

Jika berhasil, akan muncul informasi seperti:

```
Running on http://127.0.0.1:5000
```

---

## 🌐 4. Akses Aplikasi

### 4.1 Form Input Buku Tamu

Buka browser dan akses:

```
http://127.0.0.1:5000/
```

Fungsi:

* Mengisi data tamu
* Data otomatis tersimpan ke database
* Muncul notifikasi **"Data berhasil disimpan"**

---

### 4.2 Halaman Data Tamu (Tabel + Pagination)

Akses:

```
http://127.0.0.1:5000/tamu
```

Fungsi:

* Menampilkan seluruh data tamu
* Pagination otomatis
* Urut berdasarkan waktu kunjungan terbaru

---

## 🗄️ 5. Database SQLite

* Database bernama `database.db`
* Dibuat otomatis saat aplikasi pertama dijalankan

### Struktur Tabel `tamu`

| Kolom           | Tipe Data | Keterangan       |
| --------------- | --------- | ---------------- |
| id              | INTEGER   | Primary Key      |
| nama            | TEXT      | Nama tamu        |
| instansi        | TEXT      | Asal instansi    |
| tujuan          | TEXT      | Tujuan kunjungan |
| no_hp           | TEXT      | Nomor HP         |
| waktu_kunjungan | TEXT      | Timestamp        |

---

## 🎨 6. Desain Antarmuka (UI)

* Menggunakan **Tailwind CSS CDN**
* Border input tegas (`border-2`)
* Warna soft & profesional
* Cocok untuk:

  * Instansi pemerintahan
  * Sekolah / kampus
  * Kantor / pos keamanan

---

## 🚀 7. Pengembangan Lanjutan (Opsional)

Aplikasi ini siap dikembangkan ke level lanjutan:

* 🔐 Login admin / petugas
* 🔍 Pencarian & filter data tamu
* 📄 Export PDF / Excel
* 🖨️ Cetak laporan harian
* 📸 Foto tamu (kamera)
* 🧾 QR Code badge tamu
* 🖥️ Mode kiosk (layar sentuh)

---

## ✅ 8. Penutup

Aplikasi buku tamu ini cocok sebagai:

* Studi kasus pembelajaran Flask
* Sistem buku tamu digital instansi
* Prototype sistem resepsionis

Silakan dikembangkan sesuai kebutuhan organisasi Anda.

---

📌 **Dikembangkan menggunakan Python & Flask**
