import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# =========================
# CONFIG (JUDUL TIDAK DIUBAH)
# =========================
st.set_page_config(
    page_title="Kalkulator Persamaan Reaksi dan Stoikiometri",
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
# CSS (ZOOM + FLOAT + FADE)
# =========================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: radial-gradient(circle at top, #eaf3ff, #ffffff);
}

/* 🔥 PAGE TRANSITION ZOOM EFFECT */
.block-container {
    animation: zoomIn 0.5s ease;
}

@keyframes zoomIn {
    0% {
        transform: scale(0.96);
        opacity: 0;
    }
    100% {
        transform: scale(1);
        opacity: 1;
    }
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

/* BUTTON BOUNCE */
.stButton>button {
    background-color: #4da3ff;
    color: white;
    border-radius: 12px;
    box-shadow: 0 6px 0 #2b78d4;
    transition: 0.2s ease;
}

.stButton>button:hover {
    transform: translateY(-2px) scale(1.05);
}

.stButton>button:active {
    transform: translateY(3px);
    box-shadow: 0 2px 0 #2b78d4;
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
        st.markdown("### 🧑‍🔬 Laboratorium")
        if lab:
            st.markdown('<div class="float">', unsafe_allow_html=True)
            st_lottie(lab, height=280)
            st.markdown('</div>', unsafe_allow_html=True)

# =========================
# REAKSI KIMIA
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
            "S + O2 -> SO2"
        ]
    )

    if st.button("Jalankan Reaksi"):

        with st.spinner("Memproses reaksi..."):
            time.sleep(0.8)

        left, right = reaction.split("->")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='card'><h3>🔵 Reaktan</h3></div>", unsafe_allow_html=True)
            st.write(left.strip())

        with col2:
            st.markdown("<div class='card'><h3>🟢 Produk</h3></div>", unsafe_allow_html=True)
            st.write(right.strip())

        st.success("Reaksi selesai!")

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
