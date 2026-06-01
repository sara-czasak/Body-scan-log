import customtkinter as ctk
from menu_page import MenuFrame
from add_entry_page import AddEntryFrame
from setting_page import SettingsFrame
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from translator import Translator
from strategy_page import StrategiesFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.translator = Translator("English")
        self.title(self.translator.dictionary["app_title"])
        self.menu_frame = MenuFrame(self)
        self.show_menu()
        self.add_entry_frame = AddEntryFrame(self)
        self.settings_frame = SettingsFrame(self)
        self.strategies_frame = StrategiesFrame(self)



    def show_menu(self):
        self.menu_frame.pack(padx=15, pady=15)


    def hide_menu(self):
        self.menu_frame.pack_forget()


    def show_add_entry(self):
        self.hide_menu()
        self.add_entry_frame.pack(padx=15, pady=15)


    def hide_add_entry(self):
        self.add_entry_frame.pack_forget()


    def show_settings(self):
        self.hide_menu()
        self.settings_frame.pack(padx=15, pady=15)


    def hide_settings(self):
        self.settings_frame.pack_forget()


    def show_strategies_frame(self):
        self.hide_settings()
        self.strategies_frame.pack(padx=15, pady=15)


    def hide_strategies_frame(self):
        self.strategies_frame.pack_forget()


app = App()
app.mainloop()
