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
}},
    {"Polski": {
        'app_title': "PL",
        'menu_title': "PL",
        'add_menu_opt': "PL",
        'view_all_menu_optn': "PL",
        'analyze_menu_opt': "PL",
        'settings_menu_opt': "PL",
        'new_entry_title': "PL",
        'date_label': "PL",
        'notes_label': "PL",
        'submit_button': "PL",
        'jaw': "PL",
        "face": "PL",
        "neck": "PL",
        "upper back": "PL",
        "mid back": "PL",
        "lower back": "PL",
        "left shoulder": "PL",
        "right shoulder": "PL",
        "left arm": "PL",
        "right arm": "PL",
        "chest": "PL",
        "stomach": "PL",
        "left leg": "PL",
        "right leg": "PL",
        "left foot": "PL",
        "right foot": "PL",
        "back_button": "PL",
        "exit_button": "PL",
        "settings": "PL",
        "lang_option": "PL",
        "Stress decreasing strategies": "PL",
        "COPING STRATEGIES": "PL",
        "Strategies for mild stress:": "PL",
        "Strategies for mid stress:": "PL",
        "Strategies for high stress:": "PL",
        "Mild stress strategies": "PL",
        "Mid stress strategies": "PL",
        "High stress strategies": "PL",
        "Add Strategy": "PL",
        "Edit Strategy": "PL",
        "Delete Strategy": "PL",
        "option_choice": "PL",
        "strategy_options_menu_default": "PL",
        "Add new strategy": "PL",
        "Strategy Name": "PL",
        "Strategy Description": "PL",
        "submit_strategy": "PL",
        "View Strategy": "PL",
        "SELECT AN OPTION": "PL",
        "about": "PL",
        "ALL ENTRIES": "PL",
        "see_more_button": "PL",
        "last_week_average": "PL",
        "get_strategy_button": "PL",
        "show_graph_button": "PL",
        "graph_label": "PL",
    }},
]


class Translator:
    def __init__(self):
        self.dictionary = None
        self.lang = None
        self.available_languages = [
            "English",
            "Polski"
        ]


    def set_lang(self, lang):
        self.lang = lang
        self.get_dictionary(self.lang)


    def get_dictionary(self, lang):
        for i in langs:
            if lang in i:
                self.dictionary = i[lang]










