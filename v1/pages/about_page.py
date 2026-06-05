import customtkinter as ctk


class AboutFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.back_to_menu_button = None
        self.scroll_frame = None

        self.header_what_is_body_scan = None
        self.body_what_is_body_scan = None
        self.header_how_to_scan = None
        self.body_how_to_scan = None
        self.header_how_it_works = None
        self.body_how_it_works = None
        self.header_features = None
        self.body_features = None
        self.header_credit = None
        self.body_credit = None

        self.layout()


    def back(self):
        self.parent.hide_about()
        self.parent.show_menu()


    def layout(self):
        self.back_to_menu_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"],
                                                 command=self.back, font=self.parent.selected_font)
        self.back_to_menu_button.pack(padx=5, pady=5, fill="both")

        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.pack(padx=5, pady=5, fill="both", expand=True)

        self.header_what_is_body_scan = ctk.CTkLabel(self.scroll_frame, text=self.parent.translator.dictionary["about_what_is_body_scan_header"], font=self.parent.selected_font)
        self.header_what_is_body_scan.pack(padx=5, pady=5, fill="both", expand=True)

        self.body_what_is_body_scan = ctk.CTkLabel(self.scroll_frame, text=self.parent.translator.dictionary["about_what_is_body_scan_content"], wraplength=300, font=self.parent.selected_font)
        self.body_what_is_body_scan.pack(padx=5, pady=5, fill="both", expand=True)

        self.header_how_to_scan = ctk.CTkLabel(self.scroll_frame, text=self.parent.translator.dictionary["how_to_body_scan_header"], font=self.parent.selected_font)
        self.header_how_to_scan.pack(padx=5, pady=5, fill="both", expand=True)

        self.body_how_to_scan = ctk.CTkLabel(self.scroll_frame, text=self.parent.translator.dictionary["how_to_body_scan_content"], wraplength=300, font=self.parent.selected_font)
        self.body_how_to_scan.pack(padx=5, pady=5, fill="both", expand=True)

        self.header_how_it_works = ctk.CTkLabel(self.scroll_frame,
                                               text=self.parent.translator.dictionary["how_it_works_header"],
                                               font=self.parent.selected_font)
        self.header_how_it_works.pack(padx=5, pady=5, fill="both", expand=True)

        self.body_how_it_works = ctk.CTkLabel(self.scroll_frame,
                                             text=self.parent.translator.dictionary["how_it_works_content"],
                                             wraplength=300, font=self.parent.selected_font)
        self.body_how_it_works.pack(padx=5, pady=5, fill="both", expand=True)

        self.header_features = ctk.CTkLabel(self.scroll_frame,
                                                text=self.parent.translator.dictionary["features_header"],
                                                font=self.parent.selected_font)
        self.header_features.pack(padx=5, pady=5, fill="both", expand=True)

        self.body_features = ctk.CTkLabel(self.scroll_frame,
                                              text=self.parent.translator.dictionary["features_content"],
                                              wraplength=300, font=self.parent.selected_font)
        self.body_features.pack(padx=5, pady=5, fill="both", expand=True)

        self.header_credit = ctk.CTkLabel(self.scroll_frame,
                                            text=self.parent.translator.dictionary["credit_header"],
                                            font=self.parent.selected_font)
        self.header_credit.pack(padx=5, pady=5, fill="both", expand=True)

        self.body_credit = ctk.CTkLabel(self.scroll_frame,
                                          text=self.parent.translator.dictionary["credit_content"],
                                          wraplength=300, font=self.parent.selected_font)
        self.body_credit.pack(padx=5, pady=5, fill="both", expand=True)