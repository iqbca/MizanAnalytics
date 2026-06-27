from database.db_connection import engine
from analytics.portfolio_returns import calculate_portfolio_return
from analytics.benchmark_returns import calculate_benchmark_return
from analytics.excess_return import calculate_excess_return
from analytics.performance_history import save_performance
from analytics.performance_analysis import load_performance_history

print("=" * 60)
print("MIZAN ANALYTICS PLATFORM")
print("=" * 60)

holdings, portfolio_return = calculate_portfolio_return(engine)
benchmark, benchmark_return = calculate_benchmark_return(engine)
excess_return = calculate_excess_return(
    portfolio_return,
    benchmark_return
)

print("\nPortfolio Holdings\n")

print(
    holdings[
        [
            "securityname",
            "weight",
            "DailyReturnPct",
            "Contribution"
        ]
    ]
)

print("\nPortfolio Daily Return")

print(f"{portfolio_return * 100:.4f}%")

print("\nBenchmark Daily Return")

print(f"{benchmark_return * 100:.4f}%")

print("\nExcess Return")

print(f"{excess_return * 100:.4f}%")

save_performance(
    engine,
    portfolio_id=1,
    performance_date="2026-06-30",
    portfolio_return=portfolio_return,
    benchmark_return=benchmark_return,
    excess_return=excess_return
)   

history = load_performance_history(engine, 1)

print("\nPerformance History\n")

print(history)