import customtkinter as ctk
import json
from menu_page import MenuFrame
from add_entry_page import AddEntryFrame
from setting_page import SettingsFrame
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from translator import Translator
from database import BodyScanDB, DatabaseError
from strategy_page import StrategiesFrame
from add_strategy_page import AddStrategyFrame
from edit_strategy_page import EditStrategyFrame
from view_strategy_page import ViewStrategyFrame
from about_page import AboutFrame
from view_all_scans_page import ViewAllScansFrame
from analysis_page import AnalysisFrame
from edit_entry_page import EditEntryFrame
from PIL import ImageTk
from tkextrafont import Font
from CTkMessagebox import CTkMessagebox


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # TESTING
        self.theme = None
        self.language_selected = None
        self.selected_font = None

        self.get_preferences()

        self.geometry("400x470")

        try:
            img = ImageTk.PhotoImage(file="./img/logo2.png")
            self.wm_iconbitmap()
            self.iconphoto(True, img)
        except FileNotFoundError:
            pass

        fonts_dir = os.path.join(os.path.dirname(__file__), "..", "fonts")
        self.regular_font = Font(file=os.path.join(fonts_dir, "OpenDyslexic3-Regular.ttf"), family="OpenDyslexic3")
        self.bold_font = Font(file=os.path.join(fonts_dir, "OpenDyslexic3-Bold.ttf"), family="OpenDyslexic3")

        self.font_dict = {
            "Default": ("Helvetica", 15),
            "Light": ("Helvetica", 15),
            "Dark": ("Helvetica", 15),
            "Dyslexia": ("OpenDyslexic3", 15),
        }
        self.selected_font = self.font_dict.get(self.theme, ("Helvetica", 20))

        self.translator = Translator()
        self.set_language(self.language_selected, initial_load=True)

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
        self.analysis_frame = AnalysisFrame(self)
        self.edit_entry_frame = EditEntryFrame(self)


    def set_language(self, lang, initial_load=False):
        if lang is None:
            self.translator.set_lang("English")
            self.language_selected = "English"
        else:
            self.translator.set_lang(lang)
            self.language_selected = lang

            db = BodyScanDB()
            try:
                db.change_lang_pref(lang)
            except DatabaseError:
                CTkMessagebox(self, title=self.translator.dictionary["pref_db_error_title"],
                              message=self.translator.dictionary["pref_db_error_message"])
            except Exception as e:
                print("Error: ", e)

            if not initial_load:
                self.refresh_screen()
                self.show_settings()

    def get_preferences(self):
        db = BodyScanDB()
        self.font_dict = {
            "Default": ("Helvetica", 15),
            "Light": ("Helvetica", 15),
            "Dark": ("Helvetica", 15),
            "Dyslexia": ("OpenDyslexic3", 15),
        }

        try:
            data = db.get_user_preferences()
            if data and len(data) > 0:
                self.language_selected = data[0][1]
                self.theme = data[0][2]
                self.selected_font = data[0][2]
            else:
                self.language_selected = "English"
                self.theme = "Default"
        except DatabaseError:
            self.language_selected = "English"
            self.theme = "Default"
        except Exception as e:
            self.language_selected = "English"
            self.theme = "Default"


    def apply_theme_to_frames(self, theme):
        self.theme = theme
        try:
            db = BodyScanDB()
            db.change_theme_pref(theme)
        except DatabaseError:
            CTkMessagebox(self, title=self.translator.dictionary["pref_db_error_title"],
                      message=self.translator.dictionary["pref_db_error_message"])
        except Exception as e:
            print("Error: ", e)

        self.selected_font = self.font_dict[theme]
        if theme == "Light":
            ctk.set_default_color_theme("./styles/light_mode.json")
        elif theme == "Default" or theme is None:
            ctk.set_default_color_theme("blue")
        elif theme == "Dark":
            ctk.set_default_color_theme("./styles/dark_mode.json")
        elif theme == "Dyslexia":
            ctk.set_default_color_theme("./styles/dyslexia_mode.json")
        self.refresh_screen()
        self.get_listbox_style(self.theme)
        self.show_settings()


    def refresh_screen(self):
        self.menu_frame.destroy()
        self.menu_frame = MenuFrame(self)

        self.add_entry_frame.destroy()
        self.add_entry_frame = AddEntryFrame(self)

        self.settings_frame.destroy()
        self.settings_frame = SettingsFrame(self)

        self.about_frame.destroy()
        self.about_frame = AboutFrame(self)

        self.strategies_frame.destroy()
        self.strategies_frame = StrategiesFrame(self)

        self.add_strategy_frame.destroy()
        self.add_strategy_frame = AddStrategyFrame(self)

        self.edit_strategy_frame.destroy()
        self.edit_strategy_frame = EditStrategyFrame(self)

        self.view_strategy_frame.destroy()
        self.view_strategy_frame = ViewStrategyFrame(self)

        self.view_all_scans_frame.destroy()
        self.view_all_scans_frame = ViewAllScansFrame(self)

        self.analysis_frame.destroy()
        self.analysis_frame = AnalysisFrame(self)


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
        self.strategies_frame.reset_frame("to main strategy screen")
        self.strategies_frame.pack(padx=15, pady=15, fill="both", expand=True)


    def view_strategy_level_selected(self, stress_level):
        self.hide_settings()
        self.hide_add_strategy_frame()
        self.hide_edit_strategies_frame()
        self.hide_view_strategy_frame()
        self.strategies_frame.view_strategy_level_selected(stress_level)
        self.strategies_frame.pack(padx=15, pady=15, fill="both", expand=True)


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
        self.view_all_scans_frame.get_all_days_from_db()
        self.view_all_scans_frame.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_view_all_scans_frame(self):
        self.view_all_scans_frame.pack_forget()


    def show_analysis_frame(self):
        self.hide_menu()
        self.analysis_frame.pack(padx=15, pady=15, fill="both", expand=True)
        self.analysis_frame.get_scan_data()


    def hide_analysis_frame(self):
        self.analysis_frame.pack_forget()


    def show_edit_entry_frame(self, scan_id):
        self.hide_view_all_scans_frame()
        self.edit_entry_frame.scan_id = scan_id
        self.edit_entry_frame.get_entry_data()
        self.edit_entry_frame.pack(padx=15, pady=15, fill="both", expand=True)


    def hide_edit_entry_frame(self):
        self.edit_entry_frame.pack_forget()
        self.show_view_all_scans_frame()


    # Light style as default for testing
    def get_listbox_style(self, theme=None):
        if theme is None:
            return
        try:
            with open("./styles/ctklistbox_styles.json", 'r') as f:
                styles = json.load(f)
            return styles.get(theme, styles[theme])
        except FileNotFoundError:
            return {}


app = App()
app.mainloop()
