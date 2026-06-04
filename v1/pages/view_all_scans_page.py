import customtkinter as ctk
from CTkListbox import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import BodyScanDB


class ViewAllScansFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.listbox_theme = self.parent.theme

        self.back_to_menu_button = None
        self.master_scroll_frame = None
        self.all_scans_list = None
        self.all_entries_list = None
        self.all_title = None
        self.for_day_title = None
        self.see_more_button = None
        self.back_to_all_button = None
        self.notes_display = None
        self.notes_label = None

        self.date = None
        self.rating = None
        self.body_data = None

        self.scan_records = {}
        self.record_notes = {}


    def back(self):
        self.parent.hide_view_all_scans_frame()
        self.parent.show_menu()

    def switch_view(self, view_name):
        if view_name == 'main':
            if self.date is not None:
                self.date = None
            if self.rating is not None:
                self.rating = None
            if self.body_data is not None:
                self.body_data = None
            self.scan_layout()
        if view_name == 'body_data':
            self.body_layout()


    def scan_layout(self):
        self.clean_up()
        self.back_to_menu_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"],
                                                 command=self.back)
        self.back_to_menu_button.pack(padx=15, pady=15, fill="both")

        if len(self.scan_records) > 0:

            self.see_more_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["see_more_button"], command=self.see_records_in_day)
            self.see_more_button.pack(padx=15, pady=15, fill="both")

            self.master_scroll_frame = ctk.CTkScrollableFrame(self)
            self.master_scroll_frame.pack(padx=5, pady=5, fill="both", expand=True)

            self.all_title = ctk.CTkLabel(self.master_scroll_frame, text=self.parent.translator.dictionary["ALL ENTRIES"])
            self.all_title.pack(padx=5, pady=5)

            self.all_scans_list = CTkListbox(self.master_scroll_frame, height=200)

            if self.listbox_theme is not None:
                style = self.parent.get_listbox_style(self.listbox_theme)
                self.all_scans_list.configure(**style)

            self.all_scans_list.pack(padx=5, pady=5, fill="both", expand=True)

            for k, v in self.scan_records.items():
                self.all_scans_list.insert("end", f"{k} | {self.scan_records[k][2]}/10")


    def clean_up(self):
        if self.all_scans_list is not None:
            self.all_scans_list.pack_forget()
        if self.all_entries_list is not None:
            self.all_entries_list.pack_forget()
        if self.all_title is not None:
            self.all_title.pack_forget()
        if self.for_day_title is not None:
            self.for_day_title.pack_forget()
        if self.see_more_button is not None:
            self.see_more_button.pack_forget()
        if self.back_to_menu_button is not None:
            self.back_to_menu_button.pack_forget()
        if  self.master_scroll_frame is not None:
            self.master_scroll_frame.pack_forget()
        if self.back_to_all_button is not None:
            self.back_to_all_button.pack_forget()
        if self.notes_display is not None:
            self.notes_display.pack_forget()
        if self.notes_label is not None:
            self.notes_label.pack_forget()


    def body_layout(self):
        self.clean_up()

        self.back_to_all_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"], command=lambda: self.switch_view('main'))
        self.back_to_all_button.pack(padx=15, pady=15, fill="both")

        if self.body_data is not None:
            self.master_scroll_frame.pack(padx=5, pady=5, fill="both", expand=True)

            self.for_day_title = ctk.CTkLabel(self.master_scroll_frame, text=f"{self.date} | {self.rating}")
            self.for_day_title.pack(padx=5, pady=5)

            self.all_entries_list = CTkListbox(self.master_scroll_frame)

            if self.listbox_theme is not None:
                style = self.parent.get_listbox_style(self.listbox_theme)
                self.all_entries_list.configure(**style)

            self.all_entries_list.pack(padx=5, pady=5, fill="both", expand=True)

            self.notes_label = ctk.CTkLabel(self.master_scroll_frame, text=self.parent.translator.dictionary["notes_label"])
            self.notes_label.pack(padx=5, pady=5)

            for i in self.body_data:
                self.all_entries_list.insert("end", f"{i[2]} | {i[3]}/10")
        if self.record_notes != "":
            self.notes_display = ctk.CTkLabel(self.master_scroll_frame, wraplength=250)
            self.notes_display.configure(text=self.record_notes[self.date])
            self.notes_display.pack(padx=15, pady=15)
            self.all_entries_list.configure(height=180)
        else:
            self.all_entries_list.configure(height=150)


    def get_all_days_from_db(self):
        db = BodyScanDB()
        data = db.get_scan_records_with_dates_ordered()
        for record in data:
            self.scan_records[record[1]] = record
            self.record_notes[record[1]] = record[3]
        self.switch_view("main")


    def see_records_in_day(self):
        if self.all_scans_list.get():
            db = BodyScanDB()
            self.date = self.all_scans_list.get().split("|")[0].strip()
            self.rating = f"{self.scan_records[self.date][2]}/10"
            print(self.all_scans_list.get())
            key = self.scan_records[self.date][0]
            self.body_data = db.get_body_part_readings_by_scans_id(key)
            self.switch_view('body_data')

