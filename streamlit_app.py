import streamlit as st
import time

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Persamaan Reaksi & Stoikiometri",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# STYLE
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg, #f4f8ff, #ffffff);
}

.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 12px;
}

h1, h2, h3 {
    color: #1f4f8b;
}

.stButton>button {
    background-color: #4da3ff;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
}

.stButton>button:hover {
    background-color: #1f7ae0;
}

</style>
""", unsafe_allow_html=True)

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

    st.title("⚗️ Kalkulator Persamaan Reaksi Kimia & Stoikiometri")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/98/Periodic_table_large.png",
        use_container_width=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h3>🔬 Reaksi Kimia</h3><p>Analisis reaksi</p></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h3>🧪 Stoikiometri</h3><p>Hitung mol</p></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><h3>📘 Materi</h3><p>Belajar dasar kimia</p></div>", unsafe_allow_html=True)

    st.markdown("---")

    if st.button("📌 Tentang Aplikasi"):
        st.markdown("""
        <div class="card">
        <h2>📘 Tentang Aplikasi</h2>

        Aplikasi ini dibuat untuk membantu pembelajaran:
        - Persamaan reaksi kimia  
        - Stoikiometri  

        <h3>💡 Manfaat</h3>
        - Mudah digunakan  
        - Membantu belajar lebih cepat  
        - Tampilan sederhana dan jelas  

        </div>
        """, unsafe_allow_html=True)

# =========================
# REAKSI KIMIA
# =========================
elif menu == "⚗️ Reaksi Kimia":

    st.title("⚗️ Persamaan Reaksi Kimia")

    reaction = st.text_input("Contoh: H2 + O2 -> H2O")

    if st.button("Proses"):

        if reaction:
            try:
                left, right = reaction.split("->")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("<div class='card'><h3>🔵 Reaktan</h3></div>", unsafe_allow_html=True)
                    st.write(left.strip())

                with col2:
                    st.markdown("<div class='card'><h3>🟢 Produk</h3></div>", unsafe_allow_html=True)
                    st.write(right.strip())

                st.success("Berhasil diproses!")

            except:
                st.error("Format harus pakai ->")

        else:
            st.warning("Isi reaksi dulu!")

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

    st.markdown("""
    <div class="card">
    <h3>⚗️ Reaksi Kimia</h3>
    Perubahan zat menjadi zat baru
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🧪 Stoikiometri</h3>
    Hubungan kuantitatif dalam reaksi kimia
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
        st.markdown(f"<div class='card'>{m}</div>", unsafe_allow_html=True)
