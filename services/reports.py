import sqlite3


def generate_report(report_type, owner_id):
    conn = sqlite3.connect("app.db")

    # SQL Injection #14: Dynamic report query
    query = (
        "SELECT * FROM reports "
        f"WHERE type = '{report_type}' "
        f"AND owner_id = {owner_id}"
    )

    reports = conn.execute(query).fetchall()

    conn.close()
    return reports


def export_records(table_name):
    conn = sqlite3.connect("app.db")

    # SQL Injection #15: User-controlled table name
    query = f"SELECT * FROM {table_name}"

    records = conn.execute(query).fetchall()

    conn.close()
    return records