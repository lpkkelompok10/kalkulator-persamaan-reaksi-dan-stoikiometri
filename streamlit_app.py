import streamlit as st
import re

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="Kalkulator Kimia",
    page_icon="🧪",
    layout="centered"
)

# ==========================================
# JUDUL
# ==========================================

st.title("🧪 Kalkulator Kimia Lengkap")

st.write(
    "Aplikasi sederhana untuk menghitung "
    "stoikiometri, massa molar, mol, "
    "dan menampilkan reaksi kimia"
)

# ==========================================
# DATA REAKSI
# ==========================================

reaksi_data = {

    "H2 + O2 -> H2O": {
        "setara": "2H2 + O2 -> 2H2O",
        "koef": {
            "H2": 2,
            "O2": 1,
            "H2O": 2
        }
    },

    "N2 + H2 -> NH3": {
        "setara": "N2 + 3H2 -> 2NH3",
        "koef": {
            "N2": 1,
            "H2": 3,
            "NH3": 2
        }
    },

    "Fe + O2 -> Fe2O3": {
        "setara": "4Fe + 3O2 -> 2Fe2O3",
        "koef": {
            "Fe": 4,
            "O2": 3,
            "Fe2O3": 2
        }
    },

    "Na + Cl2 -> NaCl": {
        "setara": "2Na + Cl2 -> 2NaCl",
        "koef": {
            "Na": 2,
            "Cl2": 1,
            "NaCl": 2
        }
    },

    "CH4 + O2 -> CO2 + H2O": {
        "setara": "CH4 + 2O2 -> CO2 + 2H2O",
        "koef": {
            "CH4": 1,
            "O2": 2,
            "CO2": 1,
            "H2O": 2
        }
    }
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

    st.header("⚖ Persamaan Reaksi Kimia")

    pilihan = st.selectbox(

        "Pilih reaksi",

        list(reaksi_data.keys())
    )

    hasil = reaksi_data[pilihan]["setara"]

    st.success("✅ Persamaan reaksi setara")

    st.code(hasil)

# ==========================================
# FITUR STOIKIOMETRI
# ==========================================

elif menu == "Stoikiometri":

    st.header("🧪 Perhitungan Stoikiometri")

    pilihan = st.selectbox(

        "Pilih reaksi",

        list(reaksi_data.keys())
    )

    data = reaksi_data[pilihan]

    st.code(data["setara"])

    koef = data["koef"]

    semua_zat = list(koef.keys())

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

            koef[zat_ditanya] /

            koef[zat_diketahui]
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
