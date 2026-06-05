import customtkinter as ctk
from CTkListbox import *
from database import BodyScanDB, DatabaseError
from CTkMessagebox import CTkMessagebox


class StrategiesFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.listbox_theme = self.parent.theme
        self.back_to_menu_button = None
        self.mild_stress_button = None
        self.mid_stress_button = None
        self.high_stress_button = None
        self.strategies_option_menu = None
        self.select_strategy_option_button = None
        self.back_to_strategies_menu_button = None
        self.strategy_select_title = None
        self.strategy_list = None
        self.strategy_label = None
        self.current_stress_level = None
        self.view_strategies_menu()
        self.mild_strategies_dict = {}
        self.mid_strategies_dict = {}
        self.high_strategies_dict = {}


    def reset_frame(self, page):
        if page == "to level selected":
            self.strategy_select_title.pack_forget()
            self.back_to_menu_button.pack_forget()
            self.mild_stress_button.pack_forget()
            self.mid_stress_button.pack_forget()
            self.high_stress_button.pack_forget()
            self.back_to_strategies_menu_button.pack_forget()
            self.strategies_option_menu.pack_forget()
            self.select_strategy_option_button.pack_forget()
            self.strategy_label.pack_forget()
            self.strategy_list.pack_forget()
        elif page == "to main strategy screen":
            if self.back_to_strategies_menu_button is not None:
                self.back_to_strategies_menu_button.pack_forget()
            if self.strategies_option_menu is not None:
                self.strategies_option_menu.pack_forget()
            if self.select_strategy_option_button is not None:
                self.select_strategy_option_button.pack_forget()
            if self.strategy_list is not None:
                self.strategy_list.pack_forget()
            if self.strategy_label is not None:
                self.strategy_label.pack_forget()
            if self.strategy_select_title is not None:
                self.strategy_select_title.pack(padx=5, pady=5, fill="both", expand=True)
            if self.back_to_menu_button is not None:
                self.back_to_menu_button.pack(padx=5, pady=5, fill="both")
            if self.mild_stress_button is not None:
                self.mild_stress_button.pack(padx=5, pady=5, fill="both")
            if self.mid_stress_button is not None:
                self.mid_stress_button.pack(padx=5, pady=5, fill="both")
            if self.high_stress_button is not None:
                self.high_stress_button.pack(padx=5, pady=5, fill="both")


    def view_strategies_menu(self):
        self.reset_frame("to main strategy screen")

        values = [self.parent.translator.dictionary["Add Strategy"],
                  self.parent.translator.dictionary["Edit Strategy"],
                  self.parent.translator.dictionary["Delete Strategy"],
                  self.parent.translator.dictionary["View Strategy"],]
        self.strategies_option_menu = ctk.CTkOptionMenu(self, values=values)
        self.strategies_option_menu.set(self.parent.translator.dictionary["SELECT AN OPTION"])

        self.strategy_label = ctk.CTkLabel(self)

        self.strategy_list = CTkListbox(self)

        if self.listbox_theme is not None:
            style = self.parent.get_listbox_style(self.listbox_theme)
            self.strategy_list.configure(**style)

        self.select_strategy_option_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["option_choice"], font=self.parent.selected_font)

        self.strategy_select_title = ctk.CTkLabel(self, text=self.parent.translator.dictionary["COPING STRATEGIES"], font=self.parent.selected_font)
        self.strategy_select_title.pack(padx=5, pady=5, fill="both", expand=True)

        self.back_to_menu_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["back_button"],
                                                 command=self.parent.show_settings, font=self.parent.selected_font)
        self.back_to_menu_button.pack(padx=5, pady=5, fill="both")

        self.back_to_strategies_menu_button = ctk.CTkButton(self,
                                                            text=self.parent.translator.dictionary["back_button"], command=lambda: self.reset_frame("to main strategy screen"), font=self.parent.selected_font)

        self.mild_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["Mild stress strategies"], command = lambda: self.view_strategy_level_selected(1), font=self.parent.selected_font)
        self.mild_stress_button.pack(padx=5, pady=5, fill="both")

        self.mid_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["Mid stress strategies"], command = lambda: self.view_strategy_level_selected(2), font=self.parent.selected_font)
        self.mid_stress_button.pack(padx=5, pady=5, fill="both")

        self.high_stress_button = ctk.CTkButton(self, text=self.parent.translator.dictionary["High stress strategies"], command = lambda: self.view_strategy_level_selected(3), font=self.parent.selected_font)
        self.high_stress_button.pack(padx=5, pady=5, fill="both")


    def view_strategy_level_selected(self, stress_level):
        if self.strategy_list is not None:
            self.strategy_list.delete("all")
        if stress_level == 1:
            self.reset_frame("to level selected")
            self.back_to_strategies_menu_button.pack(padx=5, pady=5, fill="both")
            self.strategies_option_menu.pack(padx=5, pady=5, fill="both")
            self.select_strategy_option_button.configure(command=lambda: self.get_option(stress_level))
            self.select_strategy_option_button.pack(padx=5, pady=5, fill="both")
            self.show_strategy_screen(1)
            self.current_stress_level = 1
        elif stress_level == 2:
            self.reset_frame("to level selected")
            self.back_to_strategies_menu_button.pack(padx=5, pady=5, fill="both")
            self.strategies_option_menu.pack(padx=5, pady=5, fill="both")
            self.select_strategy_option_button.configure(command=lambda: self.get_option(stress_level))
            self.select_strategy_option_button.pack(padx=5, pady=5, fill="both")
            self.show_strategy_screen(2)
            self.current_stress_level = 2
        elif stress_level == 3:
            self.reset_frame("to level selected")
            self.back_to_strategies_menu_button.pack(padx=5, pady=5, fill="both")
            self.strategies_option_menu.pack(padx=5, pady=5, fill="both")
            self.select_strategy_option_button.configure(command=lambda: self.get_option(stress_level))
            self.select_strategy_option_button.pack(padx=5, pady=5, fill="both")
            self.show_strategy_screen(3)
            self.current_stress_level = 3
        else:
            pass


    def get_option(self, stress_level):
        option = self.strategies_option_menu.get()
        if option == self.parent.translator.dictionary["Edit Strategy"]:
            self.edit_strategies(stress_level)
        elif option == self.parent.translator.dictionary["Add Strategy"]:
            self.add_strategies(stress_level)
        elif option == self.parent.translator.dictionary["Delete Strategy"]:
            self.delete_strategies(stress_level)
        elif option == self.parent.translator.dictionary["View Strategy"]:
            self.view_strategy(stress_level)


    def show_strategy_screen(self, stress_level):
        if stress_level == 1:
            self.strategy_label.configure(text = self.parent.translator.dictionary["Strategies for mild stress:"])
            self.strategy_label.pack(padx=5, pady=5, fill="both", expand=True)

            self.strategy_list.pack(padx=5, pady=5, fill="both", expand=True)
            data = self.get_strategies_name_list(stress_level)
            if data:
                for i in data:
                    self.mild_strategies_dict[i[2]] = i[0]
                    self.strategy_list.insert(i[0], i[2])
        elif stress_level == 2:
            self.strategy_label.configure(text = self.parent.translator.dictionary["Strategies for mid stress:"])
            self.strategy_label.pack(padx=5, pady=5, fill="both", expand=True)
            self.strategy_list.pack(padx=5, pady=5, fill="both", expand=True)
            data = self.get_strategies_name_list(stress_level)
            if data:
                for i in data:
                    self.mid_strategies_dict[i[2]] = i[0]
                    self.strategy_list.insert(i[0], i[2])
        elif stress_level == 3:
            self.strategy_label.configure(text = self.parent.translator.dictionary["Strategies for high stress:"])
            self.strategy_label.pack(padx=5, pady=5, fill="both", expand=True)
            self.strategy_list.pack(padx=5, pady=5, fill="both", expand=True)
            data = self.get_strategies_name_list(stress_level)
            if data:
                for i in data:
                    self.high_strategies_dict[i[2]] = i[0]
                    self.strategy_list.insert(i[0], i[2])
        else:
            pass


    def get_strategies_name_list(self, stress_level):
        db = BodyScanDB()
        try:
            data = db.get_strategies_by_stress_level(stress_level)
            return data
        except DatabaseError:
            CTkMessagebox(self, title=self.parent.translator.dictionary["get_strategy_error_title"], message=self.parent.translator.dictionary["get_strategy_error_message"])
            return []
        except Exception as e:
            print("Error: ", e)
            return []



    def add_strategies(self, stress_level):
        self.parent.show_add_strategy_frame(stress_level)


    def edit_strategies(self, stress_level):
        try:
            if stress_level == 1:
                record_id = self.mild_strategies_dict[self.strategy_list.get()]
                self.parent.show_edit_strategies_frame(stress_level, record_id)

            elif stress_level == 2:

                record_id = self.mid_strategies_dict[self.strategy_list.get()]
                self.parent.show_edit_strategies_frame(stress_level, record_id)

            elif stress_level == 3:

                record_id = self.high_strategies_dict[self.strategy_list.get()]
                self.parent.show_edit_strategies_frame(stress_level, record_id)
            else:
                pass

        except (KeyError, IndexError):
            pass
        except DatabaseError:
            CTkMessagebox(self, title=self.parent.translator.dictionary["edit_error_title"], message=self.parent.translator.dictionary["edit_error_message"])
        except Exception as e:
            print("Error: ", e)
        try:
            self.strategy_list.deactivate(self.strategy_list.curselection())
        except (IndexError, TypeError):
            pass


    def delete_strategies(self, stress_level):
        db = BodyScanDB()
        try:
            if stress_level == 1:
                db.delete_strategy_by_id(self.mild_strategies_dict[self.strategy_list.get()])
                if self.strategy_list is not None:
                    self.strategy_list.delete('all')
                self.show_strategy_screen(self.current_stress_level)
            elif stress_level == 2:
                db.delete_strategy_by_id(self.mid_strategies_dict[self.strategy_list.get()])
                if self.strategy_list is not None:
                    self.strategy_list.delete('all')
                self.show_strategy_screen(self.current_stress_level)
            elif stress_level == 3:
                db.delete_strategy_by_id(self.high_strategies_dict[self.strategy_list.get()])
                if self.strategy_list is not None:
                    self.strategy_list.delete('all')
                self.show_strategy_screen(self.current_stress_level)
            else:
                pass

        except (KeyError, TypeError):
            pass
        except DatabaseError:
            CTkMessagebox(self, title=self.parent.translator.dictionary["delete_error_title"], message=self.parent.translator.dictionary["delete_error_message"])
        except Exception as e:
            print("Error: ", e)
        try:
            self.strategy_list.deactivate(self.strategy_list.curselection())
        except (IndexError, TypeError):
            pass


    def view_strategy(self, stress_level):
        try:
            if stress_level == 1:
                record_id = self.mild_strategies_dict[self.strategy_list.get()]
                self.parent.show_view_strategy_frame(stress_level, record_id)

            elif stress_level == 2:

                record_id = self.mid_strategies_dict[self.strategy_list.get()]
                self.parent.show_view_strategy_frame(stress_level, record_id)

            elif stress_level == 3:

                record_id = self.high_strategies_dict[self.strategy_list.get()]
                self.parent.show_view_strategy_frame(stress_level, record_id)

            else:
                pass
        except (KeyError, IndexError):
            pass
        try:
            self.strategy_list.deactivate(self.strategy_list.curselection())
        except (IndexError, TypeError):
            pass