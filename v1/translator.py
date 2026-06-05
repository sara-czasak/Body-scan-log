langs = [{"English": {
    'app_title': "Body Scan Log",
    'menu_title': "MENU",
    'add_menu_opt': "ADD NEW ENTRY",
    'view_all_menu_optn': "VIEW ALL ENTRIES",
    'analyze_menu_opt': "ANALYZE ENTRIES",
    'settings_menu_opt': "SETTINGS",
    'new_entry_title': "NEW ENTRY",
    'date_label': "DATE (YYYY-MM-DD):",
    'notes_label': "NOTES:",
    'submit_button': "SUBMIT ENTRY",
    'jaw': "JAW",
    "face": "FACE",
    "neck": "NECK",
    "upper back": "UPPER BACK",
    "mid back": "MID BACK",
    "lower back": "LOWER BACK",
    "left shoulder": "LEFT SHOULDER",
    "right shoulder": "RIGHT SHOULDER",
    "left arm": "LEFT ARM",
    "right arm": "RIGHT ARM",
    "chest": "CHEST",
    "stomach": "STOMACH",
    "left leg": "LEFT LEG",
    "right leg": "RIGHT LEG",
    "left foot": "LEFT FOOT",
    "right foot": "RIGHT FOOT",
    "back_button": "BACK",
    "exit_button": "EXIT",
    "settings": "SETTINGS",
    "lang_option": "LANGUAGES",
    "Stress decreasing strategies": "STRESS DECREASE STRATEGIES",
    "COPING STRATEGIES": "COPING STRATEGIES",
    "Strategies for mild stress:": "MILD STRESS STRATEGIES:",
    "Strategies for mid stress:": "MODERATE STRESS STRATEGIES:",
    "Strategies for high stress:": "HIGH STRESS STRATEGIES:",
    "Mild stress strategies": "MILD STRESS STRATEGIES",
    "Mid stress strategies": "MODERATE STRESS STRATEGIES",
    "High stress strategies": "HIGH STRESS STRATEGIES",
    "Add Strategy": "ADD STRATEGY",
    "Edit Strategy": "EDIT STRATEGY",
    "Delete Strategy": "DELETE STRATEGY",
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
    "select_theme": "SELECT THEME",
    "Default": "Default",
    "Dark": "Dark",
    "Light": "Light",
    "Dyslexia": "Dyslexia",
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
        "select_theme": "PL",
        "Default": "PL",
        "Dark": "PL",
        "Light": "PL",
        "Dyslexia": "PL",
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










