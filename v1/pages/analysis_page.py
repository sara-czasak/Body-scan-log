import customtkinter as ctk
from CTkListbox import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import BodyScanDB


class AnalysisFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.back_to_menu_button = None

        self.layout()


    def back(self):
        self.parent.hide_analysis_frame()
        self.parent.show_menu()


    def layout(self):
        self.back_to_menu_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"],
                                                 command=self.back)
        self.back_to_menu_button.pack(padx=5, pady=5, fill="both")


    def get_random_strategy(self):
        pass


    def get_scan_data(self):
        pass


    def graph_layout(self):
        pass