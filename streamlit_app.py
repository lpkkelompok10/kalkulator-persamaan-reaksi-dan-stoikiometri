import streamlit as st
import time

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Kimia & Stoikiometri - Kelompok 10",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# STYLE
# =========================
st.markdown("""
<style>

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
    transition: all 0.25s ease;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.06);
}

section[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
    transform: translateX(6px);
    background: #dbeaff;
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
# MENU
# =========================
menu = st.sidebar.radio(
    "📌 Menu",
    ["🏠 Home", "⚗️ Reaksi Kimia", "🧪 Stoikiometri", "📘 Materi Kimia", "👥 Kelompok 10"]
)

# =========================
# HOME
# =========================
if menu == "🏠 Home":

    st.markdown("""
    <div style="text-align:center; padding:15px">
        <h1>⚗️ Kalkulator Kimia</h1>
        <p style="color:#4d6fa3; font-size:18px">
        Persamaan Reaksi Kimia & Stoikiometri - Kelompok 10
        </p>
    </div>
    """, unsafe_allow_html=True)

    # GAMBAR KIMIA
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Periodic_table_large.png/800px-Periodic_table_large.png",
        caption="Tabel Periodik Unsur",
        use_container_width=True
    )

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
        Perhitungan mol
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>📘 Materi</h3>
        Belajar kimia interaktif
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # TENTANG APLIKASI
    if st.button("📌 Tentang Aplikasi"):

        st.markdown("""
        <div class="card">
        <h2>📘 Tentang Aplikasi</h2>

        Aplikasi ini dibuat untuk membantu pembelajaran kimia interaktif.

        <h3>🎯 Tujuan:</h3>
        - Memahami reaksi kimia lebih mudah  
        - Menghitung stoikiometri secara cepat  
        - Media belajar yang lebih interaktif  

        <h3>💡 Manfaat:</h3>
        - Belajar lebih visual  
        - Mengurangi kesulitan hitung manual  
        - Cocok untuk latihan soal  
        </div>
        """, unsafe_allow_html=True)

# =========================
# REAKSI KIMIA
# =========================
elif menu == "⚗️ Reaksi Kimia":

    st.title("⚗️ Persamaan Reaksi Kimia")

    reaction = st.text_input("Masukkan reaksi (contoh: H2 + O2 -> H2O)")

    if st.button("Proses"):

        if reaction:
            with st.spinner("⚗️ Memproses..."):
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

                st.success("Berhasil diproses!")

            except:
                st.error("Format salah!")

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
# MATERI KIMIA
# =========================
elif menu == "📘 Materi Kimia":

    st.title("📘 Materi Kimia Interaktif")

    st.markdown("""
    <div class="card">
    <h3>⚗️ Reaksi Kimia</h3>
    Reaksi kimia adalah proses perubahan zat menjadi zat baru.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🧪 Stoikiometri</h3>
    Cabang kimia yang mempelajari hubungan kuantitatif zat dalam reaksi.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>💡 Contoh Reaksi</h3>
    2H₂ + O₂ → 2H₂O
    </div>
    """, unsafe_allow_html=True)

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
        st.markdown(f"""
        <div class="card">
        {m}
        </div>
        """, unsafe_allow_html=True)
