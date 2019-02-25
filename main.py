import passwdgen
from kivy.app import App 
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

Config.set('graphics', 'resizeable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '700')

class PasswordGeneratorWidget(BoxLayout):
    pass

class PasswordManagerWidget(BoxLayout):
    pass

class SettingsWidget(BoxLayout):
    pass

class RootWidget(BoxLayout):
    def clear(self):
        self.clear_widgets()
    def next_state(self, state):
        self.ids.widg.clear_widgets()
        if state == 'PasswordGeneratorWidget':
            widg = PasswordGeneratorWidget()
        elif state == 'PasswordManagerWidget':
            widg = PasswordManagerWidget()
        elif state == 'SettingsWidget':
            widg = SettingsWidget()
        self.ids.widg.add_widget(widg)
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
