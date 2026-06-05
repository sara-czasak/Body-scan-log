import customtkinter as ctk
from database import BodyScanDB, DuplicateError, DatabaseError
from CTkMessagebox import CTkMessagebox


class EditEntryFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.scroll_frame = None
        self.form_title_label = None
        self.date_label = None
        self.date_entry = None
        self.notes_label = None
        self.notes_entry = None
        self.submit_button = None
        self.back_button = None
        self.body_part_list = [
            "jaw",
            "face",
            "neck",
            "upper back",
            "mid back",
            "lower back",
            "left shoulder",
            "right shoulder",
            "left arm",
            "right arm",
            "chest",
            "stomach",
            "left leg",
            "right leg",
            "left foot",
            "right foot",
        ]
        self.body_part_scans = {}
        self.scan_db_data = {}
        self.body_part_scans_db = {}

        self.scan_id = None
        self.scan_data = None
        self.body_part_readings = {}


    def go_back(self):
        self.reset_form()

        self.scan_id = None
        self.scan_data = None

        if self.scroll_frame is not None:
            self.scroll_frame.pack_forget()
        if self.form_title_label is not None:
            self.form_title_label.pack_forget()
        if self.date_label is not None:
            self.date_label.pack_forget()
        if self.date_entry is not None:
            self.date_entry.pack_forget()
        if self.notes_label is not None:
            self.notes_label.pack_forget()
        if self.notes_entry is not None:
            self.notes_entry.pack_forget()
        if self.submit_button is not None:
            self.submit_button.pack_forget()
        if self.back_button is not None:
            self.back_button.pack_forget()

        self.parent.hide_edit_entry_frame()


    def reset_form(self):
        self.date_entry.delete(0, "end")
        self.date_entry.insert(0, "")
        self.notes_entry.delete("1.0", "end")
        for k, v in self.body_part_scans.items():
            v.destroy()
        self.scan_db_data = {}
        self.body_part_scans_db = {}
        self.body_part_readings = {}


    def create_layout(self):
        if len(self.scan_db_data) > 0 and len(self.body_part_scans_db) > 0:
            self.back_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"], font=self.parent.selected_font, command=self.go_back)
            self.back_button.pack(padx=5, pady=5, fill="both")

            self.form_title_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["edit_entry_title"],
                                                 font=self.parent.selected_font)
            self.form_title_label.pack(padx=5, pady=5, fill="both")

            self.scroll_frame = ctk.CTkScrollableFrame(self)
            self.scroll_frame.pack(padx=5, pady=5, fill="both", expand=True)

            # FIELDS:
            self.date_label = ctk.CTkLabel(self.scroll_frame, text=self.parent.translator.dictionary["date_label"],
                                           font=self.parent.selected_font)
            self.date_label.pack(padx=5, pady=5, fill="both", expand=True)

            self.date_entry = ctk.CTkEntry(self.scroll_frame)
            self.date_entry.insert(0, self.scan_db_data['date'])
            self.date_entry.pack(padx=5, pady=5, fill="both", expand=True)

            values = [str(i) for i in range(0, 11)]
            # Body part fields
            for i in self.body_part_list:
                body_part_label = ctk.CTkLabel(self.scroll_frame, text=self.parent.translator.dictionary[i], font=self.parent.selected_font)
                body_part_label.pack(padx=5, pady=5, fill="both", expand=True)

                body_part_entry = ctk.CTkOptionMenu(self.scroll_frame, values=values)
                body_part_entry.pack(padx=5, pady=5, fill="both", expand=True)

                self.body_part_scans[i] = body_part_entry

                if i.lower() in self.body_part_scans_db.keys():
                    self.body_part_scans[i].set(self.body_part_scans_db[i])


            self.notes_label = ctk.CTkLabel(self.scroll_frame, text=self.parent.translator.dictionary["notes_label"],
                                            font=self.parent.selected_font)
            self.notes_label.pack(padx=5, pady=5, fill="both", expand=True)
            self.notes_entry = ctk.CTkTextbox(self.scroll_frame, height=90, activate_scrollbars=True, wrap="word")
            self.notes_entry.insert("0.0", self.scan_db_data['notes'])
            self.notes_entry.pack(padx=5, pady=5, fill="both", expand=True)

            self.submit_button = ctk.CTkButton(self.scroll_frame, text=self.parent.translator.dictionary["submit_button"], font=self.parent.selected_font, command=self.get_form_data)
            self.submit_button.pack(padx=5, pady=5, fill="both")


    def submit_form(self):
        self.get_form_data()


    def get_entry_data(self):
        # scan data
        db = BodyScanDB()
        scan_data = db.get_scan_by_id(self.scan_id)
        self.scan_db_data['date'] = scan_data[0][1]
        self.scan_db_data['notes'] = scan_data[0][3]

        # body data
        body_data = db.get_body_part_readings_by_scans_id(self.scan_id)
        for part in body_data:
            self.body_part_scans_db[part[2]] = part[3]
        self.create_layout()


    def get_form_data(self):
        self.scan_db_data['date'] = self.date_entry.get()

        self.scan_db_data["notes"] = self.notes_entry.get("1.0", "end")

        total_values = 0
        total_with_score = 0
        for k, v in self.body_part_scans.items():
            if int(v.get()) > 0:
                self.body_part_scans_db[k] = int(v.get())
                total_values += int(v.get())
                if self.body_part_scans_db[k] != 0:
                    total_with_score += 1

        try:
            self.scan_db_data["total_score"] = round(total_values / total_with_score)
        except ZeroDivisionError:
            self.scan_db_data["total_score"] = 0

        self.save_to_db()

        self.reset_form()


    def save_to_db(self):
        db = BodyScanDB()
        try:
            db.update_scan(
                self.scan_id,
                self.scan_db_data["date"],
                self.scan_db_data["total_score"],
                self.scan_db_data["notes"],
                )

            db.delete_body_part_readings_by_scan_id(self.scan_id)

            for k, v in self.body_part_scans_db.items():
                db.insert_body_part_reading(self.scan_id, k, v)

            self.parent.menu_frame.update_button_states()

            self.go_back()
        except DuplicateError:
            CTkMessagebox(self, title=self.parent.translator.dictionary["entry_duplicate_entry_title"],
                          message=self.parent.translator.dictionary["entry_duplicate_entry_message"])
        except DatabaseError:
            CTkMessagebox(self, title=self.parent.translator.dictionary["entry_db_error_title"],
                          message=self.parent.translator.dictionary["entry_db_error_message"])
        except Exception as e:
            print(f"Unexpected error: {e}")