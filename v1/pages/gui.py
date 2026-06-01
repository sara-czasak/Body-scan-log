import customtkinter as ctk
from menu_page import MenuFrame
from add_entry_page import AddEntryFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Body Scan Log")
        self.menu_frame = MenuFrame(self)
        self.show_menu()
        self.add_entry_frame = AddEntryFrame(self)


    def show_menu(self):
        self.menu_frame.pack(padx=15, pady=15)


    def hide_menu(self):
        self.menu_frame.pack_forget()


    def show_add_entry(self):
        self.hide_menu()
        self.add_entry_frame.pack(padx=15, pady=15)


    def hide_add_entry(self):
        self.add_entry_frame.pack_forget()





app = App()
app.mainloop()
