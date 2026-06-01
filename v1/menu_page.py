import customtkinter as ctk


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout()


    def layout(self):
        menu_label = ctk.CTkLabel(self, text="MENU")
        menu_label.pack(padx=5, pady=5)

        add_button = ctk.CTkButton(self, text="Add new body scan")
        add_button.pack(padx=5, pady=5)

        view_button = ctk.CTkButton(self, text="View all scans")
        view_button.pack(padx=5, pady=5)

        analyze_button = ctk.CTkButton(self, text="Analyze body scans")
        analyze_button.pack(padx=5, pady=5)

        settings_button = ctk.CTkButton(self, text="Settings")
        settings_button.pack(padx=5, pady=5)

