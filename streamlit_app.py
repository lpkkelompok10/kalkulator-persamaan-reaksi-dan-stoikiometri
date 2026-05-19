import streamlit as st

# Judul aplikasi
st.title("🧪 Kalkulator Stoikiometri")

st.write("Aplikasi sederhana untuk menghitung stoikiometri dan persamaan reaksi kimia")

# Input reaksi
st.header("Persamaan Reaksi Kimia")

reaksi = st.text_input(
    "Masukkan persamaan reaksi",
    placeholder="Contoh: 2H2 + O2 -> 2H2O"
)

# Tombol tampilkan reaksi
if st.button("Tampilkan Reaksi"):

    st.success(f"✅ Persamaan reaksi: {reaksi}")

    # Cek sederhana apakah reaksi contoh sudah setara
    if reaksi == "2H2 + O2 -> 2H2O":
        st.info("✔ Persamaan reaksi sudah setara")
    else:
        st.warning("⚠ Pastikan persamaan reaksi sudah setara")

# Garis pemisah
st.divider()

# Bagian stoikiometri
st.header("Perhitungan Stoikiometri")

st.write("Contoh perhitungan berdasarkan reaksi:")
st.code("2H2 + O2 -> 2H2O")

# Input massa
massa_H2 = st.number_input(
    "Masukkan massa H2 (gram)",
    min_value=0.0
)

# Data Mr
Mr_H2 = 2
Mr_O2 = 32

# Koefisien reaksi
koef_H2 = 2
koef_O2 = 1

# Tombol hitung
if st.button("Hitung Stoikiometri"):

    # Gram → mol
    mol_H2 = massa_H2 / Mr_H2

    # Perbandingan koefisien
    mol_O2 = mol_H2 * (koef_O2 / koef_H2)

    # Mol → gram
    massa_O2 = mol_O2 * Mr_O2

    # Output hasil
    st.success(f"✅ Butuh O2 sebanyak {massa_O2} gram")

    # Langkah perhitungan
    st.subheader("Langkah Perhitungan")

    st.write(f"1. Mol H2 = {massa_H2} / {Mr_H2}")
    st.write(f"2. Mol H2 = {mol_H2} mol")

    st.write(f"3. Perbandingan H2 : O2 = 2 : 1")
    st.write(f"4. Mol O2 = {mol_O2} mol")

    st.write(f"5. Massa O2 = {mol_O2} × {Mr_O2}")
    st.write(f"6. Massa O2 = {massa_O2} gram")

# Footer
st.divider()
st.caption("Dibuat dengan Python dan Streamlit")
