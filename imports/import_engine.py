from database.db_connection import engine

from imports.loaders.csv_loader import CSVLoader
from imports.loaders.package_validator import PackageValidator
from imports.loaders.database_loader import DatabaseLoader

from database.repositories.security_repository import SecurityRepository


class ImportEngine:

    def __init__(self, folder):

        self.folder = folder

        self.engine = engine

        self.loader = CSVLoader(folder)

        self.validator = PackageValidator(folder)

        self.db = DatabaseLoader(engine)

        self.security_repo = SecurityRepository(engine)

    def run(self):

        print("\nStarting Client Import\n")

        self.validator.validate()

        # -------------------------------------------------
        # 1. Security Master
        # -------------------------------------------------
        security = self.loader.load_csv(
            "SecurityMaster.csv"
        )

        security.columns = security.columns.str.lower()

        self.security_repo.upsert(security)

        # -------------------------------------------------
        # 2. Benchmarks
        # -------------------------------------------------
        benchmarks = self.loader.load_csv(
            "Benchmarks.csv"
        )

        self.db.load_dataframe(
            benchmarks,
            "Benchmarks"
        )

        print(f"✓ {len(benchmarks)} rows loaded into Benchmarks")

        # -------------------------------------------------
        # 3. Portfolio
        # -------------------------------------------------
        portfolio = self.loader.load_csv(
            "Portfolio.csv"
        )

        self.db.load_dataframe(
            portfolio,
            "Portfolio"
        )

        print(f"✓ {len(portfolio)} portfolio imported.")

        # -------------------------------------------------
        # 4. Holdings
        # -------------------------------------------------
        holdings = self.loader.load_csv(
            "Holdings.csv"
        )

        self.db.load_dataframe(
            holdings,
            "Holdings"
        )

        print(f"✓ {len(holdings)} rows loaded into Holdings")

        # -------------------------------------------------
        # 5. Daily Prices
        # -------------------------------------------------
        prices = self.loader.load_csv(
            "DailyPrices.csv"
        )

        self.db.load_dataframe(
            prices,
            "DailyPrices"
        )

        print(f"✓ {len(prices)} rows loaded into DailyPrices")

        # -------------------------------------------------
        # 6. Transactions
        # -------------------------------------------------
        transactions = self.loader.load_csv(
            "Transactions.csv"
        )

        self.db.load_dataframe(
            transactions,
            "Transactions"
        )

        print(f"✓ {len(transactions)} rows loaded into Transactions")

        # -------------------------------------------------
        # 7. Benchmark Constituents
        # -------------------------------------------------
        constituents = self.loader.load_csv(
            "BenchmarkConstituents.csv"
        )

        self.db.load_dataframe(
            constituents,
            "BenchmarkConstituents"
        )

        print(f"✓ {len(constituents)} rows loaded into BenchmarkConstituents")

        # -------------------------------------------------
        # 8. Portfolio Performance
        # -------------------------------------------------
        portfolio_perf = self.loader.load_csv(
            "PortfolioPerformance.csv"
        )

        self.db.load_dataframe(
            portfolio_perf,
            "PortfolioPerformance"
        )

        print(f"✓ {len(portfolio_perf)} rows loaded into PortfolioPerformance")

        # -------------------------------------------------
        # 9. Benchmark Performance
        # -------------------------------------------------
        benchmark_perf = self.loader.load_csv(
            "BenchmarkPerformance.csv"
        )

        self.db.load_dataframe(
            benchmark_perf,
            "BenchmarkPerformance"
        )

        print(f"✓ {len(benchmark_perf)} rows loaded into BenchmarkPerformance")

        print("\nImport Completed Successfully.")