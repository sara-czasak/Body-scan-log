import customtkinter as ctk
from menu_page import MenuFrame
from add_entry_page import AddEntryFrame
from setting_page import SettingsFrame
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from translator import Translator
from strategy_page import StrategiesFrame
from add_strategy_page import AddStrategyFrame
from edit_strategy_page import EditStrategyFrame
from view_strategy_page import ViewStrategyFrame
from about_page import AboutFrame
from view_all_scans_page import ViewAllScansFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.translator = Translator("English")
        self.title(self.translator.dictionary["app_title"])
        self.menu_frame = MenuFrame(self)
        self.show_menu()
        self.add_entry_frame = AddEntryFrame(self)
        self.settings_frame = SettingsFrame(self)
        self.about_frame = AboutFrame(self)
        self.strategies_frame = StrategiesFrame(self)
        self.add_strategy_frame = AddStrategyFrame(self)
        self.edit_strategy_frame = EditStrategyFrame(self)
        self.view_strategy_frame = ViewStrategyFrame(self)
        self.view_all_scans_frame = ViewAllScansFrame(self)


    def show_menu(self):
        self.menu_frame.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_menu(self):
        self.menu_frame.pack_forget()


    def show_add_entry(self):
        self.hide_menu()
        self.add_entry_frame.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_add_entry(self):
        self.add_entry_frame.pack_forget()


    def show_settings(self):
        self.hide_menu()
        self.hide_strategies_frame()
        self.settings_frame.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_settings(self):
        self.settings_frame.pack_forget()


    def show_strategies_frame(self):
        self.hide_settings()
        self.hide_add_strategy_frame()
        self.hide_edit_strategies_frame()
        self.hide_view_strategy_frame()
        self.strategies_frame.pack(padx=15, pady=15, fill="both", expand=True)
        self.strategies_frame.show_strategy_screen(self.strategies_frame.current_stress_level)


    def hide_strategies_frame(self):
        self.strategies_frame.pack_forget()


    def show_add_strategy_frame(self, stress_level):
        self.hide_strategies_frame()
        self.add_strategy_frame.pack(padx=15, pady=15, fill="both", expand=True)
        self.add_strategy_frame.stress_level = stress_level


    def hide_add_strategy_frame(self):
        self.add_strategy_frame.pack_forget()


    def show_about(self):
        self.hide_menu()
        self.about_frame.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_about(self):
        self.about_frame.pack_forget()


    def show_edit_strategies_frame(self, stress_level, record_id):
        self.hide_strategies_frame()
        self.edit_strategy_frame.pack(padx=15, pady=15, fill="both", expand=True)
        self.edit_strategy_frame.stress_level = stress_level
        self.edit_strategy_frame.record_id = record_id
        self.edit_strategy_frame.get_entry_data()


    def hide_edit_strategies_frame(self):
        self.edit_strategy_frame.pack_forget()


    def show_view_strategy_frame(self, stress_level, record_id):
        self.hide_strategies_frame()
        self.view_strategy_frame.stress_level = stress_level
        self.view_strategy_frame.record_id = record_id
        self.view_strategy_frame.pack(padx=15, pady=15, fill="both", expand=True)
        self.view_strategy_frame.get_entry_data()


    def hide_view_strategy_frame(self):
        self.view_strategy_frame.pack_forget()


    def show_view_all_scans_frame(self):
        self.hide_menu()
        self.view_all_scans_frame.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_view_all_scans_frame(self):
        self.view_all_scans_frame.pack_forget()


app = App()
app.mainloop()
