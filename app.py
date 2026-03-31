import streamlit as st
from fpdf import FPDF

# 1. Configuration de la page
st.set_page_config(page_title="Menu La Brioche Dorée", page_icon="🥖")

# 2. Données (nettoyées pour éviter les bugs PDF)
menu_data = {
    "SANDWICHS": [
        ["Chawarma", "1500 Fr"],
        ["Chawarma Pacha", "2500 Fr"],
        ["Hamburger", "1500 Fr"],
        ["Tacos", "2500 Fr"]
    ],
    "PIZZAS": [
        ["Pizza Reine", "4000/5000 Fr", "Jambon boeuf, emmental, olives"],
        ["Pizza Fermiere", "4000/5000 Fr", "Poulet, oignons, champignons"],
        ["Pizza 3 Fromages", "5000/6000 Fr", "Mozzarella, bleu, emmental"]
    ],
    "BOISSONS": [
        ["Sodas", "800 Fr"],
        ["Jus Locaux", "500 Fr"],
        ["Eau Kirène 1.5L", "750 Fr"]
    ]
}

# 3. Interface Web
st.title("🥖 La Brioche Dorée - Fadia")

for categorie, items in menu_data.items():
    st.header(categorie)
    for item in items:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{item[0]}**")
            if len(item) > 2:
                st.caption(item[2])
        with col2:
            st.info(item[1])

# 4. Fonction PDF sécurisée
def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 10, "MENU LA BRIOCHE DOREE", ln=True, align='C')
    pdf.ln(10)
    
    for cat, items in data.items():
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(190, 10, cat, ln=True, fill=False)
        pdf.set_font("Arial", '', 12)
        for item in items:
            # On remplace les caractères spéciaux pour éviter l'erreur latin-1
            text = f"{item[0]} : {item[1]}".encode('latin-1', 'replace').decode('latin-1')
            pdf.cell(190, 8, text, ln=True)
        pdf.ln(5)
    return pdf.output(dest='S').encode('latin-1')

# 5. Bouton de téléchargement
st.sidebar.header("Export")
try:
    pdf_output = generate_pdf(menu_data)
    st.sidebar.download_button(
        label="📥 Télécharger le Menu PDF",
        data=pdf_output,
        file_name="menu_fadia.pdf",
        mime="application/pdf"
    )
except Exception as e:
    st.sidebar.error(f"Erreur PDF : {e}")
