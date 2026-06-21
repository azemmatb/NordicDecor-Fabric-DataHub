🛋️ NordicDecor - Enterprise Data Hub (Microsoft Fabric)

🎯 Contexte du Projet

NordicDecor est une grande chaîne de magasins de meubles. L'objectif de ce projet est de moderniser le suivi du Service Après-Vente (SAV) et de calculer en temps réel la "valeur financière bloquée" dans les retours clients, afin d'optimiser la trésorerie.

Ce projet a été entièrement développé sur Microsoft Fabric et met en œuvre une double architecture : le traitement de masse (Batch) pour l'historique, et le traitement à la seconde (Streaming) pour le suivi opérationnel.

🏗️ 1. Architecture Temps Réel (Streaming)

Objectif : Fournir un moniteur en direct (rafraîchissement continu) à la logistique pour suivre les flux de livraisons et les courses en cours.

Ingestion (Haute Vélocité) : Déploiement d'une antenne Fabric Eventstream capable de capter des milliers d'événements par seconde.

Stockage Analytique : Routage des événements vers une KQL Database (Eventhouse).

Transformation & Visualisation : Utilisation du Kusto Query Language (KQL) pour effectuer un fenêtrage temporel (bin()) et alimentation d'un Real-Time Dashboard en direct.

📁 Voir le code KQL du radar en direct dans le dossier /scripts

<img width="1717" height="1247" alt="image" src="https://github.com/user-attachments/assets/1ea5a1cb-162a-43cc-8bbe-62602f8dcefe" />

<img width="1718" height="1282" alt="image" src="https://github.com/user-attachments/assets/8cbf9a08-e4b7-4c5f-bf8a-7f2175a10750" />

💾 2. Architecture Batch (Medallion Pattern)

Objectif : Nettoyer et modéliser l'historique quotidien pour le reporting de direction.

Couche Bronze (Ingestion) : Réception des fichiers plats .csv (Drop zone).

Couche Silver (Cleaned) : Nettoyage des données via PySpark (Gestion des nuls, dédoublonnage, standardisation).

Couche Gold (Curated) : Enrichissement et Modélisation en étoile via PySpark, optimisation au format Delta Parquet.

📁 Voir les scripts PySpark dans le dossier /scripts

⚙️ 3. Orchestration & Automatisation (Data Factory)

Les traitements de données Batch sont orchestrés via les Data Pipelines de Fabric.
Création d'un Graphe Orienté Acyclique (DAG) assurant que la couche Gold n'est mise à jour que si le traitement de la couche Silver réussit (Dependence On Success).

<img width="1720" height="1169" alt="pipeline factory" src="https://github.com/user-attachments/assets/3bf9a351-dddc-42f4-a520-ee79d61b7c9b" />

🔒 4. Gouvernance & Sécurité (Row-Level Security)

Pour répondre aux standards de production et de confidentialité :
Implémentation de la Row-Level Security (RLS) directement sur le SQL Analytics Endpoint en T-SQL.

Résultat : Lorsqu'un directeur de magasin se connecte au rapport, la base de données filtre nativement les lignes pour ne lui afficher que l'argent bloqué dans sa propre succursale, garantissant une sécurité à la source.

📁 Voir le code SQL de la RLS dans le dossier /scripts

<img width="1719" height="1112" alt="code rls" src="https://github.com/user-attachments/assets/a6fea5d4-ce72-4147-80b4-7cf6d7580a30" />

🔄 5. CI/CD & Contrôle de Code Source

L'espace de travail de développement Fabric est synchronisé en temps réel avec ce dépôt GitHub.
Les notebooks PySpark, les requêtes KQL, les modèles sémantiques et les pipelines sont versionnés sur la branche main.

<img width="1713" height="1143" alt="synchronisation git" src="https://github.com/user-attachments/assets/9b343e98-42d5-4991-b0b7-e00df4e16553" />
