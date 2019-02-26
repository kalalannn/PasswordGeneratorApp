from passwgen import Password
from kivy.app import App 
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard

Config.set('graphics', 'resizeable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '700')

class LabelInputWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(LabelInputWidget, self).__init__(**kwargs)
        self.label = Label(text='Count: ')
        self.text_input = TextInput(multiline=False)
        self.add_widget(self.label)
        self.add_widget(self.text_input)

class ConfigurationWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ConfigurationWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.uppercheck = CheckBoxWidget(size_hint=(.25, 1))
        self.numericcheck = CheckBoxWidget(size_hint=(.25, 1))
        self.seprcheck = CheckBoxWidget(size_hint=(.25, 1))

        self.uppercheck.label.text = 'UPPERCASE (A-Z)'
        self.numericcheck.label.text = 'Numeric (0-9)'
        self.seprcheck.label.text = "Separators {'-', '_'}"

        self.uppercheck.checkbox.bind(active=self.change_upper)
        self.numericcheck.checkbox.bind(active=self.change_numeric)
        self.seprcheck.checkbox.bind(active=self.change_sepr)

        self.add_widget(self.uppercheck)
        self.add_widget(self.numericcheck)
        self.add_widget(self.seprcheck)

        self.box = BoxLayout(orientation='horizontal')
        self.add_widget(self.box)

        self.box.count_layout = AnchorLayout(anchor_x='left')
        self.box.generator_layout = AnchorLayout(anchor_x='right')

        self.box.add_widget(self.box.count_layout)
        self.box.add_widget(self.box.generator_layout)

        self.box.count_layout.input = LabelInputWidget(size_hint=(.5, .5))

        self.box.generator_layout.generate = Button(
            text = 'Generate',
            size_hint = (.4, 1)
            )

        self.box.count_layout.add_widget(self.box.count_layout.input)
        self.box.generator_layout.add_widget(self.box.generator_layout.generate)

        self.box.generator_layout.generate.bind(on_press=self.generate)
        self.box.count_layout.input.text_input.bind(on_text_validate=self.enter_input)

    def change_upper(self, checkbox, value):
        self.parent.output.password.uppercase = value
    def change_numeric(self, checkbox, value):
        self.parent.output.password.numeric = value
    def change_sepr(self, checkbox, value):
        self.parent.output.password.sepr = value

    def generate(self, instance):
        self.parent.children[0].update()
    def enter_input(self, instance):
        int_input = self.box.count_layout.input.text_input.text
        if int_input.isdigit():
            int_input = int(int_input)
            if  1 < int_input < 25:
               self.parent.output.password.count = int_input

class CheckBoxWidget(BoxLayout):
    text = ''
    def __init__(self, **kwargs):
        super(CheckBoxWidget, self).__init__(**kwargs)
        self.orientatoion = 'horizontal'
        self.checkbox = CheckBox(size_hint=(.1, 1))
        self.widget = Widget(size_hint=(.1, 1))
        self.label = Label(
                size_hint = (.8, 1),
                font_size = '16sp',
                text_size = (130, None),
                text = self.text,
                halign = 'left',
                valign = 'middle'
                )
        self.add_widget(self.checkbox)
        self.add_widget(self.widget)
        self.add_widget(self.label)

class PasswordGeneratorWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(PasswordGeneratorWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.conf = ConfigurationWidget(size_hint=(1, .35))
        self.output = OutputWidget(size_hint=(1, .65))

        self.add_widget(self.conf)
        self.add_widget(self.output)

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
            self.label = TextInput(
                    text = x,
                    font_size = '18sp',
                    padding_y = [self.width/2,self.width/2],
                    multiline = False
                    )
            self.add_widget(self.label)

    def update(self):
        self.generate_all()
        a=0
        for label in self.children:
            label.text = self.labels[a]
            a += 1

class MenuWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.cols = 3

        self.generator = Button(text='Generator')
        self.manager = Button(text='Manager')
        self.settings = Button(text='Settings')

        self.generator.bind(on_press=self.run_generator)
        self.manager.bind(on_press=self.run_manager)
        self.settings.bind(on_press=self.run_settings)
    
        self.add_widget(self.generator)
        self.add_widget(self.manager)
        self.add_widget(self.settings)

    def run_generator(self, instance):
        self.parent.widg.clear_widgets()
        self.parent.widg.add_widget(PasswordGeneratorWidget())
    def run_manager(self, instance):
        self.parent.widg.clear_widgets()
        self.parent.widg.add_widget(PasswordManagerWidget())
    def run_settings(self, instance):
        self.parent.widg.clear_widgets()
        self.parent.widg.add_widget(SettingsWidget())

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.menu = MenuWidget(size_hint=(1, .1))
        self.widg = PasswordGeneratorWidget(size_hint=(1, .9))

        self.add_widget(self.menu)
        self.add_widget(self.widg)

class PasswordGeneratorApp(App):
    def build(self):
        root = RootWidget()
        return self.root

def __main__():
    root = PasswordGeneratorApp()
    root.run()

if __name__ == '__main__':
    __main__()
