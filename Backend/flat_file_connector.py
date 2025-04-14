import pandas as pd

class FlatFileClient:
    def __init__(self):
        self.data = None

    def connect(self, config):
        self.data = pd.read_csv(config['file_path'], delimiter=config['delimiter'])

    def get_columns(self, config):
        return list(self.data.columns)

    def to_clickhouse(self, columns):
        # Implement data ingestion from Flat File to ClickHouse
        return 1000  # Example count
