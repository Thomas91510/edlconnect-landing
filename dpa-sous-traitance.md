# Accord de sous-traitance des données personnelles (DPA) — Lokentia

*Annexe aux CGVU — Version 1.0 — [DATE]*

> ⚠️ Document préparatoire conforme à l'esprit de l'article 28 du RGPD, à faire valider par un avocat avant les premiers abonnements payants.

## 1. Parties et objet

Le présent accord est conclu entre le **Client** (tel qu'identifié lors de la souscription), agissant en qualité de **responsable de traitement**, et **ImmoCheck EDL** (SASU au capital de 150 €, RCS Évry n° 994 114 163, siège : 24 Route de Cheptainville, 91630 Marolles-en-Hurepoix), éditeur de Lokentia, agissant en qualité de **sous-traitant** (ci-après « le Sous-traitant »). Il encadre les traitements de données personnelles réalisés par le Sous-traitant pour le compte du Client dans le cadre de l'utilisation du service Lokentia, et prévaut sur les CGVU pour tout ce qui concerne ces traitements.

## 2. Description du traitement

**Nature et finalité** : hébergement, structuration et mise à disposition des données saisies par le Client ; envoi d'emails transactionnels en son nom (confirmations de rendez-vous, convocations, rappels, mise à disposition de rapports, demandes d'avis) ; génération et stockage de documents (rapports, factures) ; sauvegardes.

**Catégories de personnes concernées** : contacts professionnels du Client (agences, gestionnaires), locataires et propriétaires des biens faisant l'objet de missions.

**Catégories de données** : identité et civilité, coordonnées (email, téléphone, adresse postale des biens), informations relatives aux missions et rendez-vous (dates, type d'intervention, notes), documents produits (rapports d'état des lieux pouvant contenir des photographies du logement), données de facturation du Client vers ses propres clients. **Aucune donnée dite sensible** (article 9 RGPD) n'a vocation à être traitée ; le Client s'engage à ne pas en introduire dans le service, notamment dans les champs libres.

**Durée** : durée de l'abonnement, augmentée de la période de conservation post-résiliation prévue à l'article 8.

## 3. Instructions du Client

Le Sous-traitant traite les données uniquement sur instruction documentée du Client, la configuration et l'utilisation du service par le Client valant instruction. Il informe le Client si une instruction lui paraît contraire au RGPD. Il ne traite pas les Données Client pour son propre compte, notamment à des fins commerciales ou de démarchage des Utilisateurs finaux du Client.

## 4. Confidentialité et sécurité

Le Sous-traitant garantit que les personnes autorisées à traiter les données sont soumises à une obligation de confidentialité. Il met en œuvre les mesures techniques et organisationnelles appropriées, notamment : chiffrement des communications (TLS) et des sauvegardes au repos ; **cloisonnement des données par client** appliqué au niveau de la base de données (politiques de sécurité par ligne) et des interfaces d'accès ; authentification par lien à usage unique ; principe de moindre privilège sur les accès de production ; secrets d'infrastructure stockés hors du code ; sauvegarde quotidienne avec rétention de 30 jours et purge automatique ; journalisation des envois d'emails.

## 5. Sous-traitants ultérieurs

Le Client autorise de manière générale le recours aux sous-traitants ultérieurs listés ci-dessous, chacun étant lié par des obligations équivalentes au présent accord :

| Sous-traitant ultérieur | Prestation | Localisation / garanties |
|---|---|---|
| Supabase | Base de données, authentification, stockage | UE [région à confirmer] |
| Vercel | Hébergement applicatif | UE/USA — clauses contractuelles types |
| Brevo | Envoi d'emails | France / UE |
| Google | Synchronisation d'agenda (si activée) | UE/USA — clauses contractuelles types |
| Mistral AI | Rédaction assistée (si utilisée) | France / UE |

Toute modification de cette liste est notifiée au Client au moins 30 jours à l'avance (email ou notification dans l'application). Le Client peut s'y opposer pour motif légitime ; à défaut d'accord, il peut résilier son abonnement sans pénalité avant l'entrée en vigueur.

## 6. Assistance au responsable de traitement

Compte tenu de la nature du traitement, le Sous-traitant assiste le Client, par des mesures appropriées : réponse aux demandes d'exercice de droits des personnes concernées (les demandes reçues directement sont transmises au Client sans y répondre sur le fond, sauf instruction contraire) ; fourniture des informations raisonnablement nécessaires à la réalisation d'analyses d'impact ; capacités d'export et de suppression intégrées au service.

## 7. Violations de données

Le Sous-traitant notifie au Client toute violation de données à caractère personnel affectant ses Données **dans les meilleurs délais et au plus tard 48 heures** après en avoir pris connaissance, en documentant la nature de la violation, les catégories et le volume approximatif de données et de personnes concernées, les conséquences probables et les mesures prises ou proposées. La notification aux autorités et aux personnes concernées relève du Client, avec l'assistance du Sous-traitant.

## 8. Sort des données en fin de contrat

À l'expiration ou à la résiliation de l'abonnement, le Client peut exporter l'intégralité de ses Données (format JSON, fonction intégrée). Les Données sont conservées 90 jours en vue d'une éventuelle réactivation, puis **supprimées** des systèmes actifs ; les sauvegardes sont écrasées au terme de leur cycle de rétention de 30 jours. Sur demande expresse, la suppression anticipée est réalisée sous 30 jours, sous réserve des obligations légales de conservation.

## 9. Audit

Le Sous-traitant tient à disposition du Client la documentation nécessaire à la démonstration du respect du présent accord. Le Client peut, au plus une fois par an et moyennant un préavis de 30 jours, réaliser ou faire réaliser un audit documentaire ; les audits sur site, s'ils s'avéraient nécessaires, sont organisés d'un commun accord, aux frais du Client, sans accès aux données des autres clients du Sous-traitant.

## 10. Registre et coopération

Le Sous-traitant tient le registre des catégories d'activités de traitement effectuées pour le compte de ses clients (article 30.2 RGPD) et coopère avec l'autorité de contrôle à sa demande.
