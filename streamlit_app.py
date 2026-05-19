import streamlit as st
from chempy import balance_stoichiometry

# =====================================
# JUDUL
# =====================================

st.title("🧪 Kalkulator Stoikiometri")

st.write(
    "Aplikasi sederhana untuk menyetarakan persamaan reaksi "
    "dan menghitung stoikiometri"
)

# =====================================
# PERSAMAAN REAKSI
# =====================================

st.header("Persamaan Reaksi Kimia")

reaksi = st.text_input(
    "Masukkan persamaan reaksi",
    placeholder="Contoh: H2 + O2 -> H2O"
)

# Variabel hasil setara
hasil = ""

# Tombol setarakan
if st.button("Setarakan Reaksi"):

    try:
        # Pisahkan reaktan dan produk
        kiri, kanan = reaksi.split("->")

        reaktan = set(i.strip() for i in kiri.split("+"))
        produk = set(i.strip() for i in kanan.split("+"))

        # Setarakan otomatis
        reac, prod = balance_stoichiometry(reaktan, produk)

        # Format kiri
        hasil_kiri = " + ".join(
            [f"{v if v != 1 else ''}{k}" for k, v in reac.items()]
        )

        # Format kanan
        hasil_kanan = " + ".join(
            [f"{v if v != 1 else ''}{k}" for k, v in prod.items()]
        )

        # Hasil akhir
        hasil = hasil_kiri + " -> " + hasil_kanan

        # Output
        st.success("✅ Persamaan reaksi berhasil disetarakan!")
        st.code(hasil)

        st.info("✔ Persamaan reaksi sudah setara")

    except:
        st.error("❌ Format reaksi salah")

# =====================================
# STOIKIOMETRI
# =====================================

st.divider()

st.header("Perhitungan Stoikiometri")

st.write("Contoh perhitungan menggunakan reaksi:")
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

    st.write("3. Perbandingan koefisien H2 : O2 = 2 : 1")

    st.write(f"4. Mol O2 = {mol_O2} mol")

    st.write(f"5. Massa O2 = {mol_O2} × {Mr_O2}")

    st.write(f"6. Massa O2 = {massa_O2} gram")

# =====================================
# FOOTER
# =====================================

st.divider()
st.caption("Dibuat dengan Python, Streamlit, dan Chempy")
