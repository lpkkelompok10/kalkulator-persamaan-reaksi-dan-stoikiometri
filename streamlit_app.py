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
# THEME TOGGLE (FINAL BONUS)
# =========================
theme = st.sidebar.selectbox("🎨 Theme", ["Light", "Soft Dark"])

if theme == "Soft Dark":
    bg = "#0f172a"
    card = "#1e293b"
    text = "white"
    subtext = "#cbd5e1"
else:
    bg = "#f4f8ff"
    card = "white"
    text = "#1f4f8b"
    subtext = "#4d6fa3"

# =========================
# GLOBAL STYLE
# =========================
st.markdown(f"""
<style>

.stApp {{
    background: {bg};
    color: {text};
}}

.card {{
    background: {card};
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    transition: 0.25s ease;
}}

.card:hover {{
    transform: translateY(-6px);
}}

h1, h2, h3 {{
    color: {text};
}}

p {{
    color: {subtext};
}}

.stButton>button {{
    background-color: #4da3ff;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
}}

.stButton>button:hover {{
    background-color: #1f7ae0;
    transform: scale(1.05);
}}

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

    st.markdown("""
    <div style="text-align:center; padding:10px">
        <h1>⚗️ Kalkulator Kimia</h1>
        <p>Persamaan Reaksi Kimia & Stoikiometri - Kelompok 10</p>
    </div>
    """, unsafe_allow_html=True)

    # GAMBAR 1
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Water_molecule_3D.svg/800px-Water_molecule_3D.svg.png",
        caption="Struktur Molekul Air (H₂O)",
        use_container_width=True
    )

    # GAMBAR 2
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Periodic_table_large.png/800px-Periodic_table_large.png",
        caption="Tabel Periodik Unsur",
        use_container_width=True
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h3>🔬 Reaksi</h3><p>Analisis reaksi kimia</p></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h3>🧪 Stoikiometri</h3><p>Hitung mol otomatis</p></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><h3>📘 Materi</h3><p>Belajar kimia dasar</p></div>", unsafe_allow_html=True)

    st.markdown("---")

    if st.button("📌 Tentang Aplikasi"):

        st.markdown("""
        <div class="card">
        <h2>📘 Tentang Aplikasi</h2>

        Aplikasi ini dibuat untuk membantu pembelajaran kimia secara interaktif.

        <h3>🎯 Tujuan</h3>
        - Memahami reaksi kimia  
        - Menghitung stoikiometri  
        - Media belajar modern  

        <h3>💡 Manfaat</h3>
        - Lebih mudah dipahami  
        - Visual interaktif  
        - Latihan cepat  

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
            with st.spinner("⚗️ Memproses reaksi..."):
                time.sleep(1)

            try:
                left, right = reaction.split("->")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("<div class='card'><h3>🔵 Reaktan</h3></div>", unsafe_allow_html=True)
                    st.write(left.strip())

                with col2:
                    st.markdown("<div class='card'><h3>🟢 Produk</h3></div>", unsafe_allow_html=True)
                    st.write(right.strip())

                st.success("Berhasil!")

            except:
                st.error("Format salah!")

        else:
            st.warning("Isi dulu!")

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

            st.markdown("<div class='card'><h3>📊 Hasil</h3></div>", unsafe_allow_html=True)
            st.success(f"{mol:.4f} mol")

        else:
            st.warning("Mr tidak boleh 0")

# =========================
# MATERI
# =========================
elif menu == "📘 Materi":

    st.title("📘 Materi Kimia")

    st.markdown("<div class='card'><h3>⚗️ Reaksi Kimia</h3><p>Perubahan zat menjadi zat baru.</p></div>", unsafe_allow_html=True)

    st.markdown("<div class='card'><h3>🧪 Stoikiometri</h3><p>Hubungan kuantitatif dalam reaksi.</p></div>", unsafe_allow_html=True)

    st.markdown("<div class='card'><h3>💡 Contoh</h3><p>2H₂ + O₂ → 2H₂O</p></div>", unsafe_allow_html=True)

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
