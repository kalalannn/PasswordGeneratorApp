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
    def clear(self):
        self.clear_widgets()
    def next_state(self, state):
        self.widg.clear_widgets()
        if state == 'PasswordGeneratorWidget':
            self.new_widg = PasswordGeneratorWidget()
        elif state == 'PasswordManagerWidget':
            self.new_widg = PasswordManagerWidget()
        elif state == 'SettingsWidget':
            self.new_widg = SettingsWidget()
        self.widg.add_widget(self.new_widg)
    def generate(self):
        try:
            self.new_widg.ids.output.generate_all()
        except:
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
