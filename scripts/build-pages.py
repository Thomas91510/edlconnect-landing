#!/usr/bin/env python3
"""Génère les pages « solutions » de proposition/ (une par recherche Google visée).

Le contenu est dans PAGES ci-dessous ; modifier puis relancer
    python3 scripts/build-pages.py
"""
import html, json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
URL = 'https://lokentia.fr/'
CHECK = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'

PAGES = [
  {
    'fichier': 'logiciel-etat-des-lieux.html',
    'court': "Logiciel pour experts EDL",
    'titre': "Logiciel de gestion pour experts en état des lieux | Lokentia",
    'description': "Lokentia est le logiciel de gestion pensé pour les experts en état des lieux : missions, agences, planning, réservation en ligne et relances dans un seul outil. Essai gratuit 15 jours.",
    'tag': "Logiciel état des lieux",
    'h1': "Le logiciel de gestion pensé pour les <em>experts en état des lieux</em>",
    'intro': "Un expert EDL ne gère pas des « deals » ni des « leads » : il gère des missions d'entrée et de sortie, des agences qui confient des dossiers, des locataires à joindre et un planning qui bouge sans arrêt. Lokentia a été conçu pour ce quotidien-là.",
    'sections': [
      ("Pourquoi un CRM générique ne suffit pas",
       ["Les CRM classiques sont construits pour la vente : opportunités, devis, étapes commerciales. Pour un expert en état des lieux, l'unité de travail est la <b>mission</b> : un bien, une date, un type d'intervention, une agence et des occupants.",
        "Adapter un outil généraliste demande des heures de paramétrage, et le résultat reste approximatif. Lokentia part directement de votre métier."],
       None),
      ("Ce que Lokentia gère pour vous",
       ["Tout ce qui entoure la visite sur place, de la demande jusqu'au suivi :"],
       ["<b>Missions</b> : EDL entrant, sortant, pré-état des lieux, avec statut et historique",
        "<b>Agences et contacts</b> : agences, gestionnaires, propriétaires, locataires",
        "<b>Planning</b> : vue semaine et mois, synchronisée avec Google Agenda",
        "<b>Réservation en ligne</b> : vos clients choisissent un créneau eux-mêmes",
        "<b>Extranet client</b> : chaque agence suit ses dossiers dans son espace",
        "<b>Emails et relances</b> : confirmations, rappel la veille, campagnes vers les agences"]),
      ("Ce que Lokentia ne fait pas",
       ["Lokentia n'est pas un logiciel de saisie d'état des lieux : vous continuez à utiliser votre outil habituel sur le terrain pour le relevé pièce par pièce. Lokentia s'occupe de tout le reste — l'organisation, le suivi et la relation avec vos agences."],
       None),
      ("Pour qui ?",
       ["Les experts indépendants qui se lancent, ceux qui travaillent déjà avec plusieurs agences, et les structures dont l'activité s'intensifie. La formule Gratuite permet de démarrer ; les formules Starter et Pro accompagnent la croissance."],
       None),
    ],
    'faq': [
      ("Faut-il installer quelque chose ?", "Non. Lokentia fonctionne dans le navigateur, sur ordinateur, tablette et smartphone."),
      ("Combien coûte Lokentia ?", "Une formule Gratuite est disponible. Les formules Starter et Pro coûtent 15 € et 35 € TTC par mois, ou 12 € et 28 € par mois en annuel, sans engagement."),
      ("Puis-je essayer avant de m'engager ?", "Oui : 15 jours d'essai sur toutes les fonctionnalités, sans carte bancaire."),
    ],
  },
  {
    'fichier': 'planning-expert-edl.html',
    'court': "Planning d'expert EDL",
    'titre': "Planning et agenda pour expert en état des lieux | Lokentia",
    'description': "Organisez le planning de vos états des lieux : missions dans l'agenda, synchronisation Google Agenda, statuts en temps réel et rappels automatiques. Essai gratuit 15 jours.",
    'tag': "Planning expert EDL",
    'h1': "Un planning d'états des lieux <em>qui tient la route</em>",
    'intro': "Un entrant à 9 h, un sortant à 14 h, un pré-état des lieux à caser entre les deux, et un locataire qui demande à décaler. Le planning d'un expert EDL change plusieurs fois par jour. Lokentia le garde à jour, au même endroit que vos dossiers.",
    'sections': [
      ("Chaque mission dans votre agenda",
       ["Quand vous créez ou recevez une mission, elle rejoint automatiquement votre planning, avec son type, son adresse et son client. Plus besoin de recopier les rendez-vous d'un outil à l'autre."],
       ["Vue <b>semaine</b> pour organiser vos tournées",
        "Vue <b>mois</b> pour anticiper les périodes chargées",
        "<b>Code couleur</b> selon le type d'état des lieux"]),
      ("Synchronisé avec Google Agenda",
       ["Activez la synchronisation en un clic : vos missions apparaissent dans Google Agenda, donc sur votre téléphone, à côté de vos rendez-vous personnels. Vous voyez d'un coup d'œil où vous devez être et quand."],
       None),
      ("Des rendez-vous qui ne tombent pas à l'eau",
       ["Un état des lieux annulé faute de locataire présent, c'est un déplacement pour rien. Lokentia envoie la confirmation au moment de la réservation, puis <b>un rappel automatique la veille du rendez-vous</b>."],
       None),
      ("Le statut de chaque mission, en temps réel",
       ["Nouvelle, planifiée, réalisée : chaque mission affiche son avancement. Vous savez ce qui reste à faire cette semaine, et l'agence voit l'état de ses dossiers dans son extranet sans avoir à vous appeler."],
       None),
    ],
    'faq': [
      ("Mon agenda Google est-il modifié ?", "Lokentia y ajoute vos missions. Vos autres rendez-vous restent tels quels."),
      ("Puis-je consulter mon planning sur le terrain ?", "Oui, depuis le navigateur de votre smartphone, et dans Google Agenda si la synchronisation est activée."),
      ("Les rappels sont-ils envoyés automatiquement ?", "Oui, la veille du rendez-vous, sans action de votre part."),
    ],
  },
  {
    'fichier': 'reservation-en-ligne-etat-des-lieux.html',
    'court': "Réservation en ligne",
    'titre': "Réservation en ligne d'états des lieux pour agences et propriétaires | Lokentia",
    'description': "Laissez vos agences et propriétaires réserver un état des lieux en ligne : créneaux disponibles, confirmation par email, rappel la veille, page à vos couleurs. Essai gratuit 15 jours.",
    'tag': "Réservation en ligne",
    'h1': "Vos clients réservent leur état des lieux <em>en ligne</em>",
    'intro': "Trois appels et deux messages vocaux pour fixer un seul rendez-vous : c'est le quotidien de beaucoup d'experts EDL. Avec Lokentia, vous partagez un lien et vos clients choisissent eux-mêmes un créneau disponible.",
    'sections': [
      ("Comment ça marche",
       ["Vous partagez votre lien de réservation avec vos agences et propriétaires. Ils :"],
       ["choisissent un <b>créneau libre</b> dans votre planning",
        "indiquent le <b>type d'état des lieux</b> et l'<b>adresse du bien</b>",
        "peuvent joindre les <b>documents utiles</b> à la mission",
        "reçoivent une <b>confirmation par email</b>, puis un rappel la veille"]),
      ("Une page à votre image",
       ["La page de réservation reprend la <b>couleur de votre marque</b> : vos clients réservent chez vous, pas sur un outil anonyme."],
       None),
      ("La demande arrive directement dans vos missions",
       ["Pas de ressaisie : la réservation crée la mission dans Lokentia, avec toutes les informations transmises. Vous la retrouvez dans votre planning et dans votre liste de missions."],
       None),
      ("L'extranet : vos agences suivent leurs dossiers",
       ["Chaque agence dispose de son propre espace pour suivre ses demandes et ses missions en cours. Moins d'appels « où en est mon dossier ? », plus de temps pour le terrain."],
       None),
    ],
    'faq': [
      ("Mes clients doivent-ils créer un compte pour réserver ?", "Non, le lien de réservation suffit."),
      ("Puis-je refuser ou déplacer une réservation ?", "Oui, chaque demande arrive dans vos missions : vous gardez la main sur votre planning."),
      ("La réservation en ligne est-elle incluse dans l'essai ?", "Oui, l'essai gratuit de 15 jours donne accès à toutes les fonctionnalités."),
    ],
  },
]


AUTEUR = 'Thomas Langlade'
DATE_PUB = ('2026-10-09', '9 octobre 2026')

ARTICLES = [
  {
    'fichier': 'agences-partenaires-expert-edl.html',
    'court': "Trouver des agences partenaires",
    'titre': "Expert en état des lieux : trouver et fidéliser des agences partenaires | Lokentia",
    'description': "Cibler les bonnes agences, se présenter, relancer sans insister et fidéliser : la méthode pour développer son réseau d'agences quand on est expert en état des lieux.",
    'tag': "Ressources · Développer son activité",
    'h1': "Trouver et fidéliser des <em>agences partenaires</em>",
    'intro': "Pour un expert en état des lieux, quelques agences fidèles valent mieux qu'une longue liste de contacts froids. Voici une méthode simple pour construire ce réseau, puis le garder.",
    'lecture': '6 min',
    'sections': [
      ("1. Cibler les bonnes agences",
       ["Toutes les agences n'ont pas besoin de vous. Concentrez-vous sur celles qui ont une activité de <b>gestion locative</b> : ce sont elles qui organisent les entrées et sorties de locataires toute l'année.",
        "Limitez-vous à une zone que vous pouvez couvrir sans passer vos journées en voiture. Mieux vaut être très réactif sur un secteur que lent sur trois départements."],
       ["agences avec un service gestion locative",
        "administrateurs de biens et cabinets de gestion",
        "propriétaires bailleurs qui gèrent en direct",
        "dans un rayon de trajet raisonnable"]),
      ("2. Préparer une présentation claire",
       ["Avant le premier contact, une agence veut savoir rapidement si vous pouvez l'aider. Réunissez sur une page :"],
       ["votre <b>zone d'intervention</b> et vos <b>délais</b> habituels",
        "les <b>types de missions</b> : entrant, sortant, pré-état des lieux",
        "vos <b>tarifs</b>, ou au moins une fourchette",
        "un <b>exemple de rapport</b> anonymisé",
        "votre <b>assurance responsabilité civile professionnelle</b>"]),
      ("3. Le premier contact",
       ["Un email court et personnalisé, suivi quelques jours plus tard d'un appel, fonctionne mieux qu'un long message générique. Proposez quelque chose de concret : réaliser une première mission pour juger sur pièce.",
        "Si vous prospectez par email, restez dans le cadre fixé par la CNIL pour la prospection entre professionnels : un message en rapport avec l'activité de la personne, et un moyen simple de ne plus être sollicité."],
       None),
      ("4. Relancer sans insister",
       ["La plupart des réponses arrivent après une relance, pas après le premier message. Espacez vos relances de plusieurs semaines et apportez à chaque fois une information utile (disponibilités du mois, nouveau secteur couvert).",
        "Savoir qui a ouvert votre email aide à choisir qui rappeler en premier. Dans Lokentia, le suivi des ouvertures et le pipeline de prospection servent exactement à ça."],
       None),
      ("5. Fidéliser : la régularité avant tout",
       ["Une agence garde un expert sur lequel elle peut compter. Ce qui compte le plus pour elle :"],
       ["la <b>ponctualité</b> aux rendez-vous",
        "un <b>délai de remise du rapport</b> court et constant",
        "une <b>prise de rendez-vous simple</b>, idéalement en ligne",
        "la possibilité de <b>suivre ses dossiers</b> sans vous appeler",
        "un interlocuteur qui répond"]),
      ("6. Mesurer qui vous fait travailler",
       ["Regardez chaque mois quelles agences vous confient des missions, et lesquelles ont ralenti. Une agence silencieuse depuis deux mois mérite un appel : un changement de gestionnaire, un concurrent, ou simplement un oubli."],
       None),
    ],
  },
  {
    'fichier': 'eviter-rendez-vous-manques-etat-des-lieux.html',
    'court': "Éviter les rendez-vous manqués",
    'titre': "Rendez-vous d'état des lieux manqués : 7 habitudes pour les éviter | Lokentia",
    'description': "Locataire absent, clés introuvables, mauvaise adresse : 7 habitudes simples pour éviter les rendez-vous d'état des lieux manqués et les déplacements pour rien.",
    'tag': "Ressources · Organisation",
    'h1': "Rendez-vous manqués : <em>7 habitudes</em> pour les éviter",
    'intro': "Un état des lieux qui n'a pas lieu, c'est un déplacement perdu, un créneau gâché et une agence agacée. La plupart de ces échecs se jouent avant le rendez-vous.",
    'lecture': '5 min',
    'sections': [
      ("1. Confirmer par écrit, avec tous les détails",
       ["Une confirmation par email évite les malentendus. Elle doit contenir l'adresse complète (bâtiment, étage, code d'accès), la date, l'heure, la durée estimée et ce qu'il faut prévoir : clés, badges, présence des deux parties."],
       None),
      ("2. Avoir le bon contact",
       ["Passer uniquement par l'agence ajoute un intermédiaire. Demandez systématiquement les coordonnées directes du locataire, ou du propriétaire, pour pouvoir le joindre en cas d'imprévu."],
       None),
      ("3. Envoyer un rappel la veille",
       ["Un rappel la veille rattrape les oublis et les changements de dernière minute. C'est la mesure la plus efficace, et elle s'automatise : Lokentia l'envoie sans que vous ayez à y penser."],
       None),
      ("4. Clarifier la question des clés",
       ["Qui apporte les clés, qui les récupère, où les déposer ? Pour une sortie comme pour une entrée, réglez ce point dans la confirmation plutôt que sur le palier."],
       None),
      ("5. Prévoir des trajets réalistes",
       ["Regroupez les missions par secteur et laissez une marge entre deux rendez-vous. Un retard en cascade finit souvent par un rendez-vous annulé en fin de journée."],
       None),
      ("6. Convenir d'une règle en cas d'absence",
       ["Mettez-vous d'accord à l'avance avec vos agences : déplacement facturé ou non, délai de prévenance, nouveau créneau. Une règle connue de tous évite les discussions après coup.",
        "Pour un état des lieux de sortie qui ne peut pas être établi contradictoirement, la loi du 6 juillet 1989 (article 3-2) prévoit le recours à un commissaire de justice : un point à rappeler à l'agence si la situation se bloque."],
       None),
      ("7. Laisser le client choisir son créneau",
       ["Quand c'est le client qui choisit l'heure, il s'en souvient mieux et a moins de raisons de la déplacer. Une page de réservation en ligne lui laisse ce choix parmi vos disponibilités réelles."],
       None),
    ],
  },
]

GABARIT = (RACINE / 'scripts' / 'page-template.html').read_text()

def rendre(pg):
    corps = []
    for h2, paras, puces in pg['sections']:
        corps.append(f'<h2>{h2}</h2>')
        corps += [f'<p>{p}</p>' for p in paras]
        if puces:
            corps.append('<ul class="ticks">' + ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in puces) + '</ul>')
    faq = ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(r)}</p></details>' for q, r in pg.get('faq', []))
    article = 'lecture' in pg
    if article:
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": re.sub('<[^>]+>', '', pg['h1']),
              "description": pg['description'], "datePublished": DATE_PUB[0], "inLanguage": "fr",
              "author": {"@type": "Person", "name": AUTEUR},
              "publisher": {"@type": "Organization", "name": "Lokentia"},
              "image": URL + "proposition/og-image.jpg"}
    elif not pg.get('faq'):
        ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": pg['titre'], "description": pg['description']}
    else:
        ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in pg['faq']]}
    faq_bloc = f'<section class="faq">\n<h2>Questions fréquentes</h2>\n{faq}\n</section>' if pg.get('faq') else ''
    crumb = '<a href="./">Accueil</a> · ' + ('<a href="ressources.html">Ressources</a>' if article else html.escape(pg['tag']))
    meta = f'<p class="meta">Par {AUTEUR} · {DATE_PUB[1]} · {pg["lecture"]} de lecture</p>' if article else ''
    groupe = ARTICLES if article else PAGES
    autres = ''.join(f'<a href="{a["fichier"]}">{a["court"]} →</a>' for a in groupe if a is not pg)
    if article:
        autres = '<a href="ressources.html">Toutes les ressources →</a>' + autres
    rempl = {
        '{{TITRE}}': html.escape(pg['titre']), '{{DESCRIPTION}}': html.escape(pg['description']),
        '{{URL}}': URL + 'proposition/' + pg['fichier'], '{{TAG}}': pg['tag'], '{{H1}}': pg['h1'],
        '{{INTRO}}': pg['intro'], '{{CORPS}}': '\n'.join(corps), '{{FAQ_BLOC}}': faq_bloc, '{{AUTRES}}': autres,
        '{{CRUMB}}': crumb, '{{META}}': meta,
        '{{LDJSON}}': json.dumps(ld, ensure_ascii=False),
    }
    out = GABARIT
    for k, v in rempl.items():
        out = out.replace(k, v)
    return out

for pg in PAGES + ARTICLES:
    (RACINE / 'proposition' / pg['fichier']).write_text(rendre(pg))
    print('écrit', pg['fichier'])

# Index de la rubrique Ressources
cartes = ''.join(f'<a href="{a["fichier"]}"><b>{re.sub("<[^>]+>", "", a["h1"])}</b><span>{a["description"]}</span><small>Lire · {a["lecture"]}</small></a>' for a in ARTICLES)
index = {
    'fichier': 'ressources.html', 'court': 'Ressources',
    'titre': "Ressources pour les experts en état des lieux | Lokentia",
    'description': "Conseils pratiques pour les experts en état des lieux : développer son réseau d'agences, organiser ses rendez-vous, gagner du temps sur la gestion.",
    'tag': 'Ressources', 'h1': "Ressources pour les <em>experts en état des lieux</em>",
    'intro': "Des conseils concrets, tirés du terrain, pour développer et organiser votre activité.",
    'sections': [], 'faq': [],
}
page = rendre(index).replace('<main class="wrap">\n', '<main class="wrap">\n<div class="cards">' + cartes + '</div>\n', 1)
(RACINE / 'proposition' / 'ressources.html').write_text(page)
print('écrit ressources.html')
