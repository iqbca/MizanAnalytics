from sqlalchemy import text

def save_performance(
    engine,
    portfolio_id,
    performance_date,
    portfolio_return,
    benchmark_return,
    excess_return
):

    query = """
    INSERT INTO PerformanceHistory
    (
        PortfolioID,
        PerformanceDate,
        PortfolioReturn,
        BenchmarkReturn,
        ExcessReturn
    )
    VALUES
    (
        :portfolioid,
        :performancedate,
        :portfolioreturn,
        :benchmarkreturn,
        :excessreturn
    )
    """

    values = {
        "portfolioid": int(portfolio_id),
        "performancedate": performance_date,
        "portfolioreturn": float(portfolio_return * 100),
        "benchmarkreturn": float(benchmark_return * 100),
        "excessreturn": float(excess_return * 100),
    }

    with engine.begin() as conn:
        conn.execute(text(query), values)

    print("\nPerformance successfully saved.")