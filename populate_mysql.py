import mysql.connector, os, sys
sql_file = os.path.join(os.path.dirname(__file__), "db_init.sql")
with open(sql_file, "r") as f:
    sql = f.read()

from mysql.connector import errorcode

config = {
    "host": os.environ.get("DB_HOST","localhost"),
    "user": os.environ.get("DB_USER","root"),
    "password": os.environ.get("DB_PASS",""),
    "port": int(os.environ.get("DB_PORT",3306))
}

try:
    cnx = mysql.connector.connect(host=config["host"], user=config["user"], password=config["password"], port=config["port"])
    cursor = cnx.cursor()
    for stmt in sql.split(";"):
        s = stmt.strip()
        if s:
            cursor.execute(s)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Database initialized.")
except Exception as e:
    print("Error initializing DB:", e)
    sys.exit(1)
