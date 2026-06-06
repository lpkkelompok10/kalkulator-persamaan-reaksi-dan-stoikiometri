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
    layout="centered"
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
# ANIMATIONS
# =========================
intro_anim = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_khzniaya.json"
)

home_anim = load_lottie(
    "https://assets9.lottiefiles.com/packages/lf20_qp1q7mct.json"
)

reaction_anim = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json"
)

stoik_anim = load_lottie(
    "https://assets4.lottiefiles.com/packages/lf20_l13szxy9.json"
)

team_anim = load_lottie(
    "https://assets1.lottiefiles.com/packages/lf20_tutvdkg0.json"
)

# =========================
# SPLASH SCREEN
# =========================
splash = st.empty()

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

    if home_anim:
        st_lottie(home_anim, height=280)

    st.markdown("""
    <div style="text-align:center; padding:20px">
        <h1>⚗️ Kalkulator Persamaan Reaksi Kimia dan Stoikiometri</h1>
        <p style="font-size:18px; color:#b8863b">
        Chemistry Simulation Lab
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="card">
    <h2>📘 Tentang Aplikasi</h2>

    <p>
    Kalkulator Persamaan Reaksi Kimia dan Stoikiometri merupakan aplikasi pembelajaran berbasis digital
    yang dirancang untuk membantu memahami konsep-konsep dasar kimia dengan lebih mudah, cepat,
    dan interaktif.
    </p>

    <p>
    Dalam pembelajaran kimia, banyak siswa mengalami kesulitan ketika mempelajari reaksi kimia,
    persamaan reaksi, stoikiometri, mol, massa molekul relatif (Mr), serta hubungan antar zat
    dalam suatu reaksi.
    </p>

    <p>
    Aplikasi ini memiliki tampilan visual bertema laboratorium kimia sehingga memberikan nuansa
    seperti berada di dalam laboratorium sungguhan.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h2>🧪 Kegunaan Aplikasi</h2>

    <ul>
    <li>Membantu memahami konsep reaksi kimia</li>
    <li>Membantu menghitung jumlah mol zat</li>
    <li>Membantu memisahkan reaktan dan produk</li>
    <li>Mengurangi kesalahan perhitungan manual</li>
    <li>Mempermudah pembelajaran stoikiometri</li>
    <li>Media belajar interaktif berbasis teknologi</li>
    <li>Membantu praktikum laboratorium</li>
    <li>Membantu memahami hubungan massa dan mol</li>
    <li>Mempermudah analisis persamaan reaksi</li>
    <li>Meningkatkan minat belajar kimia</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h2>⚗️ Pengertian Stoikiometri</h2>

    <p>
    Stoikiometri adalah cabang ilmu kimia yang mempelajari hubungan kuantitatif antara pereaksi
    dan hasil reaksi dalam suatu persamaan kimia.
    </p>

    <p>
    Konsep stoikiometri sangat penting dalam dunia industri, laboratorium, farmasi,
    kedokteran, pengolahan limbah, penelitian ilmiah, dan teknologi pangan.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h2>📐 Rumus Dasar Stoikiometri</h2>
    </div>
    """, unsafe_allow_html=True)

    st.latex(r'''
    n = \frac{m}{Mr}
    ''')

    st.latex(r'''
    m = n \times Mr
    ''')

    st.latex(r'''
    n = \frac{jumlah\ partikel}{6.02 \times 10^{23}}
    ''')

    st.latex(r'''
    n = \frac{V}{22.4}
    ''')

    st.latex(r'''
    2H_2 + O_2 \rightarrow 2H_2O
    ''')

    st.markdown("""
    <div class="card">
    <h2>📖 Cara Menggunakan Aplikasi</h2>

    <ol>
    <li>Pilih menu pada sidebar</li>
    <li>Masukkan persamaan reaksi kimia</li>
    <li>Gunakan tanda -> untuk memisahkan reaktan dan produk</li>
    <li>Masukkan massa dan Mr</li>
    <li>Klik tombol hitung</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)
# =========================
# REAKSI KIMIA
# =========================
elif menu == "⚗️ Reaksi Kimia":

    if reaction_anim:
        st_lottie(reaction_anim, height=250)

    st.title("⚗️ Kalkulator Reaksi Kimia")

    st.markdown("""
    <div class="card">
    <h2>🧪 Fitur Reaksi Kimia</h2>
    <p>
    Pilih fitur yang ingin digunakan untuk mempelajari
    dan menganalisis reaksi kimia.
    </p>
    </div>
    """, unsafe_allow_html=True)

    fitur_reaksi = st.selectbox(
        "Pilih Fitur",
        [
            "Analisis Persamaan",
            "Jenis Reaksi",
            "Prediksi Produk Reaksi",
            "Daftar Reaksi Umum"
        ]
    )

    # ==================================
    # ANALISIS PERSAMAAN
    # ==================================
    if fitur_reaksi == "Analisis Persamaan Reaksi":

        reaksi = st.text_input(
            "Masukkan Persamaan Reaksi",
            placeholder="Contoh: 2H2 + O2 -> 2H2O"
        )

        if st.button("Analisis Reaksi"):

            if not reaksi:

                st.warning(
                    "Masukkan persamaan reaksi terlebih dahulu."
                )

            elif "->" not in reaksi:

                st.error(
                    "Gunakan tanda -> pada persamaan reaksi."
                )

            else:

                reaktan, produk = reaksi.split("->")

                daftar_reaktan = [
                    x.strip()
                    for x in reaktan.split("+")
                ]

                daftar_produk = [
                    x.strip()
                    for x in produk.split("+")
                ]

                st.markdown("""
                <div class="card">
                <h3>📊 Hasil Analisis</h3>
                </div>
                """, unsafe_allow_html=True)

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("🧪 Reaktan")

                    for r in daftar_reaktan:
                        st.write("•", r)

                with col2:

                    st.subheader("⚗️ Produk")

                    for p in daftar_produk:
                        st.write("•", p)

                st.success(
                    f"Jumlah reaktan = {len(daftar_reaktan)}"
                )

                st.success(
                    f"Jumlah produk = {len(daftar_produk)}"
                )
st.success("✅ Persamaan reaksi berhasil dianalisis")

st.info(
    f"Total zat dalam reaksi = "
    f"{len(daftar_reaktan) + len(daftar_produk)}"
)

st.markdown("### 📖 Interpretasi")

st.write(
    f"Persamaan reaksi memiliki "
    f"{len(daftar_reaktan)} reaktan "
    f"dan {len(daftar_produk)} produk."
)
    # ==================================
    # JENIS REAKSI
    # ==================================
    elif fitur_reaksi == "Jenis Reaksi":

        jenis = st.selectbox(
            "Pilih Jenis Reaksi",
            [
                "Pembentukan",
                "Penguraian",
                "Pembakaran",
                "Substitusi Tunggal",
                "Substitusi Ganda"
            ]
        )

        if jenis == "Pembentukan":

            st.subheader("Pembentukan")
            st.latex(r"2H_2 + O_2 \rightarrow 2H_2O")

            st.info(
                "Dua atau lebih zat bergabung membentuk satu produk."
            )

        elif jenis == "Penguraian":

            st.subheader("Penguraian")
            st.latex(r"2H_2O \rightarrow 2H_2 + O_2")

            st.info(
                "Satu senyawa terurai menjadi beberapa zat."
            )

        elif jenis == "Pembakaran":

            st.subheader("Pembakaran")
            st.latex(r"CH_4 + 2O_2 \rightarrow CO_2 + 2H_2O")

            st.info(
                "Reaksi dengan oksigen menghasilkan energi."
            )

        elif jenis == "Substitusi Tunggal":

            st.subheader("Substitusi Tunggal")
            st.latex(
                r"Zn + 2HCl \rightarrow ZnCl_2 + H_2"
            )

            st.info(
                "Satu unsur menggantikan unsur lain."
            )

        elif jenis == "Substitusi Ganda":

            st.subheader("Substitusi Ganda")
            st.latex(
                r"AgNO_3 + NaCl \rightarrow AgCl + NaNO_3"
            )

            st.info(
                "Pertukaran ion antar senyawa."
            )

    # ==================================
    # PREDIKSI PRODUK
    # ==================================
    elif fitur_reaksi == "Prediksi Produk Reaksi":

        data_produk = {

            "H2 + O2":
            "H2O",

            "Na + Cl2":
            "NaCl",

            "Mg + O2":
            "MgO",

            "C + O2":
            "CO2",

            "CaO + H2O":
            "Ca(OH)2",

            "HCl + NaOH":
            "NaCl + H2O",

            "Fe + O2":
            "Fe2O3",

            "NH3 + HCl":
            "NH4Cl"
        }

        pilihan = st.selectbox(
            "Pilih Reaktan",
            list(data_produk.keys())
        )

        if st.button("Prediksi Produk"):

            st.markdown("""
            <div class="card">
            <h3>⚗️ Produk Reaksi</h3>
            </div>
            """, unsafe_allow_html=True)

            st.success(
                data_produk[pilihan]
            )

    # ==================================
    # DAFTAR REAKSI UMUM
    # ==================================
    elif fitur_reaksi == "Daftar Reaksi Umum":

        st.markdown("""
        <div class="card">
        <h3>📚 Contoh Reaksi Kimia Umum</h3>
        </div>
        """, unsafe_allow_html=True)

        st.table({
            "Nama Reaksi": [
                "Pembentukan Air",
                "Pembakaran Metana",
                "Pembentukan Garam",
                "Pembentukan CO₂",
                "Netralisasi",
                "Pembentukan Magnesium Oksida",
                "Penguraian Air"
            ],

            "Persamaan Reaksi": [

                "2H2 + O2 -> 2H2O",

                "CH4 + 2O2 -> CO2 + 2H2O",

                "2Na + Cl2 -> 2NaCl",

                "C + O2 -> CO2",

                "HCl + NaOH -> NaCl + H2O",

                "2Mg + O2 -> 2MgO",

                "2H2O -> 2H2 + O2"
            ]
        })
# =========================
# STOIKIOMETRI
# =========================
elif menu == "🧪 Stoikiometri":

    # ===== KODE ASLI KAMU (TETAP) =====
    if stoik_anim:
        st_lottie(stoik_anim, height=250)

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
        hasil_mol = round(mol, 4)

        st.markdown("""
        <div class="card">
        <h3>📊 Hasil Perhitungan</h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🧮 Cara Penyelesaian")

        st.write("**Rumus:**")
        st.latex(r"n = \frac{m}{Mr}")

        st.write("**Diketahui:**")
        st.write(f"Massa = {massa} gram")
        st.write(f"Mr = {Mr}")

        st.write("**Perhitungan:**")
        st.write(f"n = {massa} / {Mr}")
        st.write(f"n = {hasil_mol:g} mol")

        st.success(
            f"Hasil akhir = {hasil_mol:g} mol"
        )

      else:
        st.warning("Mr tidak boleh 0")
   
    # =====================================
    # TAMBAHAN FITUR STOIKIOMETRI
    # =====================================

    st.markdown("---")

    st.markdown("""
    <div class="card">
    <h2>🧪 Kalkulator Stoikiometri Tambahan</h2>
    <p>
    Fitur tambahan untuk membantu perhitungan kimia lainnya.
    </p>
    </div>
    """, unsafe_allow_html=True)

    fitur = st.selectbox(
        "Pilih Perhitungan Tambahan",
        [
            "Mol dari Partikel",
            "Mol dari Volume Gas",
            "Molaritas",
            "Pengenceran",
            "Persen Rendemen",
            "Pereaksi Pembatas"
        ]
    )

    # =========================
    # MOL DARI PARTIKEL
    # =========================
    if fitur == "Mol dari Partikel":

        partikel = st.number_input(
            "Jumlah Partikel",
            min_value=0.0,
            format="%.2e"
        )

        if st.button("Hitung Partikel"):

            hasil = partikel / (6.02e23)

            st.markdown("""
            <div class="card">
            <h3>📊 Hasil Perhitungan</h3>
            </div>
            """, unsafe_allow_html=True)

            st.success(f"{hasil:.6e} mol")

    # =========================
    # MOL DARI VOLUME GAS
    # =========================
    elif fitur == "Mol dari Volume Gas":

        volume = st.number_input(
            "Volume Gas STP (L)",
            min_value=0.0
        )

        if st.button("Hitung Volume Gas"):

            hasil = volume / 22.4

            st.markdown("""
            <div class="card">
            <h3>📊 Hasil Perhitungan</h3>
            </div>
            """, unsafe_allow_html=True)

            st.success(f"{hasil:.4f} mol")

    # =========================
    # MOLARITAS
    # =========================
    elif fitur == "Molaritas":

        col1, col2 = st.columns(2)

        with col1:
            mol_molaritas = st.number_input(
                "Jumlah Mol ",
                min_value=0.0
            )

        with col2:
            volume_molaritas = st.number_input(
                "Volume Larutan (L)",
                min_value=0.0
            )

        if st.button("Hitung Molaritas"):

            if volume_molaritas > 0:

                hasil = (
                    mol_molaritas /
                    volume_molaritas
                )

                st.markdown("""
                <div class="card">
                <h3>📊 Hasil Perhitungan</h3>
                </div>
                """, unsafe_allow_html=True)

                st.success(f"{hasil:.4f} M")

            else:
                st.warning("Volume tidak boleh 0")

    # =========================
    # PENGENCERAN
    # =========================
    elif fitur == "Pengenceran":

        st.latex(r"M_1V_1 = M_2V_2")

        col1, col2 = st.columns(2)

        with col1:
            M1 = st.number_input(
                "M1",
                min_value=0.0
            )

            V1 = st.number_input(
                "V1 (mL)",
                min_value=0.0
            )

        with col2:
            M2 = st.number_input(
                "M2",
                min_value=0.0
            )

        if st.button("Hitung Pengenceran"):

            if M2 > 0:

                hasil = (M1 * V1) / M2

                st.markdown("""
                <div class="card">
                <h3>📊 Hasil Perhitungan</h3>
                </div>
                """, unsafe_allow_html=True)

                st.success(
                    f"Volume akhir = {hasil:.2f} mL"
                )

            else:
                st.warning("M2 tidak boleh 0")

    # =========================
    # PERSEN RENDEMEN
    # =========================
    elif fitur == "Persen Rendemen":

        col1, col2 = st.columns(2)

        with col1:
            teori = st.number_input(
                "Hasil Teori",
                min_value=0.0
            )

        with col2:
            aktual = st.number_input(
                "Hasil Aktual",
                min_value=0.0
            )

        if st.button("Hitung Rendemen"):

            if teori > 0:

                hasil = (aktual / teori) * 100

                st.markdown("""
                <div class="card">
                <h3>📊 Hasil Perhitungan</h3>
                </div>
                """, unsafe_allow_html=True)

                st.success(f"{hasil:.2f}%")

            else:
                st.warning(
                    "Hasil teori tidak boleh 0"
                )

    # =========================
    # PEREAKSI PEMBATAS
    # =========================
    elif fitur == "Pereaksi Pembatas":

        col1, col2 = st.columns(2)

        with col1:

            mol_a = st.number_input(
                "Mol Pereaksi A",
                min_value=0.0
            )

            koef_a = st.number_input(
                "Koefisien A",
                min_value=1.0
            )

        with col2:

            mol_b = st.number_input(
                "Mol Pereaksi B",
                min_value=0.0
            )

            koef_b = st.number_input(
                "Koefisien B",
                min_value=1.0
            )

        if st.button(
            "Tentukan Pereaksi Pembatas"
        ):

            nilai_a = mol_a / koef_a
            nilai_b = mol_b / koef_b

            st.markdown("""
            <div class="card">
            <h3>📊 Hasil Analisis</h3>
            </div>
            """, unsafe_allow_html=True)

            if nilai_a < nilai_b:

                st.error(
                    "⚠️ Pereaksi A adalah pereaksi pembatas"
                )

            elif nilai_b < nilai_a:

                st.error(
                    "⚠️ Pereaksi B adalah pereaksi pembatas"
                )

            else:

                st.success(
                    "✅ Kedua pereaksi habis bersamaan"
                )

# =========================
# KELOMPOK 10
# =========================
elif menu == "👥 Kelompok 10":

    if team_anim:
        st_lottie(team_anim, height=250)

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
