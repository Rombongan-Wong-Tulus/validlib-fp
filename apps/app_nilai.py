import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apps.menu import jalankan_menu
from validlib import hanya_angka, panjang, rentang, semua, wajib_isi


aturan = {
    "nim": semua(wajib_isi, hanya_angka),
    "nama": semua(wajib_isi, panjang(3, 50)),
    "skor": semua(hanya_angka, rentang(0, 100)),
}


def main() -> None:
    """Menjalankan menu pencatatan nilai mahasiswa."""
    jalankan_menu("Nilai", aturan, "Data nilai berhasil disimpan.")


if __name__ == "__main__":
    main()
