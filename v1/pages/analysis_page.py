import customtkinter as ctk
from CTkListbox import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import BodyScanDB
import random


class AnalysisFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.back_to_menu_button = None
        self.last_week_average = None
        self.get_strategy_button = None

        self.strategy_name_label = None
        self.strategy_description_label = None

        self.average = None

    def back(self):
        self.parent.hide_analysis_frame()
        self.parent.show_menu()


    def clean_up(self):
        if self.strategy_name_label is not None:
            self.strategy_name_label.pack_forget()
        if self.strategy_description_label is not None:
            self.strategy_description_label.pack_forget()


    def layout(self):
        self.back_to_menu_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"],
                                                 command=self.back)
        self.back_to_menu_button.pack(padx=5, pady=5, fill="both")

        self.last_week_average = ctk.CTkLabel(self, text=f"{self.parent.translator.dictionary["last_week_average"]}: {self.average}/10",)
        self.last_week_average.pack(padx=5, pady=5, fill="both")

        self.get_strategy_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["get_strategy_button"], command=self.get_random_strategy)
        self.get_strategy_button.pack(padx=5, pady=5, fill="both")

        self.strategy_name_label = ctk.CTkLabel(self)
        self.strategy_description_label = ctk.CTkLabel(self)


    def get_random_strategy(self):
        if self.average is not None:
            if self.average > 7:
                stress_level = 3
            elif self.average > 3:
                stress_level = 2
            else:
                stress_level = 1

            db = BodyScanDB()
            data = db.get_strategies_by_stress_level(stress_level)
            if len(data) > 0:
                strategy = random.choice(data)
                self.strategy_name_label.configure(text=strategy[2])
                self.strategy_description_label.configure(text=strategy[3])
                self.strategy_name_label.pack(padx=5, pady=5, fill="both")
                self.strategy_description_label.pack(padx=5, pady=5, fill="both")
            else:
                pass


    def get_scan_data(self):
        db = BodyScanDB()
        data = db.get_all_scans()
        total = 0
        for i in data:
            total += i[2]
        try:
            self.average = round(total / len(data))
            self.layout()
        except ZeroDivisionError:
            pass


    def graph_layout(self):
        self.strategy_name_label.pack_forget()
        self.strategy_description_label.pack_forget()