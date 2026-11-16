"""Kumpulan validator sederhana bergaya fungsional."""

from datetime import datetime
from typing import Callable, Mapping, Sequence
import re


HasilValidasi = tuple[bool, str]
Validator = Callable[[str], HasilValidasi]


def wajib_isi(nilai: str) -> HasilValidasi:
    """Memastikan teks berisi karakter selain spasi."""
    if nilai.strip() == "":
        return False, "Nilai wajib diisi"
    return True, ""


POLA_ANGKA = re.compile(
    r"""
    [0-9]+         # bagian bulat: satu digit atau lebih
    (\.[0-9]+)?    # bagian pecahan: titik + digit, boleh tidak ada
    """,
    re.VERBOSE,
)

def hanya_angka(nilai: str) -> HasilValidasi:
    if not POLA_ANGKA.fullmatch(nilai.strip()):
        return False, "Nilai harus berupa angka"
    return True, ""


# def hanya_angka(nilai: str) -> HasilValidasi:
#     """Memastikan teks dapat dikonversi menjadi angka."""
#     try:
#         float(nilai)
#     except (TypeError, ValueError):
#         return False, "Nilai harus berupa angka"
#     return True, ""


def rentang(minimum: int | float, maksimum: int | float) -> Validator:
    """Membuat validator angka dengan batas minimum dan maksimum."""
    def validasi(nilai: str) -> HasilValidasi:
        """Memastikan angka berada di dalam rentang yang ditentukan."""
        try:
            angka = float(nilai)
        except (TypeError, ValueError):
            return False, "Nilai harus berupa angka"
        if not minimum <= angka <= maksimum:
            return False, f"Nilai harus antara {minimum} dan {maksimum}"
        return True, ""

    return validasi


def panjang(minimum: int, maksimum: int) -> Validator:
    """Membuat validator panjang teks setelah spasi tepi dihapus."""
    def validasi(nilai: str) -> HasilValidasi:
        """Memastikan panjang teks berada di dalam batas."""
        panjang_teks = len(nilai.strip())
        if not minimum <= panjang_teks <= maksimum:
            return False, f"Panjang teks harus antara {minimum} dan {maksimum} karakter"
        return True, ""

    return validasi


def salah_satu(pilihan: Sequence[str]) -> Validator:
    """Membuat validator keanggotaan yang mengabaikan kapitalisasi."""
    daftar_pilihan = tuple(pilihan)
    pilihan_kecil = tuple(item.casefold() for item in daftar_pilihan)

    def validasi(nilai: str) -> HasilValidasi:
        """Memastikan nilai cocok dengan salah satu pilihan."""
        if nilai.strip().casefold() not in pilihan_kecil:
            daftar = ", ".join(daftar_pilihan)
            return False, f"Nilai harus salah satu dari: {daftar}"
        return True, ""

    return validasi


def format_tanggal(nilai: str) -> HasilValidasi:
    """Memastikan tanggal valid dan berformat YYYY-MM-DD."""
    try:
        tanggal = datetime.strptime(nilai, "%Y-%m-%d")
        if tanggal.strftime("%Y-%m-%d") != nilai:
            return False, "Tanggal harus berformat YYYY-MM-DD yang valid"
    except (TypeError, ValueError):
        return False, "Tanggal harus berformat YYYY-MM-DD yang valid"
    return True, ""


def semua(*validator: Validator) -> Validator:
    """Menggabungkan validator dan berhenti pada kegagalan pertama."""
    def validasi(nilai: str) -> HasilValidasi:
        """Menjalankan validator secara berurutan pada satu nilai."""
        for periksa in validator:
            hasil, pesan = periksa(nilai)
            if not hasil:
                return False, pesan
        return True, ""

    return validasi


def validasi_form(
    aturan: Mapping[str, Validator], data: Mapping[str, str]
) -> tuple[bool, dict[str, str]]:
    """Memeriksa setiap field dan mengumpulkan pesan untuk field yang gagal."""
    errors: dict[str, str] = {}
    for field, validator in aturan.items():
        valid, pesan = validator(data.get(field, ""))
        if not valid:
            errors[field] = pesan
    return not errors, errors
