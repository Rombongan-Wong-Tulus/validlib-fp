import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apps.menu import jalankan_menu
from validlib import format_tanggal, hanya_angka, panjang, rentang, salah_satu, semua, wajib_isi


aturan = {
    "menu": semua(wajib_isi, panjang(2, 30)),
    "kategori": salah_satu(["makanan", "minuman", "snack"]),
    "jumlah": semua(hanya_angka, rentang(1, 99)),
    "tanggal": format_tanggal,
}


def main() -> None:
    """Menjalankan menu pencatatan transaksi kasir."""
    jalankan_menu("Kasir", aturan, "Data transaksi berhasil disimpan.")


if __name__ == "__main__":
    main()