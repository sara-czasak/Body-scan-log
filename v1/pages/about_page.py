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

        self.placeholder_header = ctk.CTkLabel(self.scroll_frame, text="SECTION ONE", font=self.parent.label_font)
        self.placeholder_header.pack(padx=5, pady=5, fill="both", expand=True)

        self.placeholder_text_body = ctk.CTkLabel(self.scroll_frame, text="---Placeholder section body text--- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ultrices est vel lorem convallis, auctor varius turpis tincidunt. Cras in mi ac metus interdum lobortis nec porttitor lectus. Donec eu faucibus ex. Vivamus nec sodales odio. Nulla accumsan lacus id egestas rhoncus. Donec id dolor sit amet nulla sagittis hendrerit sed mattis est. Nunc imperdiet nunc eu accumsan aliquam. Quisque vel leo id enim iaculis imperdiet. Etiam tempus neque enim.Quisque eget lorem nec justo lacinia accumsan. Cras pellentesque erat sit amet ipsum rhoncus viverra. Nulla ullamcorper felis nec mollis placerat. Aliquam in posuere diam, quis porta turpis. Mauris sit amet turpis vel dui luctus efficitur sit amet congue velit. Mauris maximus ullamcorper felis, non ullamcorper est porta pharetra. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec accumsan erat dapibus hendrerit dignissim.Donec aliquam efficitur ante, sed laoreet nulla fermentum feugiat. Ut maximus et ligula at interdum. Proin et quam maximus, vehicula nunc at, pellentesque dui. Nam fermentum enim metus. Fusce tincidunt dolor elit, sit amet auctor augue dictum non. Vestibulum gravida sed felis quis pretium. Suspendisse et interdum magna. Donec ac leo nec arcu tincidunt vestibulum ut vitae ligula. Ut sed sapien posuere mauris dictum fringilla sit amet a tortor. Cras id faucibus arcu, a lobortis elit. ", wraplength=300)
        self.placeholder_text_body.pack(padx=5, pady=5, fill="both", expand=True)