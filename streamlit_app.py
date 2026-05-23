import streamlit as st
import requests
import time

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Stoikiometri Kelompok 10",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# STYLE SOFT BLUE MODERN
# =========================
st.markdown("""
<style>
.stApp {
    background: #f5f9ff;
}

/* sidebar */
[data-testid="stSidebar"] {
    background: #e8f2ff;
}

/* card */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 10px;
}

/* title */
h1, h2, h3 {
    color: #1f4f8b;
}

/* button */
.stButton>button {
    background-color: #4da3ff;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
}

.stButton>button:hover {
    background-color: #1f7ae0;
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
    "📌 Menu",
    ["🏠 Home", "⚗️ Stoikiometri", "🧪 Mol", "👥 Kelompok 10"]
)

# =========================
# HOME
# =========================
if menu == "🏠 Home":
    st.title("⚗️ Stoikiometri App - Kelompok 10")

    # Lottie animation
    try:
        from streamlit_lottie import st_lottie

        lottie_url = "https://assets10.lottiefiles.com/packages/lf20_jtbfg2nb.json"
        animation = load_lottie(lottie_url)

        if animation:
            st_lottie(animation, height=250)
    except:
        st.info("Animasi tidak aktif")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🔬 Reaksi</h3>
        <p>Setarakan dan baca reaksi kimia</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🧪 Mol</h3>
        <p>Kalkulator massa ke mol</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>👥 Kelompok</h3>
        <p>Anggota Kelompok 10</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# STOIKIOMETRI
# =========================
elif menu == "⚗️ Stoikiometri":
    st.title("⚗️ Setarakan Reaksi Kimia")

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
                st.error("Format salah! gunakan ->")

        else:
            st.warning("Isi reaksi dulu!")

# =========================
# MOL CALCULATOR
# =========================
elif menu == "🧪 Mol":
    st.title("🧪 Kalkulator Mol")

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
            <h3>📊 Hasil</h3>
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
