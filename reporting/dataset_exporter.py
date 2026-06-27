import os


class DatasetExporter:

    def __init__(self):
        self.folder = "exports"
        os.makedirs(self.folder, exist_ok=True)

    def export(self, report):

        # Executive Summary
        report["executive"].to_csv(
            f"{self.folder}/ExecutiveSummary.csv",
            index=False
        )

        # Holdings
        holdings = report["portfolio"][
            [
                "securityname",
                "weight",
                "DailyReturnPct",
                "ContributionPct"
            ]
        ].rename(
            columns={
                "securityname": "Security",
                "weight": "Weight",
                "DailyReturnPct": "Daily Return",
                "ContributionPct": "Contribution"
            }
        )

        holdings.to_csv(
            f"{self.folder}/Holdings.csv",
            index=False
        )

        # Benchmark
        benchmark = report["benchmark"][
            [
                "securityname",
                "weight",
                "DailyReturnPct",
                "ContributionPct"
            ]
        ].rename(
            columns={
                "securityname": "Security",
                "weight": "Weight",
                "DailyReturnPct": "Daily Return",
                "ContributionPct": "Contribution"
            }
        )

        benchmark.to_csv(
            f"{self.folder}/Benchmark.csv",
            index=False
        )

        # Performance History
        report["history"].to_csv(
            f"{self.folder}/PerformanceHistory.csv",
            index=False
        )

        # Risk Metrics
        report["risk"].to_csv(
            f"{self.folder}/RiskMetrics.csv",
            index=False
        )

        # Project Information
        report["project"].to_csv(
            f"{self.folder}/ProjectInfo.csv",
            index=False
        )

        print("\n✓ Reporting datasets exported.")