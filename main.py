from passwgen import Password
from kivy.app import App 
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

Config.set('graphics', 'resizeable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '700')

class ConfigurationWidget(BoxLayout):
    pass

class PasswordGeneratorWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(PasswordGeneratorWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.conf = ConfigurationWidget(size_hint=(1, .35))
        self.add_widget(self.conf)

        self.output = OutputWidget(size_hint=(1, .65))
        self.add_widget(self.output)
    pass

class PasswordManagerWidget(BoxLayout):
    pass

class SettingsWidget(BoxLayout):
    pass

class OutputWidget(GridLayout):
    def __init__(self, **kwargs):
        super(OutputWidget, self).__init__(**kwargs)
        self.rows = 3
        self.cols = 3
        self.password = Password()
        self.labels = []
        self.create_all()
    def generate_all(self):
        self.labels.clear()
        for x in range(9):
            self.password.generate_password()
            self.labels.append(self.password.label)
    def create_all(self):
        self.generate_all()
        for x in self.labels:
            self.add_widget(Label(text=x))
    def update(self):
        self.generate_all()
        a=0
        for label in self.children:
            label.text = self.labels[a]
            a += 1

        pass
class MenuWidget(BoxLayout):
    pass

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.menu = MenuWidget(size_hint=(1, .1))
        self.add_widget(self.menu)
        self.widg = PasswordGeneratorWidget(size_hint=(1, .9))
        self.add_widget(self.widg)

    def next_state(self, state):
        self.remove_widget(self.children[0])
        if state == 'PasswordGeneratorWidget':
            self.add_widget(PasswordGeneratorWidget())
        elif state == 'PasswordManagerWidget':
            self.add_widget(PasswordManagerWidget())
        elif state == 'SettingsWidget':
            self.add_widget(SettingsWidget())
    def update_output(self):
        self.children[0].children[0].update()
    def update_parameters(self, text):
        if text == 'UPPERCASE (A-Z)':
            self.children[0].children[0].password.uppercase = True
        elif text == 'Numeric (0-9)':
            self.children[0].children[0].password.numeric = True
        elif text == "Separators {'-', '_'}":
            self.children[0].children[0].password.sepr = True
        else:
            self.children[0].children[0].password.uppercase = False
            self.children[0].children[0].password.numeric = False
            self.children[0].children[0].password.sepr = False

class PasswordGeneratorApp(App):
    def build(self):
        root = RootWidget()
        return self.root

def __main__():
    root = PasswordGeneratorApp()
    root.run()

if __name__ == '__main__':
    __main__()
