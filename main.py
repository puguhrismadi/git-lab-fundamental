from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tamu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            instansi TEXT NOT NULL,
            tujuan TEXT NOT NULL,
            no_hp TEXT,
            waktu_kunjungan TEXT
        )
    """)
    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form["nama"]
        instansi = request.form["instansi"]
        tujuan = request.form["tujuan"]
        no_hp = request.form["no_hp"]
        waktu_kunjungan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO tamu (nama, instansi, tujuan, no_hp, waktu_kunjungan)
            VALUES (?, ?, ?, ?, ?)
        """, (nama, instansi, tujuan, no_hp, waktu_
