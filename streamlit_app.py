import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Persamaan Reaksi Kimia & Stoikiometri",
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
    return None

# =========================
# STYLE (SAFE + SMOKE + GLOW EFFECT)
# =========================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: #f4f8ff;
    position: relative;
    overflow: hidden;
}

/* 🌫️ SMOKE SAFE */
.smoke {
    position: fixed;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(77,163,255,0.25), transparent 60%);
    filter: blur(80px);
    top: -100px;
    left: -150px;
    animation: floatSmoke 14s infinite ease-in-out;
    z-index: 0;
    pointer-events: none;
}

.smoke2 {
    position: fixed;
    width: 700px;
    height: 700px;
    background: radial-gradient(circle, rgba(31,79,139,0.18), transparent 60%);
    filter: blur(90px);
    bottom: -200px;
    right: -200px;
    animation: floatSmoke 18s infinite ease-in-out;
    z-index: 0;
    pointer-events: none;
}

@keyframes floatSmoke {
    0% {transform: translate(0,0) scale(1); opacity:0.4;}
    50% {transform: translate(80px,-60px) scale(1.2); opacity:0.7;}
    100% {transform: translate(0,0) scale(1); opacity:0.4;}
}

/* REACTION GLOW BOX */
.reaction-box {
    background: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 0 0 rgba(77,163,255,0);
    transition: all 0.4s ease;
}

.reaction-box:hover {
    transform: scale(1.02);
    box-shadow: 0 0 30px rgba(77,163,255,0.4);
}

/* BUTTON */
.stButton>button {
    background-color: #4da3ff;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
    transition: all 0.2s ease;
}

.stButton>button:hover {
    background-color: #1f7ae0;
    transform: scale(1.05);
}

/* CARD */
.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    transition: 0.25s;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 18px 35px rgba(0,0,0,0.15);
}

h1,h2,h3 {color:#1f4f8b;}

.block-container {
    position: relative;
    z-index: 2;
}

</style>
""", unsafe_allow_html=True)

# smoke layer
st.markdown("""
<div class="smoke"></div>
<div class="smoke2"></div>
""", unsafe_allow_html=True)

# =========================
# MENU
# =========================
menu = st.sidebar.radio(
    "📌 Menu",
    ["🏠 Home", "⚗️ Reaksi Kimia", "🧪 Stoikiometri", "👥 Kelompok 10"]
)

# =========================
# HOME (CHEMICAL ANALYST INTRO)
# =========================
if menu == "🏠 Home":

    intro = load_lottie("https://assets2.lottiefiles.com/packages/lf20_khzniaya.json")

    st.markdown("""
    <div style="text-align:center; padding:20px">
        <h1>🧑‍🔬 Chemical Analyst Lab</h1>
        <p style="color:#4d6fa3;">Initializing Chemistry System...</p>
    </div>
    """, unsafe_allow_html=True)

    if intro:
        st_lottie(intro, height=300)

    progress = st.progress(0)
    status = st.empty()

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

        if i < 30:
            status.write("⚗️ Detecting molecules...")
        elif i < 60:
            status.write("🧪 Mixing compounds...")
        else:
            status.write("🔬 System ready!")

# =========================
# REAKSI KIMIA
# =========================
elif menu == "⚗️ Reaksi Kimia":

    st.title("⚗️ Persamaan Reaksi Kimia")

    reaction = st.text_input("Masukkan reaksi (contoh: H2 + O2 -> H2O)")

    if st.button("Proses Reaksi"):

        if reaction:

            with st.spinner("⚗️ Memproses..."):
                time.sleep(1)

            try:
                left, right = reaction.split("->")

                st.markdown('<div class="reaction-box">', unsafe_allow_html=True)

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("""
                    <div class="card"><h3>🔵 Reaktan</h3></div>
                    """, unsafe_allow_html=True)
                    st.write(left.strip())

                with col2:
                    st.markdown("""
                    <div class="card"><h3>🟢 Produk</h3></div>
                    """, unsafe_allow_html=True)
                    st.write(right.strip())

                st.markdown("</div>", unsafe_allow_html=True)

                st.success("💥 Reaksi berhasil diproses!")

            except:
                st.error("Format salah! gunakan ->")

        else:
            st.warning("Isi dulu reaksi!")

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

    if st.button("Hitung Mol"):

        if Mr > 0:

            with st.spinner("🧪 Menghitung..."):
                time.sleep(1)

            mol = massa / Mr

            st.markdown("""
            <div class="card">
            <h3>📊 Hasil</h3>
            </div>
            """, unsafe_allow_html=True)

            st.success(f"{mol:.4f} mol")

        else:
            st.warning("Mr tidak boleh 0")

# =========================
# KELOMPOK 10
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
        st.markdown(f"""
        <div class="card">
        {m}
        </div>
        """, unsafe_allow_html=True)
