
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
        "<div class='intro-title'>🧑🏻‍🔬👩🏻‍🔬CHEMICAL ANALYST LAB</div>",
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
    background: linear-gradient(135deg, #ffffff, #f8fbff);
    overflow: hidden;
}

/* FLOATING LAB IMAGE */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background-image:
    url("https://cdn-icons-png.flaticon.com/512/2784/2784445.png"),
    url("https://cdn-icons-png.flaticon.com/512/2784/2784469.png"),
    url("https://cdn-icons-png.flaticon.com/512/2784/2784459.png"),
    url("https://cdn-icons-png.flaticon.com/512/2784/2784487.png"),
    url("https://cdn-icons-png.flaticon.com/512/2784/2784474.png"),
    url("https://cdn-icons-png.flaticon.com/512/2784/2784491.png"),
    url("https://cdn-icons-png.flaticon.com/512/2784/2784509.png"),
    url("https://cdn-icons-png.flaticon.com/512/2784/2784516.png");

    background-repeat: no-repeat;

    background-size:
    100px,
    85px,
    95px,
    80px,
    90px,
    70px,
    75px,
    88px;

    background-position:
    5% 15%,
    85% 10%,
    18% 55%,
    75% 65%,
    50% 20%,
    35% 82%,
    92% 45%,
    60% 88%;

    opacity: 0.10;

    animation: floating 12s ease-in-out infinite;

    pointer-events: none;
    z-index: 0;
}

/* SECOND FLOATING LAYER */
.stApp::after {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background-image:
    url("https://cdn-icons-png.flaticon.com/512/2784/2784487.png"),
    url("https://cdn-icons-png.flaticon.com/512/2784/2784445.png"),
    url("https://cdn-icons-png.flaticon.com/512/2784/2784516.png"),
    url("https://cdn-icons-png.flaticon.com/512/2784/2784474.png");

    background-repeat: no-repeat;

    background-size:
    70px,
    75px,
    65px,
    72px;

    background-position:
    10% 90%,
    80% 85%,
    45% 50%,
    60% 8%;

    opacity: 0.08;

    animation: floating2 16s ease-in-out infinite;

    pointer-events: none;
    z-index: 0;
}

/* FLOAT ANIMATION */
@keyframes floating {

    0% {
        transform: translateY(0px) rotate(0deg);
    }

    50% {
        transform: translateY(-25px) rotate(3deg);
    }

    100% {
        transform: translateY(0px) rotate(0deg);
    }
}

@keyframes floating2 {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(20px);
    }

    100% {
        transform: translateY(0px);
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
    background: rgba(255,255,255,0.88);
    backdrop-filter: blur(10px);
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 18px;
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
    Banyak siswa kesulitan dalam memahami perubahan zat dalam reaksi kimia serta perhitungan mol, sehingga aplikasi ini hadir sebagai solusi pembelajaran visual dan praktis.
    </p>

    <p>
    Dengan aplikasi ini, pengguna dapat memasukkan persamaan reaksi dan langsung memisahkan reaktan serta produk.
    Selain itu, fitur stoikiometri membantu menghitung jumlah mol dari massa dan Mr dengan otomatis.
    </p>

    <p>
    <b>Manfaat utama:</b><br>
    - Mempermudah belajar reaksi kimia<br>
    - Membantu perhitungan stoikiometri<br>
    - Mengurangi kesalahan hitung manual<br>
    - Media belajar interaktif<br>
    - Lebih menarik dibanding metode konvensional
    </p>

    </div>
    """, unsafe_allow_html=True)
