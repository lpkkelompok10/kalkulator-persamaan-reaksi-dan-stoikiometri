import streamlit as st
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
# MODERN UI CSS (WEB APP FEEL)
# =========================
st.markdown("""
<style>

/* background */
.stApp {
    background: #f5f9ff;
}

/* sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #e8f2ff, #f7fbff);
}

/* sidebar menu (radio) */
section[data-testid="stSidebar"] div[role="radiogroup"] > label {
    background: white;
    padding: 10px;
    border-radius: 12px;
    margin-bottom: 8px;
    transition: all 0.25s ease;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.06);
}

/* hover sidebar (ngambang) */
section[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
    transform: translateX(6px);
    background: #dbeaff;
    box-shadow: 0px 10px 20px rgba(0,0,0,0.12);
}

/* card */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    transition: all 0.25s ease;
}

/* hover card (floating effect) */
.card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0px 14px 30px rgba(0,0,0,0.18);
}

/* button */
.stButton>button {
    background-color: #4da3ff;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
    transition: all 0.2s ease;
}

/* button hover */
.stButton>button:hover {
    background-color: #1f7ae0;
    transform: scale(1.05);
}

/* text */
h1, h2, h3 {
    color: #1f4f8b;
}

</style>
""", unsafe_allow_html=True)

# =========================
# MENU SIDEBAR
# =========================
menu = st.sidebar.radio(
    "📌 Menu",
    ["🏠 Home", "⚗️ Stoikiometri", "🧪 Mol", "👥 Kelompok 10"]
)

# =========================
# HOME
# =========================
if menu == "🏠 Home":
    st.title("⚗️ Stoikiometri App")

    st.markdown("""
    <div class="card">
    <h3>👋 Selamat Datang</h3>
    Aplikasi ini membantu menyetarakan reaksi kimia dan menghitung mol dengan tampilan modern.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🔬 Reaksi</h3>
        Setarakan reaksi kimia
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🧪 Mol</h3>
        Hitung massa ke mol
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>👥 Kelompok</h3>
        Data anggota kelompok 10
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
            <h3>📊 Hasil Perhitungan</h3>
            </div>
            """, unsafe_allow_html=True)

            st.success(f"Hasil = {mol:.4f} mol")

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
