import sqlite3 as sq


with sq.connect("test_base.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS EVENT")
    cur.execute("""CREATE TABLE IF NOT EXISTS EVENT(
        id NUMBER PRIMARY KEY NOT NULL,
        start_date datetime NOT NULL,
        client_data VARCHAR2(200),
        worker_id NUMBER,
        FOREIGN KEY(worker_id) REFERENCES WORKER(id)
        )""")

    cur.execute("DROP TABLE IF EXISTS WORKER")
    cur.execute("""CREATE TABLE IF NOT EXISTS WORKER(
        id NUMBER PRIMARY KEY NOT NULL,
        sur_name VARCHAR2(200),
        first_name VARCHAR2(100),
        patr_name VARCHAR2(100),
        speciality_id NUMBER,
        FOREIGN KEY(speciality_id) REFERENCES SPECIALITY(id)
        )""")

    cur.execute("DROP TABLE IF EXISTS SPECIALITY")
    cur.execute("""CREATE TABLE IF NOT EXISTS SPECIALITY(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR2(300)
        )""")
