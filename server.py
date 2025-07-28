from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    with open("config.json") as f:
        cfg = json.load(f)
    return psycopg2.connect(
        host=cfg["host"],
        database=cfg["dbname"],
        user=cfg["user"],
        password=cfg["password"]
    )

@app.get("/tables")
def list_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
    tables = cur.fetchall()
    cur.close()
    conn.close()
    return {"tables": [t[0] for t in tables]}