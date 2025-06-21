
import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv("dataset_assortiment_fmcg.csv")
    return df

df = load_data()

st.set_page_config(page_title="Optimisation Assortiment FMCG", layout="wide")

# Titre principal
st.title("🛒 Optimisation de l’Assortiment Produits - Grande Consommation")

# Filtres
categories = df["Catégorie"].unique()
selected_categories = st.multiselect("Choisir les catégories à afficher :", categories, default=categories)

filtered_df = df[df["Catégorie"].isin(selected_categories)]

# KPIs globaux
st.subheader("🔢 Indicateurs clés")
col1, col2, col3 = st.columns(3)
col1.metric("CA total (€)", f"{filtered_df['CA (€)'].sum():,.0f}")
col2.metric("Volume total vendu", f"{filtered_df['Volume vendu (unités)'].sum():,.0f}")
col3.metric("Marge totale (€)", f"{filtered_df['Marge totale (€)'].sum():,.0f}")

# Visualisation CA vs Volume
st.subheader("📊 Chiffre d'affaires vs Volume vendu")
fig1 = px.scatter(filtered_df, x="Volume vendu (unités)", y="CA (€)",
                  size="Marge totale (€)", color="Catégorie",
                  hover_name="Produit", title="Positionnement des produits")
st.plotly_chart(fig1, use_container_width=True)

# Analyse élasticité prix
st.subheader("📉 Élasticité prix et impact promo")
fig2 = px.scatter(filtered_df, x="Élasticité prix", y="Taux de promo (%)",
                  size="CA (€)", color="Catégorie",
                  hover_name="Produit", title="Sensibilité prix vs Taux de promotion")
st.plotly_chart(fig2, use_container_width=True)

# Recommandation simple
st.subheader("Recommandations automatisées")
def recommender(row):
    if row["CA (€)"] > 10000 and row["Élasticité prix"] > -1:
        return "💎 Maintenir"
    elif row["CA (€)"] < 5000 and row["Élasticité prix"] < -1.5:
        return "🔻 Retirer"
    elif row["Taux de promo (%)"] >= 20 and row["Élasticité prix"] < -1:
        return "🧪 À tester sans promo"
    else:
        return "⚙️ À surveiller"

filtered_df["Recommandation"] = filtered_df.apply(recommender, axis=1)
st.dataframe(filtered_df[["Produit", "Catégorie", "CA (€)", "Élasticité prix", 
                          "Taux de promo (%)", "Marge totale (€)", "Recommandation"]])

st.caption("Projet réalisé par Samadou Kodon – 2025")
