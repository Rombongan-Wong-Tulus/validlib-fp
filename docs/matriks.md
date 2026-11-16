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

`validasi_form` tidak lagi dipanggil langsung di tiap aplikasi. Pemanggilannya ada satu kali di
`apps/menu.py:28` (fungsi `jalankan_menu`), dan setiap aplikasi memakainya dengan memanggil
`jalankan_menu(judul, aturan, pesan_sukses)`. Karena itu, lokasi untuk `validasi_form` pada tabel
di bawah menunjuk ke baris pemanggilan `jalankan_menu` di tiap aplikasi.

| Fungsi | Aplikasi | Lokasi pemanggilan |
|---|---|---|
| `wajib_isi` | Pendaftaran | `apps/app_pendaftaran.py:9-10` |
| `wajib_isi` | Kasir | `apps/app_kasir.py:9` |
| `wajib_isi` | Keuangan | `apps/app_keuangan.py:9` |
| `wajib_isi` | Nilai | `apps/app_nilai.py:9-10` |
| `wajib_isi` | Peminjaman | `apps/app_peminjaman.py:9` |
| `hanya_angka` | Pendaftaran | `apps/app_pendaftaran.py:10` |
| `hanya_angka` | Kasir | `apps/app_kasir.py:11` |
| `hanya_angka` | Keuangan | `apps/app_keuangan.py:9` |
| `hanya_angka` | Nilai | `apps/app_nilai.py:9,11` |
| `hanya_angka` | Peminjaman | `apps/app_peminjaman.py:10` |
| `rentang` | Kasir | `apps/app_kasir.py:11` |
| `rentang` | Keuangan | `apps/app_keuangan.py:9` |
| `rentang` | Nilai | `apps/app_nilai.py:11` |
| `rentang` | Peminjaman | `apps/app_peminjaman.py:10` |
| `panjang` | Pendaftaran | `apps/app_pendaftaran.py:9` |
| `panjang` | Kasir | `apps/app_kasir.py:9` |
| `panjang` | Nilai | `apps/app_nilai.py:10` |
| `panjang` | Peminjaman | `apps/app_peminjaman.py:9` |
| `salah_satu` | Pendaftaran | `apps/app_pendaftaran.py:11` |
| `salah_satu` | Kasir | `apps/app_kasir.py:10` |
| `salah_satu` | Keuangan | `apps/app_keuangan.py:10-12` |
| `format_tanggal` | Pendaftaran | `apps/app_pendaftaran.py:12` |
| `format_tanggal` | Kasir | `apps/app_kasir.py:12` |
| `format_tanggal` | Keuangan | `apps/app_keuangan.py:13` |
| `format_tanggal` | Peminjaman | `apps/app_peminjaman.py:11` |
| `semua` | Pendaftaran | `apps/app_pendaftaran.py:9-10` |
| `semua` | Kasir | `apps/app_kasir.py:9,11` |
| `semua` | Keuangan | `apps/app_keuangan.py:9` |
| `semua` | Nilai | `apps/app_nilai.py:9-11` |
| `semua` | Peminjaman | `apps/app_peminjaman.py:9-10` |
| `validasi_form` | Pendaftaran | `apps/app_pendaftaran.py:18` → `apps/menu.py:28` |
| `validasi_form` | Kasir | `apps/app_kasir.py:18` → `apps/menu.py:28` |
| `validasi_form` | Keuangan | `apps/app_keuangan.py:19` → `apps/menu.py:28` |
| `validasi_form` | Nilai | `apps/app_nilai.py:17` → `apps/menu.py:28` |
| `validasi_form` | Peminjaman | `apps/app_peminjaman.py:17` → `apps/menu.py:28` |