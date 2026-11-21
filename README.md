<img src="assets/icon.svg" width="64" height="64" alt="">

# BestRepo

Les dépôts GitHub les plus étoilés, classés par centre d'intérêt (IA locale, agents, imagerie médicale/DICOM, Second Brain, web-apps, auto-hébergement, Mac, médias, jeux, sécurité, finances, apprentissage), avec pour chacun **à quoi ça sert**, **comment l'utiliser concrètement** et la commande pour démarrer.

👉 https://mrthomaslef.github.io/bestrepo/

## Mettre à jour

- Ajouter/modifier un dépôt : `scripts/curated.py`
- Régénérer les données (étoiles, activité) : `python3 scripts/build_data.py`
- Actualisation automatique chaque lundi via GitHub Actions.

## Pour les agents IA

- `CATALOG.md` : catalogue compact (régénéré avec les données) lu par les agents.
- `skill/bestrepo-advisor/` : skill qui fait proposer 2 à 5 dépôts pertinents quand Thomas conçoit un projet
  (lié par symlink dans `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`).
