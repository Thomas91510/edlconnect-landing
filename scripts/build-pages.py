#!/usr/bin/env python3
"""Génère les pages « solutions » de proposition/ (une par recherche Google visée).

Le contenu est dans PAGES ci-dessous ; modifier puis relancer
    python3 scripts/build-pages.py
"""
import html, json, pathlib

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

GABARIT = (RACINE / 'scripts' / 'page-template.html').read_text()

def rendre(pg):
    corps = []
    for h2, paras, puces in pg['sections']:
        corps.append(f'<h2>{h2}</h2>')
        corps += [f'<p>{p}</p>' for p in paras]
        if puces:
            corps.append('<ul class="ticks">' + ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in puces) + '</ul>')
    faq = ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(r)}</p></details>' for q, r in pg['faq'])
    autres = ''.join(f'<a href="{a["fichier"]}">{a["court"]} →</a>' for a in PAGES if a is not pg)
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in pg['faq']]}
    rempl = {
        '{{TITRE}}': html.escape(pg['titre']), '{{DESCRIPTION}}': html.escape(pg['description']),
        '{{URL}}': URL + 'proposition/' + pg['fichier'], '{{TAG}}': pg['tag'], '{{H1}}': pg['h1'],
        '{{INTRO}}': pg['intro'], '{{CORPS}}': '\n'.join(corps), '{{FAQ}}': faq, '{{AUTRES}}': autres,
        '{{LDJSON}}': json.dumps(ld, ensure_ascii=False),
    }
    out = GABARIT
    for k, v in rempl.items():
        out = out.replace(k, v)
    return out

for pg in PAGES:
    (RACINE / 'proposition' / pg['fichier']).write_text(rendre(pg))
    print('écrit', pg['fichier'])
