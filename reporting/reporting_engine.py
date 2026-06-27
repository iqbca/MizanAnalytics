import pandas as pd
from datetime import datetime


class ReportingEngine:

    def prepare(self, results, risk):

        return {

            "executive": self.prepare_executive(results, risk),

            "portfolio": self.prepare_portfolio(results),

            "benchmark": self.prepare_benchmark(results),

            "history": self.prepare_history(results),

            "risk": self.prepare_risk(risk),

            "project": self.prepare_project()

        }

    # -------------------------------------------------
    # Executive Summary
    # -------------------------------------------------

    def prepare_executive(self, results, risk):

        portfolio_value = results["portfolio"]["marketvalue"].sum()

        total_holdings = len(results["portfolio"])

        return pd.DataFrame({

            "Metric": [

                "Portfolio Return",
                "Benchmark Return",
                "Excess Return",
                "Volatility",
                "Sharpe Ratio",
                "Maximum Drawdown",
                "Portfolio Value",
                "Total Holdings"

            ],

            "Value": [

                results["portfolio_return"] * 100,

                results["benchmark_return"] * 100,

                results["excess_return"] * 100,

                risk["volatility"],

                risk["sharpe"],

                risk["max_drawdown"] * 100,

                portfolio_value,

                total_holdings

            ]

        })

    # -------------------------------------------------
    # Portfolio
    # -------------------------------------------------

    def prepare_portfolio(self, results):

        return results["portfolio"].copy()

    # -------------------------------------------------
    # Benchmark
    # -------------------------------------------------

    def prepare_benchmark(self, results):

        return results["benchmark"].copy()

    # -------------------------------------------------
    # Performance History
    # -------------------------------------------------
   
    def prepare_history(self, results):

        history = results["history"].copy()

        history["BenchmarkReturn"] = results["benchmark_return"]

        return history
    # -------------------------------------------------
    # Risk Metrics
    # -------------------------------------------------

    def prepare_risk(self, risk):

        return pd.DataFrame({

            "Metric": [

                "Volatility",
                "Sharpe Ratio",
                "Maximum Drawdown"

            ],

            "Value": [

                risk["volatility"],

                risk["sharpe"],

                risk["max_drawdown"] * 100

            ]

        })

    # -------------------------------------------------
    # Project Information
    # -------------------------------------------------

    def prepare_project(self):

        return pd.DataFrame({

            "Property": [

                "Project",
                "Version",
                "Generated On"

            ],

            "Value": [

                "Mizan Analytics",

                "1.0",

                datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ]

        })