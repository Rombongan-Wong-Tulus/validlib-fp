# validlib-fp

Library validasi bergaya fungsional dalam `validlib.py`, digunakan oleh lima aplikasi CLI untuk mengelola data sederhana.

## Anggota kelompok

Pemograman Fungsional G

- Mohamad Akbar Noviandi (202410370110388)
- Rico Shandika Jovial Agista (202410370110434)

## Setup

```bash
python -m venv venv
```

Aktifkan lingkungan virtual:

```bash
# Linux/Mac
source venv/bin/activate

# Windows PowerShell
venv\Scripts\Activate.ps1

# Windows Command Prompt
venv\Scripts\activate.bat
```

Pasang dependensi:

```bash
pip install -r requirements.txt
```

## Fungsi validasi

| Fungsi | Tugas |
|---|---|
| `wajib_isi(nilai)` | Menolak teks kosong atau hanya spasi |
| `hanya_angka(nilai)` | Memastikan teks dapat dikonversi menjadi angka |
| `rentang(minimum, maksimum)` | Membuat validator angka dalam rentang inklusif |
| `panjang(minimum, maksimum)` | Membuat validator panjang teks setelah `strip` |
| `salah_satu(pilihan)` | Membuat validator pilihan tanpa membedakan kapitalisasi |
| `format_tanggal(nilai)` | Memastikan tanggal valid dengan format `YYYY-MM-DD` |
| `semua(*validator)` | Menggabungkan validator dan berhenti pada kegagalan pertama |
| `validasi_form(aturan, data)` | Memvalidasi form dan mengumpulkan pesan per field |

Contoh pemakaian:

```python
from validlib import semua, hanya_angka, rentang

periksa_jumlah = semua(hanya_angka, rentang(1, 99))
print(periksa_jumlah("12"))  # (True, '')
print(periksa_jumlah("0"))   # (False, 'Nilai harus antara 1 dan 99')
```

## Menjalankan aplikasi

Jalankan setiap perintah dari root repo:

```bash
python apps/app_pendaftaran.py
python apps/app_kasir.py
python apps/app_keuangan.py
python apps/app_nilai.py
python apps/app_peminjaman.py
```

## Menjalankan tes

```bash
pytest -v
```

## Matriks pemakaian fungsi

| Fungsi | Pendaftaran | Kasir | Keuangan | Nilai | Peminjaman | Jumlah |
|---|:---:|:---:|:---:|:---:|:---:|---:|
| `wajib_isi` | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| `hanya_angka` | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| `rentang` |  | ✓ | ✓ | ✓ | ✓ | 4 |
| `panjang` | ✓ | ✓ |  | ✓ | ✓ | 4 |
| `salah_satu` | ✓ | ✓ | ✓ |  |  | 3 |
| `format_tanggal` | ✓ | ✓ | ✓ |  | ✓ | 4 |
| `semua` | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| `validasi_form` | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |

Rincian bukti pemakaian beserta nomor baris tersedia di [docs/matriks.md](docs/matriks.md).
