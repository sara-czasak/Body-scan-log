import sqlite3
from db_schema import CREATE_SCANS_TABLE, CREATE_BODY_PART_READING_TABLE


def create_database():
    conn = sqlite3.connect('body_scan.db')
    cursor = conn.cursor()
    cursor.execute(CREATE_SCANS_TABLE)
    cursor.execute(CREATE_BODY_PART_READING_TABLE)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()