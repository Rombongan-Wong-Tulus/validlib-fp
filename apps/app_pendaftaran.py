import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apps.menu import jalankan_menu
from validlib import format_tanggal, hanya_angka, panjang, salah_satu, semua, wajib_isi


aturan = {
    "nama": semua(wajib_isi, panjang(3, 50)),
    "nim": semua(wajib_isi, hanya_angka),
    "jurusan": salah_satu(["Informatika", "Sipil", "Mesin", "Elektro"]),
    "tgl_lahir": format_tanggal,
}


def main() -> None:
    """Menjalankan menu pendaftaran mahasiswa."""
    jalankan_menu("Pendaftaran", aturan, "Data pendaftaran berhasil disimpan.")


if __name__ == "__main__":
    main()