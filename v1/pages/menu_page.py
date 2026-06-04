import customtkinter as ctk


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.layout()


    def layout(self):
        menu_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["menu_title"], font=self.parent.label_font)
        menu_label.pack(padx=5, pady=5, fill="both", expand=True)

        add_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["add_menu_opt"], command=self.parent.show_add_entry)
        add_button.pack(padx=5, pady=5, fill="both")

        view_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["view_all_menu_optn"], command=self.parent.show_view_all_scans_frame)
        view_button.pack(padx=5, pady=5, fill="both")

        analyze_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["analyze_menu_opt"], command=self.parent.show_analysis_frame)
        analyze_button.pack(padx=5, pady=5, fill="both")

        settings_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["settings"], command=self.parent.show_settings)
        settings_button.pack(padx=5, pady=5, fill="both")

        about_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["about"], command=self.parent.show_about)
        about_button.pack(padx=5, pady=5, fill="both")

        exit_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["exit_button"], command=self.parent.destroy)
        exit_button.pack(padx=5, pady=5, fill="both")

