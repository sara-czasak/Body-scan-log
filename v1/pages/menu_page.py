import customtkinter as ctk
from add_entry_page import AddEntryFrame
from setting_page import SettingsFrame


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.layout()


    def layout(self):
        menu_label = ctk.CTkLabel(self, text="MENU")
        menu_label.pack(padx=5, pady=5)

        add_button = ctk.CTkButton(self, text="Add new body scan", command=self.parent.show_add_entry)
        add_button.pack(padx=5, pady=5)

        view_button = ctk.CTkButton(self, text="View all scans")
        view_button.pack(padx=5, pady=5)

        analyze_button = ctk.CTkButton(self, text="Analyze body scans")
        analyze_button.pack(padx=5, pady=5)

        settings_button = ctk.CTkButton(self, text="Settings", command=self.parent.show_settings)
        settings_button.pack(padx=5, pady=5)

        exit_button = ctk.CTkButton(self, text="EXIT", command=self.parent.destroy)
        exit_button.pack(padx=5, pady=5)

