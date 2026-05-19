import streamlit as st

st.title("🎈KALKULATOR PERSAMAAN REAKSI DAN STOIKIOMETRI")
st.write(import streamlit as st

# Judul aplikasi
st.set_page_config(page_title="Kalkulator Stoikiometri", page_icon="🧪")

st.title("🧪 Kalkulator Stoikiometri")
st.write("Aplikasi sederhana untuk menghitung stoikiometri dan persamaan reaksi kimia")

# Menu sidebar
menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Hitung Mol", "Hitung Massa", "Persamaan Reaksi"]
)

# =========================
# HITUNG MOL
# =========================
if menu == "Hitung Mol":

    st.header("Menghitung Mol")

    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0)
    mr = st.number_input("Masukkan Mr zat", min_value=0.1)

    if st.button("Hitung Mol"):
        mol = massa / mr
        st.success(f"Jumlah mol = {mol:.4f} mol")

        st.info("Rumus: mol = massa / Mr")

# =========================
# HITUNG MASSA
# =========================
elif menu == "Hitung Massa":

    st.header("Menghitung Massa")

    mol = st.number_input("Masukkan jumlah mol", min_value=0.0)
    mr = st.number_input("Masukkan Mr zat", min_value=0.1)

    if st.button("Hitung Massa"):
        massa = mol * mr
        st.success(f"Massa zat = {massa:.4f} gram")

        st.info("Rumus: massa = mol × Mr")

# =========================
# PERSAMAAN REAKSI
# =========================
elif menu == "Persamaan Reaksi":

    st.header("Persamaan Reaksi Kimia")

    reaksi = st.text_input(
        "Masukkan persamaan reaksi",
        placeholder="Contoh: H2 + O2 -> H2O"
    )

    if st.button("Tampilkan Reaksi"):
        st.success(f"Persamaan reaksi: {reaksi}")

        st.write("Pastikan persamaan reaksi sudah setara.")

# Footer
st.markdown("---")
st.caption("Dibuat dengan Python dan Streamlit")
    
    
