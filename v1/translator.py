langs = [{"English": {
    'app_title': "Body Scan Log",
    'menu_title': "MENU",
    'add_menu_opt': "Add new body scan",
    'view_all_menu_optn': "View all scans",
    'analyze_menu_opt': "Analyze body scans",
    'settings_menu_opt': "Settings",
    'new_entry_title': "NEW ENTRY",
    'date_label': "DATE (YYYY-MM-DD):",
    'notes_label': "NOTES:",
    'submit_button': "SUBMIT ENTRY",
    'jaw': "jaw",
    "face": "face",
    "neck": "neck",
    "upper back": "upper back",
    "mid back": "mid back",
    "lower back": "lower back",
    "left shoulder": "left shoulder",
    "right shoulder": "right shoulder",
    "left arm": "left arm",
    "right arm": "right arm",
    "chest": "chest",
    "stomach": "stomach",
    "left leg": "left leg",
    "right leg": "right leg",
    "left foot": "left foot",
    "right foot": "right foot",
    "back_button": "BACK",
    "exit_button": "EXIT",
    "settings": "SETTINGS",
    "lang_option": "Select Language",
    "Stress decreasing strategies": "Stress decreasing strategies",
    "COPING STRATEGIES": "COPING STRATEGIES",
    "Strategies for mild stress:": "Strategies for mild stress:",
    "Strategies for mid stress:": "Strategies for mid stress:",
    "Strategies for high stress:": "Strategies for high stress:",
    "Mild stress strategies": "Mild stress strategies",
    "Mid stress strategies": "Mid stress strategies",
    "High stress strategies": "High stress strategies",
    "Add Strategy": "Add Strategy",
    "Edit Strategy": "Edit Strategy",
    "Delete Strategy": "Delete Strategy",
    "option_choice": "SELECT",
    "strategy_options_menu_default": "OPTIONS",
    "Add new strategy": "Add new strategy",
    "Strategy Name": "Strategy Name",
    "Strategy Description": "Strategy Description",
    "submit_strategy": "SUBMIT STRATEGY",
    "View Strategy": "View Strategy",
    "SELECT AN OPTION": "SELECT AN OPTION",
    "about": "ABOUT",
    "ALL ENTRIES": "ALL ENTRIES",
    "see_more_button": "SEE DETAILS",
    "last_week_average": "LAST WEEK AVERAGE",
    "get_strategy_button": "GET A STRESS MANAGEMENT TECHNIQUE",
    "show_graph_button": "SHOW GRAPH",
    "graph_label": "GRAPH",
}}]


class Translator:
    def __init__(self, lang):
        self.lang = lang
        self.dictionary = None
        self.available_languages = ["English"]
        self.get_dictionary(self.lang)


    def get_dictionary(self, lang):
        for i in langs:
            if i["English"]:
                self.dictionary = i["English"]










