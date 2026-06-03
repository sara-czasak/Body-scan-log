import sqlite3
from sqlite3 import IntegrityError, OperationalError
from db_schema import CREATE_SCANS_TABLE, CREATE_BODY_PART_READING_TABLE, CREATE_STRESS_DECREASE_TABLE


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
        try:
            cursor.execute(CREATE_SCANS_TABLE)
            cursor.execute(CREATE_BODY_PART_READING_TABLE)
            cursor.execute(CREATE_STRESS_DECREASE_TABLE)
        except OperationalError:
            print("Something went wrong")
        conn.commit()
        conn.close()


    def insert_scan(self, date, overall_score, notes=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO scans (date, overall_score, notes) VALUES (?, ?, ?)", (date, overall_score, notes))
            scan_id = cursor.lastrowid
            return scan_id
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Something went wrong")
        finally:
            conn.commit()
            conn.close()
        return None


    def insert_body_part_reading(self, scan_id, body_part, score):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO body_part_reading (scan_id, body_part, score) VALUES (?, ?, ?)", (scan_id, body_part, score))
        except IntegrityError:
            print("IntegrityError")
        except OperationalError:
            print("Something went wrong")
        finally:
            conn.commit()
            conn.close()


    def insert_stress_decrease_strategy(self, stress_level, strategy_name, strategy_description):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO stress_manager (stress_level, strategy_name, strategy_description) VALUES (?, ?, ?)", (stress_level, strategy_name, strategy_description))
        except IntegrityError:
            print("Duplicate stress strategy name")
        except OperationalError:
            print("something went wrong")
        finally:
            conn.commit()
            conn.close()


    def get_strategies_by_stress_level(self, level):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM stress_manager WHERE stress_level = ?", (level,))
            data = cursor.fetchall()
            return data
        except OperationalError:
            print("Something went wrong")
        finally:
            conn.close()
        return None


    def delete_strategy_by_id(self, strategy_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM stress_manager WHERE id = ?", (strategy_id,))
        except OperationalError:
            print("something went wrong")
        finally:
            conn.commit()
            conn.close()


    def fetch_strategy_by_id(self, strategy_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM stress_manager WHERE id = ?", (strategy_id,))
            data = cursor.fetchall()
            return data
        except OperationalError:
            print("Something went wrong")
        finally:
            conn.close()
        return None



    def update_record_by_id(self, strategy_id, strategy_name, strategy_description):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE stress_manager SET strategy_name = ?, strategy_description = ? WHERE id = ?", (strategy_name, strategy_description, strategy_id))
        except IntegrityError:
            print("Duplicate stress strategy name")
        except OperationalError:
            print("something went wrong")
        finally:
            conn.commit()
            conn.close()


    def get_all_scans(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM scans")
            data = cursor.fetchall()
            return data
        except OperationalError:
            print("Something went wrong")
        finally:
            conn.close()
        return None



    def get_body_part_readings_by_scans_id(self, scan_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM body_part_reading WHERE scan_id = ?", (scan_id,))
            data = cursor.fetchall()
            return data
        except OperationalError:
            print("Something went wrong")
        finally:
            conn.close()
        return None



    def get_scan_records_last_10_days_with_dates_ordered(self, date_from, date_to):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM scans WHERE date BETWEEN ? AND ? ORDER BY date ASC", (date_from, date_to))
            data = cursor.fetchall()
            return data
        except OperationalError:
            print("Something went wrong")
        finally:
            conn.close()
        return None


    def get_scan_records_with_dates_ordered(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM scans ORDER BY date ASC")
            data = cursor.fetchall()
            return data
        except OperationalError:
            print("Something went wrong")
        finally:
            conn.close()
        return None

