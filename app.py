import streamlit as st
from fpdf import FPDF

# 1. Configuration de la page
st.set_page_config(page_title="Menu La Brioche Dorée", page_icon="🥖", layout="centered")

# 2. CSS Personnalisé pour un rendu "Application Mobile"
st.markdown("""
    <style>
    /* Centrage et taille du logo */
    .logo-container {
        display: flex;
        justify-content: center;
        padding: 20px 0;
    }
    .logo-img {
        width: 220px; /* Taille idéale pour mobile */
        filter: drop-shadow(0px 4px 4px rgba(0,0,0,0.1));
    }
    
    /* Style des titres de catégories */
    .category-header {
        background-color: #E30613; /* Rouge officiel */
        color: white !important;
        padding: 10px 20px;
        border-radius: 50px;
        font-weight: bold;
        margin: 25px 0 15px 0;
        text-align: center;
        font-size: 1.1rem;
        letter-spacing: 1px;
    }

    /* Nom des produits - S'adapte au Mode Sombre/Clair */
    .item-name {
        color: var(--text-color); 
        font-weight: 700;
        font-size: 1.05rem;
    }
    
    /* Description des produits */
    .item-desc {
        color: var(--text-color);
        opacity: 0.7;
        font-size: 0.85rem;
        line-height: 1.3;
    }

    /* Badge de prix Doré/Bronze */
    .price-badge {
        background-color: #C5A059;
        color: white !important;
        padding: 4px 12px;
        border-radius: 12px;
        font-weight: bold;
        font-size: 0.95rem;
        display: inline-block;
        white-space: nowrap;
    }

    /* Ligne de séparation fine */
    .divider {
        border-bottom: 1px solid rgba(128, 128, 128, 0.15);
        margin: 12px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Affichage du Logo Officiel
URL_LOGO = "https://menusbriochedoree.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzYsInB1ciI6ImJsb2JfaWQifX0=--0d78017dbb6238d5e994eb23c7bbaeb550fd31c1/briocheDoree-removebg-preview%20(1).png"

st.markdown(f'''
    <div class="logo-container">
        <img src="{URL_LOGO}" class="logo-img">
    </div>
''', unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#E30613; margin-top:-20px;'>FADIA</h3>", unsafe_allow_html=True)

# 4. Base de données du Menu
menu_data = {
    "🥪 NOS SANDWICHS": [
        ["Exotic", "1500 Fr"],
        ["Chawarma Royal", "2000 Fr", "Oeuf, Fromage"],
        ["Chawarma Pacha", "2500 Fr", "Oeuf, Fromage, Hot-dog"],
        ["Hamburger", "1500 Fr"],
        ["Royal Burger", "2500 Fr"],
        ["Tacos", "2500 Fr"]
    ],
    "🍕 NOS PIZZAS": [
        ["Pizza Reine", "4000 / 5000 Fr", "Jambon boeuf, emmental, olives"],
        ["Pizza Fermière", "4000 / 5000 Fr", "Poulet, oignons, champignons"],
        ["Pizza Bolognaise", "5000 / 6000 Fr", "Viande hachée, oignons, emmental"],
        ["Pizza 3 Fromages", "5000 / 6000 Fr", "Mozzarella, bleu, emmental"]
    ],
    "🥤 BOISSONS FRAÎCHES": [
        ["Sodas", "800 Fr", "Coca, Sprite, Fanta"],
        ["Jus en bouteille", "1000 Fr"],
        ["Eau Kirène 1.5L", "750 Fr"]
    ]
}

# 5. Affichage dynamique du contenu
for categorie, items in menu_data.items():
    st.markdown(f'<div class="category-header">{categorie}</div>', unsafe_allow_html=True)
    for item in items:
        col_info, col_prix = st.columns([3, 1])
        with col_info:
            st.markdown(f'<div class="item-name">{item[0]}</div>', unsafe_allow_html=True)
            if len(item) > 2:
                st.markdown(f'<div class="item-desc">{item[2]}</div>', unsafe_allow_html=True)
        with col_prix:
            st.markdown(f'<div style="text-align:right;"><span class="price-badge">{item[1]}</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# 6. Section Export PDF (Bas de page)
st.write(" ")
with st.expander("📥 Télécharger le menu (PDF)"):
    def generate_pdf(data):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(227, 6, 19)
        pdf.cell(190, 15, "LA BRIOCHE DOREE - FADIA", ln=True, align='C')
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

    if st.button("Générer le fichier"):
        pdf_content = generate_pdf(menu_data)
        st.download_button("💾 Enregistrer le Menu", pdf_content, "Menu_Brioche_Fadia.pdf", "application/pdf")

st.markdown("<p style='text-align:center; font-size:0.7rem; opacity:0.5; margin-top:30px;'>Scannez pour accéder au menu en direct</p>", unsafe_allow_html=True)
