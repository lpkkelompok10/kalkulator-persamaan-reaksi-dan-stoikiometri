import streamlit as st

st.title("🧪 Kalkulator Stoikiometri Sederhana")

# =========================
# DATA REAKSI YANG SUDAH DISETARAKAN
# =========================

reaksi_data = {
    "H2 + O2 -> H2O": {
        "hasil": "2H2 + O2 -> 2H2O",
        "koef": {
            "H2": 2,
            "O2": 1,
            "H2O": 2
        }
    },

    "N2 + H2 -> NH3": {
        "hasil": "N2 + 3H2 -> 2NH3",
        "koef": {
            "N2": 1,
            "H2": 3,
            "NH3": 2
        }
    },

    "Fe + O2 -> Fe2O3": {
        "hasil": "4Fe + 3O2 -> 2Fe2O3",
        "koef": {
            "Fe": 4,
            "O2": 3,
            "Fe2O3": 2
        }
    }
}

# =========================
# INPUT REAKSI
# =========================

reaksi = st.selectbox(
    "Pilih reaksi",
    list(reaksi_data.keys())
)

# tampilkan hasil setara
hasil = reaksi_data[reaksi]["hasil"]

st.success("✅ Persamaan setara:")

st.code(hasil)

# =========================
# STOIKIOMETRI
# =========================

st.subheader("Perhitungan Stoikiometri")

koef = reaksi_data[reaksi]["koef"]

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

# =========================
# DATA Mr
# =========================

Mr = {
    "H2": 2,
    "O2": 32,
    "H2O": 18,
    "N2": 28,
    "NH3": 17,
    "Fe": 56,
    "Fe2O3": 160
}

# =========================
# HITUNG
# =========================

if st.button("Hitung"):

    mol = massa / Mr[zat_diketahui]

    mol_hasil = (
        mol *
        koef[zat_ditanya] /
        koef[zat_diketahui]
    )

    massa_hasil = mol_hasil * Mr[zat_ditanya]

    st.success(
        f"Massa {zat_ditanya} = "
        f"{massa_hasil:.2f} gram"
    )
