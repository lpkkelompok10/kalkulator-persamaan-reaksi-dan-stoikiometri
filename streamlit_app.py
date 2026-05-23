import streamlit as st
import requests

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Stoikiometri",
    page_icon="⚗️",
    layout="centered"
)

# =========================
# CUSTOM STYLE (SOFT BLUE)
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #e6f2ff, #f7fbff);
    }

    h1, h2, h3 {
        color: #2b5d9c;
    }

    .stButton>button {
        background-color: #4da3ff;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1f7ae0;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# LOTTIE ANIMATION
# =========================
def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

# animasi kimia (safe CDN)
lottie_url = "https://assets10.lottiefiles.com/packages/lf20_jtbfg2nb.json"
animation = load_lottie(lottie_url)

try:
    from streamlit_lottie import st_lottie
    st_lottie(animation, height=250)
except:
    st.info("Animasi tidak tersedia (streamlit-lottie belum aktif)")

# =========================
# TITLE
# =========================
st.title("⚗️ Kalkulator Stoikiometri")
st.write("Masukkan reaksi kimia dan lakukan perhitungan sederhana dengan tampilan modern.")

# =========================
# INPUT REAKSI
# =========================
reaction = st.text_input("Masukkan reaksi (contoh: H2 + O2 -> H2O)")

# =========================
# SETARAKAN REAKSI (simple fallback)
# =========================
if st.button("Setarakan Reaksi"):
    if reaction:
        try:
            left, right = reaction.split("->")

            st.success("Reaksi diterima!")
            st.write("### 🔬 Reaktan:")
            st.write(left.strip())

            st.write("### 🧪 Produk:")
            st.write(right.strip())

            st.info("Catatan: versi ini menampilkan parsing dasar (bisa upgrade ke balancing otomatis penuh).")

        except:
            st.error("Format salah! Gunakan tanda ->")
    else:
        st.warning("Isi dulu reaksinya!")

# =========================
# MOL CALCULATOR
# =========================
st.divider()
st.subheader("🧪 Kalkulator Mol")

massa = st.number_input("Massa (gram)", min_value=0.0)
Mr = st.number_input("Mr zat", min_value=0.0)

if st.button("Hitung Mol"):
    if Mr > 0:
        mol = massa / Mr
        st.success(f"Hasil = {mol:.4f} mol")
    else:
        st.warning("Mr tidak boleh 0")
