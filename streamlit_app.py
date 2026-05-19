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
    "Aplikasi untuk menyetarakan reaksi kimia, "
    "menghitung stoikiometri, Mr, "
    "dan konversi gram ↔ mol"
)

# ==========================================
# DATABASE 100 REAKSI
# ==========================================

reaksi_database = {

    "H2 + O2 -> H2O": "2H2 + O2 -> 2H2O",
    "N2 + H2 -> NH3": "N2 + 3H2 -> 2NH3",
    "Fe + O2 -> Fe2O3": "4Fe + 3O2 -> 2Fe2O3",
    "Na + Cl2 -> NaCl": "2Na + Cl2 -> 2NaCl",
    "CH4 + O2 -> CO2 + H2O": "CH4 + 2O2 -> CO2 + 2H2O",
    "C2H6 + O2 -> CO2 + H2O": "2C2H6 + 7O2 -> 4CO2 + 6H2O",
    "Mg + O2 -> MgO": "2Mg + O2 -> 2MgO",
    "CaCO3 -> CaO + CO2": "CaCO3 -> CaO + CO2",
    "Zn + HCl -> ZnCl2 + H2": "Zn + 2HCl -> ZnCl2 + H2",
    "Al + O2 -> Al2O3": "4Al + 3O2 -> 2Al2O3",
    "KClO3 -> KCl + O2": "2KClO3 -> 2KCl + 3O2",
    "C3H8 + O2 -> CO2 + H2O": "C3H8 + 5O2 -> 3CO2 + 4H2O",
    "SO2 + O2 -> SO3": "2SO2 + O2 -> 2SO3",
    "P + O2 -> P2O5": "4P + 5O2 -> 2P2O5",
    "NH3 + O2 -> NO + H2O": "4NH3 + 5O2 -> 4NO + 6H2O",
    "HCl + NaOH -> NaCl + H2O": "HCl + NaOH -> NaCl + H2O",
    "H2SO4 + NaOH -> Na2SO4 + H2O": "H2SO4 + 2NaOH -> Na2SO4 + 2H2O",
    "AgNO3 + NaCl -> AgCl + NaNO3": "AgNO3 + NaCl -> AgCl + NaNO3",
    "BaCl2 + Na2SO4 -> BaSO4 + NaCl": "BaCl2 + Na2SO4 -> BaSO4 + 2NaCl",
    "Cu + AgNO3 -> Cu(NO3)2 + Ag": "Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag",
    "Fe + HCl -> FeCl2 + H2": "Fe + 2HCl -> FeCl2 + H2",
    "Na2CO3 + HCl -> NaCl + H2O + CO2": "Na2CO3 + 2HCl -> 2NaCl + H2O + CO2",
    "Ca + H2O -> Ca(OH)2 + H2": "Ca + 2H2O -> Ca(OH)2 + H2",
    "K + H2O -> KOH + H2": "2K + 2H2O -> 2KOH + H2",
    "Mg + HCl -> MgCl2 + H2": "Mg + 2HCl -> MgCl2 + H2",
    "Al + HCl -> AlCl3 + H2": "2Al + 6HCl -> 2AlCl3 + 3H2",
    "C + O2 -> CO2": "C + O2 -> CO2",
    "CO + O2 -> CO2": "2CO + O2 -> 2CO2",
    "S + O2 -> SO2": "S + O2 -> SO2",
    "H2 + Cl2 -> HCl": "H2 + Cl2 -> 2HCl",
    "Na + H2O -> NaOH + H2": "2Na + 2H2O -> 2NaOH + H2",
    "CaO + H2O -> Ca(OH)2": "CaO + H2O -> Ca(OH)2",
    "SO3 + H2O -> H2SO4": "SO3 + H2O -> H2SO4",
    "CO2 + H2O -> H2CO3": "CO2 + H2O -> H2CO3",
    "P2O5 + H2O -> H3PO4": "P2O5 + 3H2O -> 2H3PO4",
    "NO2 + H2O -> HNO3 + NO": "3NO2 + H2O -> 2HNO3 + NO",
    "Fe2O3 + CO -> Fe + CO2": "Fe2O3 + 3CO -> 2Fe + 3CO2",
    "CuO + H2 -> Cu + H2O": "CuO + H2 -> Cu + H2O",
    "ZnO + C -> Zn + CO": "ZnO + C -> Zn + CO",
    "PbO + CO -> Pb + CO2": "PbO + CO -> Pb + CO2",
    "Na + O2 -> Na2O": "4Na + O2 -> 2Na2O",
    "K + O2 -> K2O": "4K + O2 -> 2K2O",
    "Mg + N2 -> Mg3N2": "3Mg + N2 -> Mg3N2",
    "Al + Cl2 -> AlCl3": "2Al + 3Cl2 -> 2AlCl3",
    "Fe + S -> FeS": "Fe + S -> FeS",
    "Cu + O2 -> CuO": "2Cu + O2 -> 2CuO",
    "Ag + S -> Ag2S": "2Ag + S -> Ag2S",
    "Ca + Cl2 -> CaCl2": "Ca + Cl2 -> CaCl2",
    "Mg + Cl2 -> MgCl2": "Mg + Cl2 -> MgCl2",
    "Zn + O2 -> ZnO": "2Zn + O2 -> 2ZnO"
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
    "P": 31,
    "Cu": 63.5,
    "Ag": 108,
    "Ba": 137,
    "Pb": 207
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

    cocok = re.match(r'(\d*)([A-Za-z0-9()]+)', zat)

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
# FITUR PERSAMAAN REAKSI
# ==========================================

if menu == "Persamaan Reaksi":

    st.header("⚖ Penyetaraan Reaksi")

    reaksi_input = st.text_input(

        "Masukkan reaksi belum setara",

        placeholder="Contoh: H2 + O2 -> H2O"
    )

    if st.button("Setarakan Reaksi"):

        if reaksi_input in reaksi_database:

            hasil = reaksi_database[reaksi_input]

            st.success("✅ Reaksi berhasil disetarakan")

            st.code(hasil)

        else:

            st.error(
                "❌ Reaksi tidak tersedia di database"
            )

# ==========================================
# FITUR STOIKIOMETRI
# ==========================================

elif menu == "Stoikiometri":

    st.header("🧪 Perhitungan Stoikiometri")

    reaksi_input = st.text_input(

        "Masukkan reaksi belum setara",

        placeholder="Contoh: H2 + O2 -> H2O"
    )

    if reaksi_input in reaksi_database:

        reaksi = reaksi_database[reaksi_input]

        st.success("✅ Reaksi setara ditemukan")

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

# ==========================================
# FITUR HITUNG Mr
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

        if mr == 0:

            st.error("❌ Rumus tidak dikenali")

        else:

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
# ==========================================
# BACKGROUND GAMBAR
# ==========================================

page_bg = """
<style>

[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1532187863486-abf9dbad1b69");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {
    background: rgba(15,23,42,0.95);
}

.main {
    background: rgba(0,0,0,0);
}

.block-container {
    background: rgba(15,23,42,0.82);
    padding: 2rem;
    border-radius: 20px;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: white !important;
}

.stButton>button {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #1d4ed8, #6d28d9);
    color: white;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)
# ==========================================
# TENTANG KAMI
# ==========================================

st.divider()

st.subheader("👨‍🔬 Tentang Kami")

st.markdown("""
### Kelompok 10

1. Sarah Nur Ichsani (2560774)  
2. Reva Aulia (2560749)  
3. Faturrahman Chandika (2560630)  
4. Nassya Alifha Rasyikha (2560710)  
5. Naisyla Nazwa S. (2560705)

""")
