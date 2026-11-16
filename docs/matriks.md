# Matriks pemakaian validator

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

## Bukti pemakaian dari kode

Nomor baris berikut diambil dengan `grep -n` dari file aplikasi.

| Fungsi | Aplikasi | Lokasi pemanggilan |
|---|---|---|
| `wajib_isi` | Pendaftaran | `apps/app_pendaftaran.py:8-9` |
| `wajib_isi` | Kasir | `apps/app_kasir.py:8` |
| `wajib_isi` | Keuangan | `apps/app_keuangan.py:8` |
| `wajib_isi` | Nilai | `apps/app_nilai.py:8-9` |
| `wajib_isi` | Peminjaman | `apps/app_peminjaman.py:8` |
| `hanya_angka` | Pendaftaran | `apps/app_pendaftaran.py:9` |
| `hanya_angka` | Kasir | `apps/app_kasir.py:10` |
| `hanya_angka` | Keuangan | `apps/app_keuangan.py:8` |
| `hanya_angka` | Nilai | `apps/app_nilai.py:8,10` |
| `hanya_angka` | Peminjaman | `apps/app_peminjaman.py:9` |
| `rentang` | Kasir | `apps/app_kasir.py:10` |
| `rentang` | Keuangan | `apps/app_keuangan.py:8` |
| `rentang` | Nilai | `apps/app_nilai.py:10` |
| `rentang` | Peminjaman | `apps/app_peminjaman.py:9` |
| `panjang` | Pendaftaran | `apps/app_pendaftaran.py:8` |
| `panjang` | Kasir | `apps/app_kasir.py:8` |
| `panjang` | Nilai | `apps/app_nilai.py:9` |
| `panjang` | Peminjaman | `apps/app_peminjaman.py:8` |
| `salah_satu` | Pendaftaran | `apps/app_pendaftaran.py:10` |
| `salah_satu` | Kasir | `apps/app_kasir.py:9` |
| `salah_satu` | Keuangan | `apps/app_keuangan.py:9` |
| `format_tanggal` | Pendaftaran | `apps/app_pendaftaran.py:11` |
| `format_tanggal` | Kasir | `apps/app_kasir.py:11` |
| `format_tanggal` | Keuangan | `apps/app_keuangan.py:12` |
| `format_tanggal` | Peminjaman | `apps/app_peminjaman.py:10` |
| `semua` | Pendaftaran | `apps/app_pendaftaran.py:8-9` |
| `semua` | Kasir | `apps/app_kasir.py:8,10` |
| `semua` | Keuangan | `apps/app_keuangan.py:8` |
| `semua` | Nilai | `apps/app_nilai.py:8-10` |
| `semua` | Peminjaman | `apps/app_peminjaman.py:8-9` |
| `validasi_form` | Pendaftaran | `apps/app_pendaftaran.py:29` |
| `validasi_form` | Kasir | `apps/app_kasir.py:29` |
| `validasi_form` | Keuangan | `apps/app_keuangan.py:30` |
| `validasi_form` | Nilai | `apps/app_nilai.py:28` |
| `validasi_form` | Peminjaman | `apps/app_peminjaman.py:28` |
