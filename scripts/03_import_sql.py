import pandas as pd
import mysql.connector

df = pd.read_csv('data/Marketing_Clean.csv', sep=';', decimal=',')

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    database='marketing'
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS campaigns (
        Campaign_ID INT,
        Target_Audience VARCHAR(50),
        Campaign_Goal VARCHAR(50),
        Duration VARCHAR(50),
        Channel_Used VARCHAR(50),
        Conversion_Rate FLOAT,
        Acquisition_Cost FLOAT,
        ROI FLOAT,
        Location VARCHAR(50),
        Language VARCHAR(50),
        Clicks INT,
        Impressions INT,
        Engagement_Score INT,
        Customer_Segment VARCHAR(50),
        Date DATE,
        Company VARCHAR(100),
        CTR FLOAT,
        Revenue FLOAT
    )
""")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO campaigns VALUES 
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print(f"✅ {len(df)} lignes importées dans MySQL")