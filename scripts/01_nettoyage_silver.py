from pyspark.sql.functions import col, when, lit, coalesce

# 1. LECTURE DES DONNÉES 
df_retours_raw = spark.read.format("csv").option("header", "true").load("Files/raw_data/raw_retours_sav.csv")
df_pieces_raw = spark.read.format("csv").option("header", "true").load("Files/raw_data/dim_pieces.csv")

# 2. NETTOYAGE DES DONNÉES 
# Supprimer les doublons (dropDuplicates)
# Remplacer les valeurs nulles dans "ID_Piece" par "STK-999" (coalesce)
# Si "Statut" == "Inconnu", remplacer par "À vérifier", sinon garder le statut (when...otherwise)

df_retours_silver = df_retours_raw \
    .dropDuplicates() \
    .withColumn("ID_Piece", coalesce(col("ID_Piece"), lit("STK-999"))) \
    .withColumn("Statut", when(col("Statut") == "Inconnu", lit("À vérifier")).otherwise(col("Statut")))

df_pieces_silver = df_pieces_raw # Pas de nettoyage nécessaire ici

# 3. SAUVEGARDE EN TABLE DELTA (Delta Save Pattern)
# format delta, mode overwrite, saveAsTable("nom_de_la_table")

df_retours_silver.write.mode("overwrite").format("delta").saveAsTable("silver_retours_sav")
df_pieces_silver.write.mode("overwrite").format("delta").saveAsTable("silver_dim_pieces")

display(df_retours_silver)
