import streamlit as st

st.set_page_config(page_title="Kalkulator Kimia", page_icon="🧪")

st.title("🧪 Kalkulator Persamaan Reaksi & Stoikiometri")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Home", "Penyetara Reaksi", "Stoikiometri", "Massa Molar", "Tentang Kami"]
)

# HOME
if menu == "Home":
    st.write("Selamat datang di aplikasi kalkulator kimia 🧪")

# PENYETARA (VERSI SIMPLE BIAR GA ERROR)
elif menu == "Penyetara Reaksi":
    st.header("Penyetara Reaksi")
    reaksi = st.text_input("Masukkan reaksi (contoh: H2 + O2 -> H2O)")

    if st.button("Proses"):
        st.info("Fitur penyetaraan otomatis butuh sympy (versi lanjut bisa ditambah)")

# STOIKIOMETRI
elif menu == "Stoikiometri":
    st.header("Stoikiometri")
    massa = st.number_input("Massa (gram)", 0.0)
    Mr = st.number_input("Mr", 1.0)

    if st.button("Hitung"):
        mol = massa / Mr
        st.success(f"Mol = {mol}")

# MASSA MOLAR
elif menu == "Massa Molar":
    st.header("Massa Molar")
    st.write("Fitur ini bisa dikembangkan nanti")

# TENTANG KAMI
elif menu == "Tentang Kami":
    st.header("Kelompok 10")

    st.write("1. Faturrahman Chandika (2560630)")
    st.write("2. Naisyla Nazwa S. (2560...)")
    st.write("3. Nassya Alifha Rasyikha (2560710)")
    st.write("4. Reva Aulia (2560...)")
    st.write("5. Sarah Nur Ichsani (2560774)")
