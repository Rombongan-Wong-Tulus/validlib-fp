from typing import Callable

import pytest

from validlib import (
    format_tanggal,
    hanya_angka,
    panjang,
    rentang,
    salah_satu,
    semua,
    validasi_form,
    wajib_isi,
)


@pytest.mark.parametrize("nilai", ["Budi", "0", " teks "])
def test_wajib_isi_lolos(nilai: str) -> None:
    """Memastikan teks berisi diterima."""
    assert wajib_isi(nilai) == (True, "")


@pytest.mark.parametrize("nilai", ["", "   "])
def test_wajib_isi_gagal(nilai: str) -> None:
    """Memastikan teks kosong atau spasi ditolak."""
    assert wajib_isi(nilai)[0] is False


def test_wajib_isi_tidak_mengubah_input() -> None:
    """Memastikan pemeriksaan tidak mengubah teks masukan."""
    nilai = "  Budi  "
    wajib_isi(nilai)
    assert nilai == "  Budi  "


@pytest.mark.parametrize("nilai", ["12", "3.5", "-2", "0"])
def test_hanya_angka_lolos(nilai: str) -> None:
    """Memastikan bilangan bulat dan desimal diterima."""
    assert hanya_angka(nilai) == (True, "")


@pytest.mark.parametrize("nilai", ["", "abc", "3,5"])
def test_hanya_angka_gagal(nilai: str) -> None:
    """Memastikan teks bukan angka ditolak."""
    assert hanya_angka(nilai)[0] is False


def test_hanya_angka_tidak_mengubah_input() -> None:
    """Memastikan pemeriksaan angka tidak mengubah teks masukan."""
    nilai = "3.5"
    hanya_angka(nilai)
    assert nilai == "3.5"


@pytest.mark.parametrize("nilai", ["1", "5.5", "10"])
def test_rentang_batas_dan_tengah_lolos(nilai: str) -> None:
    """Memastikan nilai batas dan nilai di tengah rentang diterima."""
    assert rentang(1, 10)(nilai) == (True, "")


@pytest.mark.parametrize("nilai", ["0", "11", "bukan angka"])
def test_rentang_di_luar_atau_nonangka_gagal(nilai: str) -> None:
    """Memastikan nilai di luar rentang atau nonangka ditolak."""
    assert rentang(1, 10)(nilai)[0] is False


def test_rentang_tidak_mengubah_input() -> None:
    """Memastikan validator rentang tidak mengubah teks masukan."""
    nilai = "5"
    rentang(1, 10)(nilai)
    assert nilai == "5"


def test_rentang_pesan_menampilkan_batas_utuh() -> None:
    """Memastikan pesan batas angka besar tidak memakai notasi ilmiah."""
    assert rentang(1, 1000000000)("0") == (
        False,
        "Nilai harus antara 1 dan 1000000000",
    )


@pytest.mark.parametrize("nilai", ["abc", " abc ", "abcd"])
def test_panjang_batas_dan_tengah_lolos(nilai: str) -> None:
    """Memastikan panjang teks setelah strip memenuhi rentang."""
    assert panjang(3, 4)(nilai) == (True, "")


@pytest.mark.parametrize("nilai", ["", "  ", "ab", "abcde"])
def test_panjang_di_luar_batas_gagal(nilai: str) -> None:
    """Memastikan teks terlalu pendek atau panjang ditolak."""
    assert panjang(3, 4)(nilai)[0] is False


def test_panjang_tidak_mengubah_input() -> None:
    """Memastikan pemeriksaan panjang tidak mengubah teks masukan."""
    nilai = "  abc  "
    panjang(3, 4)(nilai)
    assert nilai == "  abc  "


@pytest.mark.parametrize("nilai", ["Merah", "BIRU", "hijau"])
def test_salah_satu_lolos_tanpa_memandang_kapitalisasi(nilai: str) -> None:
    """Memastikan pilihan diterima tanpa membedakan kapitalisasi."""
    assert salah_satu(["merah", "biru", "hijau"])(nilai) == (True, "")


@pytest.mark.parametrize("nilai", ["", "kuning", " biru "])
def test_salah_satu_gagal(nilai: str) -> None:
    """Memastikan nilai yang tidak cocok dengan pilihan ditolak."""
    assert salah_satu(["merah", "biru"])(nilai)[0] is False


def test_salah_satu_tidak_mengubah_pilihan() -> None:
    """Memastikan daftar pilihan tidak berubah saat validator dibuat."""
    pilihan = ["merah", "biru"]
    salinan = pilihan.copy()
    salah_satu(pilihan)("MERAH")
    assert pilihan == salinan


@pytest.mark.parametrize("nilai", ["2026-02-28", "2000-02-29", "2024-12-31"])
def test_format_tanggal_lolos(nilai: str) -> None:
    """Memastikan tanggal kalender valid diterima."""
    assert format_tanggal(nilai) == (True, "")


@pytest.mark.parametrize(
    "nilai", ["", "2026-02-30", "2026-2-03", "03-02-2026"]
)
def test_format_tanggal_gagal(nilai: str) -> None:
    """Memastikan tanggal tidak valid atau format berbeda ditolak."""
    assert format_tanggal(nilai)[0] is False


def test_format_tanggal_tidak_mengubah_input() -> None:
    """Memastikan validasi tanggal tidak mengubah teks masukan."""
    nilai = "2026-02-28"
    format_tanggal(nilai)
    assert nilai == "2026-02-28"


def test_semua_lolos() -> None:
    """Memastikan seluruh validator yang lolos menghasilkan sukses."""
    periksa = semua(wajib_isi, hanya_angka, rentang(1, 20))
    assert periksa("12") == (True, "")


def test_semua_menghentikan_di_kegagalan_pertama() -> None:
    """Memastikan validator berikutnya tidak dipanggil setelah gagal."""
    dipanggil: list[str] = []

    def validator_kedua(nilai: str) -> tuple[bool, str]:
        """Mencatat pemanggilan validator kedua."""
        dipanggil.append(nilai)
        return False, "Kesalahan pertama"

    def validator_ketiga(nilai: str) -> tuple[bool, str]:
        """Mencatat pemanggilan yang seharusnya terhenti."""
        dipanggil.append("ketiga")
        return False, "Kesalahan berikutnya"

    periksa = semua(validator_kedua, validator_ketiga)
    assert periksa("x") == (False, "Kesalahan pertama")
    assert dipanggil == ["x"]


def test_semua_tidak_mengubah_input() -> None:
    """Memastikan komposisi validator tidak mengubah teks masukan."""
    nilai = "  "
    semua(wajib_isi, hanya_angka)(nilai)
    assert nilai == "  "


def test_validasi_form_semua_lolos() -> None:
    """Memastikan semua field valid menghasilkan errors kosong."""
    aturan: dict[str, Callable[[str], tuple[bool, str]]] = {
        "nama": wajib_isi,
        "nim": hanya_angka,
    }
    data = {"nama": "Budi", "nim": "123"}
    assert validasi_form(aturan, data) == (True, {})


def test_validasi_form_satu_gagal() -> None:
    """Memastikan satu field gagal tercatat dengan namanya."""
    aturan = {"nama": wajib_isi, "nim": hanya_angka}
    assert validasi_form(aturan, {"nama": "", "nim": "123"}) == (
        False,
        {"nama": "Nilai wajib diisi"},
    )


def test_validasi_form_banyak_gagal() -> None:
    """Memastikan semua field gagal dikumpulkan dalam errors."""
    aturan = {"nama": wajib_isi, "nim": hanya_angka}
    valid, errors = validasi_form(aturan, {"nama": " ", "nim": "abc"})
    assert valid is False
    assert set(errors) == {"nama", "nim"}


def test_validasi_form_field_hilang_diperlakukan_kosong() -> None:
    """Memastikan field yang tidak tersedia dianggap sebagai teks kosong."""
    assert validasi_form({"nama": wajib_isi}, {}) == (
        False,
        {"nama": "Nilai wajib diisi"},
    )


def test_validasi_form_tidak_mengubah_input() -> None:
    """Memastikan pemetaan aturan dan data tidak dimutasi."""
    aturan = {"nama": wajib_isi}
    data = {"nama": "Budi"}
    aturan_asli = aturan.copy()
    data_asli = data.copy()
    validasi_form(aturan, data)
    assert aturan == aturan_asli
    assert data == data_asli
