import streamlit as st
import time

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Persamaan Reaksi Kimia & Stoikiometri",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# STYLE (FINAL CLEAN POLISH)
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
# SIDEBAR
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
        Persamaan Reaksi Kimia & Stoikiometri
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

    # =========================
    # 📘 PENJELASAN PANJANG (TAMBAHAN BARU)
    # =========================
    st.markdown("---")

    st.markdown("""
    <div class="card">
    <h2>📘 Tentang & Kegunaan Kalkulator</h2>

    <p>
    Aplikasi <b>Kalkulator Persamaan Reaksi Kimia dan Stoikiometri</b> ini dibuat untuk membantu memahami konsep dasar kimia secara lebih mudah, cepat, dan interaktif.
    Dalam pembelajaran kimia, banyak siswa sering mengalami kesulitan dalam menyeimbangkan persamaan reaksi serta menghitung perbandingan zat dalam reaksi kimia.
    </p>

    <p>
    Melalui aplikasi ini, pengguna dapat memasukkan persamaan reaksi kimia sederhana untuk kemudian dianalisis menjadi bagian reaktan dan produk.
    Hal ini membantu dalam memahami bagaimana suatu zat berubah menjadi zat lain dalam reaksi kimia.
    Selain itu, fitur stoikiometri memungkinkan pengguna untuk menghitung jumlah mol dari suatu zat berdasarkan massa dan Mr (massa molekul relatif), sehingga perhitungan kimia menjadi lebih praktis.
    </p>

    <p>
    <b>Manfaat utama aplikasi ini antara lain:</b><br>
    - Mempermudah pemahaman konsep reaksi kimia<br>
    - Membantu latihan soal stoikiometri dengan cepat<br>
    - Mengurangi kesalahan dalam perhitungan manual<br>
    - Menjadi media belajar interaktif berbasis teknologi<br>
    - Membuat pembelajaran kimia lebih menarik dan tidak membosankan
    </p>

    <p>
    Aplikasi ini dirancang dengan tampilan sederhana agar mudah digunakan oleh pelajar.
    Dengan sistem otomatis, pengguna dapat lebih cepat memahami konsep kimia yang sebelumnya terasa sulit.
    </p>

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
                time.sleep(1.2)

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

    st.markdown("""
    <div class="card">
    <h3>📋 Anggota Kelompok</h3>
    </div>
    """, unsafe_allow_html=True)

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
