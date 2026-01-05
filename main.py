from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
import math

app = Flask(__name__)
app.secret_key = "secret-key-buku-tamu"  # wajib untuk flash
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
        conn = get_db_connection()
        conn.execute("""
            INSERT INTO tamu (nama, instansi, tujuan, no_hp, waktu_kunjungan)
            VALUES (?, ?, ?, ?, ?)
        """, (
            request.form["nama"],
            request.form["instansi"],
            request.form["tujuan"],
            request.form["no_hp"],
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        conn.commit()
        conn.close()

        flash("✅ Data tamu berhasil disimpan.", "success")
        return redirect(url_for("index"))

    return render_template("index.html")


@app.route("/tamu")
def tamu_list():
    page = request.args.get("page", 1, type=int)
    limit = 5
    offset = (page - 1) * limit

    conn = get_db_connection()

    total_data = conn.execute("SELECT COUNT(*) FROM tamu").fetchone()[0]
    total_pages = math.ceil(total_data / limit)

    tamu = conn.execute("""
        SELECT * FROM tamu
        ORDER BY waktu_kunjungan DESC
        LIMIT ? OFFSET ?
    """, (limit, offset)).fetchall()

    conn.close()

    return render_template(
        "tamu_list.html",
        tamu=tamu,
        page=page,
        total_pages=total_pages
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
