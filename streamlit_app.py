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
# STYLE + PARTICLE BACKGROUND
# =========================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #eaf3ff, #ffffff);
    overflow-x: hidden;
}

/* FLOAT ANIMATION */
.float-box {
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0px); }
}

/* PARTICLE BACKGROUND */
.particle {
    position: fixed;
    width: 6px;
    height: 6px;
    background: rgba(100,150,255,0.4);
    border-radius: 50%;
    animation: move 10s linear infinite;
}

@keyframes move {
    0% { transform: translateY(100vh); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(-10vh); opacity: 0; }
}

h1, h2, h3 {
    color: #1f4f8b;
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
# PARTICLE GENERATOR (VISUAL FAKE BACKGROUND)
# =========================
st.markdown("""
<div class="particle" style="left:10%; animation-delay:0s;"></div>
<div class="particle" style="left:25%; animation-delay:2s;"></div>
<div class="particle" style="left:40%; animation-delay:4s;"></div>
<div class="particle" style="left:60%; animation-delay:1s;"></div>
<div class="particle" style="left:75%; animation-delay:3s;"></div>
<div class="particle" style="left:90%; animation-delay:5s;"></div>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("⚗️ Kalkulator Persamaan Reaksi & Stoikiometri")
st.markdown("### 🌌 Chemistry Cinematic Lab Mode")

# =========================
# ANIMASI FLOATING
# =========================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ⚛️ Atom Simulation")
    if atom:
        st.markdown('<div class="float-box">', unsafe_allow_html=True)
        st_lottie(atom, height=280)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 🧑‍🔬 Lab Simulation")
    if lab:
        st.markdown('<div class="float-box">', unsafe_allow_html=True)
        st_lottie(lab, height=280)
        st.markdown('</div>', unsafe_allow_html=True)

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
            "Al + O2 -> Al2O3"
        ]
    )

    if st.button("Jalankan"):

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

        st.success("Reaksi selesai!")

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
