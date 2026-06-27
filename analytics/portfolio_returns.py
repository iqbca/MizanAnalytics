import pandas as pd


def calculate_security_returns(engine):

    query = """
    SELECT
        dp.SecurityID,
        sm.SecurityName,
        dp.PriceDate,
        dp.Price
    FROM DailyPrices dp
    JOIN SecurityMaster sm
        ON dp.SecurityID = sm.SecurityID
    ORDER BY
        dp.SecurityID,
        dp.PriceDate
    """

    prices = pd.read_sql(query, engine)

    prices["pricedate"] = pd.to_datetime(prices["pricedate"])

    prices["price"] = pd.to_numeric(
        prices["price"],
        errors="coerce"
    )

    prices = prices.sort_values(
        ["securityid", "pricedate"]
    )

    prices["DailyReturn"] = (
        prices.groupby("securityid")["price"]
        .pct_change()
    )

    prices["DailyReturnPct"] = (
        prices["DailyReturn"] * 100
    ).round(4)

    return prices


def load_portfolio_holdings(engine):

    query = """
    SELECT
        h.PortfolioID,
        h.SecurityID,
        s.SecurityName,
        h.Weight,
        h.MarketValue
    FROM Holdings h
    JOIN SecurityMaster s
        ON h.SecurityID = s.SecurityID
    """

    holdings = pd.read_sql(query, engine)

    return holdings


def calculate_portfolio_return(engine):

    prices = calculate_security_returns(engine)

    holdings = load_portfolio_holdings(engine)

    # Keep only rows where a return exists
    prices = prices.dropna(subset=["DailyReturn"])

    # Latest available return for each security
    latest_returns = (
        prices
        .sort_values(["securityid", "pricedate"])
        .groupby("securityid")
        .tail(1)
        .drop(columns=["securityname"])
    )

    merged = holdings.merge(
        latest_returns,
        on="securityid",
        how="left"
    )

    merged["DailyReturn"] = merged["DailyReturn"].fillna(0)

    merged["DailyReturnPct"] = merged["DailyReturnPct"].fillna(0)

    merged["Contribution"] = (
        merged["weight"] / 100
    ) * merged["DailyReturn"]

    merged["ContributionPct"] = (
        merged["Contribution"] * 100
    )

    portfolio_return = merged["Contribution"].sum()

    return merged, portfolio_return