import streamlit as st
from fpdf import FPDF

# Configuration de la page
st.set_page_config(page_title="Menu Digital - La Brioche Dorée Fadia", layout="centered")

# --- STYLE PERSONNALISÉ ---
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stHeader { color: #e63946; }
    .price-tag { color: #1d3557; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- DONNÉES DU MENU ---
menu_data = {
    "🥪 LES SANDWICHS": [
        ("Exotic", "1500 Fr"), ("Chawarma", "1500 Fr"), ("Chawarma Pacha", "2500 Fr"),
        ("Chawarma Royal", "2000 Fr"), ("Hamburger", "1500 Fr"), ("Royal Burger", "2500 Fr"),
        ("Tacos", "2500 Fr")
    ],
    "🍕 LES PIZZAS (MM / GM)": [
        ("Pizza Reine", "4000 / 5000 Fr", "Sauce tomate, jambon boeuf, emmental, olives"),
        ("Pizza Fermière", "4000 / 5000 Fr", "Sauce tomate, poulet, oignons, champignons"),
        ("Pizza Bolognaise", "5000 / 6000 Fr", "Sauce tomate, viande hachée, oignons, emmental"),
        ("Pizza 3 Fromages", "5000 / 6000 Fr", "Sauce tomate, mozzarella bleu, emmental")
    ],
    "🥤 BOISSONS FRAÎCHES": [
        ("Sodas (Coca, Sprite, Fanta)", "800 Fr"), ("Jus en bouteille", "1000 Fr"),
        ("Jus Locaux", "500 Fr"), ("Eau Kirène 1.5L", "750 Fr")
    ]
}

# --- INTERFACE ---
st.title("🥖 La Brioche Dorée - Fadia")
st.subheader("Menu Interactif & Commande")

# Navigation par onglets
tabs = st.tabs(list(menu_data.keys()))

for i, category in enumerate(menu_data.keys()):
    with tabs[i]:
        for item in menu_data[category]:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{item[0]}**")
                if len(item) > 2:  # Si description présente
                    st.caption(item[2])
            with col2:
                st.markdown(f"<span class='price-tag'>{item[1]}</span>", unsafe_allow_html=True)
            st.divider()

# --- FONCTION EXPORT PDF ---
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="MENU - LA BRIOCHE DOREE FADIA", ln=True, align='C')
    pdf.ln(10)
    
    for cat, items in menu_data.items():
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt=cat, ln=True)
        pdf.set_font("Arial", '', 10)
        for item in items:
            pdf.cell(200, 8, txt=f"{item[0]} : {item[1]}", ln=True)
        pdf.ln(5)
    return pdf.output(dest='S').encode('latin-1')

st.sidebar.title("Options")
if st.sidebar.button("Télécharger le Menu en PDF"):
    pdf_bytes = generate_pdf()
    st.sidebar.download_button(label="📄 Cliquer ici pour le PDF", 
                               data=pdf_bytes, 
                               file_name="menu_brioche_doree.pdf", 
                               mime="application/pdf")

st.sidebar.info("📞 Réservation : +221 33 829 92 92")
