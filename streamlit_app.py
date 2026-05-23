import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Persamaan Reaksi & Stoikiometri",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# LOTTIE
# =========================
def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

atom = load_lottie("https://assets9.lottiefiles.com/packages/lf20_yd8qxj.json")
lab = load_lottie("https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json")

# =========================
# STYLE CINEMATIC CLEAN
# =========================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #eaf3ff, #ffffff);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1f4f8b;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    color: #4d6fa3;
    font-size: 18px;
    margin-bottom: 20px;
}

.card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 12px;
}

.stButton>button {
    background-color: #4da3ff;
    color: white;
    border-radius: 10px;
}

.stButton>button:hover {
    background-color: #1f7ae0;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER CINEMATIC
# =========================
st.markdown("<div class='title'>⚗️ CHEMISTRY SIMULATION LAB</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Kalkulator Persamaan Reaksi Kimia & Stoikiometri - Kelompok 10</div>", unsafe_allow_html=True)

# =========================
# INTRO PENJELASAN (REQUEST KAMU)
# =========================
with st.expander("📘 Apa kegunaan aplikasi ini? (Klik untuk lihat)"):
    st.markdown("""
    Aplikasi ini digunakan untuk:
    
    - Menghitung dan memahami **persamaan reaksi kimia**
    - Menghitung **stoikiometri (mol, massa, Mr)**
    - Membantu belajar kimia secara **visual dan interaktif**
    
    💡 Cocok untuk latihan soal dan pembelajaran di kelas.
    """)

st.markdown("---")

# =========================
# ANIMASI
# =========================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ⚛️ Atom Simulation")
    if atom:
        st_lottie(atom, height=280)

with col2:
    st.markdown("### 🧑‍🔬 Lab Simulation")
    if lab:
        st_lottie(lab, height=280)

st.markdown("---")

# =========================
# MENU
# =========================
menu = st.sidebar.radio(
    "📌 Menu",
    ["🏠 Home", "⚗️ Reaksi Kimia", "🧪 Stoikiometri", "📘 Materi", "👥 Kelompok 10"]
)

# =========================
# HOME
# =========================
if menu == "🏠 Home":

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/98/Periodic_table_large.png",
        use_container_width=True
    )

    st.markdown("### 🔬 Fitur Aplikasi")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h3>🔬 Reaksi Kimia</h3></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h3>🧪 Stoikiometri</h3></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><h3>📘 Materi</h3></div>", unsafe_allow_html=True)

# =========================
# REAKSI KIMIA (EXPANDED + LEBIH BANYAK)
# =========================
elif menu == "⚗️ Reaksi Kimia":

    st.title("⚗️ Simulasi Persamaan Reaksi Kimia")

    reaction = st.selectbox(
        "Pilih Reaksi",
        [
            "H2 + O2 -> H2O",
            "Na + Cl -> NaCl",
            "C + O2 -> CO2",
            "Fe + O2 -> Fe2O3",
            "CH4 + O2 -> CO2 + H2O",
            "CaCO3 -> CaO + CO2"
        ]
    )

    if st.button("Jalankan Reaksi"):

        with st.spinner("Memproses reaksi..."):
            time.sleep(1)

        left, right = reaction.split("->")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='card'><h3>🔵 Reaktan</h3></div>", unsafe_allow_html=True)
            st.write(left.strip())

        with col2:
            st.markdown("<div class='card'><h3>🟢 Produk</h3></div>", unsafe_allow_html=True)
            st.write(right.strip())

        st.success("Reaksi selesai diproses!")

# =========================
# STOIKIOMETRI
# =========================
elif menu == "🧪 Stoikiometri":

    st.title("🧪 Kalkulator Stoikiometri")

    col1, col2 = st.columns(2)

    with col1:
        massa = st.number_input("Massa (gram)", min_value=0.0)

    with col2:
        Mr = st.number_input("Mr zat", min_value=0.0)

    if st.button("Hitung"):

        if Mr > 0:
            mol = massa / Mr
            st.markdown("<div class='card'><h3>📊 Hasil</h3></div>", unsafe_allow_html=True)
            st.success(f"{mol:.4f} mol")
        else:
            st.warning("Mr tidak boleh 0")

# =========================
# MATERI
# =========================
elif menu == "📘 Materi":

    st.title("📘 Materi Kimia")

    st.markdown("""
    <div class='card'>
    <h3>⚗️ Reaksi Kimia</h3>
    Perubahan zat menjadi zat baru
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h3>🧪 Stoikiometri</h3>
    Hubungan kuantitatif dalam reaksi kimia
    </div>
    """, unsafe_allow_html=True)

# =========================
# KELOMPOK
# =========================
elif menu == "👥 Kelompok 10":

    st.title("👥 Kelompok 10")

    members = [
        "Faturrahman Chandika (2560774)",
        "Naisyla Nazwa S. (2560705)",
        "Nassya Alifha Rasyikha (2560710)",
        "Reva Aulia (2560749)",
        "Sarah Nur Ichsani (2560774)"
    ]

    for m in members:
        st.markdown(f"<div class='card'>{m}</div>", unsafe_allow_html=True)
