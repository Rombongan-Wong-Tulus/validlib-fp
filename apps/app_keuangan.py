import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from validlib import format_tanggal, hanya_angka, rentang, salah_satu, semua, validasi_form, wajib_isi


aturan = {
    "nominal": semua(wajib_isi, hanya_angka, rentang(1, 1000000000)),
    "kategori": salah_satu(
        ["pemasukan", "makanan", "transport", "hiburan", "lainnya"]
    ),
    "tanggal": format_tanggal,
}


def main() -> None:
    """Menjalankan menu pencatatan keuangan."""
    catatan: list[dict[str, str]] = []
    while True:
        print("\nMenu Keuangan")
        print("1. Tambah data")
        print("2. Lihat data")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            data = {
                field: input(f"{field.replace('_', ' ').title()}: ")
                for field in aturan
            }
            valid, errors = validasi_form(aturan, data)
            if valid:
                catatan.append(data)
                print("Data keuangan berhasil disimpan.")
            else:
                for field, pesan in errors.items():
                    print(f"{field}: {pesan}")
        elif pilihan == "2":
            if catatan:
                for data in catatan:
                    print(data)
            else:
                print("Belum ada data.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan menu tidak valid.")


if __name__ == "__main__":
    main()
