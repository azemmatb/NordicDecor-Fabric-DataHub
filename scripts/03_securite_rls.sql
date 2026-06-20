-- 1. Créer un schéma pour ranger nos règles de sécurité
CREATE SCHEMA Securite;
GO

-- 2. Créer la fonction de filtrage
CREATE FUNCTION Securite.FiltreMagasin(@Magasin_Ligne varchar(50))
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN SELECT 1 AS AccesAutorise
-- Si l'email correspond au magasin (ex: mons@nordicdecor.com), il voit les lignes 'Mons'
WHERE USER_NAME() = @Magasin_Ligne + '@nordicdecor.com'
-- OU ALORS, c'est toi (l'Architecte), donc tu as le droit de tout voir !
   OR USER_NAME() = 'architecte@azemmatbgmail.onmicrosoft.com'; 
GO

-- 3. Activer la règle sur la table Gold
CREATE SECURITY POLICY Policy_Retours_Gold
ADD FILTER PREDICATE Securite.FiltreMagasin(Magasin)
ON dbo.gold_retours_valorises
WITH (STATE = ON);
GO
