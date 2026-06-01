import sqlite3
from db_schema import CREATE_SCANS_TABLE, CREATE_BODY_PART_READING_TABLE


class BodyScanDB:
    def __init__(self):
        self.create_database()


    def get_connection(self):
        conn = sqlite3.connect('body_scan.db')
        conn.execute("PRAGMA foreign_keys = ON")
        return conn


    def create_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(CREATE_SCANS_TABLE)
        cursor.execute(CREATE_BODY_PART_READING_TABLE)
        conn.commit()
        conn.close()


    def insert_scan(self, date, overall_score, notes=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scans (date, overall_score, notes) VALUES (?, ?, ?)", (date, overall_score, notes))
        conn.commit()
        conn.close()


    def insert_body_part_reading(self, scan_id, body_part, score):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO body_part_reading (scan_id, body_part, score) VALUES (?, ?, ?)", (scan_id, body_part, score))
        conn.commit()
        conn.close()





if __name__ == '__main__':
    # create_database()
    # insert_scan("2026-05-27", 7)
    # insert_scan("2026-05-28", 3)
    # insert_scan("2026-05-29", 2)
    # insert_scan("2026-05-30", 5)
    # insert_scan("2026-05-31", 7)
    # insert_body_part_reading(2, "jaw", 3)
    # insert_body_part_reading(2, "shoulders", 3)
    # insert_body_part_reading(3, "upper back", 2)
    # insert_body_part_reading(3, "neck", 2)
    #
    # insert_body_part_reading(4, "upper back", 2)
    # insert_body_part_reading(4, "jaw", 2)
    # insert_body_part_reading(4, "stomach", 2)
    # insert_body_part_reading(4, "shoulders", 2)
    #
    # insert_body_part_reading(5, "upper back", 7)
    # insert_body_part_reading(5, "jaw", 7)
    # insert_body_part_reading(5, "shoulders", 7)
    pass