import numpy as np
import pandas as pd


class RiskMetricsEngine:

    def calculate(self, history):

        returns = pd.to_numeric(
            history["portfolioreturn"],
            errors="coerce"
        )

        # Remove blanks/invalid values
        returns = returns.dropna()

        # If returns are stored as percentages (e.g. 1.25),
        # convert them to decimals (0.0125)
        if returns.abs().max() > 1:
            returns = returns / 100

        if len(returns) < 2:
            return {
                "volatility": 0,
                "sharpe": 0,
                "max_drawdown": 0
            }

        volatility = returns.std()

        if np.isnan(volatility) or volatility == 0:
            sharpe = 0
        else:
            sharpe = returns.mean() / volatility

        cumulative = (1 + returns).cumprod()

        running_max = cumulative.cummax()

        drawdown = (cumulative - running_max) / running_max

        max_drawdown = drawdown.min()

        return {
            "volatility": float(volatility),
            "sharpe": float(sharpe),
            "max_drawdown": float(max_drawdown)
        }