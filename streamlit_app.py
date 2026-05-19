import streamlit as st
import pandas as pd
import re
from sympy import Matrix, lcm
from collections import Counter

st.set_page_config(
    page_title="Kalkulator Persamaan Reaksi & Stoikiometri",
    page_icon="🧪",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

.stButton>button {
    background-color: #7c3aed;
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #c084fc;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #d8b4fe;
}

.card {
    background-color: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🧪 Kalkulator Persamaan Reaksi & Stoikiometri</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Website pembelajaran kimia interaktif berbasis Python & Streamlit</div>', unsafe_allow_html=True)

st.write("")

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.selectbox(
    "📌 Pilih Menu",
    [
        "Home",
        "Penyetara Reaksi",
        "Stoikiometri",
        "Massa Molar",
        "Konverter Mol",
        "Tentang Kami"
    ]
)

# =========================
# FUNCTIONS
# =========================

def parse_formula(formula):
    tokens = re.findall(r'([A-Z][a-z]?)(\d*)', formula)
    composition = {}
    for element, count in tokens:
        composition[element] = composition.get(element, 0) + int(count or 1)
    return composition


def balance_equation(equation):
    left, right = equation.split('->')
    left_compounds = [c.strip() for c in left.split('+')]
    right_compounds = [c.strip() for c in right.split('+')]

    compounds = left_compounds + right_compounds

    elements = sorted(set(
        el for compound in compounds
        for el in parse_formula(compound)
    ))

    matrix = []

    for element in elements:
        row = []
        for compound in left_compounds:
            row.append(parse_formula(compound).get(element, 0))
        for compound in right_compounds:
            row.append(-parse_formula(compound).get(element, 0))
        matrix.append(row)

    mat = Matrix(matrix)
    null_space = mat.nullspace()

    if not null_space:
        return "Persamaan tidak bisa disetarakan"

    vec = null_space[0]
    multiplier = lcm([term.q for term in vec])
    coeffs = [abs(int(term * multiplier)) for term in vec]

    left_side = ' + '.join(
        f'{coeffs[i]}{left_compounds[i]}'
        for i in range(len(left_compounds))
    )

    right_side = ' + '.join(
        f'{coeffs[i+len(left_compounds)]}{right_compounds[i]}'
        for i in range(len(right_compounds))
    )

    return left_side + ' -> ' + right_side


atomic_masses = {
    'H': 1,
    'C': 12,
    'O': 16,
    'Na': 23,
    'Cl': 35.5,
    'N': 14,
    'S': 32,
    'K': 39,
    'Ca': 40,
    'Mg': 24
}


def calculate_molar_mass(formula):
    composition = parse_formula(formula)
    total = 0

    for element, count in composition.items():
        if element in atomic_masses:
            total += atomic_masses[element] * count

    return total


# =========================
# HOME
# =========================
if menu == "Home":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("✨ Fitur Website")

    st.write("✅ Penyetara Persamaan Reaksi")
    st.write("✅ Kalkulator Stoikiometri")
    st.write("✅ Kalkulator Massa Molar")
    st.write("✅ Konversi Mol")
    st.write("✅ Tampilan Modern")
    st.write("✅ Pembelajaran Kimia Interaktif")

    st.markdown('</div>', unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1532187643603-ba119ca4109e",
        use_container_width=True
    )

# =========================
# PENYETARA REAKSI
# =========================
elif menu == "Penyetara Reaksi":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("⚗️ Penyetara Persamaan Reaksi")

    equation = st.text_input(
        "Masukkan Persamaan Reaksi",
        placeholder="Contoh: H2 + O2 -> H2O"
    )

    if st.button("Setarakan"):
        try:
            result = balance_equation(equation)
            st.success(f"Hasil: {result}")
        except:
            st.error("Format salah. Gunakan format seperti H2 + O2 -> H2O")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# STOIKIOMETRI
# =========================
elif menu == "Stoikiometri":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("🧪 Kalkulator Stoikiometri")

    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0)
    mr = st.number_input("Masukkan massa molar / Mr", min_value=1.0)

    if st.button("Hitung Mol"):
        mol = massa / mr

        st.success(f"Jumlah mol = {mol:.3f} mol")

        st.latex(r"n = \frac{m}{Mr}")

        st.write(f"n = {massa} / {mr}")
        st.write(f"n = {mol:.3f} mol")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# MASSA MOLAR
# =========================
elif menu == "Massa Molar":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("⚛️ Kalkulator Massa Molar")

    formula = st.text_input(
        "Masukkan rumus kimia",
        placeholder="Contoh: H2SO4"
    )

    if st.button("Hitung Massa Molar"):
        try:
            result = calculate_molar_mass(formula)
            st.success(f"Massa molar {formula} = {result} g/mol")
        except:
            st.error("Rumus tidak valid")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# KONVERTER MOL
# =========================
elif menu == "Konverter Mol":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("🔄 Konverter Mol dan Partikel")

    mol = st.number_input("Masukkan jumlah mol", min_value=0.0)

    if st.button("Konversi"):
        partikel = mol * 6.02e23
        st.success(f"Jumlah partikel = {partikel:.2e}")

        st.latex(r"N = n \times 6.02 \times 10^{23}")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# TENTANG KAMI
# =========================
elif menu == "Tentang Kami":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("👩‍🔬 Tentang Kami")

    st.write("### Kelompok 10")
    st.write("1. Faturrahman Chandika (2560630)")
    st.write("2. Naisyla Nazwa S. (2560...)")
    st.write("3. Nassya Alifha Rasyikha (2560710)")
    st.write("4. Reva Aulia (2560...)")
    st.write("5. Sarah Nur Ichsani (2560774)")

    st.write("")

    st.write(
        "Website ini dibuat untuk membantu pembelajaran kimia terutama "
        "pada materi stoikiometri dan persamaan reaksi secara interaktif."
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.write("")
st.markdown("---")
st.caption("© 2026 | Kalkulator Persamaan Reaksi & Stoikiometri")
