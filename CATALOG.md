# Catalogue BestRepo — dépôts recommandés pour les projets de Thomas

_Généré le 2026-11-23 par scripts/build_data.py — ne pas éditer à la main (modifier scripts/curated.py)._

Format : `owner/repo` (★ étoiles · niveau · type) — à quoi ça sert · **Pour Thomas :** usage · `démarrage`

## 🧠 IA locale & modèles (`ia-locale`)
_Faire tourner des modèles d'IA directement sur ton Mac, sans envoyer de données (idéal pour tout ce qui touche au médical)._

- `ollama/ollama` ⭐ (★188k · facile · app) — Télécharge et fait tourner des LLM (Llama, Qwen, Mistral, Gemma…) en local en une commande. **Pour Thomas :** Anonymiser ou reformuler un CR, résumer un article, sans que rien ne quitte ton Mac. Tes scripts Python peuvent l'appeler comme une API. · `brew install ollama && ollama run qwen3`
- `huggingface/transformers` (★169k · avancé · lib) — La bibliothèque de référence pour utiliser des milliers de modèles pré-entraînés. **Pour Thomas :** Base de tout projet de recherche IA (texte ou image) en Python. · `pip install transformers`
- `langgenius/dify` (★162k · moyen · selfhost) — Plateforme visuelle pour créer des assistants et workflows IA. **Pour Thomas :** Monter un assistant « protocoles du service » sans coder. · `docker compose up -d (voir README)`
- `open-webui/open-webui` ⭐ (★159k · moyen · selfhost) — Une interface type ChatGPT pour tes modèles locaux (Ollama) ou distants, avec documents et recherche. **Pour Thomas :** Ton « ChatGPT privé » : glisser un PDF de recommandations SFR/ESSR et poser des questions dessus en local. · `docker run -d -p 3000:8080 ghcr.io/open-webui/open-webui:main`
- `Comfy-Org/ComfyUI` (★148k · moyen · app) — Génération d'images (Stable Diffusion, Flux…) par nœuds visuels. **Pour Thomas :** Créer les logos illustrés de tes apps du Tapp Store et des visuels de cours. · `Télécharger ComfyUI Desktop (macOS)`
- `ggml-org/llama.cpp` (★136k · avancé · cli) — Le moteur d'inférence LLM en C/C++ optimisé Apple Silicon, à la base de la plupart des outils locaux. **Pour Thomas :** Pour aller plus loin qu'Ollama : quantification, serveur compatible OpenAI ultra léger. · `brew install llama.cpp`
- `Mintplex-Labs/anything-llm` (★69k · facile · app) — App de bureau tout-en-un : discuter avec tes documents (RAG) avec n'importe quel modèle. **Pour Thomas :** Indexer ta biblio Zotero / tes cours et interroger l'ensemble en langage naturel. · `Télécharger l'app macOS sur anythingllm.com`
- `janhq/jan` (★46k · facile · app) — Alternative open-source à ChatGPT qui tourne 100 % hors-ligne. **Pour Thomas :** L'option la plus simple si tu veux une IA locale sans terminal. · `brew install --cask jan`
- `ml-explore/mlx` (★29k · avancé · lib) — Le framework d'Apple pour le machine learning sur puces M1–M4. **Pour Thomas :** Entraîner ou affiner un petit modèle (classification d'images, quiz) en exploitant toute la puissance du Mac. · `pip install mlx mlx-lm`

## 🤖 Agents de code & Claude (`agents`)
_Les outils qui te font gagner le plus de temps pour créer et maintenir tes web-apps (Tapp Store, Cochin RI, quiz…)._

- `obra/superpowers` (★325k · moyen · extension) — Bibliothèque de skills qui imposent une méthode (spec → plan → tests → vérification) aux agents. **Pour Thomas :** Tu l'utilises déjà en partie (skill superpowers) : la source pour les mises à jour. · `/plugin install dans Claude Code`
- `n8n-io/n8n` ⭐ (★212k · moyen · selfhost) — Automatisations visuelles type Zapier, avec nœuds IA, auto-hébergeable. **Pour Thomas :** « Nouveau mail du secrétariat → ligne dans l'Agenda RI → SMS de rappel » sans écrire de code. · `npx n8n`
- `anthropics/claude-code` ⭐ (★157k · moyen · cli) — L'agent de code de Claude dans le terminal : lit, modifie, teste et pousse ton code. **Pour Thomas :** C'est déjà ton moteur via T3 Code. Le dépôt sert pour suivre les nouveautés, plugins et signaler des bugs. · `npm i -g @anthropic-ai/claude-code`
- `x1xhlol/system-prompts-and-models-of-ai-tools` (★145k · facile · liste) — Collection des prompts système des grands outils IA (Cursor, v0, Claude…). **Pour Thomas :** S'inspirer pour écrire de meilleurs prompts pour tes propres assistants. · `Lire sur GitHub`
- `openai/codex` (★136k · moyen · cli) — L'agent de code d'OpenAI dans le terminal. **Pour Thomas :** Idem : utile en relais ou pour comparer les approches (skill council). · `npm i -g @openai/codex`
- `browser-use/browser-use` (★122k · avancé · lib) — Permet à une IA de piloter un vrai navigateur (cliquer, remplir, lire). **Pour Thomas :** Automatiser une tâche web répétitive (récupérer un planning, remplir un formulaire administratif). · `pip install browser-use`
- `google-gemini/gemini-cli` (★109k · moyen · cli) — L'agent en ligne de commande de Google Gemini. **Pour Thomas :** Un deuxième avis ou une alternative quand ton quota Claude est atteint. · `npm i -g @google/gemini-cli`
- `microsoft/playwright` (★101k · avancé · lib) — Automatisation et tests de navigateurs (Chrome, Safari, Firefox). **Pour Thomas :** Tester automatiquement tes web-apps sur un format iPhone avant chaque push. · `npm init playwright@latest`
- `modelcontextprotocol/servers` ⭐ (★92k · moyen · lib) — Les serveurs MCP officiels : brancher Claude sur des fichiers, Git, le web, des bases de données… **Pour Thomas :** Donner à tes agents l'accès à Google Drive, au navigateur ou à une base SQLite de tes projets. · `Voir README de chaque serveur (npx …)`
- `hesreallyhim/awesome-claude-code` (★59k · facile · liste) — La liste communautaire des meilleures commandes, hooks, skills et workflows Claude Code. **Pour Thomas :** Piocher des skills/hooks prêts à l'emploi pour ton écosystème T3. · `Lire sur GitHub`
- `anthropics/claude-cookbooks` (★55k · moyen · liste) — Recettes officielles Anthropic : RAG, outils, vision, extraction structurée… **Pour Thomas :** Copier une recette pour extraire automatiquement des données d'un CR ou d'une capture. · `Lire les notebooks dans le navigateur`

## 🩻 Imagerie médicale & DICOM (`radio`)
_Viewers, segmentation automatique et bibliothèques DICOM — directement utiles pour TPack, l'enseignement et la recherche._

- `MIC-DKFZ/nnUNet` (★9k · avancé · lib) — La méthode de segmentation par deep learning qui gagne la plupart des challenges médicaux. **Pour Thomas :** Projet de recherche : entraîner un modèle de segmentation de tumeurs osseuses sur vos données. · `pip install nnunetv2`
- `Project-MONAI/MONAI` (★9k · avancé · lib) — Framework PyTorch dédié à l'imagerie médicale (chargement DICOM/NIfTI, augmentations, modèles). **Pour Thomas :** La boîte à outils standard si tu montes un projet IA avec un ingénieur ou un interne. · `pip install monai`
- `bowang-lab/MedSAM` (★4k · avancé · lib) — « Segment Anything » adapté à l'imagerie médicale : segmenter en dessinant une boîte. **Pour Thomas :** Segmentation semi-auto rapide pour illustrer un cours ou mesurer une lésion. · `Voir README`
- `OHIF/Viewers` ⭐ (★4k · moyen · app) — Viewer DICOM web de référence (zéro installation côté utilisateur), MPR, mesures, segmentation. **Pour Thomas :** Base idéale pour faire évoluer TPack / dicomviewer : afficher des cas anonymisés dans le navigateur pour les internes. · `Démo : viewer.ohif.org`
- `wasserth/TotalSegmentator` ⭐ (★3k · moyen · cli) — Segmente automatiquement 100+ structures (os, muscles, organes) sur TDM et IRM. **Pour Thomas :** Volumétrie musculaire, planification de voies d'abord, reconstructions 3D pour l'enseignement — en une commande. · `pip install TotalSegmentator`
- `Slicer/Slicer` (★3k · moyen · app) — Logiciel gratuit d'analyse d'images médicales : segmentation, 3D, recalage, impression 3D. **Pour Thomas :** Préparer un modèle 3D d'une lésion osseuse pour une RCP ou planifier une cimentoplastie. · `Télécharger sur slicer.org`
- `pydicom/pydicom` (★2k · avancé · lib) — Lire, modifier et écrire des fichiers DICOM en Python. **Pour Thomas :** Anonymiser des séries (supprimer nom/IPP/date) avant de créer un .tpack — script de 20 lignes. · `pip install pydicom`
- `InsightSoftwareConsortium/ITK` (★2k · avancé · lib) — Boîte à outils historique de traitement d'images médicales (filtres, recalage). **Pour Thomas :** Recaler deux examens (avant / après RF) pour comparer précisément. · `pip install itk`
- `nroduit/Weasis` (★1k · facile · app) — Viewer DICOM de bureau gratuit, rapide, multiplateforme. **Pour Thomas :** Ouvrir un CD patient ou un export sur ton Mac perso sans OsiriX payant. · `Télécharger sur weasis.org`
- `cornerstonejs/cornerstone3D` (★1k · avancé · lib) — La bibliothèque JavaScript qui fait le rendu DICOM 2D/3D (utilisée par OHIF). **Pour Thomas :** Intégrer un vrai viewer (fenêtrage, scroll, MPR) dans tes quiz Cochin MSK. · `npm i @cornerstonejs/core`
- `horosproject/horos` (★651 · facile · app) — Viewer DICOM gratuit pour macOS (dérivé d'OsiriX). **Pour Thomas :** Alternative familière à OsiriX pour revoir des cas d'enseignement. · `Télécharger sur horosproject.org`
- `jodogne/OrthancMirror` (★44 · moyen · selfhost) — Mini-PACS léger avec API REST. **Pour Thomas :** Un PACS d'enseignement perso pour stocker tes cas anonymisés et les servir à OHIF. · `brew install --cask orthanc (ou Docker)`

## 📚 Recherche, biblio & Second Brain (`savoir`)
_Gérer articles, PDF et notes : BiblioOstéo, Zotero, Obsidian, extraction de texte des PDF._

- `microsoft/markitdown` (★198k · moyen · cli) — Convertit presque tout (PDF, Office, images, audio) en Markdown pour les LLM. **Pour Thomas :** Préparer des documents pour les donner à Claude en contexte. · `pip install 'markitdown[all]'`
- `Stirling-Tools/Stirling-PDF` (★97k · moyen · selfhost) — Toutes les opérations PDF (fusion, découpe, OCR, signature, compression) en local. **Pour Thomas :** Remplace iLovePDF sans envoyer de documents sensibles sur Internet. · `docker run -p 8080:8080 stirlingtools/stirling-pdf`
- `docling-project/docling` ⭐ (★71k · moyen · lib) — Convertit PDF/Word/PPT en Markdown propre (tableaux, figures, formules). **Pour Thomas :** Transformer des articles ou anciens cours PowerPoint en notes Obsidian exploitables. · `pip install docling`
- `paperless-ngx/paperless-ngx` (★49k · moyen · selfhost) — Gestion documentaire : scan, OCR, tags automatiques, recherche. **Pour Thomas :** Une version auto-hébergée de ton coffre-fort de documents (impôts, contrats, fiches de paie). · `Docker (script d'installation dans le README)`
- `logseq/logseq` (★46k · facile · app) — Prise de notes en blocs reliés, open-source, local. **Pour Thomas :** Alternative à Obsidian pour un journal quotidien de vacation. · `brew install --cask logseq`
- `datalab-to/marker` (★41k · moyen · cli) — PDF → Markdown très fidèle, rapide, avec OCR. **Pour Thomas :** Numériser des livres ou polycopiés scannés de radiologie. · `pip install marker-pdf`
- `khoj-ai/khoj` (★38k · moyen · selfhost) — Assistant IA personnel qui cherche dans tes notes et documents. **Pour Thomas :** Interroger ton Second Brain Obsidian en langage naturel. · `pip install 'khoj[local]'`
- `ocrmypdf/OCRmyPDF` (★35k · moyen · cli) — Ajoute une couche de texte cherchable aux PDF scannés. **Pour Thomas :** Rendre cherchables les 774 documents de ton coffre-fort. · `brew install ocrmypdf`
- `zotero/zotero` (★16k · facile · app) — Le gestionnaire de références open-source. **Pour Thomas :** Cœur de BiblioOstéo / BiblioMarie. Le dépôt sert à suivre les nouveautés (Zotero 7+). · `brew install --cask zotero`
- `blacksmithgu/obsidian-dataview` ⭐ (★9k · facile · extension) — Plugin Obsidian : requêtes sur tes notes comme une base de données. **Pour Thomas :** Tableau auto dans ton Second Brain : « toutes les fiches RI avec statut = à relire », « cas RCP de 2026 ». · `Obsidian → Plugins communautaires → Dataview`
- `retorquere/zotero-better-bibtex` (★7k · facile · extension) — Extension Zotero : clés de citation stables et export automatique. **Pour Thomas :** Exporter ta biblio en continu vers un fichier lu par tes scripts / Obsidian. · `Installer le .xpi depuis les Releases`

## 🌐 Créer des web-apps & PWA (`web`)
_Les briques pour des apps mobiles rapides, belles et hors-ligne sur GitHub Pages._

- `shadcn-ui/ui` (★129k · avancé · lib) — Composants d'interface élégants à copier dans ton projet. **Pour Thomas :** Des écrans pro (tableaux, formulaires, dialogues) pour tes apps React. · `npx shadcn@latest init`
- `mrdoob/three.js` (★119k · avancé · lib) — 3D dans le navigateur (WebGL/WebGPU). **Pour Thomas :** Monopoly 3D, ou un modèle 3D d'articulation manipulable pour l'enseignement. · `npm i three`
- `supabase/supabase` (★115k · avancé · selfhost) — Alternative open-source à Firebase (Postgres, auth, stockage). **Pour Thomas :** Synchroniser des données entre iPhone et Mac (AssMat, Agenda Famille) ou rendre une app multi-utilisateurs (internes de Radio B). · `Version cloud gratuite ou Docker`
- `tailwindlabs/tailwindcss` ⭐ (★99k · moyen · lib) — CSS utilitaire : des interfaces propres et responsives très vite. **Pour Thomas :** Uniformiser le style de toutes tes apps du Tapp Store. · `npm i tailwindcss`
- `sveltejs/svelte` (★90k · avancé · lib) — Framework web compilé, léger et agréable à écrire. **Pour Thomas :** Pour une app plus ambitieuse (Agenda RI) avec beaucoup d'états. · `npx sv create mon-app`
- `vitejs/vite` (★84k · moyen · cli) — L'outil de build/serveur de dev le plus rapide pour le web moderne. **Pour Thomas :** Démarrer une nouvelle web-app en 10 secondes avec rechargement instantané. · `npm create vite@latest`
- `chartjs/Chart.js` (★68k · moyen · lib) — Graphiques simples et jolis en JavaScript. **Pour Thomas :** Statistiques d'activité RI, suivi des dépenses, scores des quiz. · `<script src="https://cdn.jsdelivr.net/npm/chart.js">`
- `bigskysoftware/htmx` (★50k · moyen · lib) — Rendre une page dynamique avec de simples attributs HTML. **Pour Thomas :** Interfaces réactives sans framework lourd, si un jour tu as un petit serveur. · `<script src="https://unpkg.com/htmx.org">`
- `Leaflet/Leaflet` (★46k · moyen · lib) — Cartes interactives légères. **Pour Thomas :** Carte des restos (Resto en Amoureux), des voyages ou des annonces d'appartement. · `npm i leaflet`
- `alpinejs/alpine` (★32k · moyen · lib) — Interactivité légère directement dans le HTML, sans build. **Pour Thomas :** Parfait pour tes PWA statiques GitHub Pages : filtres, onglets, modales en quelques attributs. · `<script src="https://cdn.jsdelivr.net/npm/alpinejs" defer>`
- `lucide-icons/lucide` (★26k · facile · lib) — 1 500+ icônes SVG propres et cohérentes. **Pour Thomas :** Icônes homogènes pour toutes tes apps (au lieu d'emojis). · `<script src="https://unpkg.com/lucide">`
- `GoogleChrome/workbox` (★13k · avancé · lib) — Service workers clé en main pour le mode hors-ligne et le cache. **Pour Thomas :** Rendre tes PWA fiables hors-ligne… sans les soucis de cache qui bloquent les mises à jour. · `npm i workbox-window`

## 🏠 Auto-hébergement & maison (`selfhost`)
_Remplacer des services payants par les tiens, sur le Mac ou un mini-serveur : photos, films, domotique, automatisations._

- `immich-app/immich` ⭐ (★120k · moyen · selfhost) — Alternative auto-hébergée à Google Photos : sauvegarde iPhone, reconnaissance faciale, recherche IA. **Pour Thomas :** Héberger les photos de famille (Émile !) sur le GamingSSD avec l'app iPhone, après ton export Google Takeout. · `docker compose (guide officiel immich.app)`
- `louislam/uptime-kuma` (★95k · moyen · selfhost) — Surveille que tes sites/services répondent et t'alerte sinon. **Pour Thomas :** Être prévenu si une de tes apps GitHub Pages ou ton tunnel tombe. · `docker run -d -p 3001:3001 louislam/uptime-kuma`
- `home-assistant/core` (★93k · moyen · selfhost) — La plateforme domotique open-source de référence. **Pour Thomas :** Piloter lumières, chauffage, ESP32 Xiaozhi, et créer des routines (coucher d'Émile, départ au travail). · `Home Assistant OS sur mini-PC ou Raspberry Pi`
- `syncthing/syncthing` (★91k · facile · app) — Synchronisation de fichiers pair-à-pair, sans cloud. **Pour Thomas :** Garder ton Second Brain synchronisé entre plusieurs Mac sans iCloud. · `brew install --cask syncthing`
- `pi-hole/pi-hole` (★62k · moyen · selfhost) — Bloqueur de pubs et traqueurs pour tout le réseau de la maison. **Pour Thomas :** Moins de pubs sur la TV, l'iPad d'Émile et tous les téléphones. · `Sur Raspberry Pi : curl -sSL https://install.pi-hole.net | bash`
- `jellyfin/jellyfin` (★60k · moyen · selfhost) — Ton Netflix perso pour films et séries stockés chez toi. **Pour Thomas :** Regarder ta médiathèque du SSD sur la télé, l'iPad ou en voyage. · `brew install --cask jellyfin`
- `tailscale/tailscale` ⭐ (★40k · facile · app) — VPN privé sans configuration entre tous tes appareils. **Pour Thomas :** Accéder à ton Mac (et au tunnel Mon Drive) depuis l'iPhone n'importe où, de façon sécurisée. · `brew install --cask tailscale`
- `gethomepage/homepage` (★34k · moyen · selfhost) — Tableau de bord élégant pour tous tes services. **Pour Thomas :** Page d'accueil maison regroupant Immich, Jellyfin, Home Assistant… · `Docker`
- `78/xiaozhi-esp32` (★34k · avancé · lib) — Assistant vocal IA open-source sur ESP32. **Pour Thomas :** Le projet amont de ton Xiaozhi ESP32-S3 AMOLED : nouveautés et firmwares. · `Voir README (ESP-IDF)`
- `FreshRSS/FreshRSS` (★17k · moyen · selfhost) — Lecteur de flux RSS auto-hébergé. **Pour Thomas :** Suivre les sommaires de Radiology, Skeletal Radiology, EJR et les blogs IA au même endroit. · `Docker`
- `esphome/esphome` (★12k · moyen · cli) — Programmer des ESP32/ESP8266 en YAML, sans coder en C. **Pour Thomas :** Capteurs maison (température chambre d'Émile) intégrés à Home Assistant. · `pip install esphome`

## 🍎 Mac & terminal (`mac`)
_Petites apps et outils en ligne de commande qui rendent le Mac nettement plus agréable._

- `ohmyzsh/ohmyzsh` (★191k · moyen · cli) — Configuration zsh avec plugins et thèmes. **Pour Thomas :** Autocomplétion et raccourcis Git pour ton terminal. · `Voir README (une ligne curl)`
- `localsend/localsend` (★100k · facile · app) — AirDrop open-source entre Mac, iPhone, Android et Windows. **Pour Thomas :** Envoyer un fichier à un PC de l'hôpital ou au téléphone Android d'un proche. · `brew install --cask localsend`
- `junegunn/fzf` (★84k · moyen · cli) — Recherche floue interactive dans le terminal. **Pour Thomas :** Retrouver instantanément un fichier ou une commande passée. · `brew install fzf`
- `jesseduffield/lazygit` (★84k · moyen · cli) — Interface Git visuelle dans le terminal. **Pour Thomas :** Voir et annuler facilement ce que les agents ont modifié dans tes dépôts. · `brew install lazygit`
- `BurntSushi/ripgrep` (★70k · moyen · cli) — Recherche de texte ultra-rapide dans des milliers de fichiers. **Pour Thomas :** Chercher un mot dans tout ton Second Brain ou tes 32 projets en une fraction de seconde. · `brew install ripgrep`
- `starship/starship` (★61k · moyen · cli) — Invite de terminal belle et informative. **Pour Thomas :** Voir d'un coup d'œil le projet et la branche Git courants. · `brew install starship`
- `Homebrew/brew` ⭐ (★50k · facile · cli) — Le gestionnaire de paquets du Mac : installer n'importe quel outil en une commande. **Pour Thomas :** La base pour installer la moitié des outils de cette page. · `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- `exelban/stats` (★44k · facile · app) — CPU, RAM, température, réseau dans la barre de menus. **Pour Thomas :** Voir si un modèle IA local ou un export photo sature le Mac. · `brew install --cask stats`
- `ajeetdsouza/zoxide` (★41k · moyen · cli) — « cd » intelligent qui retient tes dossiers fréquents. **Pour Thomas :** Taper « z biblio » pour sauter dans biblioosteo. · `brew install zoxide`
- `MonitorControl/MonitorControl` (★35k · facile · app) — Régler luminosité/volume d'un écran externe avec les touches du Mac. **Pour Thomas :** Pratique avec un second écran de lecture. · `brew install --cask monitorcontrol`
- `rxhanson/Rectangle` (★30k · facile · app) — Ranger les fenêtres au clavier (moitié, tiers, plein écran). **Pour Thomas :** Article à gauche, note Obsidian à droite, en un raccourci. · `brew install --cask rectangle`
- `jordanbaird/Ice` (★30k · facile · app) — Cacher et organiser les icônes de la barre de menus. **Pour Thomas :** Une barre de menus propre malgré tous tes outils. · `brew install --cask jordanbaird-ice`
- `p0deje/Maccy` (★22k · facile · app) — Historique du presse-papiers léger. **Pour Thomas :** Retrouver un texte d'arrêt d'anticoagulant ou un CR-type copié il y a une heure. · `brew install --cask maccy`

## 🎬 Photo, vidéo & audio (`medias`)
_Traiter photos de famille, vidéos, transcrire des cours ou des dictées._

- `yt-dlp/yt-dlp` (★210k · moyen · cli) — Télécharge vidéos et audio de milliers de sites. **Pour Thomas :** Garder hors-ligne un webinaire ou une vidéo de technique interventionnelle pour un cours. · `brew install yt-dlp`
- `openai/whisper` (★113k · moyen · lib) — Le modèle de reconnaissance vocale multilingue d'OpenAI. **Pour Thomas :** Version Python, pratique dans un script de traitement par lot. · `pip install openai-whisper`
- `obsproject/obs-studio` (★80k · facile · app) — Enregistrement d'écran et streaming professionnel. **Pour Thomas :** Enregistrer un cours ou une démonstration de tes apps pour les internes. · `brew install --cask obs`
- `FFmpeg/FFmpeg` (★68k · moyen · cli) — Le couteau suisse audio/vidéo : convertir, couper, compresser. **Pour Thomas :** Transformer une ciné-IRM en MP4/GIF pour une présentation. · `brew install ffmpeg`
- `ggml-org/whisper.cpp` ⭐ (★55k · moyen · cli) — Transcription vocale Whisper ultra-rapide en local sur Apple Silicon. **Pour Thomas :** Transcrire un staff, un cours enregistré ou une dictée de CR sans service en ligne. · `brew install whisper-cpp`
- `upscayl/upscayl` (★53k · facile · app) — Agrandit et améliore les images par IA, en local. **Pour Thomas :** Redonner de la netteté à de vieilles photos de famille ou à une capture basse définition. · `brew install --cask upscayl`
- `iina/iina` (★47k · facile · app) — Lecteur vidéo moderne pour macOS. **Pour Thomas :** Lit tout (MKV, sous-titres…) avec une interface native. · `brew install --cask iina`
- `photoprism/photoprism` (★40k · moyen · selfhost) — Gestion de photos auto-hébergée avec IA (alternative à Immich). **Pour Thomas :** Parcourir et classer les archives Google Takeout par lieux et visages. · `Docker`
- `danielgatis/rembg` (★26k · moyen · cli) — Supprime l'arrière-plan d'une image automatiquement. **Pour Thomas :** Détourer des objets pour les logos et visuels de tes apps. · `pip install 'rembg[cli]'`
- `HandBrake/HandBrake` (★25k · facile · app) — Conversion et compression vidéo simple. **Pour Thomas :** Réduire la taille des vidéos d'Émile avant de les partager. · `brew install --cask handbrake`

## 🎮 Jeux, émulation & création (`jeux`)
_Rétro-gaming à la manette 8BitDo, streaming de jeux, et moteurs pour créer tes propres jeux familiaux._

- `godotengine/godot` ⭐ (★121k · moyen · app) — Moteur de jeu 2D/3D gratuit et léger. **Pour Thomas :** Créer un vrai jeu familial (DinoCiel, Forestia) exportable sur iPhone et le web. · `brew install --cask godot`
- `SunshineStream/Sunshine` (★44k · moyen · app) — Le serveur de streaming de jeux à installer sur le PC (pour Moonlight). **Pour Thomas :** Côté PC, pour streamer vers tous tes écrans. · `Télécharger dans les Releases`
- `phaserjs/phaser` (★41k · avancé · lib) — Framework de jeux 2D HTML5. **Pour Thomas :** Jeux web jouables directement depuis le Tapp Store / Mapp Store. · `npm create @phaserjs/game@latest`
- `moonlight-stream/moonlight-qt` (★20k · facile · app) — Streaming de jeux depuis un PC vers Mac, iPad, TV. **Pour Thomas :** Jouer aux jeux du PC gaming sur la télé ou l'iPad. · `brew install --cask moonlight`
- `OpenEmu/OpenEmu` (★18k · facile · app) — Émulation rétro « à la Apple », très simple sur macOS. **Pour Thomas :** L'option la plus simple pour Marie : glisser un jeu, brancher la manette, jouer. · `brew install --cask openemu`
- `dolphin-emu/dolphin` (★16k · facile · app) — Émulateur GameCube et Wii. **Pour Thomas :** Mario Kart Double Dash / Wii Sports en famille sur le Mac. · `brew install --cask dolphin`
- `libretro/RetroArch` ⭐ (★15k · facile · app) — Front-end d'émulation multi-consoles, compatible toutes manettes. **Pour Thomas :** Toutes tes consoles rétro dans une app, manette 8BitDo reconnue, sauvegardes instantanées. · `brew install --cask retroarch`
- `N64Recomp/N64Recomp` (★8k · avancé · cli) — Recompile des jeux N64 en applications natives modernes. **Pour Thomas :** La technologie derrière les « Recomp » natifs que tu lances déjà. · `Voir README`
- `PokeAPI/pokeapi` (★5k · moyen · lib) — API ouverte avec toutes les données Pokémon. **Pour Thomas :** Source de données pour PokéQuiz et milTCG. · `https://pokeapi.co/api/v2/pokemon/pikachu`
- `mmatyas/pegasus-frontend` (★2k · moyen · app) — Interface « console de salon » personnalisable pour lancer tous tes jeux. **Pour Thomas :** Un menu plein écran joli, pilotable à la manette, pour toute la famille. · `Télécharger sur pegasus-frontend.org`

## 🔐 Sécurité & vie privée (`securite`)
_Mots de passe, chiffrement, blocage des pubs et des traqueurs, éviter de pousser un secret sur GitHub._

- `gorhill/uBlock` ⭐ (★70k · facile · extension) — Le bloqueur de pubs et traqueurs le plus efficace et léger. **Pour Thomas :** Navigation plus rapide et plus sûre sur tous tes navigateurs. · `Extension Firefox / Chrome (uBlock Origin Lite)`
- `StevenBlack/hosts` (★32k · moyen · liste) — Liste consolidée de domaines de pub/malware à bloquer. **Pour Thomas :** Alimenter Pi-hole ou le fichier hosts du Mac. · `Voir README`
- `gitleaks/gitleaks` ⭐ (★31k · moyen · cli) — Détecte les mots de passe et clés API commis par erreur dans Git. **Pour Thomas :** Vérifier qu'aucun secret ni donnée patient n'est poussé dans tes dépôts publics GitHub Pages. · `brew install gitleaks && gitleaks detect`
- `keepassxreboot/keepassxc` (★30k · facile · app) — Gestionnaire de mots de passe 100 % local. **Pour Thomas :** Coffre chiffré hors-ligne de secours. · `brew install --cask keepassxc`
- `trufflesecurity/trufflehog` (★30k · moyen · cli) — Cherche les secrets exposés dans tout l'historique Git. **Pour Thomas :** Audit complet de tes 50+ dépôts. · `brew install trufflehog`
- `FiloSottile/age` (★24k · moyen · cli) — Chiffrement de fichiers simple et moderne. **Pour Thomas :** Chiffrer un export sensible avant de le mettre sur le Drive. · `brew install age`
- `cryptomator/cryptomator` (★17k · facile · app) — Coffre chiffré transparent par-dessus n'importe quel cloud. **Pour Thomas :** Dossier chiffré sur Google Drive pour les documents importants. · `brew install --cask cryptomator`
- `bitwarden/clients` (★14k · facile · app) — Gestionnaire de mots de passe open-source, synchronisé partout. **Pour Thomas :** Partager les mots de passe du foyer avec Marie (complément de t3-vault). · `brew install --cask bitwarden`
- `objective-see/LuLu` (★14k · facile · app) — Pare-feu macOS qui montre quelles apps se connectent à Internet. **Pour Thomas :** Savoir qui « appelle la maison » depuis ton Mac. · `brew install --cask lulu`

## 💶 Finances personnelles (`finance`)
_Budgets et patrimoine (banque, crypto, investissements) en gardant tes données chez toi._

- `actualbudget/actual` ⭐ (★30k · moyen · selfhost) — Budget par enveloppes, local-first, rapide. **Pour Thomas :** Budget du foyer partagé avec Marie (dépenses, nounou, vacances). · `npx @actual-app/sync-server (ou Docker)`
- `firefly-iii/firefly-iii` (★25k · moyen · selfhost) — Gestion financière personnelle complète (comptes, règles, rapports). **Pour Thomas :** Importer les relevés Crédit Mutuel et catégoriser automatiquement. · `Docker`
- `ghostfolio/ghostfolio` (★10k · moyen · selfhost) — Suivi de patrimoine et d'investissements (actions, ETF, crypto). **Pour Thomas :** Complément de PatrimoineOS : performance globale et répartition. · `Docker`
- `rotki/rotki` (★4k · facile · app) — Suivi crypto privé et local, avec rapports fiscaux. **Pour Thomas :** Suivre Ledger/MetaMask sans donner tes adresses à un service tiers. · `Télécharger dans les Releases`

## 🎓 Apprendre & listes de référence (`apprendre`)
_Les « awesome lists » et cours gratuits les plus étoilés de GitHub — des mines d'or à parcourir._

- `sindresorhus/awesome` ⭐ (★541k · facile · liste) — La liste des listes « awesome » : le meilleur de chaque sujet. **Pour Thomas :** Point de départ pour explorer n'importe quel domaine (macOS, self-hosted, médical…). · `Lire sur GitHub`
- `public-apis/public-apis` (★501k · facile · liste) — Des centaines d'API gratuites (météo, transports, jours fériés…). **Pour Thomas :** Trouver une source de données pour une nouvelle app (météo pour Voyages-Voyages, jours fériés pour les plannings). · `Lire sur GitHub`
- `EbookFoundation/free-programming-books` (★402k · facile · liste) — Des milliers de livres de programmation gratuits, dont en français. **Pour Thomas :** Apprendre Python ou JavaScript à ton rythme. · `Lire sur GitHub`
- `nilbuild/developer-roadmap` (★373k · facile · liste) — Feuilles de route visuelles pour apprendre le dev (frontend, IA, DevOps…). **Pour Thomas :** Savoir quoi apprendre ensuite pour progresser sur tes apps. · `roadmap.sh`
- `awesome-selfhosted/awesome-selfhosted` (★340k · facile · liste) — Le catalogue de tous les logiciels auto-hébergeables. **Pour Thomas :** Avant de payer un abonnement, vérifier s'il existe une alternative gratuite. · `Lire sur GitHub`
- `microsoft/generative-ai-for-beginners` (★124k · moyen · liste) — 21 leçons gratuites sur l'IA générative. **Pour Thomas :** Base solide pour un cours IA aux internes. · `Lire sur GitHub`
- `rasbt/LLMs-from-scratch` (★109k · avancé · liste) — Livre/cours pour comprendre et construire un LLM étape par étape. **Pour Thomas :** Comprendre vraiment comment marchent les IA que tu utilises tous les jours. · `Notebooks Jupyter`
- `dair-ai/Prompt-Engineering-Guide` (★80k · facile · liste) — Guide complet du prompt engineering. **Pour Thomas :** Mieux formuler tes demandes aux agents. · `promptingguide.ai`
- `karpathy/nanoGPT` (★65k · avancé · lib) — Le plus petit code complet pour entraîner un GPT. **Pour Thomas :** Expérimenter l'entraînement d'un modèle sur ton Mac pour comprendre. · `git clone`
- `kakoni/awesome-healthcare` (★4k · facile · liste) — Logiciels et ressources open-source pour la santé. **Pour Thomas :** Veille sur les outils médicaux open-source (dossiers, imagerie, interopérabilité). · `Lire sur GitHub`
