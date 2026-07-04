import pandas as pd

df = pd.read_csv('data/Social_Media_Advertising.csv')

# 1. Nettoyer Acquisition_Cost (enlever le $ et convertir en nombre)
df['Acquisition_Cost'] = df['Acquisition_Cost'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)

# 2. Convertir la date
df['Date'] = pd.to_datetime(df['Date'])

# 3. Vérifier si Acquisition_Cost varie vraiment
print("=== ACQUISITION COST - STATS ===")
print(df['Acquisition_Cost'].describe())

# 4. Calculer des métriques utiles
df['CTR'] = (df['Clicks'] / df['Impressions'] * 100).round(2)
df['Revenue'] = (df['Acquisition_Cost'] * df['Conversion_Rate'] * df['Clicks'] / 100).round(2)

# 5. Sauvegarder
df.to_csv('data/Marketing_Clean.csv', index=False, sep=';', decimal=',')
print("\n✅ Fichier nettoyé sauvegardé : Marketing_Clean.csv")