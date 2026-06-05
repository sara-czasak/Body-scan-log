import customtkinter as ctk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import BodyScanDB


class ViewStrategyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.record_id = None
        self.stress_level = None
        self.back_to_strategy_page_button = None

        self.name = None
        self.description = None
        self.strategy_scroll_frame = None

        self.data = None


    def go_back(self):
        self.name.configure(text="")
        self.name.pack_forget()
        self.description.configure(text="")
        self.description.pack_forget()
        self.back_to_strategy_page_button.pack_forget()
        self.parent.show_strategies_frame()


    def clear_layout(self):
        if self.back_to_strategy_page_button is not None:
            self.back_to_strategy_page_button.pack_forget()
        if self.name is not None:
            self.name.pack_forget()
        if self.description is not None:
            self.description.pack_forget()
        if self.strategy_scroll_frame is not None:
            self.strategy_scroll_frame.pack_forget()


    def create_layout(self):
        if self.data is not None:
            self.back_to_strategy_page_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"], command=self.go_back, font=self.parent.selected_font)
            self.back_to_strategy_page_button.pack(padx=5, pady=5, fill="both")

            self.strategy_scroll_frame = ctk.CTkScrollableFrame(self)
            self.strategy_scroll_frame.pack(fill="both", expand=True)

            self.name = ctk.CTkLabel(self.strategy_scroll_frame, text=self.data[0][2], font=self.parent.selected_font)
            self.name.pack(padx=5, pady=5, fill="both")
            self.description = ctk.CTkLabel(self.strategy_scroll_frame, text=self.data[0][3], wraplength=300, font=self.parent.selected_font)
            self.description.pack(padx=5, pady=5, fill="both", expand=True)


    def get_entry_data(self):
        db = BodyScanDB()
        self.data = db.fetch_strategy_by_id(self.record_id)
        self.clear_layout()
        self.create_layout()








