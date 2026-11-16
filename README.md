# validlib-fp

Library validasi bergaya fungsional dalam `validlib.py`, digunakan oleh lima aplikasi CLI untuk mengelola data sederhana. Loop menu yang sama untuk kelima aplikasi berada di `apps/menu.py`.

## Anggota kelompok

Pemrograman Fungsional G

- Mohamad Akbar Noviandi (202410370110388)
- Rico Shandika Jovial Agista (202410370110433)

## Struktur proyek

```
validlib.py          library validasi (8 fungsi)
apps/menu.py         menu CLI bersama (jalankan_menu)
apps/app_*.py        lima aplikasi: pendaftaran, kasir, keuangan, nilai, peminjaman
test_validlib.py     tes untuk validlib.py
test_menu.py         tes untuk apps/menu.py
docs/matriks.md      matriks pemakaian fungsi beserta nomor baris
laporan/             tempat laporan PDF
```

## Setup

Dibutuhkan Python 3.10 atau lebih baru.

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
| `hanya_angka(nilai)` | Memastikan teks berupa angka desimal biasa tanpa tanda, misalnya `12` atau `3.5`. Menolak `-2`, `+7`, `nan`, `inf`, `1e3`, `5.`, dan `.5` |
| `rentang(minimum, maksimum)` | Membuat validator angka dalam rentang inklusif, dengan aturan angka yang sama seperti `hanya_angka` |
| `panjang(minimum, maksimum)` | Membuat validator panjang teks setelah `strip` |
| `salah_satu(pilihan)` | Membuat validator pilihan tanpa membedakan kapitalisasi dan mengabaikan spasi di tepi |
| `format_tanggal(nilai)` | Memastikan tanggal valid dengan format `YYYY-MM-DD` |
| `semua(*validator)` | Menggabungkan validator dan berhenti pada kegagalan pertama |
| `validasi_form(aturan, data)` | Memvalidasi form dan mengumpulkan pesan per field |

Setiap validator mengembalikan tuple `(lolos, pesan)`. Jika lolos, pesannya string kosong.

Contoh pemakaian:

```python
from validlib import semua, hanya_angka, rentang

periksa_jumlah = semua(hanya_angka, rentang(1, 99))
print(periksa_jumlah("12"))  # (True, '')
print(periksa_jumlah("0"))   # (False, 'Nilai harus antara 1 dan 99')
print(periksa_jumlah("1e3")) # (False, 'Nilai harus berupa angka')
```

## Menu bersama

`jalankan_menu(judul, aturan, pesan_sukses)` di `apps/menu.py` menampilkan menu tambah data, lihat data, dan keluar. Fungsi ini memanggil `validasi_form` untuk memeriksa setiap data baru. Setiap aplikasi hanya mendefinisikan `aturan`, judul, dan pesan suksesnya sendiri.

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

Jalankan dari root repo:

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

`validasi_form` dipanggil di `apps/menu.py` dan dipakai oleh kelima aplikasi lewat `jalankan_menu`.

Rincian bukti pemakaian beserta nomor baris tersedia di [docs/matriks.md](docs/matriks.md).