import streamlit as st
import time
from PIL import Image, ImageDraw

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
    background: linear-gradient(180deg, #f4f8ff, #ffffff);
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    transition: 0.25s ease;
}

.card:hover {
    transform: translateY(-6px);
}

h1, h2, h3 {
    color: #1f4f8b;
}

.stButton>button {
    background-color: #4da3ff;
    color: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# GAMBAR 1: MOLEKUL AIR (H2O)
# =========================
def create_water_molecule():
    img = Image.new("RGB", (600, 400), "white")
    draw = ImageDraw.Draw(img)

    # Oxygen
    draw.ellipse((270, 170, 330, 230), fill="red")
    draw.text((285, 200), "O", fill="white")

    # Hydrogen 1
    draw.ellipse((180, 100, 230, 150), fill="blue")
    draw.text((200, 120), "H", fill="white")
    draw.line((270, 200, 210, 130), fill="black", width=3)

    # Hydrogen 2
    draw.ellipse((370, 100, 420, 150), fill="blue")
    draw.text((390, 120), "H", fill="white")
    draw.line((330, 200, 395, 130), fill="black", width=3)

    return img

# =========================
# GAMBAR 2: TABEL PERIODIK MINI
# =========================
def create_periodic_table():
    img = Image.new("RGB", (600, 300), "white")
    draw = ImageDraw.Draw(img)

    elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"]

    x, y = 20, 20
    for i, el in enumerate(elements):
        draw.rectangle((x, y, x+50, y+50), outline="black")
        draw.text((x+15, y+15), el, fill="black")
        x += 55
        if (i+1) % 5 == 0:
            x = 20
            y += 60

    return img

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

    st.title("⚗️ Kalkulator Kimia & Stoikiometri")

    st.markdown("### 🔬 Visual Molekul Air (H₂O)")
    st.image(create_water_molecule(), use_container_width=True)

    st.markdown("### 🧪 Tabel Periodik Mini")
    st.image(create_periodic_table(), use_container_width=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h3>🔬 Reaksi Kimia</h3></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h3>🧪 Stoikiometri</h3></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><h3>📘 Materi</h3></div>", unsafe_allow_html=True)

    st.markdown("---")

    if st.button("📌 Tentang Aplikasi"):
        st.markdown("""
        <div class="card">
        <h2>📘 Tentang Aplikasi</h2>

        Aplikasi ini dibuat untuk membantu pembelajaran kimia.

        <h3>🎯 Tujuan</h3>
        - Memahami reaksi kimia  
        - Menghitung stoikiometri  
        - Media belajar interaktif  

        <h3>💡 Manfaat</h3>
        - 100% tanpa error gambar  
        - Jalan offline  
        - Visual sederhana tapi jelas  

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
            with st.spinner("Memproses..."):
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
            with st.spinner("Menghitung..."):
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
