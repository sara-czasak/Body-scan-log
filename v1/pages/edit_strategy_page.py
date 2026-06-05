import customtkinter as ctk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import BodyScanDB, DuplicateError


class EditStrategyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.record_id = None
        self.stress_level = None
        self.back_to_strategy_page_button = None

        self.title = None
        self.strategy_name_label = None
        self.strategy_name_entry = None
        self.strategy_description_label = None
        self.strategy_description_entry = None
        self.save_edit_strategy_button = None
        self.data = None


    def clear_layout(self):
        if self.back_to_strategy_page_button is not None:
            self.back_to_strategy_page_button.pack_forget()
        if self.title is not None:
            self.title.pack_forget()
        if self.strategy_name_label is not None:
            self.strategy_name_label.pack_forget()
        if self.strategy_description_label is not None:
            self.strategy_description_label.pack_forget()
        if self.strategy_description_entry is not None:
            self.strategy_description_entry.pack_forget()
        if self.strategy_name_entry is not None:
            self.strategy_name_entry.pack_forget()
        if self.save_edit_strategy_button is not None:
            self.save_edit_strategy_button.pack_forget()


    def go_back(self):
        self.strategy_description_entry.delete("1.0", "end")
        self.strategy_name_entry.delete(0, "end")
        self.parent.view_strategy_level_selected(self.stress_level)


    def create_layout(self):
        if self.data is not None:
            self.title = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Edit Strategy"], font=self.parent.selected_font)
            self.title.pack(padx=5, pady=5, fill="both", expand=True)

            self.back_to_strategy_page_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"],
                                                     command=self.go_back, font=self.parent.selected_font)
            self.back_to_strategy_page_button.pack(padx=5, pady=5, fill="both")

            self.strategy_name_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Strategy Name"], font=self.parent.selected_font)
            self.strategy_name_label.pack(padx=5, pady=5, fill="both", expand=True)

            self.strategy_name_entry = ctk.CTkEntry(self)
            self.strategy_name_entry.insert(0, self.data[0][2])
            self.strategy_name_entry.pack(padx=5, pady=5, fill="both", expand=True)

            self.strategy_description_label = ctk.CTkLabel(self, text=self.parent.translator.dictionary["Strategy Description"], font=self.parent.selected_font)
            self.strategy_description_label.pack(padx=5, pady=5, fill="both", expand=True)

            self.strategy_description_entry = ctk.CTkTextbox(self, height=160, activate_scrollbars=True, wrap="word")
            self.strategy_description_entry.pack(padx=5, pady=5, fill="both", expand=True)
            self.strategy_description_entry.insert("1.0", self.data[0][3])

            self.save_edit_strategy_button = ctk.CTkButton(
                self,
                text=self.parent.translator.dictionary["submit_strategy"], command=self.save_edit_and_return, font=self.parent.selected_font)
            self.save_edit_strategy_button.pack(padx=5, pady=5, fill="both")


    def get_entry_data(self):
        db = BodyScanDB()
        self.data = db.fetch_strategy_by_id(self.record_id)
        self.clear_layout()
        self.create_layout()


    def save_edit_and_return(self):
        db = BodyScanDB()
        try:
            db.update_record_by_id(
                self.record_id,
                self.strategy_name_entry.get(),
                self.strategy_description_entry.get("1.0", "end")
            )
            self.strategy_description_entry.delete("1.0", "end")
            self.strategy_name_entry.delete(0, "end")
            self.parent.show_strategies_frame()
        except DuplicateError:
            print("This strategy already exists!")
        except Exception as e:
            print("Error: ", e)




