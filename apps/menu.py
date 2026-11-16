"""Menu CLI bersama untuk semua aplikasi."""

from typing import Callable, Mapping

from validlib import Validator, validasi_form


def jalankan_menu(
    judul: str,
    aturan: Mapping[str, Validator],
    pesan_sukses: str,
    baca: Callable[[str], str] = input,
    tulis: Callable[[str], None] = print,
) -> list[dict[str, str]]:
    """Menjalankan menu tambah/lihat data dan mengembalikan data yang tersimpan."""
    tersimpan: list[dict[str, str]] = []
    while True:
        tulis(f"\nMenu {judul}")
        tulis("1. Tambah data")
        tulis("2. Lihat data")
        tulis("0. Keluar")
        pilihan = baca("Pilih menu: ")
        if pilihan == "1":
            data = {
                field: baca(f"{field.replace('_', ' ').title()}: ")
                for field in aturan
            }
            valid, errors = validasi_form(aturan, data)
            if valid:
                tersimpan.append(data)
                tulis(pesan_sukses)
            else:
                for field, pesan in errors.items():
                    tulis(f"{field}: {pesan}")
        elif pilihan == "2":
            if tersimpan:
                for data in tersimpan:
                    tulis(str(data))
            else:
                tulis("Belum ada data.")
        elif pilihan == "0":
            tulis("Program selesai.")
            return tersimpan
        else:
            tulis("Pilihan menu tidak valid.")