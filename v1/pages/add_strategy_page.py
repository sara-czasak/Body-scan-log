import customtkinter as ctk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import BodyScanDB


class AddStrategyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.back_to_strategy_page_button = None

        self.title = None
        self.strategy_name_label = None
        self.strategy_name_entry = None
        self.strategy_description_label = None
        self.strategy_description_entry = None
        self.add_strategy_button = None
        self.stress_level = None

        self.create_layout()


    def create_layout(self):
        self.title = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Add new strategy"])
        self.title.pack(padx=5, pady=5)

        self.back_to_strategy_page_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"],
                                                 command=self.parent.show_strategies_frame)
        self.back_to_strategy_page_button.pack(padx=5, pady=5)

        self.strategy_name_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Strategy Name"])
        self.strategy_name_label.pack(padx=5, pady=5)

        self.strategy_name_entry = ctk.CTkEntry(self)
        self.strategy_name_entry.pack(padx=5, pady=5)

        self.strategy_description_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Strategy Description"])
        self.strategy_description_label.pack(padx=5, pady=5)

        self.strategy_description_entry = ctk.CTkTextbox(self, height=160, activate_scrollbars=True)
        self.strategy_description_entry.pack(padx=5, pady=5)

        self.add_strategy_button = ctk.CTkButton(
            self,
            text=self.parent.translator.dictionary["submit_strategy"], command=self.gather_data_to_submit)
        self.add_strategy_button.pack(padx=5, pady=5)


    def gather_data_to_submit(self):
        name = self.strategy_name_entry.get()
        description = self.strategy_description_entry.get("1.0", "end")

        if name != "" and description != "":
            db = BodyScanDB()
            db.insert_stress_decrease_strategy(
                self.stress_level,
                name,
                description,
            )
            self.strategy_description_entry.delete("1.0", "end")
            self.strategy_name_entry.delete(0, "end")
            self.parent.show_strategies_frame()
        else:
            pass


