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
👀 **en 15 secondes, on sait quoi faire** avec chaque produit 

---

## 💡 Pourquoi ce projet ?

La gestion d’un assortiment est **un enjeu stratégique** en grande distribution :  
mal optimiser sa gamme, c’est perdre en CA, en fidélité ou en lisibilité.

J’ai donc voulu créer un **outil concret, simple et actionnable** à partir de données simulées, pour montrer ma capacité à :

- Modéliser une problématique métier
- Concevoir une interface utile aux décideurs
- Aller de la donnée brute à la recommandation exploitable

  
---
## 👤 Projet réalisé par  
**Samadou KODON**  
🔗 [Portfolio](https://samadkod.github.io/) | [LinkedIn](https://www.linkedin.com/in/skodon)


---

## ✅ Recommandations concrètes issues des données

Voici des exemples d’analyses actionnables que l’on peut tirer grâce à cette application :

### 1. Réduire l’assortiment sur les produits peu performants
- Certains produits ont un **faible chiffre d'affaires**, une **marge quasi nulle** et une **forte sensibilité au prix**.
- 🔻 **Action :** les retirer ou réduire leur présence en rayon.
- 🎯 **Objectif :** gagner en lisibilité et rentabilité.

### 2. Optimiser les promotions
- Certains produits sont **trop dépendants des promos**.
- 🧪 **Action :** tester une réduction des remises pour voir si les ventes restent stables.
- 🎯 **Objectif :** dépenser moins en promotion sans perdre de volume.

### 3. Consolider les produits rentables
- Certains produits sont stables, peu sensibles au prix, et très rentables.
- 💎 **Action :** les conserver et bien les mettre en avant.
- 🎯 **Objectif :** sécuriser le chiffre d’affaires et fidéliser les clients.

### 4. Repenser les prix
- Des produits avec un **volume élevé mais une marge faible** peuvent être mal positionnés.
- ⚙️ **Action :** revoir leur prix ou leur positionnement.
- 🎯 **Objectif :** améliorer la marge globale.

### 5. Surveiller les produits "fragiles"
- Marge moyenne, sensibilité fluctuante, performances incertaines.
- 👁️ **Action :** les suivre dans le temps.
- 🎯 **Objectif :** prévenir les pertes ou arbitrer au bon moment.

---

Grâce à cette application, on peut transformer un simple tableau produit en **outil de pilotage stratégique**, accessible à tous.

---
## 📁 Contenu du dépôt

| Fichier                              | Description                                      |
|-------------------------------------|--------------------------------------------------|
| `app_streamlit_assortiment.py`      | Code Python de l’application Streamlit          |
| `dataset_assortiment_fmcg.csv`      | Données simulées – 30 produits, 5 catégories     |
| `requirements.txt`                  | Dépendances pour exécution sur Streamlit Cloud   |
| `README.md`                         | Présentation du projet                           |
