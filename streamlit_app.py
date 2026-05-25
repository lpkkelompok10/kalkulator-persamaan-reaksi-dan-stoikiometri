# =========================
# IMPORT
# =========================
import streamlit as st
import requests
from chempy import balance_stoichiometry
from streamlit_lottie import st_lottie

# =========================
# CONFIG PAGE
# =========================
st.set_page_config(
    page_title="Kalkulator Persamaan Reaksi & Stoikiometri",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# FUNCTION LOTTIE
# =========================
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# =========================
# LOAD ANIMATION
# =========================
chem_anim = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_x62chJ.json"
)

atom_anim = load_lottieurl(
    "https://assets2.lottiefiles.com/packages/lf20_touohxv0.json"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

h1, h2, h3, h4, h5, h6 {
    color: white;
}

p, label, div {
    color: white;
}

.stButton>button {
    background-color: #38bdf8;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

.stTextInput>div>div>input {
    border-radius: 10px;
}

.box {
    padding: 20px;
    border-radius: 15px;
    background-color: #1e293b;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
col1, col2 = st.columns([1,2])

with col1:
    st_lottie(chem_anim, height=300)

with col2:
    st.title("⚗️ Kalkulator Persamaan Reaksi & Stoikiometri")

    st.write("""
    Website ini membantu menyetarakan persamaan reaksi kimia 
    serta menghitung stoikiometri secara otomatis dan lebih cepat.

    Cocok digunakan untuk:
    - Pelajar
    - Mahasiswa
    - Praktikum laboratorium
    - Pembelajaran kimia dasar

    Dibuat untuk mempermudah proses perhitungan tanpa harus menghitung manual.
    """)

# =========================
# PENJELASAN
# =========================
st.markdown("## 🔬 Apa Itu Stoikiometri?")

st.markdown("""
<div class="box">

Stoikiometri adalah metode perhitungan kimia yang digunakan 
untuk menentukan hubungan jumlah zat dalam suatu reaksi kimia.

Dengan stoikiometri, kita dapat mengetahui:
<ul>
<li>Jumlah produk yang dihasilkan</li>
<li>Massa zat hasil reaksi</li>
<li>Pereaksi pembatas</li>
<li>Hubungan mol antar senyawa</li>
</ul>

Stoikiometri digunakan dalam:
<ul>
<li>Industri kimia</li>
<li>Farmasi</li>
<li>Pengolahan makanan</li>
<li>Praktikum laboratorium</li>
<li>Penelitian ilmiah</li>
</ul>

</div>
""", unsafe_allow_html=True)

# =========================
# CARA PAKAI
# =========================
st.markdown("## 📘 Cara Menggunakan")

st.info("""
1. Masukkan persamaan reaksi kimia  
2. Klik tombol setarakan  
3. Masukkan massa dan Mr zat  
4. Klik hitung mol  
5. Lihat hasil otomatis  
""")

# =========================
# CONTOH REAKSI
# =========================
st.markdown("## ✨ Contoh Reaksi")

st.success("""
Contoh:
H2 + O2 -> H2O
""")

# =========================
# INPUT REAKSI
# =========================
st.markdown("## ⚖️ Penyetaraan Reaksi Kimia")

reaction = st.text_input(
    "Masukkan Persamaan Reaksi",
    placeholder="Contoh: H2 + O2 -> H2O"
)

# =========================
# FUNCTION PARSE
# =========================
def parse_reaction(reaction):
    reactants, products = reaction.split("->")

    reactants = [
        r.strip()
        for r in reactants.split("+")
    ]

    products = [
        p.strip()
        for p in products.split("+")
    ]

    return reactants, products

# =========================
# BUTTON SETARAKAN
# =========================
if st.button("⚗️ Setarakan Reaksi"):

    try:
        reactants, products = parse_reaction(reaction)

        reac, prod = balance_stoichiometry(
            set(reactants),
            set(products)
        )

        balanced_reactants = " + ".join(
            [
                f"{v if v != 1 else ''}{k}"
                for k, v in reac.items()
            ]
        )

        balanced_products = " + ".join(
            [
                f"{v if v != 1 else ''}{k}"
                for k, v in prod.items()
            ]
        )

        st.success("✅ Reaksi berhasil disetarakan!")

        st.markdown(f"""
        <div class="box">
        <h3>Hasil Reaksi Setara</h3>
        <h2>{balanced_reactants} → {balanced_products}</h2>
        </div>
        """, unsafe_allow_html=True)

    except:
        st.error("❌ Format reaksi salah!")

# =========================
# STOIKIOMETRI
# =========================
st.markdown("## 🧪 Kalkulator Stoikiometri")

col3, col4 = st.columns(2)

with col3:
    massa = st.number_input(
        "Masukkan Massa Zat (gram)",
        min_value=0.0
    )

with col4:
    mr = st.number_input(
        "Masukkan Mr Zat",
        min_value=1.0
    )

# =========================
# HITUNG MOL
# =========================
if st.button("🔍 Hitung Mol"):

    mol = massa / mr

    st.success(f"Jumlah mol = {mol:.2f} mol")

    st.markdown("""
    <div class="box">
    Perhitungan menggunakan rumus:
    </div>
    """, unsafe_allow_html=True)

    st.latex(r'''
    n = \frac{m}{Mr}
    ''')

# =========================
# ANIMATION SECTION
# =========================
st.markdown("## ⚛️ Kimia Itu Menarik!")

col5, col6 = st.columns([2,1])

with col5:
    st.write("""
    Kimia bukan hanya tentang rumus dan angka, 
    tetapi juga tentang memahami bagaimana zat bereaksi 
    dan berubah dalam kehidupan sehari-hari.

    Stoikiometri membantu manusia dalam:
    - Membuat obat
    - Memproduksi makanan
    - Mengolah limbah
    - Menciptakan energi
    - Penelitian laboratorium
    """)

with col6:
    st_lottie(atom_anim, height=250)

# =========================
# ABOUT US
# =========================
st.markdown("## 👨‍🔬 Tentang Kami")

st.markdown("""
<div class="box">

<h4>Kelompok 10</h4>

<ul>
<li>Sarah Nur Ichsani</li>
<li>Anggota Kelompok</li>
</ul>

Website ini dibuat sebagai media pembelajaran kimia interaktif 
untuk membantu memahami konsep stoikiometri dan penyetaraan reaksi kimia secara lebih mudah dan menarik.

</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
---
<center>
⚗️ Dibuat dengan Streamlit | Kelompok 10
</center>
""", unsafe_allow_html=True)
