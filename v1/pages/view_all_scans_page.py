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
        self.back_to_menu_button = None
        self.master_scroll_frame = None
        self.scroll_frame_all_entries = None
        self.scroll_frame_all_entries_on_day = None
        self.all_entries_list = None
        self.all_title = None
        self.for_day_title = None
        self.see_more_button = None

        self.layout()


    def back(self):
        self.parent.hide_view_all_scans_frame()
        self.parent.show_menu()


    def layout(self):
        self.back_to_menu_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"],
                                                 command=self.back)
        self.back_to_menu_button.pack(padx=15, pady=15, fill="both")

        self.see_more_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["see_more_button"],)
        self.see_more_button.pack(padx=15, pady=15, fill="both")

        self.master_scroll_frame = ctk.CTkScrollableFrame(self)
        self.master_scroll_frame.pack(padx=5, pady=5, fill="both", expand=True)

        self.scroll_frame_all_entries = ctk.CTkScrollableFrame(self.master_scroll_frame)
        self.scroll_frame_all_entries.pack(padx=5, pady=5, fill="both")

        self.all_title = ctk.CTkLabel(self.scroll_frame_all_entries, text=self.parent.translator.dictionary["ALL ENTRIES"])
        self.all_title.pack(padx=15, pady=15)

        self.scroll_frame_all_entries_on_day = ctk.CTkScrollableFrame(self.master_scroll_frame)
        # self.scroll_frame_all_entries_on_day.pack(padx=5, pady=5, fill="both")

        self.for_day_title = ctk.CTkLabel(self.scroll_frame_all_entries_on_day, text="---DATE PLACEHOLDER---")
        # self.for_day_title.pack(padx=15, pady=15)
