import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Kimia - Movie Mode",
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
# 🎬 CINEMATIC INTRO (MOVIE OPENING)
# =========================
intro = st.empty()

with intro.container():
    st.markdown("""
    <style>
    .intro {
        text-align:center;
        padding: 80px 20px;
        animation: fadeIn 2s ease;
    }

    @keyframes fadeIn {
        from {opacity:0;}
        to {opacity:1;}
    }
    </style>

    <div class="intro">
        <h1>⚗️ CHEMISTRY CINEMATIC LAB</h1>
        <h3>Kalkulator Persamaan Reaksi & Stoikiometri</h3>
        <p>Kelompok 10</p>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2)

intro.empty()

# =========================
# STYLE (MOVIE MODE)
# =========================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: radial-gradient(circle at top, #eaf3ff, #ffffff);
}

/* 🎈 FLOATING EFFECT */
.float {
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-12px); }
    100% { transform: translateY(0px); }
}

/* 💥 BUTTON BOUNCE (BANTAL EFFECT) */
.stButton>button {
    background-color: #4da3ff;
    color: white;
    border-radius: 14px;
    padding: 10px 18px;
    transition: 0.2s ease;
    box-shadow: 0 6px 0 #2b78d4;
}

.stButton>button:hover {
    transform: translateY(-2px) scale(1.05);
    box-shadow: 0 10px 0 #2b78d4;
}

.stButton>button:active {
    transform: translateY(4px);
    box-shadow: 0 2px 0 #2b78d4;
}

/* 🎬 FADE TRANSITION CONTENT */
.block-container {
    animation: fadeUp 0.6s ease;
}

@keyframes fadeUp {
    from {opacity:0; transform: translateY(10px);}
    to {opacity:1; transform: translateY(0);}
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

    st.title("⚗️ Chemistry Movie Mode Lab")

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
# REAKSI KIMIA
# =========================
elif menu == "⚗️ Reaksi Kimia":

    st.title("⚗️ Simulasi Reaksi Kimia")

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
            "N2 + H2 -> NH3"
        ]
    )

    if st.button("▶ Jalankan"):

        with st.spinner("Running reaction..."):
            time.sleep(1)

        left, right = reaction.split("->")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='card'><h3>🔵 Reaktan</h3></div>", unsafe_allow_html=True)
            st.write(left.strip())

        with col2:
            st.markdown("<div class='card'><h3>🟢 Produk</h3></div>", unsafe_allow_html=True)
            st.write(right.strip())

        st.success("Reaction completed!")

# =========================
# STOIKIOMETRI
# =========================
elif menu == "🧪 Stoikiometri":

    st.title("🧪 Stoikiometri Calculator")

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

    st.markdown("<div class='card'><h3>⚗️ Reaksi Kimia</h3><p>Perubahan zat menjadi zat baru</p></div>", unsafe_allow_html=True)

    st.markdown("<div class='card'><h3>🧪 Stoikiometri</h3><p>Hubungan kuantitatif reaksi</p></div>", unsafe_allow_html=True)

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
