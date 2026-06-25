import pandas as pd

from database.db_connection import engine

print("="*50)
print("MIZAN ANALYTICS PLATFORM")
print("="*50)

query = """
SELECT *
FROM Portfolio
"""

df = pd.read_sql(query, engine)

print(df)