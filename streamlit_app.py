import streamlit as st
import re

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="Kalkulator Kimia Lengkap",
    page_icon="🧪",
    layout="centered"
)

# ==========================================
# JUDUL
# ==========================================

st.title("🧪 Kalkulator Kimia Lengkap")

st.write(
    "Aplikasi untuk menyetarakan reaksi sederhana, "
    "menghitung stoikiometri, Mr, dan konversi mol"
)

# ==========================================
# DATABASE REAKSI
# ==========================================

reaksi_database = {

    "H2 + O2 -> H2O":
    "2H2 + O2 -> 2H2O",

    "N2 + H2 -> NH3":
    "N2 + 3H2 -> 2NH3",

    "Fe + O2 -> Fe2O3":
    "4Fe + 3O2 -> 2Fe2O3",

    "Na + Cl2 -> NaCl":
    "2Na + Cl2 -> 2NaCl",

    "CH4 + O2 -> CO2 + H2O":
    "CH4 + 2O2 -> CO2 + 2H2O",

    "C2H6 + O2 -> CO2 + H2O":
    "2C2H6 + 7O2 -> 4CO2 + 6H2O",

    "Mg + O2 -> MgO":
    "2Mg + O2 -> 2MgO",

    "CaCO3 -> CaO + CO2":
    "CaCO3 -> CaO + CO2",

    "Zn + HCl -> ZnCl2 + H2":
    "Zn + 2HCl -> ZnCl2 + H2",

    "Al + O2 -> Al2O3":
    "4Al + 3O2 -> 2Al2O3",

    "KClO3 -> KCl + O2":
    "2KClO3 -> 2KCl + 3O2",

    "C3H8 + O2 -> CO2 + H2O":
    "C3H8 + 5O2 -> 3CO2 + 4H2O",

    "SO2 + O2 -> SO3":
    "2SO2 + O2 -> 2SO3",

    "P + O2 -> P2O5":
    "4P + 5O2 -> 2P2O5",

    "NH3 + O2 -> NO + H2O":
    "4NH3 + 5O2 -> 4NO + 6H2O"
}

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
    "Mg": 24,
    "Ca": 40,
    "Zn": 65,
    "Al": 27,
    "K": 39,
    "S": 32,
    "P": 31
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
# AMBIL KOEFISIEN
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
# MENU
# ==========================================

menu = st.sidebar.selectbox(

    "Pilih Fitur",

    [
        "Persamaan Reaksi",
        "Stoikiometri",
        "Hitung Mr",
        "Konversi Gram ↔ Mol",
        "Daftar Massa Atom"
    ]
)

# ==========================================
# FITUR REAKSI
# ==========================================

if menu == "Persamaan Reaksi":

    st.header("⚖ Penyetaraan Reaksi")

    reaksi_input = st.text_input(

        "Masukkan reaksi belum setara",

        placeholder="Contoh: H2 + O2 -> H2O"
    )

    if st.button("Setarakan"):

        if reaksi_input in reaksi_database:

            hasil = reaksi_database[reaksi_input]

            st.success("✅ Reaksi berhasil disetarakan")

            st.code(hasil)

        else:

            st.error(
                "❌ Reaksi belum tersedia di database"
            )

# ==========================================
# FITUR STOIKIOMETRI
# ==========================================

elif menu == "Stoikiometri":

    st.header("🧪 Kalkulator Stoikiometri")

    reaksi_input = st.text_input(

        "Masukkan reaksi belum setara",

        placeholder="Contoh: H2 + O2 -> H2O"
    )

    if reaksi_input in reaksi_database:

        reaksi = reaksi_database[reaksi_input]

        st.success("✅ Persamaan reaksi setara")

        st.code(reaksi)

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

        if st.button("Hitung Stoikiometri"):

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

    else:

        st.info(
            "Masukkan reaksi yang tersedia "
            "di database"
        )

# ==========================================
# FITUR Mr
# ==========================================

elif menu == "Hitung Mr":

    st.header("⚛ Hitung Massa Molar")

    rumus = st.text_input(

        "Masukkan rumus kimia",

        placeholder="Contoh: H2SO4"
    )

    if st.button("Hitung Mr"):

        mr = hitung_mr(rumus)

        st.success(f"✅ Mr {rumus} = {mr}")

# ==========================================
# FITUR KONVERSI
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
                f"✅ {nilai} gram "
                f"{rumus} = "
                f"{hasil:.2f} mol"
            )

        else:

            hasil = nilai * mr

            st.success(
                f"✅ {nilai} mol "
                f"{rumus} = "
                f"{hasil:.2f} gram"
            )

# ==========================================
# FITUR MASSA ATOM
# ==========================================

elif menu == "Daftar Massa Atom":

    st.header("📚 Daftar Massa Atom")

    for unsur, massa in massa_atom.items():

        st.write(f"• {unsur} = {massa}")

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Dibuat dengan Python dan Streamlit"
)
