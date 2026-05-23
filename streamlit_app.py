import streamlit as st
import requests

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Stoikiometri",
    page_icon="⚗️",
    layout="centered"
)

# =========================
# STYLE SIMPLE (SOFT BLUE)
# =========================
st.markdown("""
<style>
.stApp {
    background: #f3f8ff;
}

h1, h2, h3 {
    color: #1f4f8b;
}

.stButton>button {
    background-color: #4da3ff;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("⚗️ Kalkulator Stoikiometri")
st.write("Aplikasi sederhana untuk menyetarakan reaksi dan menghitung mol")

# =========================
# REAKSI (SIMPEL)
# =========================
st.subheader("🔬 Setarakan Reaksi")

reaction = st.text_input("Masukkan reaksi (contoh: H2 + O2 -> H2O)")

if st.button("Proses Reaksi"):
    if reaction:
        try:
            left, right = reaction.split("->")

            st.success("Reaksi terbaca!")

            st.write("### Reaktan")
            st.write(left.strip())

            st.write("### Produk")
            st.write(right.strip())

        except:
            st.error("Format salah! pakai tanda ->")
    else:
        st.warning("Isi dulu reaksi!")

# =========================
# MOL CALCULATOR
# =========================
st.divider()
st.subheader("🧪 Hitung Mol")

massa = st.number_input("Massa (gram)", min_value=0.0)
Mr = st.number_input("Mr zat", min_value=0.0)

if st.button("Hitung"):
    if Mr > 0:
        mol = massa / Mr
        st.success(f"Hasil mol = {mol:.4f}")
    else:
        st.warning("Mr tidak boleh 0")

# =========================
# KELOMPOK 10
# =========================
st.divider()
st.title("👥 Kelompok 10")

st.markdown("""
1. Faturrahman Chandika (2560774)  
2. Naisyla Nazwa S. (2560705)  
3. Nassya Alifha Rasyikha (2560710)  
4. Reva Aulia (2560749)  
5. Sarah Nur Ichsani (2560774)  
""")

st.success("Kelompok 10 - Stoikiometri")
