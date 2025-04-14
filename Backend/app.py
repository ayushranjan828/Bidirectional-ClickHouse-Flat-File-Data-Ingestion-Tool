from flask import Flask, request, jsonify
from clickhouse_connector import ClickHouseClient
from flat_file_connector import FlatFileClient

from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../Frontend', static_url_path='')

# Initialize clients
clickhouse_client = ClickHouseClient()
flatfile_client = FlatFileClient()

#--------------------------------
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/connect', methods=['POST'])
def connect():
    try:
        source = request.json.get('source')
        if source == 'ClickHouse':
            clickhouse_client.connect(request.json)
            return jsonify({"message": "Connected to ClickHouse successfully"}), 200
        elif source == 'FlatFile':
            flatfile_client.connect(request.json)
            return jsonify({"message": "Connected to Flat File successfully"}), 200
        else:
            return jsonify({"message": "Invalid source selected"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/load_columns', methods=['POST'])
def load_columns():
    try:
        source = request.json.get('source')
        if source == 'ClickHouse':
            columns = clickhouse_client.get_columns(request.json)
            return jsonify({"columns": columns}), 200
        elif source == 'FlatFile':
            columns = flatfile_client.get_columns(request.json)
            return jsonify({"columns": columns}), 200
        else:
            return jsonify({"message": "Invalid source selected"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ingest', methods=['POST'])
def ingest():
    try:
        source = request.json.get('source')
        target = request.json.get('target')
        columns = request.json.get('columns')
        if source == 'ClickHouse' and target == 'FlatFile':
            count = clickhouse_client.to_flatfile(columns)
        elif source == 'FlatFile' and target == 'ClickHouse':
            count = flatfile_client.to_clickhouse(columns)
        else:
            return jsonify({"message": "Invalid source/target combination"}), 400
        return jsonify({"message": f"Data ingestion successful. {count} records processed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
