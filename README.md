# 🧮 Calculateur d'IMC avec Streamlit

Bienvenue dans cette mini-application développée avec [Streamlit](https://streamlit.io/) permettant de calculer l'Indice de Masse Corporelle (IMC) à partir du poids et de la taille de l'utilisateur.

---

## 🚀 Fonctionnalités

- Entrée du **poids** en kilogrammes (Kg)  
- Entrée de la **taille** dans trois formats :
  - centimètres (cm)
  - mètres (m)
  - pieds (feet)
- Calcul de l’**IMC** et affichage du résultat
- Interprétation personnalisée selon les recommandations de l’OMS
- Thème personnalisé :
  - Fond **bleu nuit**
  - Champs et boutons en **couleurs claires** pour une meilleure lisibilité

---

## 🔧 Installation

Assurez-vous d’avoir **Python** installé, puis installez les dépendances :

```bash
pip install streamlit
▶️ Lancer l'application
Dans le terminal, à la racine du projet (où se trouve app.py), exécutez :

bash
streamlit run app.py
L'application s’ouvrira automatiquement dans votre navigateur.

📂 Structure du projet
bash
.
├── app.py          # Code source de l'application
├── .streamlit/
│   └── config.toml # Fichier de personnalisation du thème
└── README.md       # Ce fichier
🎨 Personnalisation
Le thème sombre est configuré via .streamlit/config.toml. Il définit :

La couleur de fond

La couleur des boutons

Les couleurs des champs de saisie

Exemple de configuration :
[theme]
base="dark"
primaryColor="#FFFFFF"
backgroundColor="#0B1A2C"
secondaryBackgroundColor="#102840"
textColor="#FAFAFA"
📏 À propos de l'IMC
L’IMC est un indicateur simple du poids par rapport à la taille, utilisé pour évaluer les risques liés au surpoids ou à la maigreur. Voici les catégories d’interprétation intégrées :

🚨 Moins de 16 : Extrême maigreur

⚠️ 16 - 18.5 : Maigreur

✅ 18.5 - 25 : Corpulence normale

⚠️ 25 - 30 : Surpoids

🚨 Plus de 30 : Obésité

📬 Contact
Développé par Cheikh Niang
Tu peux me retrouver sur LinkedIn ou sur GitHub

📄 Licence
Ce projet est open source .
