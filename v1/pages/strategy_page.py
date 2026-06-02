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
        self.back_to_strategies_menu_button = None
        self.strategy_select_title = None
        self.view_strategies_menu()


    def reset_frame(self):
        self.strategy_select_title.pack_forget()
        self.back_to_menu_button.pack_forget()
        self.mild_stress_button.pack_forget()
        self.mid_stress_button.pack_forget()
        self.high_stress_button.pack_forget()


    def view_strategies_menu(self):
        if self.back_to_strategies_menu_button is not None:
            self.back_to_strategies_menu_button.pack_forget()

        values = [self.parent.translator.dictionary["Add Strategy"],
                  self.parent.translator.dictionary["Edit Strategy"],
                  self.parent.translator.dictionary["Delete Strategy"],]
        self.strategies_option_menu = ctk.CTkOptionMenu(self, values=values)

        self.select_strategy_option_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["option_choice"])

        self.strategy_select_title = ctk.CTkLabel(self, text=self.parent.translator.dictionary["COPING STRATEGIES"])
        self.strategy_select_title.pack(padx=5, pady=5)

        self.back_to_menu_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"],
                                                 command=self.parent.show_settings)
        self.back_to_menu_button.pack(padx=5, pady=5)

        self.back_to_strategies_menu_button = ctk.CTkButton(self,
                                                            text=self.parent.translator.dictionary["back_button"], command=self.view_strategies_menu)

        self.mild_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["Mild stress strategies"], command = lambda: self.view_strategy_level_selected(1))
        self.mild_stress_button.pack(padx=5, pady=5)

        self.mid_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["Mid stress strategies"], command = lambda: self.view_strategy_level_selected(2))
        self.mid_stress_button.pack(padx=5, pady=5)

        self.high_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["High stress strategies"], command = lambda: self.view_strategy_level_selected(3))
        self.high_stress_button.pack(padx=5, pady=5)


    def view_strategy_level_selected(self, stress_level):
        print(stress_level)
        if stress_level == 1:
            self.reset_frame()
            self.back_to_strategies_menu_button.pack(padx=5, pady=5)
            print("MILD")
        elif stress_level == 2:
            self.reset_frame()
            self.back_to_strategies_menu_button.pack(padx=5, pady=5)
            print("MID")
        elif stress_level == 3:
            self.reset_frame()
            self.back_to_strategies_menu_button.pack(padx=5, pady=5)
            print("HIGH")
        else:
            pass

    def show_strategy_screen(self):
        pass

    def add_strategies(self, stress_level):
        self.clear_screen()


    def edit_strategies(self, stress_level):
        self.clear_screen()


    def delete_strategies(self, stress_level):
        self.clear_screen()