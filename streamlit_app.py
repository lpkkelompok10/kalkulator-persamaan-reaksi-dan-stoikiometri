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

# =========================
# STYLE
# =========================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #eaf3ff, #ffffff);
}

.card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 12px;
}

.reaction {
    font-size: 20px;
    text-align: center;
    padding: 14px;
    background: #f0f7ff;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (WAJIB SESUAI REQUEST KAMU)
# =========================
st.title("⚗️ Kalkulator Persamaan Reaksi Kimia dan Stoikiometri")
st.markdown("### 🔬 Science Simulator Mode (Interaktif)")

# =========================
# ATOM ANIMATION
# =========================
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### ⚛️ Animasi Atom")
    if atom:
        st_lottie(atom, height=280)

with col2:
    st.markdown("### 🧪 Panel Reaksi")

    reaction = st.selectbox(
        "Pilih Reaksi",
        [
            "H2 + O2 → H2O",
            "Na + Cl → NaCl",
            "C + O2 → CO2"
        ]
    )

    run = st.button("▶ Jalankan Simulasi")

# =========================
# SIMULATION AREA
# =========================
st.markdown("---")
st.markdown("## 🔬 Reaction Simulation Chamber")

box = st.empty()

if run:

    if reaction == "H2 + O2 → H2O":
        steps = [
            "🔵 H₂ bergerak mendekat...",
            "🟡 O₂ aktif...",
            "💥 Ikatan lama terputus...",
            "⚛️ Atom bergabung...",
            "🧪 H₂O terbentuk!"
        ]

    elif reaction == "Na + Cl → NaCl":
        steps = [
            "🟠 Na bergerak...",
            "🟢 Cl mendekat...",
            "⚡ Elektron berpindah...",
            "🧲 Ikatan ion terbentuk...",
            "🧂 NaCl terbentuk!"
        ]

    else:
        steps = [
            "⚫ C aktif...",
            "🔴 O₂ mendekat...",
            "🔥 Reaksi pembakaran...",
            "💨 Energi dilepas...",
            "🧪 CO₂ terbentuk!"
        ]

    for s in steps:
        with box.container():
            st.markdown(f"""
            <div class="reaction">
                {s}
            </div>
            """, unsafe_allow_html=True)
        time.sleep(1)

    st.success("Simulasi selesai!")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("🧪 Kelompok 10 - Kalkulator Persamaan Reaksi & Stoikiometri (Science Simulator Mode)")
