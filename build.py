# -*- coding: utf-8 -*-
"""Site de la classe BTS MEC.

    python3 build.py

Génère :
  index.html                   accueil de la classe (projets)
  quantitatif-ifc/index.html   TP « Réaliser un quantitatif à partir d'un IFC » (Étude n°4)
  quantitatif-ifc/consigne.html  le sujet en version web

Fichiers fournis tels quels (ne pas générer) :
  quantitatif-ifc/outil.html   outil de métré LKBIM Métré IFC
  quantitatif-ifc/tuto.html    tutoriel découverte + attestation
  quantitatif-ifc/fichiers/    maquette IFC (+ .zip) et sujet PDF

Pour modifier un contenu : changer les données ci-dessous, puis relancer le script.
"""
import os, html, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
e = html.escape

# =====================================================================
# LIENS — coller ici les liens externes (laisser "" si pas prêt)
# =====================================================================
LIENS = {
    "depot": "",   # dossier / espace de dépôt des rendus (Classroom, Moodle, Drive…)
}

CLASSE = {"titre": "BTS MEC", "sous_titre": "Management économique de la construction", "annee": "2026-2027"}

TP = {
    "dossier": "quantitatif-ifc",
    "projet": "Projet petite construction",
    "etude": "Étude n°4 · Extraire des données BIM",
    "titre": "Réaliser un quantitatif à partir d’un IFC",
    "situation": "Vous êtes opérateur BIM dans votre entreprise et vous devez effectuer un quantitatif pour réaliser une étude de prix.",
    "problematique": "« Comment extraire d’une maquette numérique un métré fiable, justifié et directement exploitable pour une étude de prix ? »",
    "duree": "4 h",
    "modalite": "Distanciel · TP évalué",
    "maquette": "fichiers/LKBIM-PPC-S02-TP01.ifc",
    "maquette_zip": "fichiers/LKBIM-PPC-S02-TP01.zip",
    "sujet_pdf": "fichiers/LKBIM-PPC-S01-TP01-sujet.pdf",
}

LOTS = [
    ("1", "Gros œuvre", ["Calculer le volume des semelles filantes", "Calculer la surface des différents types de murs (soubassement, élévations, etc.)", "Calculer le volume des dalles béton", "Calculer le volume des escaliers"]),
    ("2", "Plâtrerie", ["Calculer la surface de doublage", "Calculer la surface de cloison", "Calculer la surface des plafonds"]),
    ("3", "Toiture", ["Calculer la longueur des arêtiers", "Calculer la longueur des noues", "Calculer la longueur des faîtages", "Calculer la longueur des lignes d’égout", "Calculer la surface de couverture"]),
]
COMPETENCES = [
    ("C6.3", "Extraire des données d’une maquette numérique BIM"),
    ("C7.1", "Préparer le quantitatif"),
    ("C7.2", "Réaliser le quantitatif"),
]
CRITERES = ["Des arrondis justes", "Des unités clairement exprimées", "Des captures d’écran pour justifier vos métrés"]
DEROULE = [
    ("0 h 15", "Préparer", "Lire la consigne, ouvrir l’outil et la maquette, créer les chapitres et les ouvrages (unités, arrondis)."),
    ("1 h 15", "Lot 1 · Gros œuvre", "Semelles, murs par type, dalles, escaliers. Nomenclatures et contrôle des doublons."),
    ("0 h 45", "Lot 2 · Plâtrerie", "Doublages, cloisons, plafonds."),
    ("1 h 00", "Lot 3 · Toiture", "Outil Arête pour arêtiers, noues, faîtages, égouts ; surface de couverture."),
    ("0 h 45", "Contrôler et rendre", "Mode Contrôle, captures titrées, export Excel, vérification du fichier, dépôt."),
]

# =====================================================================
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">'

def ver():
    h = hashlib.md5()
    for f in ("assets/style.css", "assets/site.js"):
        h.update(open(os.path.join(ROOT, f), "rb").read())
    return h.hexdigest()[:8]

EXTRA_CSS = """<style>
.steps4{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,15rem),1fr));gap:1rem}
.step4{display:flex;flex-direction:column;gap:.5rem;background:var(--sheet);border:2px solid var(--ink);padding:1rem 1.1rem;text-decoration:none;position:relative;box-shadow:5px 5px 0 var(--line)}
.step4:hover{box-shadow:7px 7px 0 var(--line-strong);transform:translate(-1px,-1px)}
.step4 .n{font-family:var(--font-mono);font-size:.8rem;color:var(--ink-soft)}
.step4 .t{font-family:var(--font-display);font-size:1.6rem;font-weight:700;line-height:1.05}
.step4 .d{font-size:.95rem;color:var(--ink-soft)}
.step4 .go{margin-top:auto;font-weight:600;color:var(--u21)}
.step4.is-key{background:var(--u21-tint)}
.lots{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,18rem),1fr));gap:1rem}
.lot-card{background:var(--sheet);border:1px solid var(--line);border-top:4px solid var(--u21);padding:1rem 1.1rem}
.lot-card:nth-child(2){border-top-color:var(--u22)}.lot-card:nth-child(3){border-top-color:var(--u23)}
.lot-card h3{margin-bottom:.5rem}
.horaire{width:100%;border-collapse:collapse;background:var(--sheet)}
.horaire td{border-bottom:1px solid var(--line);padding:.55rem .7rem;vertical-align:top}
.horaire td:first-child{font-family:var(--font-mono);white-space:nowrap;width:1%}
.horaire td:nth-child(2){font-weight:600;white-space:nowrap}
.alert{border-left:5px solid var(--u23);background:var(--u23-tint);padding:.8rem 1rem}
.dl-list{list-style:none;padding:0;margin:0;display:grid;gap:.6rem}
.dl-list a{display:flex;gap:.8rem;align-items:center;text-decoration:none;background:var(--sheet);border:1px solid var(--line);padding:.6rem .8rem}
.dl-list a:hover{border-color:var(--ink)}
.dl-list .ext{font-family:var(--font-mono);font-size:.75rem;font-weight:600;color:#fff;background:var(--ink);padding:.2rem .45rem;min-width:3.2rem;text-align:center}
.dl-list small{display:block;color:var(--ink-soft)}
</style>"""

def page(title, body, depth=0, nav_html=""):
    up = "../" * depth
    v = ver()
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
{FONTS}
<link rel="stylesheet" href="{up}assets/style.css?v={v}">
{EXTRA_CSS}
</head>
<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a href="{up}index.html" class="brand">
      <span class="brand-mark" aria-hidden="true">MEC</span>
      <span class="brand-text"><strong>{e(CLASSE['titre'])}</strong><span>{e(CLASSE['sous_titre'])}</span></span>
    </a>
    <nav class="nav" aria-label="Navigation principale">{nav_html}</nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <table class="cartouche" aria-label="Cartouche">
      <tr><th>Classe</th><td>{e(CLASSE['titre'])} · {e(CLASSE['sous_titre'])}</td><th>Année</th><td class="mono">{e(CLASSE['annee'])}</td></tr>
      <tr><th>Formateur</th><td>Kevin Lormeau · LKBIM</td><th>Unité</th><td class="mono">U61</td></tr>
    </table>
  </div>
</footer>
<script src="{up}assets/site.js?v={v}"></script>
</body>
</html>
"""

def nav(items, active):
    return "".join(f'<a href="{h}" class="nav-link{" is-active" if k == active else ""}"{" aria-current=\"page\"" if k == active else ""}>{e(t)}</a>' for k, t, h in items)

def write(rel, txt):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(txt); print("écrit", rel)

D = TP["dossier"]
OUTIL = f"outil.html?ifc={TP['maquette']}"

# ---------------- Accueil de la classe ----------------
home = f"""
<section class="hero-band">
  <div class="wrap hero-split">
    <div class="hero-text">
      <p class="eyebrow">Site de la classe · {e(CLASSE['annee'])}</p>
      <h1>{e(CLASSE['titre'])}</h1>
      <p class="hero-sub">{e(CLASSE['sous_titre'])}</p>
      <p class="lead">Consignes, outils, tutoriels et fichiers des TP : tout le travail de la classe est ici, accessible depuis n’importe quel ordinateur, en cours comme à distance.</p>
      <div class="actions"><a class="btn" href="{D}/index.html">TP en cours : quantitatif IFC</a></div>
    </div>
    <figure class="planche">
      <img src="assets/img/maquette-3d.jpg" alt="Maquette numérique du projet petite construction">
      <figcaption><span class="mono">PL-00</span><span>{e(TP['projet'])} · maquette numérique</span></figcaption>
    </figure>
  </div>
</section>
<section class="wrap section">
  <div class="section-head"><span class="section-num mono">01</span><h2>Projets et TP</h2></div>
  <div class="projets"><a class="projet-card is-on" href="{D}/index.html">
  <span class="projet-img"><img src="assets/img/toiture-plan-h.jpg" alt="Vue en plan de la toiture de la maquette" loading="lazy" style="object-fit:contain;background:#fff"><span class="statut is-on">En cours</span></span>
  <span class="projet-body">
    <span class="projet-num mono">PPC · ÉTUDE 04 · TP</span>
    <span class="projet-title">{e(TP['titre'])}</span>
    <span class="projet-resume">{e(TP['situation'])}</span>
    <span class="projet-meta"><span><b>Durée</b>{e(TP['duree'])}</span><span><b>Modalité</b>{e(TP['modalite'])}</span><span><b>Compétences</b>C6.3 · C7.1 · C7.2</span></span>
    <span class="btn projet-cta">Ouvrir le TP →</span>
  </span>
</a></div>
</section>
<section class="wrap section">
  <div class="section-head"><span class="section-num mono">02</span><h2>Travailler à distance</h2></div>
  <ul class="list">
    <li>Un ordinateur avec <b>Chrome, Edge ou Firefox</b> à jour et une souris : aucun logiciel à installer.</li>
    <li>Vos saisies restent dans le navigateur de votre poste : <b>sauvegardez</b> régulièrement et rendez vos fichiers avant l’heure limite.</li>
    <li>Commencez toujours par le <b>tutoriel</b> du TP : il se termine par une attestation à imprimer en PDF.</li>
  </ul>
</section>"""
write("index.html", page(f"{CLASSE['titre']} – site de la classe", home, 0, nav([("home", "Accueil", "index.html"), ("tp", "TP quantitatif IFC", f"{D}/index.html")], "home")))

# ---------------- Page du TP ----------------
tp_nav = nav([("cl", "← Classe", "../index.html"), ("tp", "TP", "index.html"), ("tuto", "1 · Tuto", "tuto.html"), ("cons", "2 · Consigne", "consigne.html"), ("outil", "3 · Outil", OUTIL)], "tp")
depot = f'<a class="go" href="{e(LIENS["depot"])}" target="_blank" rel="noopener">Ouvrir l’espace de dépôt →</a>' if LIENS["depot"] else '<span class="go">Lien de dépôt communiqué par votre formateur</span>'
steps4 = f"""<div class="steps4">
<a class="step4" href="tuto.html"><span class="n">ÉTAPE 1 · 30 min · avant le TP</span><span class="t">Tuto découverte</span><span class="d">7 missions guidées pour prendre l’outil en main, puis votre attestation à imprimer en PDF.</span><span class="go">Commencer le tuto →</span></a>
<a class="step4" href="consigne.html"><span class="n">ÉTAPE 2 · 10 min</span><span class="t">Lire la consigne</span><span class="d">Situation, lots à métrer, résultats attendus, critères de réussite, déroulé conseillé.</span><span class="go">Lire la consigne →</span></a>
<a class="step4 is-key" href="{OUTIL}"><span class="n">ÉTAPE 3 · 3 h 30</span><span class="t">Réaliser le métré</span><span class="d">L’outil s’ouvre dans le navigateur ; cliquez « Charger la maquette du TP ».</span><span class="go">Ouvrir l’outil →</span></a>
<div class="step4"><span class="n">ÉTAPE 4 · fin du TP</span><span class="t">Rendre</span><span class="d">Exporter Excel, vérifier le fichier, le déposer avec votre attestation du tuto.</span>{depot}</div>
</div>"""
tp = f"""
<section class="hero-band">
  <div class="wrap hero-split">
    <div class="hero-text">
      <p class="eyebrow">{e(TP['projet'])} · {e(TP['etude'])} · {e(TP['duree'])}</p>
      <h1>{e(TP['titre'])}</h1>
      <p class="lead"><b>Situation professionnelle :</b> {e(TP['situation'])}</p>
      <p class="problematique">{e(TP['problematique'])}</p>
      <div class="actions"><a class="btn" href="tuto.html">Commencer par le tuto</a><a class="btn btn-ghost" href="{OUTIL}">Ouvrir l’outil</a></div>
    </div>
    <figure class="planche">
      <img src="../assets/img/maquette-3d.jpg" alt="Maquette numérique LKBIM-PPC-S02-TP01">
      <figcaption><span class="mono">PL-01</span><span>La maquette fournie : LKBIM-PPC-S02-TP01.ifc</span></figcaption>
    </figure>
  </div>
</section>
<section class="wrap" style="margin-top:1.5rem">
    <dl class="titleblock">
      <div><dt>Activité</dt><dd>TP · Réaliser un quantitatif à partir d’un IFC</dd></div>
      <div><dt>Durée</dt><dd>{e(TP['duree'])}</dd></div>
      <div><dt>Modalité</dt><dd>{e(TP['modalite'])}</dd></div>
      <div><dt>Rendu</dt><dd>Un fichier Excel : une feuille par lot + captures</dd></div>
    </dl>
</section>
<section class="wrap section">
  <div class="section-head"><span class="section-num mono">01</span><h2>Les 4 étapes</h2></div>
  {steps4}
</section>
<section class="wrap section two-col">
  <figure class="planche small-planche">
    <img src="../assets/img/toiture-plan-h.jpg" alt="Vue en plan de la toiture">
    <figcaption><span class="mono">PL-02</span><span>Vue en plan de la toiture : arêtiers, noues, faîtages, égouts</span></figcaption>
  </figure>
  <div class="note">
    <div class="section-head"><span class="section-num mono">02</span><h2>Ce que vous livrez</h2></div>
    <ul class="deliverables">
      <li>Le fichier Excel exporté par l’outil : <b>une feuille par lot</b> (1 Gros œuvre, 2 Plâtrerie, 3 Toiture)</li>
      <li>Un métré <b>exploitable</b> : ouvrages désignés, unités, arrondis, totaux</li>
      <li>Les <b>captures d’écran</b> qui justifient chaque métré (intégrées au fichier)</li>
      <li>L’<b>attestation</b> du tuto découverte en PDF</li>
    </ul>
  </div>
</section>
<section class="wrap section">
  <div class="section-head"><span class="section-num mono">03</span><h2>Compétences évaluées</h2></div>
  <div class="comps">{''.join(f'<div class="comp"><p class="comp-code mono">{c}</p><h3>{e(t)}</h3></div>' for c, t in COMPETENCES)}</div>
</section>
<section class="wrap section">
  <div class="section-head"><span class="section-num mono">04</span><h2>Fichiers</h2></div>
  <ul class="dl-list">
    <li><a href="{OUTIL}"><span class="ext">HTML</span><span><b>Outil LKBIM Métré IFC</b><small>S’ouvre dans le navigateur, avec chargement de la maquette en un clic</small></span></a></li>
    <li><a href="{TP['maquette']}" download><span class="ext">IFC</span><span><b>LKBIM-PPC-S02-TP01.ifc</b><small>La maquette (33 Mo), si vous préférez travailler hors ligne</small></span></a></li>
    <li><a href="{TP['maquette_zip']}" download><span class="ext">ZIP</span><span><b>LKBIM-PPC-S02-TP01.zip</b><small>La même maquette compressée (6,5 Mo), pour une connexion lente</small></span></a></li>
    <li><a href="outil.html" download="LKBIM-Metre-IFC.html"><span class="ext">HTML</span><span><b>LKBIM-Metre-IFC.html</b><small>L’outil à télécharger pour un usage hors ligne</small></span></a></li>
    <li><a href="{TP['sujet_pdf']}" target="_blank"><span class="ext">PDF</span><span><b>Sujet du TP</b><small>Version imprimable de la consigne</small></span></a></li>
  </ul>
</section>"""
write(f"{D}/index.html", page(f"TP · {TP['titre']}", tp, 1, tp_nav))

# ---------------- Consigne ----------------
cons_nav = nav([("cl", "← Classe", "../index.html"), ("tp", "TP", "index.html"), ("tuto", "1 · Tuto", "tuto.html"), ("cons", "2 · Consigne", "consigne.html"), ("outil", "3 · Outil", OUTIL)], "cons")
lots = "".join(f'<div class="lot-card"><p class="comp-code mono">LOT {n}</p><h3>{e(t)}</h3><ul class="checks">{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>' for n, t, items in LOTS)
horaire = "".join(f"<tr><td>{d}</td><td>{e(t)}</td><td>{e(x)}</td></tr>" for d, t, x in DEROULE)
cons = f"""
<section class="hero-band">
  <div class="wrap hero-split">
    <div class="hero-text">
      <p class="eyebrow">{e(TP['projet'])} · {e(TP['etude'])} · Consigne</p>
      <h1>Consigne du TP</h1>
      <p class="lead"><b>Situation professionnelle :</b> {e(TP['situation'])}</p>
      <p class="lead"><b>On vous donne :</b> la maquette numérique <span class="mono">LKBIM-PPC-S02-TP01.ifc</span>.</p>
      <div class="actions"><a class="btn" href="{OUTIL}">Ouvrir l’outil</a><a class="btn btn-ghost" href="{TP['sujet_pdf']}" target="_blank">Sujet en PDF</a></div>
    </div>
    <figure class="planche">
      <a href="{TP['sujet_pdf']}" target="_blank"><img src="../assets/img/sujet-p1.jpg" alt="Première page du sujet"></a>
      <figcaption><span class="mono">PDF</span><span>Le sujet original (cliquer pour ouvrir)</span></figcaption>
    </figure>
  </div>
</section>
<section class="wrap section">
  <div class="section-head"><span class="section-num mono">01</span><h2>On vous demande</h2></div>
  <p class="section-lead">À l’aide de la maquette numérique, réaliser le quantitatif des lots suivants.</p>
  <div class="lots">{lots}</div>
</section>
<section class="wrap section two-col">
  <div class="note">
    <div class="section-head"><span class="section-num mono">02</span><h2>Résultats attendus</h2></div>
    <ul class="deliverables"><li>Présenter <b>une feuille Excel par chapitre</b> (1 / 2 / 3).</li><li>Chaque feuille doit avoir un <b>métré exploitable</b>.</li></ul>
  </div>
  <div class="note">
    <div class="section-head"><span class="section-num mono">03</span><h2>Critères de réussite</h2></div>
    <ul class="checks">{''.join(f'<li>{e(c)}</li>' for c in CRITERES)}</ul>
  </div>
</section>
<section class="wrap section">
  <div class="section-head"><span class="section-num mono">04</span><h2>Compétences évaluées</h2></div>
  <div class="comps">{''.join(f'<div class="comp"><p class="comp-code mono">{c}</p><h3>{e(t)}</h3></div>' for c, t in COMPETENCES)}</div>
</section>
<section class="wrap section">
  <div class="section-head"><span class="section-num mono">05</span><h2>Déroulé conseillé ({e(TP['duree'])})</h2></div>
  <table class="horaire">{horaire}</table>
  <p class="alert" style="margin-top:1rem"><b>Pensez-y :</b> cliquez « Sauvegarder » dans l’outil toutes les 30 minutes, et vérifiez votre fichier Excel avant de le déposer.</p>
</section>"""
write(f"{D}/consigne.html", page(f"Consigne · {TP['titre']}", cons, 1, cons_nav))
