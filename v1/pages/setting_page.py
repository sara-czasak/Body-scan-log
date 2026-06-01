import customtkinter as ctk


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.language_options = ["English",]
        self.lang_buttons = {}
        self.settings_label = None
        self.language_button = None
        self.set_coping_strategies = None
        self.back_to_menu_button = None
        self.back_to_settings_button = None
        self.layout()


    def layout(self):
        self.settings_label = ctk.CTkLabel(self, text="SETTINGS")
        self.settings_label.pack(padx=5, pady=5)

        self.back_to_menu_button = ctk.CTkButton(self, text="BACK", command=self.go_back_to_menu)
        self.back_to_menu_button.pack(padx=5, pady=5)

        self.language_button = ctk.CTkButton(self, text="Select Language", command=self.set_lang)
        self.language_button.pack(padx=5, pady=5)

        self.set_coping_strategies = ctk.CTkButton(self, text="Set coping strategies")
        self.set_coping_strategies.pack(padx=5, pady=5)

        self.back_to_settings_button = ctk.CTkButton(self, text="BACK", command=self.go_back_to_settings)


    def set_lang(self):
        self.clear_layout()
        for i in self.language_options:
            option = ctk.CTkButton(self, text=i)
            option.pack(padx=5, pady=5)
            self.lang_buttons[i] = option


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