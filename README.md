🛋️ NordicDecor - Enterprise Data Hub (Microsoft Fabric)

📌 Contexte du Projet

NordicDecor est une grande chaîne de magasins de meubles. L'objectif de ce projet est de moderniser le suivi du Service Après-Vente (SAV) et de calculer en temps réel la "Valeur financière bloquée" dans les retours clients, afin d'optimiser la trésorerie.

🏗️ Architecture Technique (Medallion Pattern)

Ce projet a été entièrement développé sur Microsoft Fabric (Capacité F2) en utilisant une architecture Medallion pour garantir la qualité et la performance :

Couche Bronze (Raw) : Ingestion des fichiers plats (.csv) quotidiens (Tickets SAV et Catalogue Meubles) dans le stockage OneLake (Files).

Couche Silver (Cleaned) : Nettoyage des données via PySpark.

Traitement des valeurs nulles (Data Quality Patterns avec coalesce).

Dédoublonnage (dropDuplicates).

Standardisation des statuts métiers (when().otherwise()).

Sauvegarde au format Delta Lake (mode("overwrite")).

Couche Gold (Curated) : Enrichissement et Modélisation.

Jointure PySpark entre les retours et le catalogue dimensionnel.

Calcul de la métrique métier (Valeur_Bloquee).

Optimisation des performances de lecture via un partitionnement physique (partitionBy("Magasin")).

⚙️ Orchestration & Automatisation (Data Factory)

Les traitements de données ont été industrialisés via les Data Pipelines de Fabric :

Création d'un Graphe Orienté Acyclique (DAG) assurant que la couche Gold n'est mise à jour que si le traitement de la couche Silver réussit (Dépendance On Success).

Planification (Schedule) quotidienne automatique pour une mise à disposition des données avant l'ouverture des magasins.

(Glisse et dépose ta capture d'écran de ton pipeline ici pour remplacer ce texte)

🛡️ Gouvernance & Sécurité (Row-Level Security)

Pour répondre aux standards de production et de confidentialité :

Implémentation du Row-Level Security (RLS) directement sur le SQL Analytics Endpoint en T-SQL.

Création d'une fonction de filtrage dynamique basée sur USER_NAME() (EntraID/Azure AD).

Résultat : Lorsqu'un directeur de magasin se connecte au rapport, la base de données filtre nativement les lignes pour ne lui afficher que l'argent bloqué dans sa propre succursale (ex: Mons ne voit que Mons), garantissant une sécurité à la source.

(Glisse et dépose ta capture d'écran de ton code SQL ici pour remplacer ce texte)

🔄 CI/CD & Contrôle de Code Source

L'espace de travail de développement Fabric est synchronisé en temps réel avec ce dépôt GitHub.

Le code PySpark, les modèles sémantiques et les pipelines sont versionnés sur la branche main, prêts pour un déploiement sécurisé vers les environnements de TEST et de PROD via les Deployment Pipelines de Fabric.

(Glisse et dépose ta capture d'écran de l'espace de travail "Synced" ici pour remplacer ce texte)

📂 Navigation dans le code

💡 Note pour les relecteurs : L'intégration continue de Fabric générant une arborescence complexe, les codes sources principaux ont été extraits et mis au propre dans le dossier scripts/ de ce dépôt pour faciliter votre lecture.

Projet réalisé de bout-en-bout (Data Engineering, Cloud Architecture, BI, CI/CD).
