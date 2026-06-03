import customtkinter as ctk


class AboutFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.back_to_menu_button = None
        self.scroll_frame = None

        self.placeholder_header = None
        self.placeholder_text_body = None

        self.layout()


    def back(self):
        self.parent.hide_about()
        self.parent.show_menu()


    def layout(self):
        self.back_to_menu_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"],
                                                 command=self.back)
        self.back_to_menu_button.pack(padx=5, pady=5, fill="both")

        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.pack(padx=5, pady=5, fill="both", expand=True)

        self.placeholder_header = ctk.CTkLabel(self.scroll_frame, text="SECTION ONE")
        self.placeholder_header.pack(padx=5, pady=5, fill="both", expand=True)

        self.placeholder_text_body = ctk.CTkLabel(self.scroll_frame, text="Placeholder section body text", wraplength=250)
        self.placeholder_text_body.pack(padx=5, pady=5, fill="both", expand=True)