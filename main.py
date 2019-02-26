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

class PasswordGeneratorWidget(BoxLayout):
    pass

class PasswordManagerWidget(BoxLayout):
    pass

class SettingsWidget(BoxLayout):
    pass

class OutputWidget(GridLayout):
    password = Password()
    def generate_all(self):
        self.clear_widgets()
        for x in range(9):
            self.add_widget(Label(text=self.password.generate_password()))
    pass

class RootWidget(BoxLayout):
    def clear(self):
        self.clear_widgets()
    def next_state(self, state):
        self.ids.widg.clear_widgets()
        if state == 'PasswordGeneratorWidget':
            self.widg = PasswordGeneratorWidget()
        elif state == 'PasswordManagerWidget':
            self.widg = PasswordManagerWidget()
        elif state == 'SettingsWidget':
            self.widg = SettingsWidget()
        self.ids.widg.add_widget(self.widg)
    def generate(self):
        self.widg.ids.output.generate_all()
        pass
    pass


class PasswordGeneratorApp(App):
    def build(self):
        root = RootWidget()
        return self.root

def __main__():
    root = PasswordGeneratorApp()
    root.run()

if __name__ == '__main__':
    __main__()
