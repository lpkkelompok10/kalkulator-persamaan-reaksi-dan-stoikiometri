import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# =========================
# CONFIG (JUDUL FIX)
# =========================
st.set_page_config(
    page_title="Kalkulator Persamaan Reaksi dan Stoikiometri",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# FORCE TRANSITION STATE (INI KUNCI)
# =========================
if "loaded" not in st.session_state:
    st.session_state.loaded = True
    st.rerun()

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
# GLOBAL CSS (INI YANG BIKIN SEMUA TRANSISI)
# =========================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: radial-gradient(circle at top, #eaf3ff, #ffffff);
}

/* 🔥 GLOBAL PAGE ZOOM SETIAP RERUN */
.block-container {
    animation: pageIn 0.45s ease;
}

@keyframes pageIn {
    0% {
        transform: scale(0.97);
        opacity: 0;
    }
    100% {
        transform: scale(1);
        opacity: 1;
    }
}

/* 💥 BUTTON BOUNCE (SEMUA BUTTON) */
.stButton>button {
    background-color: #4da3ff;
    color: white;
    border-radius: 12px;
    box-shadow: 0 6px 0 #2b78d4;
    transition: all 0.15s ease;
}

.stButton>button:hover {
    transform: scale(1.05);
}

.stButton>button:active {
    transform: scale(0.92);
    box-shadow: 0 2px 0 #2b78d4;
}

/* FLOAT ANIMATION */
.float {
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-12px); }
    100% { transform: translateY(0px); }
}

/* CARD */
.card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 12px;
}

</style>
""", unsafe_allow_html=True)

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

    st.title("⚗️ Kalkulator Persamaan Reaksi dan Stoikiometri")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ⚛️ Atom")
        if atom:
            st.markdown('<div class="float">', unsafe_allow_html=True)
            st_lottie(atom, height=280)
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("### 🧑‍🔬 Lab")
        if lab:
            st.markdown('<div class="float">', unsafe_allow_html=True)
            st_lottie(lab, height=280)
            st.markdown('</div>', unsafe_allow_html=True)

# =========================
# REAKSI
# =========================
elif menu == "⚗️ Reaksi Kimia":

    st.title("⚗️ Persamaan Reaksi Kimia")

    reaction = st.selectbox(
        "Pilih Reaksi",
        [
            "H2 + O2 -> H2O",
            "Na + Cl -> NaCl",
            "C + O2 -> CO2",
            "Fe + O2 -> Fe2O3",
            "CH4 + O2 -> CO2 + H2O",
            "CaCO3 -> CaO + CO2",
            "Mg + O2 -> MgO",
            "Al + O2 -> Al2O3",
            "N2 + H2 -> NH3",
            "S + O2 -> SO2",
            "H2 + Cl2 -> HCl"
        ]
    )

    if st.button("Jalankan Reaksi"):

        with st.spinner("Memproses..."):
            time.sleep(0.6)

        left, right = reaction.split("->")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='card'><h3>🔵 Reaktan</h3></div>", unsafe_allow_html=True)
            st.write(left.strip())

        with col2:
            st.markdown("<div class='card'><h3>🟢 Produk</h3></div>", unsafe_allow_html=True)
            st.write(right.strip())

        st.success("Selesai!")

# =========================
# STOIKIOMETRI
# =========================
elif menu == "🧪 Stoikiometri":

    st.title("🧪 Stoikiometri")

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
    Hubungan kuantitatif reaksi kimia
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
