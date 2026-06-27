from analytics.portfolio_returns import calculate_portfolio_return
from analytics.benchmark_returns import calculate_benchmark_return
from analytics.excess_return import calculate_excess_return
from analytics.performance_analysis import load_performance_history


class AnalyticsEngine:

    def __init__(self, engine):

        self.engine = engine

    def run(self):

        # ------------------------
        # Portfolio Analytics
        # ------------------------

        portfolio_df, portfolio_return = calculate_portfolio_return(
            self.engine
        )

        # ------------------------
        # Benchmark Analytics
        # ------------------------

        benchmark_df, benchmark_return = calculate_benchmark_return(
            self.engine
        )

        # ------------------------
        # Relative Performance
        # ------------------------

        excess_return = calculate_excess_return(
            portfolio_return,
            benchmark_return
        )

        # ------------------------
        # Historical Performance
        # ------------------------

        history = load_performance_history(
            self.engine,
            portfolio_id=1
        )

        return {

            "portfolio": portfolio_df,

            "benchmark": benchmark_df,

            "history": history,

            "portfolio_return": portfolio_return,

            "benchmark_return": benchmark_return,

            "excess_return": excess_return

        }