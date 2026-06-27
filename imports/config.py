REQUIRED_FILES = {

    "SecurityMaster.csv": [
        "SecurityID",
        "SecurityName"
    ],

    "Holdings.csv": [
        "PortfolioID",
        "SecurityID",
        "Weight",
        "MarketValue"
    ],

    "Transactions.csv": [
        "TransactionID",
        "PortfolioID",
        "SecurityID"
    ],

    "DailyPrices.csv": [
        "SecurityID",
        "PriceDate",
        "Price"
    ],

    "Benchmarks.csv": [
        "BenchmarkID",
        "BenchmarkName"
    ],

    "BenchmarkConstituents.csv": [
        "BenchmarkID",
        "SecurityID",
        "Weight"
    ],

    "BenchmarkPerformance.csv": [
        "BenchmarkID",
        "PerformanceDate",
        "Return"
    ],

    "PortfolioPerformance.csv": [
        "PortfolioID",
        "PerformanceDate",
        "Return"
    ],

    "ClientInfo.csv": [
        "ClientID",
        "ClientName"
    ]
}