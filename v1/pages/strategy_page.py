import customtkinter as ctk
from CTkListbox import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import BodyScanDB


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
        self.mild_coping_strategies_list = None
        self.mid_coping_strategies_list = None
        self.high_coping_strategies_list = None
        self.mild_label = None
        self.mid_label = None
        self.high_label = None
        self.view_strategies_menu()
        self.mild_strategies_dict = {}
        self.mid_strategies_dict = {}
        self.high_strategies_dict = {}


    def reset_frame(self, page):
        if page == "to level selected":
            self.strategy_select_title.pack_forget()
            self.back_to_menu_button.pack_forget()
            self.mild_stress_button.pack_forget()
            self.mid_stress_button.pack_forget()
            self.high_stress_button.pack_forget()
        elif page == "to main strategy screen":
            if self.back_to_strategies_menu_button is not None:
                self.back_to_strategies_menu_button.pack_forget()
            if self.strategies_option_menu is not None:
                self.strategies_option_menu.pack_forget()
            if self.select_strategy_option_button is not None:
                self.select_strategy_option_button.pack_forget()
            if self.mild_coping_strategies_list is not None:
                self.mild_coping_strategies_list.pack_forget()
            if self.mid_coping_strategies_list is not None:
                self.mid_coping_strategies_list.pack_forget()
            if self.high_coping_strategies_list is not None:
                self.high_coping_strategies_list.pack_forget()
            if self.mild_label is not None:
                self.mild_label.pack_forget()
            if self.mid_label is not None:
                self.mid_label.pack_forget()
            if self.high_label is not None:
                self.high_label.pack_forget()



    def view_strategies_menu(self):
        self.reset_frame("to main strategy screen")

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
            self.reset_frame("to level selected")
            self.back_to_strategies_menu_button.pack(padx=5, pady=5)
            self.strategies_option_menu.pack(padx=5, pady=5)
            self.select_strategy_option_button.configure(command=lambda: self.get_option(stress_level))
            self.select_strategy_option_button.pack(padx=5, pady=5)
            self.show_strategy_screen(1)
            print("MILD")
        elif stress_level == 2:
            self.reset_frame("to level selected")
            self.back_to_strategies_menu_button.pack(padx=5, pady=5)
            self.strategies_option_menu.pack(padx=5, pady=5)
            self.select_strategy_option_button.configure(command=lambda: self.get_option(stress_level))
            self.select_strategy_option_button.pack(padx=5, pady=5)
            self.show_strategy_screen(2)
            print("MID")
        elif stress_level == 3:
            self.reset_frame("to level selected")
            self.back_to_strategies_menu_button.pack(padx=5, pady=5)
            self.strategies_option_menu.pack(padx=5, pady=5)
            self.select_strategy_option_button.configure(command=lambda: self.get_option(stress_level))
            self.select_strategy_option_button.pack(padx=5, pady=5)
            self.show_strategy_screen(3)
            print("HIGH")
        else:
            pass


    def get_option(self, stress_level):
        option = self.strategies_option_menu.get()
        if option == "Edit Strategy":
            pass
        elif option == "Add Strategy":
            self.add_strategies(stress_level)
        elif option == "Delete Strategy":
            pass


    def show_strategy_screen(self, stress_level):
        if stress_level == 1:
            self.mild_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Strategies for mild stress:"])
            self.mild_label.pack(padx=5, pady=5)
            self.mild_coping_strategies_list = CTkListbox(self)
            self.mild_coping_strategies_list.pack(padx=5, pady=5)
            data = self.get_strategies_name_list(stress_level)
            for i in data:
                self.mild_strategies_dict[i[0]] = i[2]
                self.mild_coping_strategies_list.insert(i[0], i[2])
        elif stress_level == 2:
            self.mid_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Strategies for mid stress:"])
            self.mid_label.pack(padx=5, pady=5)
            self.mid_coping_strategies_list = CTkListbox(self)
            self.mid_coping_strategies_list.pack(padx=5, pady=5)
            data = self.get_strategies_name_list(stress_level)
            for i in data:
                self.mid_strategies_dict[i[0]] = i[2]
                self.mid_coping_strategies_list.insert(i[0], i[2])
        elif stress_level == 3:
            self.high_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Strategies for high stress:"])
            self.high_label.pack(padx=5, pady=5)
            self.high_coping_strategies_list = CTkListbox(self)
            self.high_coping_strategies_list.pack(padx=5, pady=5)
            data = self.get_strategies_name_list(stress_level)
            for i in data:
                self.high_strategies_dict[i[0]] = i[2]
                self.high_coping_strategies_list.insert(i[0], i[2])
        else:
            pass


    def get_strategies_name_list(self, stress_level):
        db = BodyScanDB()
        data = db.get_strategies_by_stress_level(stress_level)
        return data


    def add_strategies(self, stress_level):
        self.parent.show_add_strategy_frame(stress_level)


    def edit_strategies(self, stress_level):
        pass


    def delete_strategies(self, stress_level):
        pass