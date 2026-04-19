Prompts:
1-"npm run dev — npm error Missing script: dev / python run.py — zsh: command not found:
python / source bin/activate — source: no such file or directory"

2-"sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (2003, Can't connect to
MySQL server on localhost, Connection refused)"

3-"les KPIs affichent 0 0 0 0 mais le badge sidebar affiche 25 alertes et l'API retourne 25
alertes actives, 5 pompes actives, 4 zones critiques. Le Network tab montre 0 requêtes vers
/alertes"

4-"BUG 2 — AdminPanel : page blanche au clic sur toggle utilisateur. Symptôme : Cliquer
sur le bouton vert (activer/désactiver compte) → page devient blanche et reste bloquée"

5-"nom, email et password sont requis — erreur 400 lors de la création d'un utilisateur
depuis AdminPanel"

6-"POST /auth/login HTTP/1.1 401 UNAUTHORIZED — je ne peux pas me connecter avec
admin, la page reste bloquée sur le login sans message d'erreur"

Bugs:

Voici les 6 problèmes principaux rencontrés durant le projet :

**1. Backend ne démarre pas — commande `python` introuvable**
*Problème :* Sur macOS, la commande `python` n'existe pas, seule `python3` fonctionne. Le venv n'était pas encore créé.
*Solution :* Créer le venv avec `python3 -m venv venv`, l'activer et installer les dépendances.

**2. Connexion MySQL refusée — base de données inaccessible**
*Problème :* Le backend retournait une erreur `Can't connect to MySQL server on localhost (Connection refused)`.
*Solution :* XAMPP n'était pas démarré. Lancer MySQL depuis le panneau XAMPP avant de démarrer Flask.

**3. KPIs affichaient 0 malgré des données réelles en base**
*Problème :* Les 4 cartes KPI (Alertes, Pompes, Zones, Pannes) affichaient toutes `0`. L'API retournait pourtant 25 alertes actives. Cause : le hook `useAnimatedCounter` démarrait l'animation avant que les données ne soient chargées, puis ne se mettait plus à jour.
*Solution :* Réécriture complète du hook avec `useRef` pour gérer correctement les animations au premier rendu.

**4. Page blanche lors du clic sur AdminPanel**
*Problème :* Cliquer sur le bouton d'activation/désactivation d'un utilisateur provoquait une page blanche complète.
*Solution :* Deux bugs corrigés — import manquant `CheckCircle` depuis lucide-react, et `showDeleteModal.id` remplacé par `showDeleteModal.user_id`.

**5. Création d'utilisateur impossible — erreur 400**
*Problème :* Le formulaire de création d'utilisateur dans AdminPanel envoyait le champ `mot_de_passe` mais le backend attendait `password`.
*Solution :* Correction de l'appel `createUser` pour envoyer `{ nom, email, password, role }` au lieu de `formData` directement.

**6. Login admin bloqué — page restait sur l'écran de connexion**
*Problème :* L'intercepteur Axios 401 déclenchait un rechargement de page même lors d'une erreur de login, effaçant le message d'erreur et donnant l'impression que rien ne se passait. De plus, `fetchData` dans Dashboard créait une boucle infinie d'appels API.
*Solution :* Modification de l'intercepteur pour ignorer la route `/auth/login`, et stabilisation de `fetchData` en supprimant la dépendance circulaire sur `apiStatus`.
