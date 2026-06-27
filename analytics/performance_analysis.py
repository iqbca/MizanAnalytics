import pandas as pd


def load_performance_history(engine, portfolio_id):

    query = """
    SELECT
        p.portfolioid,
        p.performancedate,
        p.return AS portfolioreturn,
        b.return AS benchmarkreturn
    FROM PortfolioPerformance p
    LEFT JOIN BenchmarkPerformance b
        ON p.performancedate = b.performancedate
    WHERE p.portfolioid = %(portfolioid)s
    ORDER BY TO_DATE(p.performancedate,'DD-MM-YYYY')
    """

    history = pd.read_sql(
        query,
        engine,
        params={"portfolioid": portfolio_id}
    )

    history["portfolioreturn"] = pd.to_numeric(
        history["portfolioreturn"],
        errors="coerce"
    )

    history["benchmarkreturn"] = pd.to_numeric(
        history["benchmarkreturn"],
        errors="coerce"
    )

    return history