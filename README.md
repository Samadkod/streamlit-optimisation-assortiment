# 🛒 Optimisation d’Assortiment FMCG  
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?logo=streamlit)  
🔗 [→ Lancer l’application en ligne](https://app-optimisation-aapprtiment-fmcg-aaa2kax5ty2sjwjrjcsgsj.streamlit.app/)

---

## 🎯 À quoi sert cette application ?

Cette application permet de **mieux choisir les produits à garder ou à retirer d’un catalogue**, en se basant sur des données simples mais stratégiques : chiffre d’affaires, marges, volume vendu, sensibilité au prix, promo…

C’est un **outil d’aide à la décision** pour les équipes marketing et commerciales dans le secteur **FMCG (produits de grande consommation)**.

---

## 👀 Ce que l’application vous montre

- Les **performances des produits** : CA, volume, marge
- Les **réactions aux promos** et à la variation des prix
- Des **recommandations automatiques** (à conserver, tester, retirer…)
- Une interface simple avec des **graphiques clairs et des filtres interactifs**

---

## 🧠 Comment sont faites les recommandations ?

| Produit avec... | On recommande de... | Pourquoi ? |
|-----------------|----------------------|------------|
| ❌ Faible CA + faible marge + forte sensibilité prix | 🔻 Retirer | Ce produit coûte plus qu’il ne rapporte |
| ✅ Bon CA + bonne marge + prix stable | 💎 Conserver | Produit rentable et fiable |
| ⚠️ Dépend beaucoup des promos | 🧪 Tester sans promo | Peut-être trop dépendant, à ajuster |
| 😐 Marge limite + sensibilité moyenne | ⚙️ Surveiller | À garder sous les yeux, évolution incertaine |

---

## 📸 Un aperçu rapide

| KPI                  | Valeur         |
|----------------------|----------------|
| CA total             | 209 234 €      |
| Volume total vendu   | 74 179 unités  |
| Marge totale         | 80 043 €       |

> Et des visuels comme CA vs Volume ou Promo vs Élasticité dans l’app !

---

## ⚙️ Tech utilisée

- Python (Pandas, Plotly)
- Streamlit pour créer le dashboard
- Données simulées pour 30 produits, 5 catégories

---

## 💬 Pourquoi ce projet est utile

🔹 Un mauvais assortiment = des pertes de ventes, une confusion client, des rayons inefficaces  
🔹 Ici, on montre comment utiliser **la data simplement pour guider des choix produits**

Pas besoin d’être analyste expert :  
👀 **en 15 secondes, on sait quoi faire** avec chaque produit !

---

## 👤 Projet réalisé par  
**Samadou KODON**  
🔗 [Portfolio](https://samadkod.github.io/) | [LinkedIn](https://www.linkedin.com/in/skodon)













# 🛒 Optimisation d’Assortiment FMCG  
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?logo=streamlit)  
🔗 [→ Lancer l’application en ligne](https://app-optimisation-aapprtiment-fmcg-aaa2kax5ty2sjwjrjcsgsj.streamlit.app/)

---

## 🎯 Objectif du projet

Ce projet simule un **outil d’aide à la décision** pour les équipes marketing, commerciales ou category managers dans le secteur **FMCG (grande consommation)**.

Grâce à l’analyse de données simulées (CA, volume, marge, promotion, élasticité), l’application permet de :

- Visualiser les performances produits par catégorie
- Identifier les produits à **conserver**, **retirer**, **surveiller** ou **tester**
- Formuler des recommandations stratégiques basées sur les données

---

## 📸 Aperçu de l’application
> [Clique ici pour tester l’application Streamlit](https://app-optimisation-aapprtiment-fmcg-aaa2kax5ty2sjwjrjcsgsj.streamlit.app/)

- 🎛️ Filtres interactifs par catégorie
- 📊 Graphiques : CA vs volume / Promo vs élasticité
- 💬 Recommandations générées automatiquement
- 📈 KPI synthétiques en haut du tableau de bord

---

## 🧠 Comment sont générées les recommandations ?

| Scénario produit | Recommandation | Raisonnement |
|------------------|----------------|--------------|
| 🟥 Faible CA, faible marge, forte élasticité prix | **🔻 Retirer** | Produit peu rentable, coûte plus qu’il ne rapporte |
| 🟢 Bon CA, bonne marge, faible sensibilité prix | **💎 Conserver** | Produit stable, rentable, à garder dans la gamme |
| 🟡 Promo forte + sensibilité prix élevée | **🧪 Tester sans promo** | Trop dépendant de la promo, peut-être repositionner |
| 🔵 Marge limite, élasticité moyenne | **⚙️ Surveiller** | Produit fragile, à suivre dans le temps |

---

## 📁 Contenu du dépôt

| Fichier                              | Description                                      |
|-------------------------------------|--------------------------------------------------|
| `app_streamlit_assortiment.py`      | Code Python de l’application Streamlit          |
| `dataset_assortiment_fmcg.csv`      | Données simulées – 30 produits, 5 catégories     |
| `requirements.txt`                  | Dépendances pour exécution sur Streamlit Cloud   |
| `README.md`                         | Présentation du projet                           |

---

## 🧰 Technologies utilisées

- **Python** – Pandas, Plotly
- **Streamlit** – pour le dashboard interactif
- **Visualisation & UX** – Filtrage, mise en forme, recommandations
- **Logique métier simulée** – Élasticité, scoring produit, merchandising

---

## 💡 Pourquoi ce projet ?

La gestion d’un assortiment est **un enjeu stratégique** en grande distribution :  
mal optimiser sa gamme, c’est perdre en CA, en fidélité ou en lisibilité.

J’ai donc voulu créer un **outil concret, simple et actionnable** à partir de données simulées, pour montrer ma capacité à :

- Modéliser une problématique métier
- Concevoir une interface utile aux décideurs
- Aller de la donnée brute à la recommandation exploitable

---

## 👤 Réalisé par  
**Samadou KODON**  
🔗 [Portfolio](https://samadkod.github.io/) | [LinkedIn](https://www.linkedin.com/in/skodon)









