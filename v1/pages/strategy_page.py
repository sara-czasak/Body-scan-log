import customtkinter as ctk
from CTkListbox import *


class StrategiesFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


    def clear_screen(self):
        self.parent.hide_settings()
        self.parent.hide_menu()


    def view_strategies(self, stress_level):
        self.clear_screen()


    def add_strategies(self, stress_level):
        self.clear_screen()


    def edit_strategies(self, stress_level):
        self.clear_screen()


    def delete_strategies(self, stress_level):
        self.clear_screen()