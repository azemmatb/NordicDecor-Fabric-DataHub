from pyspark.sql.functions import col, round, when, lit 

# 1. LECTURE DES TABLES SILVER (Format Delta)
# On ne lit plus des CSV, on lit directement nos tables propres !
df_retours = spark.read.table("silver_retours_sav")
df_pieces = spark.read.table("silver_dim_pieces")

# 2. LA JOINTURE (Enrichissement)
# Objectif : Joindre df_retours et df_pieces sur la colonne "ID_Piece"
# Utilise une jointure de type "left" (gauche)

df_gold_join = df_retours.join(
    df_pieces,
    "ID_Piece",
    "left"
)

# 3. CRÉATION DE LA VALEUR MÉTIER (Calcul)
# Objectif : On a besoin d'une nouvelle colonne "Valeur_Bloquee". 
# Si le Statut est "En attente" ou "En cours", la valeur bloquée = le "Prix" de la pièce.
# Sinon (ex: "Remboursé", "Livré"), la valeur bloquée = 0.
# Indice : Tu auras besoin d'importer la fonction 'when' et 'lit' que tu as utilisée dans le notebook précédent !

df_gold_final = df_gold_join.withColumn(
    "Valeur_Bloquee",
    when((col("Statut") == "En attente") | (col("Statut") == "En cours"), col("Prix")).otherwise(lit(0))
)

# 4. SAUVEGARDE EN COUCHE GOLD (Optimisation)
# Objectif : Sauvegarder en Delta, mais cette fois-ci, on veut partitionner physiquement 
# les données par "Magasin" pour que les requêtes de chaque directeur soient ultra-rapides.
# Nomme la table "gold_retours_valorises"

df_gold_final.write \
    .partitionBy("Magasin") \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("gold_retours_valorises")

display(df_gold_final)
