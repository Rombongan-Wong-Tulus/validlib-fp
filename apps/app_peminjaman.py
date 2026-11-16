import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from validlib import format_tanggal, hanya_angka, panjang, rentang, semua, validasi_form, wajib_isi


aturan = {
    "judul": semua(wajib_isi, panjang(3, 100)),
    "lama_pinjam": semua(hanya_angka, rentang(1, 14)),
    "tanggal_pinjam": format_tanggal,
}


def main() -> None:
    """Menjalankan menu pencatatan peminjaman buku."""
    peminjaman: list[dict[str, str]] = []
    while True:
        print("\nMenu Peminjaman")
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
                peminjaman.append(data)
                print("Data peminjaman berhasil disimpan.")
            else:
                for field, pesan in errors.items():
                    print(f"{field}: {pesan}")
        elif pilihan == "2":
            if peminjaman:
                for data in peminjaman:
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
