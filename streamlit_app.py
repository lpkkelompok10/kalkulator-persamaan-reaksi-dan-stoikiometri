import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Stoikiometri Kelompok 10",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# STYLE (SOFT BLUE MODERN APP)
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

/* cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
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
# SIDEBAR
# =========================
menu = st.sidebar.radio(
    "📌 Menu",
    ["🏠 Home", "⚗️ Stoikiometri", "🧪 Mol", "👥 Kelompok 10"]
)

# =========================
# HOME (LANDING PAGE STYLE)
# =========================
if menu == "🏠 Home":
    st.title("⚗️ Stoikiometri App")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🔬 Reaksi</h3>
        <p>Setarakan reaksi kimia dengan tampilan rapi</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🧪 Mol</h3>
        <p>Kalkulator mol sederhana dan cepat</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>👥 Kelompok 10</h3>
        <p>Data anggota kelompok lengkap</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# STOIKIOMETRI PAGE
# =========================
elif menu == "⚗️ Stoikiometri":
    st.title("⚗️ Setarakan Reaksi Kimia")

    reaction = st.text_input("Masukkan reaksi (contoh: H2 + O2 -> H2O)")

    col1, col2 = st.columns(2)

    if st.button("Proses Reaksi"):
        if reaction:
            try:
                left, right = reaction.split("->")

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
