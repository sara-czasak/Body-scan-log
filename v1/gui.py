import customtkinter as ctk
from menu_page import MenuFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Body Scan Log")
        self.menu_frame = MenuFrame(self)
        self.menu_frame.pack(padx=15, pady=15)





app = App()
app.mainloop()
