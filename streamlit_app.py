import streamlit as st
from chempy import balance_stoichiometry
import re

# ==========================================
# JUDUL
# ==========================================

st.set_page_config(
    page_title="Kalkulator Kimia",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Kalkulator Kimia Lengkap")

st.write(
    "Aplikasi untuk menyetarakan reaksi, "
    "menghitung stoikiometri, mol, massa, "
    "dan massa molar (Mr)"
)

# ==========================================
# DATA MASSA ATOM
# ==========================================

massa_atom = {
    "H": 1,
    "O": 16,
    "C": 12,
    "N": 14,
    "Na": 23,
    "Cl": 35.5,
    "K": 39,
    "Ca": 40,
    "Mg": 24,
    "Fe": 56,
    "S": 32,
    "P": 31,
    "Al": 27,
    "Cu": 63.5,
    "Zn": 65
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
# MENU FITUR
# ==========================================

menu = st.sidebar.selectbox(

    "Pilih Fitur",

    [
        "Penyetaraan Reaksi",
        "Stoikiometri",
        "Hitung Mr",
        "Konversi Gram ↔ Mol",
        "Daftar Massa Atom"
    ]
)

# ==========================================
# FITUR 1
# PENYETARAAN REAKSI
# ==========================================

if menu == "Penyetaraan Reaksi":

    st.header("⚖ Penyetaraan Persamaan Reaksi")

    reaksi = st.text_input(
        "Masukkan reaksi",
        placeholder="Contoh: H2 + O2 -> H2O"
    )

    if st.button("Setarakan"):

        try:

            kiri, kanan = reaksi.split("->")

            reaktan = set(
                i.strip() for i in kiri.split("+")
            )

            produk = set(
                i.strip() for i in kanan.split("+")
            )

            reac, prod = balance_stoichiometry(
                reaktan,
                produk
            )

            hasil_kiri = " + ".join(
                [
                    f"{v if v != 1 else ''}{k}"
                    for k, v in reac.items()
                ]
            )

            hasil_kanan = " + ".join(
                [
                    f"{v if v != 1 else ''}{k}"
                    for k, v in prod.items()
                ]
            )

            hasil = hasil_kiri + " -> " + hasil_kanan

            st.success("✅ Reaksi berhasil disetarakan")

            st.code(hasil)

        except:

            st.error("❌ Format salah")

# ==========================================
# FITUR 2
# STOIKIOMETRI
# ==========================================

elif menu == "Stoikiometri":

    st.header("🧪 Kalkulator Stoikiometri")

    reaksi = st.text_input(
        "Masukkan persamaan reaksi",
        placeholder="Contoh: H2 + O2 -> H2O"
    )

    if reaksi:

        try:

            kiri, kanan = reaksi.split("->")

            reaktan = set(
                i.strip() for i in kiri.split("+")
            )

            produk = set(
                i.strip() for i in kanan.split("+")
            )

            reac, prod = balance_stoichiometry(
                reaktan,
                produk
            )

            hasil_kiri = " + ".join(
                [
                    f"{v if v != 1 else ''}{k}"
                    for k, v in reac.items()
                ]
            )

            hasil_kanan = " + ".join(
                [
                    f"{v if v != 1 else ''}{k}"
                    for k, v in prod.items()
                ]
            )

            hasil = hasil_kiri + " -> " + hasil_kanan

            st.success("✅ Persamaan setara")

            st.code(hasil)

            semua_zat = (
                list(reac.keys()) +
                list(prod.keys())
            )

            semua_koef = {}

            semua_koef.update(reac)
            semua_koef.update(prod)

            zat_diketahui = st.selectbox(
                "Zat diketahui",
                semua_zat
            )

            zat_ditanya = st.selectbox(
                "Zat ditanya",
                semua_zat
            )

            massa = st.number_input(
                f"Massa {zat_diketahui} (gram)",
                min_value=0.0
            )

            if st.button("Hitung Stoikiometri"):

                mr1 = hitung_mr(zat_diketahui)
                mr2 = hitung_mr(zat_ditanya)

                mol = massa / mr1

                mol_hasil = (
                    mol *
                    semua_koef[zat_ditanya] /
                    semua_koef[zat_diketahui]
                )

                massa_hasil = mol_hasil * mr2

                st.success(
                    f"✅ Massa {zat_ditanya} = "
                    f"{massa_hasil:.2f} gram"
                )

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
                    f"Mol {zat_ditanya} = "
                    f"{mol_hasil:.2f} mol"
                )

                st.write(
                    f"Massa {zat_ditanya} = "
                    f"{massa_hasil:.2f} gram"
                )

        except:

            st.error("❌ Reaksi salah")

# ==========================================
# FITUR 3
# HITUNG Mr
# ==========================================

elif menu == "Hitung Mr":

    st.header("⚛ Hitung Massa Molar (Mr)")

    rumus = st.text_input(
        "Masukkan rumus kimia",
        placeholder="Contoh: H2SO4"
    )

    if st.button("Hitung Mr"):

        mr = hitung_mr(rumus)

        st.success(f"✅ Mr {rumus} = {mr}")

# ==========================================
# FITUR 4
# KONVERSI GRAM MOL
# ==========================================

elif menu == "Konversi Gram ↔ Mol":

    st.header("🔄 Konversi Gram dan Mol")

    rumus = st.text_input(
        "Masukkan rumus",
        placeholder="Contoh: NaCl"
    )

    pilihan = st.radio(

        "Pilih konversi",

        [
            "Gram ke Mol",
            "Mol ke Gram"
        ]
    )

    nilai = st.number_input(
        "Masukkan nilai",
        min_value=0.0
    )

    if st.button("Konversi"):

        mr = hitung_mr(rumus)

        if pilihan == "Gram ke Mol":

            hasil = nilai / mr

            st.success(
                f"✅ {nilai} gram {rumus} = "
                f"{hasil:.2f} mol"
            )

        else:

            hasil = nilai * mr

            st.success(
                f"✅ {nilai} mol {rumus} = "
                f"{hasil:.2f} gram"
            )

# ==========================================
# FITUR 5
# DAFTAR MASSA ATOM
# ==========================================

elif menu == "Daftar Massa Atom":

    st.header("📚 Daftar Massa Atom Relatif")

    for unsur, massa in massa_atom.items():

        st.write(f"• {unsur} = {massa}")

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Dibuat dengan Python, Streamlit, dan Chempy"
)
