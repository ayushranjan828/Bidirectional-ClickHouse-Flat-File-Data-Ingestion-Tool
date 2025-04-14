import clickhouse_driver

class ClickHouseClient:
    def __init__(self):
        self.client = None

    def connect(self, config):
        self.client = clickhouse_driver.Client(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['jwt_token']
        )
        self.client.execute('SELECT 1')

    def get_columns(self, config):
        tables = self.client.execute('SHOW TABLES')
        columns = {}
        for table in tables:
            columns[table[0]] = [col[0] for col in self.client.execute(f"DESCRIBE TABLE {table[0]}")]
        return columns

    def to_flatfile(self, columns):
        # Implement data ingestion from ClickHouse to Flat File
        return 1000  # Example count
