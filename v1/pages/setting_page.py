import customtkinter as ctk


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.settings_label = None
        self.language_button = None
        self.set_coping_strategies = None
        self.back_button = None
        self.layout()


    def layout(self):
        self.settings_label = ctk.CTkLabel(self, text="SETTINGS")
        self.settings_label.pack(padx=5, pady=5)

        self.back_button = ctk.CTkButton(self, text="BACK", command=self.go_back)
        self.back_button.pack(padx=5, pady=5)

        self.language_button = ctk.CTkButton(self, text="Select Language")
        self.language_button.pack(padx=5, pady=5)

        self.set_coping_strategies = ctk.CTkButton(self, text="Set coping strategies")
        self.set_coping_strategies.pack(padx=5, pady=5)


    def go_back(self):
        self.parent.hide_settings()
        self.parent.show_menu()