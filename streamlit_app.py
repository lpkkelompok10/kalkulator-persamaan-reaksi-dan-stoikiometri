import streamlit as st
from chempy import balance_stoichiometry

st.title("🧪 Kalkulator Stoikiometri")

st.write("Aplikasi untuk menyetarakan persamaan reaksi kimia")

# Input reaksi
reaksi = st.text_input(
    "Masukkan persamaan reaksi",
    placeholder="Contoh: H2 + O2 -> H2O"
)

# Tombol
if st.button("Setarakan Reaksi"):

    try:
        # Pisahkan reaktan dan produk
        kiri, kanan = reaksi.split("->")

        reaktan = set(i.strip() for i in kiri.split("+"))
        produk = set(i.strip() for i in kanan.split("+"))

        # Setarakan otomatis
        reac, prod = balance_stoichiometry(reaktan, produk)

        # Format hasil
        hasil_kiri = " + ".join(
            [f"{v if v != 1 else ''}{k}" for k, v in reac.items()]
        )

        hasil_kanan = " + ".join(
            [f"{v if v != 1 else ''}{k}" for k, v in prod.items()]
        )

        hasil = hasil_kiri + " -> " + hasil_kanan

        # Output
        st.success("✅ Persamaan reaksi berhasil disetarakan!")
        st.code(hasil)

    except:
        st.error("❌ Format reaksi salah")
