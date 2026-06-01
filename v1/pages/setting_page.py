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
        self.strategy_scroll_screen = None
        self.mild_stress_button = None
        self.mid_stress_button = None
        self.high_stress_button = None
        self.mild_coping_strategies_list = None
        self.mid_coping_strategies_list = None
        self.high_coping_strategies_list = None
        self.layout()


    def layout(self):
        self.settings_label = ctk.CTkLabel(self, text="SETTINGS")
        self.settings_label.pack(padx=5, pady=5)

        self.back_to_menu_button = ctk.CTkButton(self, text="BACK", command=self.go_back_to_menu)
        self.back_to_menu_button.pack(padx=5, pady=5)

        self.language_button = ctk.CTkButton(self, text="Select Language", command=self.set_lang)
        self.language_button.pack(padx=5, pady=5)

        self.set_coping_strategies_button = ctk.CTkButton(self, text="Stress decreasing strategies", command=self.set_coping_strategies)
        self.set_coping_strategies_button.pack(padx=5, pady=5)

        self.back_to_settings_button = ctk.CTkButton(self, text="BACK", command=self.go_back_to_settings)


    def set_lang(self):
        self.clear_layout()
        for i in self.language_options:
            option = ctk.CTkButton(self, text=i)
            option.pack(padx=5, pady=5)
            self.lang_buttons[i] = option


    def set_coping_strategies(self):
        self.clear_layout()

        title = ctk.CTkLabel(self, text="COPING STRATEGIES")
        title.pack(padx=5, pady=5)


        self.mild_stress_button = ctk.CTkButton(self, text="Mild stress strategies")
        self.mild_stress_button.pack(padx=5, pady=5)

        self.mid_stress_button = ctk.CTkButton(self, text="Mid stress strategies")
        self.mid_stress_button.pack(padx=5, pady=5)

        self.high_stress_button = ctk.CTkButton(self, text="High stress strategies")
        self.high_stress_button.pack(padx=5, pady=5)

        # self.strategy_scroll_screen = ctk.CTkScrollableFrame(self)
        # self.strategy_scroll_screen.pack(padx=5, pady=5)

        # mild_label = ctk.CTkLabel(self.strategy_scroll_screen, text="Strategies for mild stress:")
        # mild_label.pack(padx=5, pady=5)
        # self.mild_coping_strategies_list = CTkListbox(self.strategy_scroll_screen)
        # self.mild_coping_strategies_list.pack(padx=5, pady=5)
        # self.mild_coping_strategies_list.insert(0, "Strategie name placeholder")
        # self.mild_coping_strategies_list.insert(1, "Strategie name placeholder")
        # self.mild_coping_strategies_list.insert(2, "Strategie name placeholder")
        # self.mild_coping_strategies_list.insert(3, "Strategie name placeholder")
        #
        # mid_label = ctk.CTkLabel(self.strategy_scroll_screen, text="Strategies for mid stress:")
        # mid_label.pack(padx=5, pady=5)
        # self.mid_coping_strategies_list = CTkListbox(self.strategy_scroll_screen)
        # self.mid_coping_strategies_list.pack(padx=5, pady=5)
        # self.mid_coping_strategies_list.insert(0, "Strategie name placeholder")
        # self.mid_coping_strategies_list.insert(1, "Strategie name placeholder")
        # self.mid_coping_strategies_list.insert(2, "Strategie name placeholder")
        # self.mid_coping_strategies_list.insert(3, "Strategie name placeholder")
        #
        #
        # high_label = ctk.CTkLabel(self.strategy_scroll_screen, text="Strategies for high stress:")
        # high_label.pack(padx=5, pady=5)
        # self.high_coping_strategies_list = CTkListbox(self.strategy_scroll_screen)
        # self.high_coping_strategies_list.pack(padx=5, pady=5)
        # self.high_coping_strategies_list.insert(0, "Strategie name placeholder")
        # self.high_coping_strategies_list.insert(1, "Strategie name placeholder")
        # self.high_coping_strategies_list.insert(2, "Strategie name placeholder")
        # self.high_coping_strategies_list.insert(3, "Strategie name placeholder")



    def clear_layout(self):
        for i in self.winfo_children():
            i.pack_forget()
        self.back_to_settings_button.pack(padx=5, pady=5)


    def go_back_to_settings(self):
        for i in self.winfo_children():
            i.pack_forget()
        self.layout()


    def go_back_to_menu(self):
        self.parent.hide_settings()
        self.parent.show_menu()