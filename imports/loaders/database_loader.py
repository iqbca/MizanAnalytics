import pandas as pd


class DatabaseLoader:

    def __init__(self, engine):
        self.engine = engine

    def load_dataframe(
        self,
        dataframe,
        table_name
    ):

        # Convert all column names to lowercase
        dataframe.columns = dataframe.columns.str.lower()

        dataframe.to_sql(
            table_name.lower(),
            self.engine,
            if_exists="append",
            index=False
        )

        print(
            f"✓ {len(dataframe)} rows loaded into {table_name}"
        )