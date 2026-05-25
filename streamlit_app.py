
import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Persamaan Reaksi Kimia & Stoikiometri",
    page_icon="🧑🏻‍🔬👩🏻‍🔬",
    layout="wide"
)

# =========================
# LOTTIE FUNCTION
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
# SPLASH SCREEN
# =========================
splash = st.empty()

intro_anim = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_khzniaya.json"
)

with splash.container():

    st.markdown("""
    <style>
    .intro-title{
        text-align:center;
        font-size:42px;
        font-weight:bold;
        color:#1f4f8b;
        margin-top:40px;
        animation: fadeIn 1s ease;
    }

    .intro-sub{
        text-align:center;
        color:#4d6fa3;
        font-size:18px;
    }

    @keyframes fadeIn {
        from {opacity:0;}
        to {opacity:1;}
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='intro-title'>🧑‍🔬 CHEMICAL ANALYST LAB</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='intro-sub'>Initializing Chemistry Simulation System...</div>",
        unsafe_allow_html=True
    )

    if intro_anim:
        st_lottie(intro_anim, height=320)

    # =========================
    # LOADING BAR
    # =========================
    progress = st.progress(0)
    status = st.empty()

    for i in range(100):

        time.sleep(0.02)

        progress.progress(i + 1)

        if i < 30:
            status.write("⚗️ Loading atoms...")
        elif i < 60:
            status.write("🧪 Mixing compounds...")
        elif i < 90:
            status.write("🔬 Calibrating reactions...")
        else:
            status.write("✅ System ready!")

    time.sleep(0.5)

splash.empty()

# =========================
# STYLE
# =========================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #dfefff, #f8fbff);
    overflow: hidden;
}

/* FLOATING LAB ICONS */
.stApp::before {
    content: "⚗️ 🧪 ⚱️ ⚛️ 🔬 🧫 ⚗️ 🧪";
    position: fixed;
    top: 5%;
    left: 2%;
    font-size: 70px;
    color: rgba(255,255,255,0.5);
    z-index: 0;
    animation: float1 18s linear infinite;
    pointer-events: none;
}

.stApp::after {
    content: "🧪 ⚗️ 🔬 ⚱️ 🧫 ⚛️";
    position: fixed;
    bottom: 10%;
    right: 2%;
    font-size: 60px;
    color: rgba(255,255,255,0.45);
    z-index: 0;
    animation: float2 22s linear infinite;
    pointer-events: none;
}

/* FLOAT ANIMATION */
@keyframes float1 {
    0% {
        transform: translateY(0px) rotate(0deg);
    }

    50% {
        transform: translateY(-25px) rotate(4deg);
    }

    100% {
        transform: translateY(0px) rotate(0deg);
    }
}

@keyframes float2 {
    0% {
        transform: translateY(0px) rotate(0deg);
    }

    50% {
        transform: translateY(30px) rotate(-4deg);
    }

    100% {
        transform: translateY(0px) rotate(0deg);
    }
}

/* sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #e6f0ff, #f9fbff);
}

/* sidebar items */
section[data-testid="stSidebar"] div[role="radiogroup"] > label {
    background: white;
    padding: 10px;
    border-radius: 12px;
    margin-bottom: 8px;
    transition: 0.25s ease;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

section[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
    transform: translateX(6px);
    background: #dbeaff;
    box-shadow: 0px 10px 22px rgba(0,0,0,0.12);
}

/* card */
.card {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(10px);
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    transition: all 0.25s ease;
    position: relative;
    z-index: 2;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 18px 35px rgba(0,0,0,0.15);
}

/* button */
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

/* title */
h1, h2, h3 {
    color: #1f4f8b;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR MENU
# =========================
menu = st.sidebar.radio(
    "📌 Menu",
    ["🏠 Home", "⚗️ Reaksi Kimia", "🧪 Stoikiometri", "👥 Kelompok 10"]
)

# =========================
# HOME
# =========================
if menu == "🏠 Home":

    st.markdown("""
    <div style="text-align:center; padding:20px">
        <h1>⚗️ Kalkulator Persamaan Reaksi Kimia dan Stoikiometri</h1>
        <p style="font-size:18px; color:#4d6fa3">
        Chemistry Simulation Lab
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🔬 Reaksi Kimia</h3>
        Analisis persamaan reaksi
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🧪 Stoikiometri</h3>
        Hitung mol dengan cepat
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>👥 Kelompok 10</h3>
        Informasi anggota kelompok
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="card">
    <h2>📘 Tentang & Kegunaan Kalkulator</h2>

    <p>
    Aplikasi ini dibuat untuk membantu memahami konsep dasar kimia seperti reaksi kimia dan stoikiometri secara lebih mudah, cepat, dan interaktif.
    </p>

    <p>
    Dengan aplikasi ini, pengguna dapat memasukkan persamaan reaksi dan langsung memisahkan reaktan serta produk.
    </p>

    </div>
    """, unsafe_allow_html=True)

# =========================
# REAKSI KIMIA
# =========================
elif menu == "⚗️ Reaksi Kimia":

    st.title("⚗️ Persamaan Reaksi Kimia")

    reaction = st.text_input(
        "Masukkan reaksi (contoh: H2 + O2 -> H2O)"
    )

    if st.button("Proses Reaksi"):

        if reaction:

            with st.spinner("⚗️ Memproses reaksi..."):
                time.sleep(1)

            try:
                left, right = reaction.split("->")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("""
                    <div class="card">
                    <h3>🔵 Reaktan</h3>
                    </div>
                    """, unsafe_allow_html=True)

                    st.write(left.strip())

                with col2:
                    st.markdown("""
                    <div class="card">
                    <h3>🟢 Produk</h3>
                    </div>
                    """, unsafe_allow_html=True)

                    st.write(right.strip())

                st.success("Reaksi berhasil diproses!")

            except:
                st.error("Format salah! gunakan tanda ->")

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
            <h3>📊 Hasil Perhitungan</h3>
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
        "Faturrahman Chandika (2560630)",
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

