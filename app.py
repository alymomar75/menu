import streamlit as st
from fpdf import FPDF

# 1. Configuration de la page
st.set_page_config(page_title="Menu La Brioche Dorée", page_icon="🥖")

# 2. CSS Optimisé pour la lisibilité
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* Titre Principal */
    .main-title {
        color: #B22222;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0px;
    }
    
    /* Titres de catégories - Fond Rouge, Texte Blanc */
    .category-header {
        background-color: #B22222;
        color: white !important;
        padding: 8px 15px;
        border-radius: 5px;
        font-size: 1.1rem;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    
    /* Noms des plats - NOIR pour lisibilité sur blanc */
    .item-name {
        color: #1A1A1A !important;
        font-size: 1.05rem;
        font-weight: 600;
    }
    
    /* Descriptions - Gris foncé */
    .item-desc {
        color: #4F4F4F !important;
        font-size: 0.9rem;
        line-height: 1.2;
    }
    
    /* Prix - Style "Badge" Doré */
    .price-badge {
        background-color: #FFD700;
        color: #000000;
        padding: 2px 10px;
        border-radius: 10px;
        font-weight: bold;
        float: right;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Données
menu_data = {
    "🥪 LES SANDWICHS": [
        ["Exotic", "1500 Fr"],
        ["Chawarma Pacha", "2500 Fr"],
        ["Hamburger", "1500 Fr"],
        ["Tacos", "2500 Fr"],
        ["Sandwich Steak", "1500 Fr"]
    ],
    "🍕 LES PIZZAS": [
        ["Pizza Reine", "4000/5000 Fr", "Jambon boeuf, emmental, olives"],
        ["Pizza Fermière", "4000/5000 Fr", "Poulet, oignons, champignons"],
        ["Pizza 3 Fromages", "5000/6000 Fr", "Mozzarella, bleu, emmental"]
    ],
    "🥤 BOISSONS": [
        ["Sodas", "800 Fr"],
        ["Jus en bouteille", "1000 Fr"],
        ["Eau Kirène 1.5L", "750 Fr"]
    ]
}

# 4. Affichage du Menu
st.markdown('<p class="main-title">LA BRIOCHE DORÉE</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#B22222; font-weight:bold;'>FADIA</p>", unsafe_allow_html=True)

for categorie, items in menu_data.items():
    st.markdown(f'<div class="category-header">{categorie}</div>', unsafe_allow_html=True)
    for item in items:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f'<span class="item-name">{item[0]}</span>', unsafe_allow_html=True)
            if len(item) > 2:
                st.markdown(f'<div class="item-desc">{item[2]}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<span class="price-badge">{item[1]}</span>', unsafe_allow_html=True)
        st.markdown("<hr style='margin:10px 0; border:0.5px solid #EEEEEE'>", unsafe_allow_html=True)

# 5. Export PDF - Version Discrète dans l'Expander
st.write("---")
with st.expander("📥 Options d'impression"):
    def generate_pdf(data):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(178, 34, 34)
        pdf.cell(190, 10, "LA BRIOCHE DOREE - FADIA", ln=True, align='C')
        pdf.ln(10)
        for cat, items in data.items():
            pdf.set_font("Arial", 'B', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(190, 10, cat.encode('latin-1', 'replace').decode('latin-1'), ln=True)
            pdf.set_font("Arial", '', 11)
            for item in items:
                line = f"{item[0]} : {item[1]}".encode('latin-1', 'replace').decode('latin-1')
                pdf.cell(190, 7, line, ln=True)
            pdf.ln(5)
        return pdf.output(dest='S').encode('latin-1')

    if st.button("Générer le PDF maintenant"):
        pdf_bytes = generate_pdf(menu_data)
        st.download_button("Cliquez ici pour télécharger", pdf_bytes, "Menu_Fadia.pdf", "application/pdf")
