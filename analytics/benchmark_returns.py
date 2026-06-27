import pandas as pd
from analytics.portfolio_returns import calculate_security_returns


def load_benchmark(engine):

    query = """
    SELECT
        bc.BenchmarkID,
        bc.SecurityID,
        sm.SecurityName,
        bc.Weight
    FROM BenchmarkConstituents bc
    JOIN SecurityMaster sm
        ON bc.SecurityID = sm.SecurityID
    """

    benchmark = pd.read_sql(query, engine)

    return benchmark


def calculate_benchmark_return(engine):

    prices = calculate_security_returns(engine)

    benchmark = load_benchmark(engine)

    latest_returns = (
        prices
        .sort_values("pricedate")
        .groupby("securityid")
        .tail(1)
    )

    latest_returns = latest_returns.drop(columns=["securityname"])

    merged = benchmark.merge(
        latest_returns,
        on="securityid"
    )

    merged["Contribution"] = (
        merged["weight"] / 100
    ) * merged["DailyReturn"]
    
    merged["ContributionPct"] = (
    merged["Contribution"] * 100
)

    benchmark_return = merged["Contribution"].sum()

    return merged, benchmark_return