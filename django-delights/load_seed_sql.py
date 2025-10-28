import sqlite3

with open("delights/sql/seed_data.sql", "r", encoding="utf-8") as f:
    sql = f.read()

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

cursor.executescript(sql)
conn.commit()
conn.close()

print("Seed data loaded successfully.")
