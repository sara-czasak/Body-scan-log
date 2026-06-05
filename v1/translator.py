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
    "View Strategy": "VIEW STRATEGY",
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
    "name_error_title": "This strategy name already exists",
    "name_error_message": "Please change the strategy name and try again",
    "pref_db_error_title": "Save Failed",
    "pref_db_error_message": "Something went wrong while saving your preference. Please try again.",
}},
    {"Polski": {
        'app_title': "PL",
        'menu_title': "MENU",
        'add_menu_opt': "DODAJ NOWY WPIS",
        'view_all_menu_optn': "WSZYSTKIE WPISY",
        'analyze_menu_opt': "ANALIZA WPISÓW",
        'settings_menu_opt': "USTAWIENIA",
        'new_entry_title': "NOWY WPIS",
        'date_label': "DATA",
        'notes_label': "NOTATKI",
        'submit_button': "ZAPISZ",
        'jaw': "PL",
        "face": "TWARZ",
        "neck": "SZYJA",
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
        "settings": "USTAWIENIA",
        "lang_option": "JĘZYKI",
        "Stress decreasing strategies": "STRATEGIE PRZECIWSTRESOWE",
        "COPING STRATEGIES": "PL",
        "Strategies for mild stress:": "PL",
        "Strategies for mid stress:": "PL",
        "Strategies for high stress:": "PL",
        "Mild stress strategies": "PL",
        "Mid stress strategies": "PL",
        "High stress strategies": "PL",
        "Add Strategy": "DODAJ STRATEGIE",
        "Edit Strategy": "EDYTUJ STRATEGIE",
        "Delete Strategy": "USUŃ STRATEGIE",
        "option_choice": "OPCJE",
        "strategy_options_menu_default": "PL",
        "Add new strategy": "DODAJ STRATEGIE",
        "Strategy Name": "NAZWA",
        "Strategy Description": "OPIS",
        "submit_strategy": "ZAPISZ",
        "View Strategy": "ZOBACZ STRATEGIE",
        "SELECT AN OPTION": "WYBIERZ OPCJE",
        "about": "PL",
        "ALL ENTRIES": "WSZYSTKIE WPISY",
        "see_more_button": "ZOBACZ WIĘCEJ",
        "last_week_average": "ŚREDNIA Z OSTATNICH 10 DNI",
        "get_strategy_button": "ZOBACZ STRATEGIE",
        "show_graph_button": "ZOBACZ WYKRES",
        "graph_label": "WYKRES",
        "select_theme": "PL",
        "Default": "PL",
        "Dark": "PL",
        "Light": "PL",
        "Dyslexia": "PL",
        "name_error_title": "Ta nazwa strategi jest zajęta.",
        "name_error_message": "Wprowadz inną nazwe i sprubuj ponownie",
        "pref_db_error_title": "Nie udało się zapisać zmian",
        "pref_db_error_message": "Coś poszło nie tak podczas zapisywania zmian. Sprubuj ponownie.",
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










