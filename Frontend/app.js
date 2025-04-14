async function connect() {
    const source = document.getElementById('source').value;
    const data = {
        source: source,
        host: document.getElementById('host').value,
        port: document.getElementById('port').value,
        user: document.getElementById('user').value,
        jwt_token: document.getElementById('jwt_token').value,
        file_path: document.getElementById('flatfile').value,
        delimiter: document.getElementById('delimiter').value
    };

    const response = await fetch('/connect', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    });

    const result = await response.json();
    document.getElementById('status').innerText = result.message || result.error;
}

async function ingest() {
    const source = document.getElementById('source').value;
    const target = (source === 'ClickHouse') ? 'FlatFile' : 'ClickHouse';
    const columns = [];  // Fetch selected columns

    const data = {
        source: source,
        target: target,
        columns: columns
    };

    const response = await fetch('/ingest', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    });

    const result = await response.json();
    document.getElementById('status').innerText = result.message || result.error;
}
