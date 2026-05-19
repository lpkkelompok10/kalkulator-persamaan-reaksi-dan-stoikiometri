import streamlit as st
import re

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="Kalkulator Kimia",
    page_icon="🧪"
)

# ==========================================
# JUDUL
# ==========================================

st.title("🧪 Kalkulator Stoikiometri")

st.write(
    "Masukkan persamaan reaksi kimia "
    "yang sudah setara"
)

# ==========================================
# MASSA ATOM
# ==========================================

massa_atom = {

    "H": 1,
    "O": 16,
    "C": 12,
    "N": 14,
    "Na": 23,
    "Cl": 35.5,
    "Fe": 56,
    "S": 32,
    "K": 39,
    "Mg": 24,
    "Ca": 40
}

# ==========================================
# FUNGSI HITUNG Mr
# ==========================================

def hitung_mr(rumus):

    pola = r'([A-Z][a-z]?)(\d*)'

    hasil = re.findall(pola, rumus)

    mr = 0

    for unsur, jumlah in hasil:

        jumlah = int(jumlah) if jumlah else 1

        if unsur in massa_atom:

            mr += massa_atom[unsur] * jumlah

    return mr

# ==========================================
# FUNGSI AMBIL KOEFISIEN
# ==========================================

def ambil_koef(zat):

    cocok = re.match(r'(\d*)([A-Za-z0-9]+)', zat)

    if cocok:

        angka = cocok.group(1)
        rumus = cocok.group(2)

        koef = int(angka) if angka else 1

        return koef, rumus

    return 1, zat

# ==========================================
# INPUT REAKSI
# ==========================================

reaksi = st.text_input(

    "Masukkan reaksi setara",

    placeholder="Contoh: 2H2 + O2 -> 2H2O"
)

# ==========================================
# PROSES REAKSI
# ==========================================

if reaksi:

    try:

        kiri, kanan = reaksi.split("->")

        kiri_list = [
            i.strip()
            for i in kiri.split("+")
        ]

        kanan_list = [
            i.strip()
            for i in kanan.split("+")
        ]

        semua = kiri_list + kanan_list

        koef_data = {}

        nama_zat = []

        for zat in semua:

            koef, rumus = ambil_koef(zat)

            koef_data[rumus] = koef

            nama_zat.append(rumus)

        st.success("✅ Reaksi berhasil dibaca")

        st.code(reaksi)

        # ==========================================
        # STOIKIOMETRI
        # ==========================================

        st.divider()

        st.header("🧪 Perhitungan Stoikiometri")

        zat_diketahui = st.selectbox(

            "Zat diketahui",

            nama_zat
        )

        zat_ditanya = st.selectbox(

            "Zat ditanya",

            nama_zat
        )

        massa = st.number_input(

            f"Massa {zat_diketahui} (gram)",

            min_value=0.0
        )

        if st.button("Hitung"):

            mr1 = hitung_mr(zat_diketahui)

            mr2 = hitung_mr(zat_ditanya)

            mol = massa / mr1

            mol_hasil = (

                mol *

                koef_data[zat_ditanya] /

                koef_data[zat_diketahui]
            )

            massa_hasil = mol_hasil * mr2

            st.success(

                f"✅ Massa {zat_ditanya} = "
                f"{massa_hasil:.2f} gram"
            )

            # ==========================================
            # LANGKAH
            # ==========================================

            st.subheader("Langkah Perhitungan")

            st.write(f"Mr {zat_diketahui} = {mr1}")

            st.write(
                f"Mol {zat_diketahui} = "
                f"{massa} / {mr1}"
            )

            st.write(
                f"Mol {zat_diketahui} = "
                f"{mol:.2f} mol"
            )

            st.write(
                f"Perbandingan koefisien = "
                f"{koef_data[zat_diketahui]} : "
                f"{koef_data[zat_ditanya]}"
            )

            st.write(
                f"Mol {zat_ditanya} = "
                f"{mol_hasil:.2f} mol"
            )

            st.write(
                f"Massa {zat_ditanya} = "
                f"{massa_hasil:.2f} gram"
            )

    except:

        st.error(
            "❌ Format salah\n\n"
            "Contoh benar:\n"
            "2H2 + O2 -> 2H2O"
        )

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Dibuat dengan Python dan Streamlit"
)
