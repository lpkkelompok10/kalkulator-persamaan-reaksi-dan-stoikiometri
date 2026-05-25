
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
# 🎬 SPLASH SCREEN
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
        color:#8b5e34;
        margin-top:40px;
        animation: fadeIn 1s ease;
    }

    .intro-sub{
        text-align:center;
        color:#b8863b;
        font-size:18px;
    }

    @keyframes fadeIn {
        from {opacity:0;}
        to {opacity:1;}
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='intro-title'>🧑🏻‍🔬👩🏻‍🔬 CHEMICAL ANALYST LAB</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='intro-sub'>Initializing Chemistry Simulation System...</div>",
        unsafe_allow_html=True
    )

    if intro_anim:
        st_lottie(intro_anim, height=320)

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
    background: linear-gradient(135deg, #fffaf0, #fdf6e3);
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

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fff5dc, #fffaf0);
}

/* SIDEBAR ITEMS */
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
    background: #ffeec2;
    box-shadow: 0px 10px 22px rgba(0,0,0,0.12);
}

/* CARD */
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

/* BUTTON */
.stButton>button {
    background-color: #d6a75f;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
    transition: all 0.2s ease;
}

.stButton>button:hover {
    background-color: #b8863b;
    transform: scale(1.05);
}

/* TITLE */
h1, h2, h3 {
    color: #8b5e34;
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
        <p style="font-size:18px; color:#b8863b">
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
    Aplikasi Kalkulator Persamaan Reaksi Kimia dan Stoikiometri ini dibuat sebagai media pembelajaran interaktif untuk membantu memahami konsep dasar kimia secara lebih mudah, modern, dan menarik.
    Dalam pembelajaran kimia, banyak siswa mengalami kesulitan ketika mempelajari persamaan reaksi, hubungan antar zat, serta perhitungan mol dan massa zat.
    Karena itu, aplikasi ini hadir sebagai solusi digital yang membantu proses belajar menjadi lebih cepat dan praktis.
    </p>

    <p>
    Melalui aplikasi ini, pengguna dapat memisahkan reaktan dan produk dari suatu persamaan reaksi kimia serta melakukan perhitungan stoikiometri secara otomatis menggunakan rumus dasar kimia.
    Aplikasi ini juga dirancang dengan tampilan visual laboratorium agar pembelajaran terasa lebih interaktif dan tidak membosankan.
    </p>

    <p>
    <b>Manfaat aplikasi:</b>
    </p>

    <ul>
    <li>Mempermudah memahami konsep reaksi kimia</li>
    <li>Membantu menghitung mol secara otomatis</li>
    <li>Mengurangi kesalahan perhitungan manual</li>
    <li>Menjadi media belajar kimia interaktif</li>
    <li>Membantu praktikum dan pembelajaran laboratorium</li>
    <li>Meningkatkan minat belajar siswa terhadap kimia</li>
    <li>Membantu memahami hubungan massa, mol, dan Mr</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h2>🧪 Apa Itu Stoikiometri?</h2>

    <p>
    Stoikiometri adalah cabang ilmu kimia yang mempelajari hubungan kuantitatif antara pereaksi dan hasil reaksi dalam suatu persamaan kimia.
    Stoikiometri digunakan untuk menghitung jumlah zat yang diperlukan maupun yang dihasilkan dalam suatu reaksi berdasarkan koefisien reaksi yang telah setara.
    </p>

    <p>
    Konsep stoikiometri sangat penting dalam kimia karena digunakan dalam berbagai bidang seperti industri, farmasi, laboratorium, pengolahan limbah, hingga penelitian ilmiah.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h2>📐 Rumus Dasar Stoikiometri</h2>
    <h3>1️⃣ Menghitung Mol</h3>
    </div>
    """, unsafe_allow_html=True)

    st.latex(r'''
    n = \frac{m}{Mr}
    ''')

    st.markdown("""
    <div class="card">
    <ul>
    <li><b>n</b> = jumlah mol</li>
    <li><b>m</b> = massa zat (gram)</li>
    <li><b>Mr</b> = massa molekul relatif</li>
    </ul>

    <h3>2️⃣ Hubungan Jumlah Partikel</h3>
    </div>
    """, unsafe_allow_html=True)

    st.latex(r'''
    n = \frac{jumlah\ partikel}{6.02 \times 10^{23}}
    ''')

    st.markdown("""
    <div class="card">
    <h3>3️⃣ Volume Gas</h3>
    </div>
    """, unsafe_allow_html=True)

    st.latex(r'''
    n = \frac{V}{22.4}
    ''')

    st.markdown("""
    <div class="card">
    <p>
    Rumus volume gas digunakan pada kondisi STP (Suhu dan Tekanan Standar),
    dimana 1 mol gas memiliki volume 22,4 liter.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h2>📖 Cara Menggunakan Aplikasi</h2>

    <ol>
    <li>Pilih menu pada sidebar sesuai kebutuhan</li>
    <li>Masukkan persamaan reaksi kimia</li>
    <li>Gunakan tanda -> untuk memisahkan reaktan dan produk</li>
    <li>Masukkan massa zat dan nilai Mr</li>
    <li>Klik tombol hitung</li>
    <li>Hasil perhitungan mol akan muncul otomatis</li>
    </ol>

    <p>
    <b>Contoh reaksi:</b><br>
    H₂ + O₂ -> H₂O
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h2>🌍 Penerapan Kimia dalam Kehidupan</h2>

    <ul>
    <li>Produksi obat dan vaksin</li>
    <li>Pembuatan makanan dan minuman</li>
    <li>Pengolahan limbah industri</li>
    <li>Pembuatan pupuk</li>
    <li>Pembuatan kosmetik</li>
    <li>Produksi bahan bakar</li>
    <li>Penelitian laboratorium</li>
    <li>Analisis kualitas produk</li>
    <li>Industri farmasi dan kesehatan</li>
    <li>Teknologi energi dan lingkungan</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

# =========================
# REAKSI KIMIA
# =========================
elif menu == "⚗️ Reaksi Kimia":

    st.title("⚗️ Persamaan Reaksi Kimia")

    reaction = st.text_input("Masukkan reaksi (contoh: H2 + O2 -> H2O)")

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

            st.latex(r'''
            n = \frac{m}{Mr}
            ''')

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
        <h3>🧑‍🔬 {m}</h3>
        </div>
        """, unsafe_allow_html=True)

