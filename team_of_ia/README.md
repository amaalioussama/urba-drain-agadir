# Urba-Drain Agadir 🌊
> **Plateforme intelligente de gestion et surveillance du réseau de drainage urbain — Agadir, Souss-Massa.**

[![Statut](https://img.shields.io/badge/Statut-Stable-success)]()
[![Stack](https://img.shields.io/badge/Stack-Flask%20%7C%20React%20%7C%20MySQL-blue)]()
[![Équipe](https://img.shields.io/badge/Équipe-Augmenteds-orange)]()
[![Cours](https://img.shields.io/badge/Cours-SIBD%202025--2026-purple)]()

**Urba-Drain Agadir** est une plateforme Smart City avancée conçue pour surveiller, gérer et sécuriser le réseau de drainage des eaux pluviales urbaines d'Agadir. Développé dans le cadre du module SIBD à l'ENSIASD Taroudant, ce système offre une visibilité en temps réel sur l'état du réseau, automatise les réponses d'urgence et permet une gestion efficace des infrastructures hydrauliques.

---

## 🎥 Démo Vidéo

👉 [**Voir la démonstration complète du projet**](https://drive.google.com/file/d/1HP1QkuV06eJoPk_QwjkY2V00aiL1pLlz/view?usp=sharing)

---

## 🌍 Contexte Réel

Ce projet simule un système de contrôle réel du drainage urbain d'Agadir, combinant surveillance en temps réel, réponse automatisée et aide à la décision pour la résilience des infrastructures urbaines de la région Souss-Massa.

---

## 🚀 Fonctionnalités Principales

- **📡 Surveillance en Temps Réel** : Suivi en direct de 12 zones de drainage urbain avec évaluation dynamique des risques.
- **⚠️ Niveaux de Risque Dynamiques** : Catégorisation intelligente : `FAIBLE` | `MOYEN` | `ELEVE` | `CRITIQUE`.
- **⚙️ Gestion des Pompes** : Contrôle centralisé des pompes urbaines avec détection des pannes et notification aux techniciens.
- **📩 Messagerie Interne** : Système de messagerie entre les membres du staff (Admin, Opérateur, Technicien, Lecteur).
- **🛡️ RBAC Sécurisé** : Contrôle d'accès basé sur les rôles via JWT.
- **📈 Tableau de Bord Analytique** : Interface premium avec carte Leaflet, KPIs animés et graphiques Recharts.
- **⛈️ Simulateur Météorologique** : Simulation de scénarios d'orage via procédures stockées MySQL.
- **🔐 Changement de Mot de Passe** : Chaque utilisateur peut modifier son mot de passe depuis le tableau de bord.
- **🔔 Badge API Dynamique** : Indicateur en temps réel de l'état de connexion au backend.

---

## 🏗️ Architecture

La plateforme suit une architecture trois tiers moderne :

- **Frontend** : SPA construite avec **React 18** et **Vite**, utilisant **Leaflet** pour la carte, **Recharts** pour les graphiques et **Lucide React** pour les icônes.
- **Backend** : API REST robuste propulsée par **Flask** (Python), avec **SQLAlchemy** (ORM) et **JWT** pour la gestion sécurisée des sessions.
- **Base de Données** : Schéma **MySQL** relationnel en 3NF avec 10 tables, 3 triggers et 2 procédures stockées.

---

## 🛠️ Guide d'Installation

### 1. Prérequis
- Python 3.8+
- Node.js 18+
- MySQL Server 8.0+ (via XAMPP recommandé)

### 2. Configuration de la Base de Données
```bash
# Créer la base de données
mysql -u root -p -e "CREATE DATABASE urba_drain_agadir CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Importer le schéma
mysql -u root -p urba_drain_agadir < database/schema/01_create_tables.sql

# Charger les données de test
mysql -u root -p urba_drain_agadir < database/seed/01_seed_data.sql

# Charger les triggers
mysql -u root -p urba_drain_agadir < database/triggers/01_trg_activation_pompe.sql
mysql -u root -p urba_drain_agadir < database/triggers/02_trg_creation_alerte.sql
mysql -u root -p urba_drain_agadir < database/triggers/03_trg_log_pompe.sql

# Charger les procédures stockées
mysql -u root -p urba_drain_agadir < database/procedures/01_sp_simuler_cheminement.sql
mysql -u root -p urba_drain_agadir < database/procedures/02_sp_simuler_orage.sql
```

### 3. Configuration du Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Configuration du Frontend
```bash
cd frontend
npm install
```

---

## 🚦 Lancement du Projet

### 1. Backend (API Flask)
```bash
cd backend
source venv/bin/activate
python3 run.py
```
> ✅ Le serveur démarre sur `http://127.0.0.1:5000`

### 2. Frontend (Dashboard React)
```bash
cd frontend
npm run dev
```
> ✅ Ouvrir `http://localhost:3000` dans le navigateur.

---

## 🔐 Accès par Défaut & RBAC

| Rôle | Email | Mot de passe | Accès |
| :--- | :--- | :--- | :--- |
| **Administrateur** | `admin@urba-drain-agadir.ma` | `admin123` | Accès total |
| **Opérateur** | `operateur@urba-drain-agadir.ma` | `admin123` | Zones, Pompes, Alertes |
| **Technicien** | `technicien@urba-drain-agadir.ma` | `admin123` | Zones, Capteurs, Alertes |
| **Lecteur** | `lecteur@urba-drain-agadir.ma` | `admin123` | Vue zones uniquement |

---

## 🧪 Scénario de Test — Démo Complète

1. **Connexion** en tant qu'Administrateur.
2. Aller dans l'onglet **Simulation**.
3. Choisir une zone (ex: Bensergao) et le scénario **Orage fort (70 mm/h)**.
4. Cliquer sur **Lancer l'injection SQL**.
5. Observer :
   - Mise à jour en temps réel des KPIs.
   - Génération automatique d'alertes CRITIQUE via trigger MySQL.
   - Activation automatique des pompes via trigger MySQL.
   - Logs enregistrés dans LOG_ACTIVITE.
6. Aller dans **Alertes** → résoudre une alerte.
7. Aller dans **Messagerie** → envoyer un message au technicien.

---

## 📂 Structure du Projet

```text
team_of_ia/
├── backend/                    # API Flask
│   ├── app/
│   │   ├── models/             # Modèles SQLAlchemy
│   │   ├── routes/             # Blueprints & Endpoints
│   │   └── middleware/         # RBAC & JWT
│   ├── config.py
│   ├── db.py
│   └── run.py
├── frontend/                   # Application React 18
│   ├── src/
│   │   ├── api/                # client.js (Axios)
│   │   ├── components/         # Composants UI
│   │   └── pages/              # Dashboard, Login
│   └── vite.config.js
├── database/                   # Scripts SQL
│   ├── schema/                 # Tables & Contraintes
│   ├── seed/                   # Données de test
│   ├── triggers/               # Triggers MySQL
│   └── procedures/             # Procédures Stockées
└── docs/                       # Documentation (MCD/MLD/QA)
```

---

## 🔮 Perspectives d'Évolution

- **Prévision IA** : Modèles de séries temporelles pour prédire les inondations à l'avance.
- **Expansion IoT** : Support de capteurs hardware (LoRaWAN) pour une surveillance terrain.
- **Application Mobile** : Application Flutter pour les techniciens de terrain.
- **Alertes Citoyens** : Notifications SMS/email automatiques pour les résidents des zones à risque.

---

## 👥 Équipe : Augmenteds — Groupe 2

Projet développé dans le cadre du cours **SIBD 2025-2026** à **ENSIASD Taroudant**, sous la supervision de **Pr. S. EL-ATEIF**.

| Membre | Rôle |
| :--- | :--- |
| **BELAAJIN Abdelaali** | Chef d'équipe · Lead Developer · IA/Frontend |
| **BELHADJ Chadi** | Développeur Backend Flask |
| **BENELMALIH Mohamed** | IA / Modélisation / Frontend |
| **AMAL Oussama** | GitHub Owner · Lecteur |

**Abdelaali Belaajin** — [GitHub](https://github.com/Abdelaali-belaajin)

---

## 📜 Licence

Ce projet est sous licence **MIT**.
