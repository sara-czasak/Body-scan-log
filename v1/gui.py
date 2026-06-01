from tkinter import ttk

import customtkinter as ctk


root = ctk.CTk()
root.title("Body Scan App")
root.geometry("300x300")

# Frame for main menu
main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.pack()

menu_label = ctk.CTkLabel(main_frame, text="MENU")
menu_label.grid(row=0, column=0)






root.mainloop()