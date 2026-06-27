import os
import pandas as pd


class CSVLoader:

    def __init__(self, folder):

        self.folder = folder

    def load_csv(self, filename):

        path = os.path.join(self.folder, filename)

        if not os.path.exists(path):
            raise FileNotFoundError(f"{filename} not found.")

        df = pd.read_csv(path)

        print(f"{filename} loaded successfully.")

        return df       