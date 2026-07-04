import pandas as pd

df = pd.read_csv('data/Social_Media_Advertising.csv')

print("=== COLONNES ===")
print(df.columns.tolist())

print("\n=== DIMENSIONS ===")
print(f"Lignes: {len(df)}, Colonnes: {len(df.columns)}")

print("\n=== APERÇU ===")
print(df.head(5))

print("\n=== TYPES ===")
print(df.dtypes)

print("\n=== ACQUISITION COST - EXEMPLES ===")
print(df['Acquisition_Cost'].head(5))

print("\n=== DUPLICATES ===")
print(f"Doublons: {df.duplicated().sum()}")

print("\n=== VALEURS MANQUANTES ===")
print(df.isnull().sum())

print("\n=== CHANNELS UNIQUES ===")
print(df['Channel_Used'].unique())