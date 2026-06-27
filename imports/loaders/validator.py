import os
import pandas as pd


class CSVValidator:

    def __init__(self, folder):

        self.folder = folder

    def validate_file_exists(self, filename):

        path = os.path.join(self.folder, filename)

        if not os.path.exists(path):
            raise FileNotFoundError(f"{filename} not found.")

        print(f"✓ {filename} found.")

    def validate_not_empty(self, df, filename):

        if df.empty:
            print(f"⚠ {filename} contains no records.")
        else:
            print(f"✓ {filename} contains {len(df)} records.")

    def validate_columns(self, df, required_columns):

        missing = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing:
            raise Exception(
                f"Missing columns: {missing}"
            )

        print("✓ Required columns verified.")