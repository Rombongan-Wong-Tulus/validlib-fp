import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from validlib import format_tanggal, hanya_angka, panjang, rentang, salah_satu, semua, validasi_form, wajib_isi


aturan = {
    "menu": semua(wajib_isi, panjang(2, 30)),
    "kategori": salah_satu(["makanan", "minuman", "snack"]),
    "jumlah": semua(hanya_angka, rentang(1, 99)),
    "tanggal": format_tanggal,
}


def main() -> None:
    """Menjalankan menu pencatatan transaksi kasir."""
    transaksi: list[dict[str, str]] = []
    while True:
        print("\nMenu Kasir")
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
                transaksi.append(data)
                print("Data transaksi berhasil disimpan.")
            else:
                for field, pesan in errors.items():
                    print(f"{field}: {pesan}")
        elif pilihan == "2":
            if transaksi:
                for data in transaksi:
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
