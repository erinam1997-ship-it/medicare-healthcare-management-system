from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-demo-secret"
DB_PATH = Path(__file__).with_name("medicare.db")


def get_db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialise_database():
    with get_db_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                age INTEGER NOT NULL,
                phone TEXT NOT NULL,
                reason TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.route("/")
def index():
    with get_db_connection() as connection:
        patients = connection.execute(
            "SELECT * FROM patients ORDER BY id DESC"
        ).fetchall()
        total_patients = connection.execute(
            "SELECT COUNT(*) FROM patients"
        ).fetchone()[0]
    return render_template(
        "index.html", patients=patients, total_patients=total_patients
    )


@app.route("/patients/add", methods=["POST"])
def add_patient():
    full_name = request.form.get("full_name", "").strip()
    age_text = request.form.get("age", "").strip()
    phone = request.form.get("phone", "").strip()
    reason = request.form.get("reason", "").strip()

    if not all([full_name, age_text, phone, reason]):
        flash("Please complete every field.", "error")
        return redirect(url_for("index"))

    try:
        age = int(age_text)
        if age < 0 or age > 120:
            raise ValueError
    except ValueError:
        flash("Please enter a valid age between 0 and 120.", "error")
        return redirect(url_for("index"))

    with get_db_connection() as connection:
        connection.execute(
            """INSERT INTO patients (full_name, age, phone, reason)
               VALUES (?, ?, ?, ?)""",
            (full_name, age, phone, reason)
        )

    flash("Patient record added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/patients/<int:patient_id>/delete", methods=["POST"])
def delete_patient(patient_id):
    with get_db_connection() as connection:
        connection.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
    flash("Patient record deleted.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    initialise_database()
    app.run(debug=True)
