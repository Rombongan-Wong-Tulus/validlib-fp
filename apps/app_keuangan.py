import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apps.menu import jalankan_menu
from validlib import format_tanggal, hanya_angka, rentang, salah_satu, semua, wajib_isi


aturan = {
    "nominal": semua(wajib_isi, hanya_angka, rentang(1, 1000000000)),
    "kategori": salah_satu(
        ["pemasukan", "makanan", "transport", "hiburan", "lainnya"]
    ),
    "tanggal": format_tanggal,
}


def main() -> None:
    """Menjalankan menu pencatatan keuangan."""
    jalankan_menu("Keuangan", aturan, "Data keuangan berhasil disimpan.")


if __name__ == "__main__":
    main()