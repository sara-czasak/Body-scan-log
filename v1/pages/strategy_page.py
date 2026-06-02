import customtkinter as ctk
from CTkListbox import *


class StrategiesFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.back_to_menu_button = None
        self.mild_stress_button = None
        self.mid_stress_button = None
        self.high_stress_button = None
        self.strategies_option_menu = None
        self.select_strategy_option_button = None
        self.view_strategies()


    def clear_screen(self):
        self.parent.hide_settings()
        self.parent.hide_menu()


    def view_strategies(self):
        values = [self.parent.translator.dictionary["Add Strategy"],
                  self.parent.translator.dictionary["Edit Strategy"],
                  self.parent.translator.dictionary["Delete Strategy"],]
        self.strategies_option_menu = ctk.CTkOptionMenu(self, values=values)

        self.select_strategy_option_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["option_choice"])

        title = ctk.CTkLabel(self, text=self.parent.translator.dictionary["COPING STRATEGIES"])
        title.pack(padx=5, pady=5)

        self.mild_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["Mild stress strategies"])
        self.mild_stress_button.pack(padx=5, pady=5)

        self.mid_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["Mid stress strategies"])
        self.mid_stress_button.pack(padx=5, pady=5)

        self.high_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["High stress strategies"])
        self.high_stress_button.pack(padx=5, pady=5)


    def add_strategies(self, stress_level):
        self.clear_screen()


    def edit_strategies(self, stress_level):
        self.clear_screen()


    def delete_strategies(self, stress_level):
        self.clear_screen()