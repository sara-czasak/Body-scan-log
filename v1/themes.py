


class Themes:
    def __init__(self):
        self.theme = None


    def set_theme(self, theme):
        if theme == 'default':
            pass
        elif theme == 'dark':
            self.dark_theme()
        elif theme == 'light':
            self.light_theme()
        elif theme == 'dyslexia':
            self.dyslexia_theme()
        print(theme)


    def dark_theme(self):
        self.theme = "dark"


    def light_theme(self):
        self.theme = "light"


    def dyslexia_theme(self):
        self.theme = "dyslexia"