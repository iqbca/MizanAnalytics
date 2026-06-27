from imports.import_engine import ImportEngine
from analytics.analytics_engine import AnalyticsEngine
from analytics.risk_metrics_engine import RiskMetricsEngine
from reporting.reporting_engine import ReportingEngine
from reporting.dataset_exporter import DatasetExporter


class MizanAnalytics:

    def __init__(self):

        self.client_folder = "imports/Gemswire"

    def run(self):

        self.print_banner()

        # ------------------------
        # Import Client Data
        # ------------------------

        importer = ImportEngine(self.client_folder)
        importer.run()

        # ------------------------
        # Analytics
        # ------------------------

        analytics = AnalyticsEngine(importer.engine)
        results = analytics.run()

        # ------------------------
        # Risk Analytics
        # ------------------------

        risk_engine = RiskMetricsEngine()

        risk_results = risk_engine.calculate(
            results["history"]
        )

        # ------------------------
        # Reporting Layer
        # ------------------------

        reporting = ReportingEngine()

        report = reporting.prepare(
            results,
            risk_results
        )

        # ------------------------
        # Export Datasets
        # ------------------------

        exporter = DatasetExporter()

        exporter.export(report)

        # ------------------------
        # Console Output
        # ------------------------

        self.print_results(
            results,
            risk_results
        )

    def print_banner(self):

        print("=" * 60)
        print("MIZAN ANALYTICS PLATFORM")
        print("Version 1.0")
        print("=" * 60)

    def print_results(self, results, risk):

        print("\nAnalytics Complete\n")

        print(
            f"Portfolio Return : {results['portfolio_return']*100:.4f}%"
        )

        print(
            f"Benchmark Return : {results['benchmark_return']*100:.4f}%"
        )

        print(
            f"Excess Return    : {results['excess_return']*100:.4f}%"
        )

        print("\nRisk Metrics\n")

        print(
            f"Volatility       : {risk['volatility']:.6f}"
        )

        print(
            f"Sharpe Ratio     : {risk['sharpe']:.4f}"
        )

        print(
            f"Maximum Drawdown : {risk['max_drawdown']:.4%}"
        )

        print("\nApplication Finished Successfully.")
        
