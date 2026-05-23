import streamlit as st
import time
import requests

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Kimia - Kelompok 10",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# STYLE (ULTIMATE CLEAN UI)
# =========================
st.markdown("""
<style>

/* background */
.stApp {
    background: linear-gradient(180deg, #f4f8ff, #ffffff);
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
    box-shadow: 0px 12px 24px rgba(0,0,0,0.12);
}

/* CARD */
.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
    transition: all 0.25s ease;
    margin-bottom: 12px;
}

.card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0px 18px 40px rgba(0,0,0,0.15);
}

/* BUTTON */
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

/* TITLE */
h1, h2, h3 {
    color: #1f4f8b;
}

/* CENTER HEADER */
.header {
    text-align: center;
    padding: 20px;
}

.header h1 {
    font-size: 40px;
    margin-bottom: 0;
}

.header p {
    color: #4d6fa3;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

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

# =========================
# SIDEBAR MENU
# =========================
menu = st.sidebar.radio(
    "📌 Navigation",
    ["🏠 Home", "⚗️ Reaksi Kimia", "🧪 Stoikiometri", "👥 Kelompok 10"]
)

# =========================
# HOME (ULTIMATE LANDING PAGE)
# =========================
if menu == "🏠 Home":

    st.markdown("""
    <div class="header">
        <h1>⚗️ Kalkulator Kimia</h1>
        <p>Persamaan Reaksi Kimia & Stoikiometri - Kelompok 10</p>
    </div>
    """, unsafe_allow_html=True)

    # LOTTIE ANIMATION
    try:
        from streamlit_lottie import st_lottie

        animation = load_lottie(
            "https://assets10.lottiefiles.com/packages/lf20_jtbfg2nb.json"
        )

        if animation:
            st_lottie(animation, height=260)
    except:
        st.info("Animasi tidak aktif")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🔬 Reaksi Kimia</h3>
        Analisis & baca persamaan reaksi
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🧪 Stoikiometri</h3>
        Hitung mol dengan cepat & mudah
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
# REAKSI KIMIA
# =========================
elif menu == "⚗️ Reaksi Kimia":

    st.title("⚗️ Persamaan Reaksi Kimia")

    reaction = st.text_input("Masukkan reaksi (contoh: H2 + O2 -> H2O)")

    if st.button("Proses Reaksi"):

        if reaction:

            with st.spinner("⚗️ Memproses reaksi..."):
                time.sleep(1.3)

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
                st.error("Format salah! gunakan ->")

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
