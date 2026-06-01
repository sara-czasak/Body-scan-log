import customtkinter as ctk
import datetime


class AddEntryFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.scroll_frame = None
        self.today = None
        self.form_title_label = None
        self.date_label = None
        self.date_entry = None
        self.notes_label = None
        self.notes_entry = None
        self.submit_button = None
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
        self.body_part_scores = {}
        self.scan_db_data = {}
        self.body_part_scans_db = {}
        self.layout()


    def layout(self):
        self.form_title_label = ctk.CTkLabel(self, text="NEW ENTRY")
        self.form_title_label.pack(padx=5, pady=5)

        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.pack(padx=5, pady=5)

        # FIELDS:
        self.date_label = ctk.CTkLabel(self.scroll_frame, text="DATE: ")
        self.date_label.pack(padx=5, pady=5)
        self.date_entry = ctk.CTkEntry(self.scroll_frame)

        self.today = datetime.date.today().strftime("%Y-%m-%d")
        self.date_entry.insert(0, self.today)
        self.date_entry.pack(padx=5, pady=5)


        values = [str(i) for i in range(0, 11)]
        # Body part fields
        for i in self.body_part_list:
            body_part_label = ctk.CTkLabel(self.scroll_frame, text=i)
            body_part_label.pack(padx=5, pady=5)
            body_part_entry = ctk.CTkOptionMenu(self.scroll_frame, values=values)
            body_part_entry.pack(padx=5, pady=5)

            self.body_part_scans[i] = body_part_entry

        self.notes_label = ctk.CTkLabel(self.scroll_frame, text="NOTES: ")
        self.notes_label.pack(padx=5, pady=5)
        self.notes_entry = ctk.CTkTextbox(self.scroll_frame, height=160, activate_scrollbars=True)
        self.notes_entry.pack(padx=5, pady=5)

        self.submit_button = ctk.CTkButton(self.scroll_frame, text="SUBMIT ENTRY", command=self.submit_form)
        self.submit_button.pack(padx=5, pady=5)


    def submit_form(self):
        self.get_form_data()


    def get_form_data(self):
        self.scan_db_data['date'] = self.date_entry.get()

        self.scan_db_data["notes"] = self.notes_entry.get("1.0", "end")

        total_values = 0
        total_with_score = 0
        for k, v in self.body_part_scans.items():
            self.body_part_scans_db[k] = int(v.get())
            total_values += int(v.get())
            if self.body_part_scans_db[k] != 0:
                total_with_score += 1

        total_score = 0
        try:
            self.scan_db_data["total_score"] = int(total_values / total_with_score)
        except ZeroDivisionError:
            self.scan_db_data["total_score"] = 0

        self.reset_form()

    def reset_form(self):
        self.date_entry.delete(0, "end")
        self.date_entry.insert(0, self.today)
        self.notes_entry.delete("1.0", "end")
        for k, v in self.body_part_scans.items():
            v.set("0")
