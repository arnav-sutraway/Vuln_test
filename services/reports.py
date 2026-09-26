import sqlite3


def generate_report(report_type, owner_id):
    conn = sqlite3.connect("app.db")

    query = "SELECT * FROM reports WHERE type = ? AND owner_id = ?"

    reports = conn.execute(query, (report_type, owner_id)).fetchall()

    conn.close()
    return reports


def export_records(table_name):
    conn = sqlite3.connect("app.db")

    allowed_tables = {"users", "products", "reports", "comments", "audit_logs"}
    if table_name not in allowed_tables:
        raise ValueError("Unsupported table name")
    query = f"SELECT * FROM {table_name}"

    records = conn.execute(query).fetchall()

    conn.close()
    return records