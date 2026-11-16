import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apps.menu import jalankan_menu
from validlib import format_tanggal, hanya_angka, panjang, rentang, semua, wajib_isi


aturan = {
    "judul": semua(wajib_isi, panjang(3, 100)),
    "lama_pinjam": semua(hanya_angka, rentang(1, 14)),
    "tanggal_pinjam": format_tanggal,
}


def main() -> None:
    """Menjalankan menu pencatatan peminjaman buku."""
    jalankan_menu("Peminjaman", aturan, "Data peminjaman berhasil disimpan.")


if __name__ == "__main__":
    main()