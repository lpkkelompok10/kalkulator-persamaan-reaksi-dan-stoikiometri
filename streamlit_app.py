```python
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

intro_anim = load_lottie("https://assets2.lottiefiles.com/packages/lf20_khzniaya.json")

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

    st.markdown("<div class='intro-title'>🧑‍🔬 CHEMICAL ANALYST LAB</div>", unsafe_allow_html=True)
    st.markdown("<div class='intro-sub'>Initializing Chemistry Simulation System...</div>", unsafe_allow_html=True)

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

/* background */
.stApp {
    background: #f4f8ff;
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
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    transition: all 0.25s ease;
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

    # =========================
    # TENTANG APLIKASI
    # =========================
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

    # =========================
    # APA ITU STOIKIOMETRI
    # =========================
    st.markdown("""
    <div class="card">
    <h2>🔬 Apa Itu Stoikiometri?</h2>

    <p>
    Stoikiometri adalah cabang ilmu kimia yang mempelajari hubungan kuantitatif antara zat-zat yang terlibat dalam suatu reaksi kimia.
    Dengan stoikiometri, kita dapat menentukan jumlah pereaksi maupun produk berdasarkan persamaan reaksi yang sudah setara.
    </p>

    <p>
    Dalam pembelajaran kimia, stoikiometri digunakan untuk:
    </p>

    <ul>
        <li>Menghitung jumlah mol zat</li>
        <li>Menentukan massa zat hasil reaksi</li>
        <li>Menganalisis pereaksi pembatas</li>
        <li>Memahami hubungan koefisien reaksi</li>
        <li>Membantu perhitungan laboratorium</li>
    </ul>

    <p>
    Stoikiometri tidak hanya digunakan di sekolah atau laboratorium,
    tetapi juga dimanfaatkan dalam industri farmasi, pengolahan makanan,
    produksi bahan bakar, hingga penelitian ilmiah modern.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =========================
    # CARA MENGGUNAKAN
    # =========================
    st.markdown("""
    <div class="card">
    <h2>📘 Cara Menggunakan Aplikasi</h2>

    <ol>
        <li>Pilih menu melalui sidebar</li>
        <li>Masukkan persamaan reaksi kimia</li>
        <li>Gunakan tanda -> untuk memisahkan reaktan dan produk</li>
        <li>Masukkan massa dan nilai Mr pada menu stoikiometri</li>
        <li>Klik tombol hitung</li>
    </ol>

    <p>
    Contoh reaksi:
    <br>
    <b>H2 + O2 -> H2O</b>
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =========================
    # PENERAPAN KIMIA
    # =========================
    st.markdown("""
    <div class="card">
    <h2>🌍 Penerapan Kimia dalam Kehidupan</h2>

    <p>
    Ilmu kimia memiliki peran penting dalam kehidupan sehari-hari.
    Hampir semua aktivitas manusia berkaitan dengan reaksi kimia.
    </p>

    <ul>
        <li>Produksi obat dan vaksin</li>
        <li>Pembuatan makanan dan minuman</li>
        <li>Pengolahan limbah</li>
        <li>Pembuatan kosmetik</li>
        <li>Produksi energi</li>
        <li>Penelitian laboratorium</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

# =========================
# REAKSI KIMIA
# =========================
elif menu == "⚗️ Reaksi Kimia":

    st.title("⚗️ Persamaan Reaksi Kimia")

    st.info("Contoh input: H2 + O2 -> H2O")

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

    st.markdown("""
    <div class="card">
    Stoikiometri digunakan untuk menghitung hubungan jumlah zat
    dalam suatu reaksi kimia menggunakan konsep mol.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        massa = st.number_input(
            "Massa (gram)",
            min_value=0.0
        )

    with col2:
        Mr = st.number_input(
            "Mr zat",
            min_value=0.0
        )

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
```
