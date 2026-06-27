from imports.loaders.business_validator import BusinessValidator
from imports.config import REQUIRED_FILES
from imports.loaders.csv_loader import CSVLoader
from imports.loaders.validator import CSVValidator


class PackageValidator:

    def __init__(self, folder):

        self.loader = CSVLoader(folder)
        self.validator = CSVValidator(folder)
        self.business = BusinessValidator()

    def validate(self):

        print("\nValidating Client Package\n")

        for file, columns in REQUIRED_FILES.items():

            self.validator.validate_file_exists(file)

            df = self.loader.load_csv(file)

            self.validator.validate_not_empty(df, file)

            self.validator.validate_columns(
                df,
                columns
            )
            
            if file == "Holdings.csv":
                self.business.validate_holdings(df)

        print("\nClient Package Validation Complete.\n")