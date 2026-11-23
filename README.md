# BTS MEC – site de la classe

Consignes, outils, tutoriels et fichiers des TP de la classe de BTS Management économique de la construction.

| Dossier / fichier | Contenu |
|---|---|
| `index.html` | Accueil de la classe |
| `quantitatif-ifc/` | TP « Réaliser un quantitatif à partir d'un IFC » (Étude n°4) |
| `quantitatif-ifc/tuto.html` | Tuto découverte + attestation PDF |
| `quantitatif-ifc/consigne.html` | Consigne en version web |
| `quantitatif-ifc/outil.html` | Outil LKBIM Métré IFC (`outil.html?ifc=…` charge la maquette du TP en un clic) |
| `quantitatif-ifc/fichiers/` | Maquette IFC (+ .zip) et sujet PDF |
| `assets/` | Style et script communs |

## Modifier le site
1. Modifier les données en tête de `build.py` (textes, déroulé, lien de dépôt `LIENS["depot"]`).
2. Lancer `python3 build.py`, puis publier (commit + push sur `main`).

## Publication
Settings → Pages → branche `main`, dossier `/ (root)`.

⚠ Dépôt public : ne jamais y placer de corrigé ni de grille de notation.
