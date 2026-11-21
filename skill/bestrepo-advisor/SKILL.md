---
name: bestrepo-advisor
description: Conseiller de dépôts GitHub de Thomas (catalogue BestRepo, 122 dépôts très étoilés classés par intérêt avec usages concrets). Utiliser dès que Thomas conçoit, planifie ou démarre un projet, une nouvelle app/web-app/PWA, un script, une automatisation, un outil de recherche/imagerie/DICOM, un jeu, un service auto-hébergé, ou ajoute une fonctionnalité notable — pour lui proposer les dépôts open-source pertinents AVANT de tout coder à la main. Ne pas utiliser pour un petit correctif.
---

# Conseiller BestRepo — proposer les bons dépôts au moment de concevoir

Thomas veut que, **quand il conçoit un projet**, l'agent lui propose spontanément les dépôts GitHub
pertinents de sa sélection BestRepo (https://mrthomaslef.github.io/bestrepo/) plutôt que de réinventer la roue.

## Quand

- Nouveau projet, nouvelle app/PWA, refonte, script ou automatisation, fonctionnalité qui touche
  un domaine couvert (IA locale, agents, DICOM/imagerie, notes/biblio/PDF, web, auto-hébergement,
  Mac/terminal, médias, jeux, sécurité, finances, apprentissage).
- **Pas** pour un petit correctif, une question factuelle, ou si Thomas a déjà choisi sa pile.
- Une seule proposition par projet/conception : ne pas répéter à chaque message.

## Comment

1. Lire le catalogue (uniquement la ou les sections utiles) :
   `/Users/thomaslefevre/.t3/projects/bestrepo/CATALOG.md`
   (sections `## … (\`id\`)` : ia-locale, agents, radio, savoir, web, selfhost, mac, medias, jeux,
   securite, finance, apprendre). Recherche rapide : `rg -i "<mot-clé>" .../bestrepo/CATALOG.md`.
2. Retenir **2 à 5 dépôts vraiment pertinents** pour le besoin exprimé (pas de liste fourre-tout).
   Privilégier : ⭐ coups de cœur, niveau compatible (statique GitHub Pages → bibliothèques CDN légères,
   pas de serveur), hors-ligne / local pour tout ce qui est médical ou privé.
3. Les présenter **en tête de plan, avant de coder**, au format court :

   > **📦 Dépôts BestRepo utiles pour ce projet**
   > - **`owner/repo`** (★ 188k · 🟢 facile) — ce que ça apporte *ici*, en une ligne.
   > - …
   > Je pars avec X et Y, ou tu préfères que je code sans ?

   Si Thomas est absent / mode autonome : choisir soi-même la meilleure option, l'indiquer en une ligne,
   et continuer sans bloquer.
4. Si un besoin n'est couvert par **aucun** dépôt du catalogue mais qu'un dépôt très connu s'impose,
   le proposer aussi en le signalant « (hors catalogue) », puis suggérer de l'ajouter à
   `/Users/thomaslefevre/.t3/projects/bestrepo/scripts/curated.py`.

## Garde-fous

- Ne jamais présenter un dépôt marqué ⚠️archivé comme premier choix.
- Données patients : ne proposer que des outils locaux (aucun service cloud) — anonymisation absolue.
- Aucune installation (brew, pip, docker…) sans l'accord de Thomas, sauf bibliothèque JS chargée
  dans le code du projet lui-même.
- Le catalogue est rafraîchi chaque lundi sur GitHub ; pour la copie locale :
  `git -C /Users/thomaslefevre/.t3/projects/bestrepo pull -q` si besoin de chiffres à jour.
