import streamlit as st
import requests
from chempy import balance_stoichiometry

# LOTTIE SAFE IMPORT
try:
    from streamlit_lottie import st_lottie
except:
    st_lottie = None

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Kalkulator Stoikiometri", page_icon="⚗️", layout="centered")

# =========================
# FUNCTION LOTTIE
# =========================
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# =========================
# TITLE
# =========================
st.title("⚗️ Kalkulator Stoikiometri")

st.write("Masukkan reaktan untuk menyeimbangkan reaksi kimia")

# =========================
# INPUT
# =========================
reaktan = st.text_input("Reaktan (pisahkan dengan spasi)", "H2 O2")
produk = st.text_input("Produk (pisahkan dengan spasi)", "H2O")

if st.button("Setarakan Reaksi"):
    try:
        reac, prod = balance_stoichiometry(
            set(reaktan.split()),
            set(produk.split())
        )

        st.success("Hasil reaksi setara:")

        st.write("### Reaktan:")
        st.write(reac)

        st.write("### Produk:")
        st.write(prod)

    except Exception as e:
        st.error("Terjadi error pada perhitungan")
        st.write(e)

# =========================
# OPTIONAL LOTTIE (SAFE)
# =========================
lottie_url = "https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json"
anim = load_lottie(lottie_url)

if st_lottie and anim:
    st_lottie(anim, height=250)
