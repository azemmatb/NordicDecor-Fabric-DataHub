🛋️ NordicDecor - Enterprise Data Hub (Microsoft Fabric)

📌 Contexte du Projet

NordicDecor est une grande chaîne de magasins de meubles. L'objectif de ce projet est de moderniser le suivi du Service Après-Vente (SAV) et de calculer en temps réel la "Valeur financière bloquée" dans les retours clients, afin d'optimiser la trésorerie.

🏗️ Architecture Technique (Medallion Pattern)

Ce projet a été entièrement développé sur Microsoft Fabric (Capacité F2) en utilisant une architecture Medallion pour garantir la qualité et la performance :

Couche Bronze (Raw) : Ingestion des fichiers plats (.csv) quotidiens.

Couche Silver (Cleaned) : Nettoyage des données via PySpark (Gestion des nuls, dédoublonnage, standardisation).

Couche Gold (Curated) : Enrichissement et Modélisation (Jointure PySpark, optimisation Delta format).

⚙️ Orchestration & Automatisation (Data Factory)

Les traitements de données ont été industrialisés via les Data Pipelines de Fabric :

Création d'un Graphe Orienté Acyclique (DAG) assurant que la couche Gold n'est mise à jour que si le traitement de la couche Silver réussit (Dépendance On Success).

Planification (Schedule) quotidienne automatique pour une mise à disposition des données avant l'ouverture des magasins.

<img width="1720" height="1169" alt="image" src="https://github.com/user-attachments/assets/ae2daf8e-961a-44c5-aa15-4d88516bf425" />

🛡️ Gouvernance & Sécurité (Row-Level Security)

Pour répondre aux standards de production et de confidentialité :

Implémentation du Row-Level Security (RLS) directement sur le SQL Analytics Endpoint en T-SQL.

Résultat : Lorsqu'un directeur de magasin se connecte au rapport, la base de données filtre nativement les lignes pour ne lui afficher que l'argent bloqué dans sa propre succursale (ex: Mons ne voit que Mons), garantissant une sécurité à la source.

<img width="1719" height="1112" alt="image" src="https://github.com/user-attachments/assets/b65e81b2-c5a0-48a5-9bd2-d625c7d2d37a" />

🔄 CI/CD & Contrôle de Code Source

L'espace de travail de développement Fabric est synchronisé en temps réel avec ce dépôt GitHub.

Le code PySpark, les modèles sémantiques et les pipelines sont versionnés sur la branche main.

<img width="1713" height="1143" alt="image" src="https://github.com/user-attachments/assets/e54a2241-3638-4fbb-b1f4-076a1c462cc5" />

💡 Note pour les recruteurs : Les fichiers sources générés par l'intégration Fabric se trouvent à la racine. Pour une lecture rapide de mon code Python et SQL, veuillez consulter le dossier /scripts.
