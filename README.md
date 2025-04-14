🔁 Bidirectional ClickHouse & Flat File Data Ingestion Tool

A web-based application that allows data ingestion between ClickHouse and flat files (CSV) with support for JWT authentication, column selection, schema discovery, and record count reporting.

🧩 Features
      Bidirectional data ingestion:

      ClickHouse ➜ Flat File

      Flat File ➜ ClickHouse

      JWT-based ClickHouse authentication

      Column selection from source

      Schema and table discovery

      Record count reporting after ingestion

      Error handling & status messages

      (Bonus) Support for ClickHouse table joins

🏗️ Tech Stack
      Backend: Python (Flask), ClickHouse driver

      Frontend: HTML, CSS, JavaScript (Vanilla)

      Data I/O: CSV, Pandas

      Authentication: JWT (passed via headers)

📁 Project Structure

      project/
      ├── backend/
      │   ├── app.py
      │   ├── clickhouse_client.py
      │   └── flat_file_connector.py
      ├── frontend/
      │   ├── index.html
      │   ├── style.css
      │   └── app.js
      ├
      ├── README.md
      └── requirements.txt

⚙️ Setup Instructions
   ✅ Prerequisites
         Python 3.7+
         Pip package manager

📦 Installation
   Create a virtual environment 

      python -m venv venv
      venv\Scripts\activate
   
   Install dependencies
      pip install -r requirements.txt

🧪 Running the App
   cd backend
   python app.py

   The backend will run at http://127.0.0.1:5000

   Open your browser and go to: http://127.0.0.1:5000/
