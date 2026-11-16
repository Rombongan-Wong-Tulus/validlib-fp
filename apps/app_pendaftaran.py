import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from validlib import format_tanggal, hanya_angka, panjang, salah_satu, semua, validasi_form, wajib_isi


aturan = {
    "nama": semua(wajib_isi, panjang(3, 50)),
    "nim": semua(wajib_isi, hanya_angka),
    "jurusan": salah_satu(["Informatika", "Sipil", "Mesin", "Elektro"]),
    "tgl_lahir(YYYY-MM-DD)": format_tanggal,
}


def main() -> None:
    """Menjalankan menu pendaftaran mahasiswa."""
    data_mahasiswa: list[dict[str, str]] = []
    while True:
        print("\nMenu Pendaftaran")
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
                data_mahasiswa.append(data)
                print("Data pendaftaran berhasil disimpan.")
            else:
                for field, pesan in errors.items():
                    print(f"{field}: {pesan}")
        elif pilihan == "2":
            if data_mahasiswa:
                for data in data_mahasiswa:
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
