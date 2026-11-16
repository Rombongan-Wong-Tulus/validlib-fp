import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from validlib import hanya_angka, panjang, rentang, semua, validasi_form, wajib_isi


aturan = {
    "nim": semua(wajib_isi, hanya_angka),
    "nama": semua(wajib_isi, panjang(3, 50)),
    "skor": semua(hanya_angka, rentang(0, 100)),
}


def main() -> None:
    """Menjalankan menu pencatatan nilai mahasiswa."""
    nilai_mahasiswa: list[dict[str, str]] = []
    while True:
        print("\nMenu Nilai")
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
                nilai_mahasiswa.append(data)
                print("Data nilai berhasil disimpan.")
            else:
                for field, pesan in errors.items():
                    print(f"{field}: {pesan}")
        elif pilihan == "2":
            if nilai_mahasiswa:
                for data in nilai_mahasiswa:
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
