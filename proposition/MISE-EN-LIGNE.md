# Mise en ligne de la nouvelle version du site

Rien de ce dossier n'est en production tant que les étapes ci-dessous ne sont pas faites.

## Avant

- [ ] Remplacer « 9 octobre 2026 » par la vraie date de mise en ligne dans les 4 fichiers `.md` juridiques
      (`sed -i 's/9 octobre 2026/JJ mois AAAA/' cgvu-lokentia.md dpa-sous-traitance.md mentions-legales.md politique-confidentialite.md`), puis `python3 scripts/build-legal.py`
- [ ] Faire relire CGVU, politique de confidentialité et DPA par un avocat
- [ ] Vérifier les chiffres affichés (500+ missions, 2 h gagnées par semaine) et la lettre du fondateur
- [ ] Mettre en ligne le correctif de l'app `edlconnect-crm` (CORS de `/api/contact-form`, branche `claude/compassionate-maxwell-yn1axw`) — sinon le formulaire de contact ne marchera pas
- [ ] Activer Analytics dans le projet Vercel `edlconnect-landing`

## Bascule

1. Déplacer le contenu de `proposition/` à la racine (remplace l'ancien `index.html`)
2. Poser `sitemap.xml` et `robots.txt` de `a-poser-a-la-racine/` à la racine
3. Remplacer les chemins `/proposition/` restants :
   `grep -rl "proposition/" *.html scripts/` (photo du fondateur, image de partage, URLs canoniques)
4. Retirer `<meta name="robots" content="noindex, nofollow">` de toutes les pages
   (et du gabarit `scripts/page-template.html`, `scripts/legal-template.html`)
5. Supprimer `MISE-EN-LIGNE.md` et le dossier `a-poser-a-la-racine/`

## Après

- [ ] Envoyer un message test avec le formulaire de contact
- [ ] Déclarer `https://lokentia.fr/sitemap.xml` dans Google Search Console
- [ ] Tester l'aperçu de partage (LinkedIn Post Inspector)
- [ ] Si les questions fréquentes de l'accueil changent, mettre à jour le bloc JSON-LD `FAQPage` en haut de `index.html`
