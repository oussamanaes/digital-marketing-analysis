import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Charger le dataset nettoyé
df = pd.read_csv('data/Marketing_Clean.csv', sep=';', decimal=',')
df['Date'] = pd.to_datetime(df['Date'])

# 2. ROI moyen par canal
plt.figure(figsize=(8, 5))
df.groupby('Channel_Used')['ROI'].mean().sort_values().plot(kind='barh', color='steelblue')
plt.title('ROI moyen par canal')
plt.xlabel('ROI')
plt.tight_layout()
plt.savefig('data/01_roi_canal.png')
plt.show()
print("✅ Graphique 1 sauvegardé")

# 3. Revenue moyen par canal
plt.figure(figsize=(8, 5))
df.groupby('Channel_Used')['Revenue'].mean().sort_values().plot(kind='barh', color='seagreen')
plt.title('Revenue moyen par canal')
plt.xlabel('Revenue ($)')
plt.tight_layout()
plt.savefig('data/02_revenue_canal.png')
plt.show()
print("✅ Graphique 2 sauvegardé")

# 4. Distribution du ROI
plt.figure(figsize=(8, 5))
sns.histplot(df['ROI'], bins=50, color='tomato')
plt.title('Distribution du ROI')
plt.xlabel('ROI')
plt.tight_layout()
plt.savefig('data/03_distribution_roi.png')
plt.show()
print("✅ Graphique 3 sauvegardé")

# 5. Relation Acquisition_Cost / Revenue par canal
# 4. Relation Acquisition_Cost / Revenue par canal (échantillon réduit)
df_sample = df[['Acquisition_Cost', 'Revenue', 'Channel_Used']].sample(2000, random_state=1)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_sample, x='Acquisition_Cost', y='Revenue', hue='Channel_Used', alpha=0.4, s=20)
plt.title('Coût d\'acquisition vs Revenue par canal')
plt.tight_layout()
plt.savefig('data/04_cout_vs_revenue.png')
plt.show()
print("✅ Graphique 4 sauvegardé")