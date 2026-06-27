class BusinessValidator:

    def validate_holdings(self, df):

        print("\nValidating Holdings Business Rules")

        # Rule 1 - Weight between 0 and 100
        invalid = df[
            (df["Weight"] < 0) |
            (df["Weight"] > 100)
        ]

        if len(invalid) == 0:
            print("✓ All weights are valid.")
        else:
            print(f"✗ {len(invalid)} invalid weights found.")

        # Rule 2 - Total weight

        total_weight = df["Weight"].sum()

        if abs(total_weight - 100) < 0.01:
            print("✓ Portfolio weights total 100%.")
        else:
            print(f"⚠ Portfolio weight totals {total_weight:.2f}%")