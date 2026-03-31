import streamlit as st
from fpdf import FPDF

# 1. Configuration de la page
st.set_page_config(page_title="Menu La Brioche Dorée", page_icon="🥖")

# 2. Injection de CSS pour le thème Couleurs
st.markdown("""
    <style>
    /* Couleur de fond de l'application */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Style du titre principal */
    h1 {
        color: #B22222; /* Rouge Bordeaux */
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        border-bottom: 3px solid #FFD700; /* Ligne Dorée */
        padding-bottom: 10px;
    }
    
    /* Style des en-têtes de catégories */
    h2 {
        background-color: #B22222;
        color: white !important;
        padding: 10px;
        border-radius: 5px;
        font-size: 1.2rem !important;
    }
    
    /* Style des étiquettes de prix */
    .price-box {
        background-color: #FFD700; /* Jaune Doré */
        color: #000000;
        padding: 5px 10px;
        border-radius: 15px;
        font-weight: bold;
        display: inline-block;
    }

    /* Personnalisation de la barre latérale */
    [data-testid="stSidebar"] {
        background-color: #f8f8f8;
        border-right: 2px solid #B22222;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Données du Menu
menu_data = {
    "🥪 LES SANDWICHS": [
        ["Exotic", "1500 Fr"],
        ["Chawarma Pacha", "2500 Fr"],
        ["Hamburger", "1500 Fr"],
        ["Tacos", "2500 Fr"]
    ],
    "🍕 LES PIZZAS": [
        ["Pizza Reine", "4000/5000 Fr", "Jambon boeuf, emmental, olives"],
        ["Pizza Fermière", "4000/5000 Fr", "Poulet, oignons, champignons"],
        ["Pizza 3 Fromages", "5000/6000 Fr", "Mozzarella, bleu, emmental"]
    ],
    "🥤 BOISSONS": [
        ["Sodas", "800 Fr"],
        ["Jus Locaux", "500 Fr"],
        ["Eau Kirène 1.5L", "750 Fr"]
    ]
}

# 4. Affichage de l'interface
st.title("LA BRIOCHE DORÉE")
st.markdown("<p style='text-align:center; color:grey;'>Mini-Restaurant Fadia - Menu Officiel</p>", unsafe_allow_html=True)

for categorie, items in menu_data.items():
    st.header(categorie)
    for item in items:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{item[0]}**")
            if len(item) > 2:
                st.caption(item[2])
        with col2:
            # Utilisation de notre classe CSS 'price-box'
            st.markdown(f"<div class='price-box'>{item[1]}</div>", unsafe_allow_html=True)
    st.write("") # Espace entre catégories

# 5. Gestion du PDF (Sidebar)
def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    # En-tête PDF Rouge
    pdf.set_fill_color(178, 34, 34) # Rouge Bordeaux
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 15, "LA BRIOCHE DOREE - FADIA", ln=True, align='C', fill=True)
    
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    
    for cat, items in data.items():
        pdf.set_font("Arial", 'B', 12)
        pdf.set_fill_color(240, 240, 240)
        pdf.cell(190, 10, cat.encode('latin-1', 'replace').decode('latin-1'), ln=True, fill=True)
        pdf.set_font("Arial", '', 11)
        for item in items:
            text = f"{item[0]} : {item[1]}".encode('latin-1', 'replace').decode('latin-1')
            pdf.cell(190, 8, text, ln=True)
        pdf.ln(5)
    return pdf.output(dest='S').encode('latin-1')

st.sidebar.image("https://upload.wikimedia.org/wikipedia/fr/b/b2/La_Brioche_Dor%C3%A9e_Logo.png", width=150) # Logo simulé
st.sidebar.markdown("---")
if st.sidebar.button("📄 Générer le Menu PDF"):
    pdf_bytes = generate_pdf(menu_data)
    st.sidebar.download_button("⬇️ Télécharger", pdf_bytes, "menu_brioche.pdf", "application/pdf")
