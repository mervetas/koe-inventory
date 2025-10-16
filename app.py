from flask import Flask, jsonify, abort, render_template
import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration via environment variables
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASS", "")
DB_NAME = os.environ.get("DB_NAME", "koe_inventory")
DB_PORT = int(os.environ.get("DB_PORT", 3306))

def get_mysql_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            port=DB_PORT
        )
        return conn
    except mysql.connector.Error as err:
        print("MySQL connection error:", err)
        return None

@app.route("/asset/<asset_id>", methods=["GET"])
def get_asset(asset_id):
    conn = get_mysql_connection()
    if conn is None:
        abort(500, "Database connection not available. Check environment variables and DB status.")
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT a.asset_id, a.tag, a.name, a.type, a.serial, a.status,
               u.employee_id, u.full_name, u.department
        FROM assets a
        LEFT JOIN employees u ON a.assigned_to = u.employee_id
        WHERE a.asset_id = %s
    """
    cursor.execute(query, (asset_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if not row:
        return jsonify({"error": "Asset not found"}), 404

    return render_template("asset.html", asset=row)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status":"ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
