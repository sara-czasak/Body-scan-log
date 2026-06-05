import customtkinter as ctk


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.language_options = ["English", "Polski"]
        self.theme_options = [
            self.parent.translator.dictionary["Default"],
            self.parent.translator.dictionary["Dark"],
            self.parent.translator.dictionary["Light"],
            self.parent.translator.dictionary["Dyslexia"],
        ]
        self.lang_buttons = {}
        self.settings_label = None
        self.language_button = None
        self.set_coping_strategies_button = None
        self.select_theme_pref_button = None
        self.back_to_menu_button = None
        self.back_to_settings_button = None
        self.layout()


    def layout(self):
        self.settings_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["settings"], font=self.parent.selected_font)
        self.settings_label.pack(padx=5, pady=5, fill="both", expand=True)

        self.back_to_menu_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"], command=self.go_back_to_menu, font=self.parent.selected_font)
        self.back_to_menu_button.pack(padx=5, pady=5, fill="both")

        self.language_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["lang_option"], command=self.set_lang, font=self.parent.selected_font)
        self.language_button.pack(padx=5, pady=5, fill="both")

        self.select_theme_pref_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["select_theme"], command=self.choose_theme, font=self.parent.selected_font)
        self.select_theme_pref_button.pack(padx=5, pady=5, fill="both")

        self.set_coping_strategies_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["Stress decreasing strategies"], command=self.parent.show_strategies_frame, font=self.parent.selected_font)
        self.set_coping_strategies_button.pack(padx=5, pady=5, fill="both")

        self.back_to_settings_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"], command=self.go_back_to_settings, font=self.parent.selected_font)


    def set_lang(self):
        self.clear_layout()
        for i in self.language_options:
            option = ctk.CTkButton(self, text=i, command=lambda lang=i: self.get_lang_and_back_to_settings(lang), font=self.parent.selected_font)
            option.pack(padx=5, pady=5, fill="both")
            self.lang_buttons[i] = option


    def get_lang_and_back_to_settings(self, lang):
        self.parent.translator.set_lang(lang)
        self.go_back_to_settings()
        self.parent.set_language(lang)


    def choose_theme(self):
        self.clear_layout()
        for i in self.theme_options:
            option = ctk.CTkButton(self, text=i, command=lambda theme=i: self.parent.apply_theme_to_frames(theme), font=self.parent.selected_font)
            option.pack(padx=5, pady=5, fill="both")


    def clear_layout(self):
        for i in self.winfo_children():
            i.pack_forget()
        self.back_to_settings_button.pack(padx=5, pady=5, fill="both")


    def go_back_to_settings(self):
        for i in self.winfo_children():
            i.pack_forget()
        self.layout()


    def go_back_to_menu(self):
        self.parent.hide_settings()
        self.parent.show_menu()