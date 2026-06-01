import customtkinter as ctk
from CTkListbox import *


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.language_options = ["English",]
        self.lang_buttons = {}
        self.settings_label = None
        self.language_button = None
        self.set_coping_strategies_button = None
        self.back_to_menu_button = None
        self.back_to_settings_button = None
        self.mild_stress_button = None
        self.mid_stress_button = None
        self.high_stress_button = None
        self.mild_coping_strategies_list = None
        self.mid_coping_strategies_list = None
        self.high_coping_strategies_list = None
        self.back_to_strategies_button = None
        self.strategies_option_menu = None
        self.select_strategy_option_button = None
        self.layout()


    def layout(self):
        self.settings_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["settings"])
        self.settings_label.pack(padx=5, pady=5)

        self.back_to_menu_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"], command=self.go_back_to_menu)
        self.back_to_menu_button.pack(padx=5, pady=5)

        self.language_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["lang_option"], command=self.set_lang)
        self.language_button.pack(padx=5, pady=5)

        self.set_coping_strategies_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["Stress decreasing strategies"], command=self.set_coping_strategies)
        self.set_coping_strategies_button.pack(padx=5, pady=5)

        self.back_to_settings_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"], command=self.go_back_to_settings)


    def set_lang(self):
        self.clear_layout()
        for i in self.language_options:
            option = ctk.CTkButton(self, text=i)
            option.pack(padx=5, pady=5)
            self.lang_buttons[i] = option


    def set_coping_strategies(self):
        self.clear_layout()

        values = [self.parent.translator.dictionary["Add Strategy"],
                  self.parent.translator.dictionary["Edit Strategy"],
                  self.parent.translator.dictionary["Delete Strategy"],]
        self.strategies_option_menu = ctk.CTkOptionMenu(self, values=values)

        self.select_strategy_option_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["option_choice"])

        title = ctk.CTkLabel(self, text=self.parent.translator.dictionary["COPING STRATEGIES"])
        title.pack(padx=5, pady=5)


        self.mild_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["Mild stress strategies"], command=self.mild_coping_strategies_view)
        self.mild_stress_button.pack(padx=5, pady=5)

        self.mid_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["Mid stress strategies"], command=self.mid_coping_strategies_view)
        self.mid_stress_button.pack(padx=5, pady=5)

        self.high_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["High stress strategies"], command=self.high_coping_strategies_view)
        self.high_stress_button.pack(padx=5, pady=5)


    def mild_coping_strategies_view(self):
        self.clear_layout()
        self.back_to_settings_button.pack_forget()
        self.back_to_strategies_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"], command=self.back_to_strategies)
        self.back_to_strategies_button.pack(padx=5, pady=5)

        self.strategies_option_menu.pack(padx=5, pady=5)
        self.strategies_option_menu.set(self.parent.translator.dictionary["strategy_options_menu_default"])
        self.select_strategy_option_button.configure(command = lambda: self.strategy_changes_options(1))
        self.select_strategy_option_button.pack(padx=5, pady=5)

        mild_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Strategies for mild stress:"])
        mild_label.pack(padx=5, pady=5)
        self.mild_coping_strategies_list = CTkListbox(self)
        self.mild_coping_strategies_list.pack(padx=5, pady=5)
        self.mild_coping_strategies_list.insert(0, "Strategie name placeholder")
        self.mild_coping_strategies_list.insert(1, "Strategie name placeholder")
        self.mild_coping_strategies_list.insert(2, "Strategie name placeholder")
        self.mild_coping_strategies_list.insert(3, "Strategie name placeholder")


    def mid_coping_strategies_view(self):
        self.clear_layout()
        self.back_to_settings_button.pack_forget()
        self.back_to_strategies_button = ctk.CTkButton(self, text="BACK", command=self.back_to_strategies)
        self.back_to_strategies_button.pack(padx=5, pady=5)

        self.strategies_option_menu.pack(padx=5, pady=5)
        self.select_strategy_option_button.configure(command=lambda: self.strategy_changes_options(2))
        self.select_strategy_option_button.pack(padx=5, pady=5)

        mid_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Strategies for mid stress:"])
        mid_label.pack(padx=5, pady=5)
        self.mid_coping_strategies_list = CTkListbox(self)
        self.mid_coping_strategies_list.pack(padx=5, pady=5)
        self.mid_coping_strategies_list.insert(0, "Strategie name placeholder")
        self.mid_coping_strategies_list.insert(1, "Strategie name placeholder")
        self.mid_coping_strategies_list.insert(2, "Strategie name placeholder")
        self.mid_coping_strategies_list.insert(3, "Strategie name placeholder")


    def high_coping_strategies_view(self):
        self.clear_layout()
        self.back_to_settings_button.pack_forget()
        self.back_to_strategies_button = ctk.CTkButton(self, text="BACK", command=self.back_to_strategies)
        self.back_to_strategies_button.pack(padx=5, pady=5)

        self.strategies_option_menu.pack(padx=5, pady=5)
        self.select_strategy_option_button.configure(command=lambda: self.strategy_changes_options(3))
        self.select_strategy_option_button.pack(padx=5, pady=5)

        high_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Strategies for high stress:"])
        high_label.pack(padx=5, pady=5)
        self.high_coping_strategies_list = CTkListbox(self)
        self.high_coping_strategies_list.pack(padx=5, pady=5)
        self.high_coping_strategies_list.insert(0, "Strategie name placeholder")
        self.high_coping_strategies_list.insert(1, "Strategie name placeholder")
        self.high_coping_strategies_list.insert(2, "Strategie name placeholder")
        self.high_coping_strategies_list.insert(3, "Strategie name placeholder")


    def strategy_changes_options(self, stress_level):
        selected_stress_level = stress_level
        selected = self.strategies_option_menu.get()
        if selected == "OPTIONS":
            return
        elif selected == "Add Strategy":
            print("add ", selected_stress_level)
        elif selected == "Edit Strategy":
            print("edit ", selected_stress_level)
        elif selected == "Delete Strategy":
            print("delete ", selected_stress_level)
        else:
            return


    def clear_layout(self):
        for i in self.winfo_children():
            i.pack_forget()
        self.back_to_settings_button.pack(padx=5, pady=5)

        if self.strategies_option_menu is not None:
            self.strategies_option_menu.set("OPTIONS")


    def back_to_strategies(self):
        for i in self.winfo_children():
            i.pack_forget()
        self.set_coping_strategies()


    def go_back_to_settings(self):
        for i in self.winfo_children():
            i.pack_forget()
        self.layout()


    def go_back_to_menu(self):
        self.parent.hide_settings()
        self.parent.show_menu()