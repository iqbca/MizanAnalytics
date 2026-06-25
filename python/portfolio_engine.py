import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/mizan_analytics"
)

query = """
SELECT
    s.SecurityName,
    h.Weight AS PortfolioWeight,
    COALESCE(bc.Weight,0) AS BenchmarkWeight
FROM Holdings h

JOIN SecurityMaster s
ON h.SecurityID = s.SecurityID

LEFT JOIN BenchmarkConstituents bc
ON h.SecurityID = bc.SecurityID

WHERE h.PortfolioID = 1
"""
df = pd.read_sql(query, engine)

df["ActiveWeight"] = (
    df["portfolioweight"]
    - df["benchmarkweight"]
)
print("\nPortfolio vs Benchmark\n")

for _, row in df.iterrows():

    print(
        f"{row['securityname']:<25}"
        f"{row['portfolioweight']:>8.2f}%"
        f"{row['benchmarkweight']:>12.2f}%"
        f"{row['ActiveWeight']:>12.2f}%"
    )