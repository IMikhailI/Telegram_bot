import sqlite3 as sq


# Speciality = [
#     ("Хирург",),
#     ("Психолог",),
#     ("ВРАЧ",),
#     ("Окулист",),
#     ("Нарколог",),
#     ("Дантист",),
#     ("Терапевт",),
#     ("Спортивный врач",)
# ]

with sq.connect("test_base.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS EVENT")
    cur.execute("""CREATE TABLE IF NOT EXISTS EVENT(
        id NUMBER PRIMARY KEY NOT NULL,
        start_date DATE NOT NULL,
        client_data VARCHAR2(200),
        duration NUMBER NOT NULL,
        worker_id NUMBER,
        event_type_id NUMBER NOT NULL,
        FOREIGN KEY(event_type_id) REFERENCES EVENT_TYPE(id),
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

    cur.execute("DROP TABLE IF EXISTS EVENT_TYPE")
    cur.execute("""CREATE TABLE IF NOT EXISTS EVENT_TYPE(
        id NUMBER PRIMARY KEY NOT NULL,
        name VARCHAR2(150)
        )""")

    cur.execute("DROP TABLE IF EXISTS SPECIALITY")
    cur.execute("""CREATE TABLE IF NOT EXISTS SPECIALITY(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR2(300)
        )""")

    # cur.executemany('INSERT INTO SPECIALITY VALUES(NULL, ?)', Speciality)
