from passwgen import Password
from kivy.app import App 
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Line
from kivy.core.image import Image

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '700')

class CheckBoxWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CheckBoxWidget, self).__init__(**kwargs)
        self.orientatoion = 'horizontal'
        self.checkbox = CheckBox(
            size_hint=(None, None),
            size = (40, 40)
        )
        self.label = Label(
            size = (170, 40),
            text_size = (170, 40),
            size_hint = (None, None),
            font_size = '18sp',
            halign = 'left',
            valign = 'center'
        )
        self.add_widget(self.checkbox)
        self.add_widget(self.label)

class LabelInputWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(LabelInputWidget, self).__init__(**kwargs)
        self.label = Label(
            size = (80,30),
            size_hint = (None,None),
            valign = 'center',
            halign = 'left',
            text_size=(80,30),
            font_size = '20sp'
        )
        self.text_input = TextInput(
            multiline=False,
            size=(50, 30),
            size_hint = (None,None)
        )
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

        self.box.count_layout = AnchorLayout(anchor_x='left')
        self.box.generator_layout = AnchorLayout(anchor_x='right')

        self.box.count_layout.input = LabelInputWidget()
        self.box.count_layout.input.label.text = 'Count :'
        self.box.count_layout.input.text_input.text = '8'

        self.box.generator_layout.generate = Button(
            text = 'Generate',
            size_hint = (.4, 1)
        )

        self.box.generator_layout.generate.bind(on_press=self.generate)
        self.box.count_layout.input.text_input.bind(on_text_validate=self.enter_input)

        self.box.count_layout.add_widget(self.box.count_layout.input)
        self.box.generator_layout.add_widget(self.box.generator_layout.generate)

        self.box.add_widget(self.box.count_layout)
        self.box.add_widget(self.box.generator_layout)

        self.add_widget(self.box)

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

class PasswordGeneratorWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(PasswordGeneratorWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.conf = ConfigurationWidget(size_hint=(1, .35))
        self.output = OutputWidget(size_hint=(1, .65))

        self.add_widget(self.conf)
        self.add_widget(self.output)

class ConfigurationManagerWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ConfigurationManagerWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.url_input = LabelInputWidget()
        self.login_input = LabelInputWidget()
        self.password_input = LabelInputWidget()

        self.url_input.label.text = 'url: '
        self.url_input.label.size = (150, 30)
        self.url_input.label.text_size = (150, 30)
        self.url_input.label.halign = 'left'
        self.url_input.text_input.text = 'default'
        self.url_input.text_input.size = (200, 30)
        self.url_input.text_input.font_size = '18sp'

        self.login_input.label.text = 'login: '
        self.login_input.label.size = (150, 30)
        self.login_input.label.text_size = (150, 30)
        self.login_input.label.halign = 'left'
        self.login_input.text_input.text = 'default'
        self.login_input.text_input.size = (200, 30)
        self.login_input.text_input.font_size = '18sp'

        self.password_input.label.text = 'password: '
        self.password_input.label.size = (150, 30)
        self.password_input.label.text_size = (150, 30)
        self.password_input.label.halign = 'left'
        self.password_input.text_input.text = 'default'
        self.password_input.text_input.size = (200, 30)
        self.password_input.text_input.font_size = '18sp'

        self.add_widget(self.url_input)
        self.add_widget(self.login_input)
        self.add_widget(self.password_input)

        self.layout = AnchorLayout(anchor_x = 'right')

        self.layout.btn = Button(text='Add', size_hint = (.2, 1))

        self.layout.btn.bind(on_press=self.add_account)

        self.layout.add_widget(self.layout.btn)
        self.add_widget(self.layout)
        
    def add_account(self, instance):
        self.url = MainLabel(
            text = self.url_input.text_input.text,
        )
        self.login = MainLabel(
            text = self.login_input.text_input.text,
            font_size = '20sp'
        )
        self.password = MainLabel(
            text = self.password_input.text_input.text,
            font_size = '20sp'
        )
        self.btn = Button(text='del', size_hint=(None, None), size=(20, 20))
        self.btn.bind(on_press=self.delete_account)

        self.parent.manager.item = BoxLayout(orientation = 'horizontal')

        self.parent.manager.item.add_widget(self.url)
        self.parent.manager.item.add_widget(self.login)
        self.parent.manager.item.add_widget(self.password)
        self.parent.manager.item.add_widget(self.btn)

        self.parent.manager.body.box.add_widget(self.parent.manager.item)

    def delete_account(self, instance):
        pass


class ManagerWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ManagerWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.head = BoxLayout(size_hint=(1, .1))

        self.head.add_widget(MainLabel(text='url'))
        self.head.add_widget(MainLabel(text='login'))
        self.head.add_widget(MainLabel(text='password'))
        self.head.add_widget(MainLabel(text='delete'))

        self.add_widget(self.head)

        self.body = ScrollView(size_hint=(1, .7))
        self.body.box = BoxLayout(orientation='vertical')

        self.body.add_widget(self.body.box)
        self.add_widget(self.body)

class PasswordManagerWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(PasswordManagerWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 10, 10, 10]

        self.conf = ConfigurationManagerWidget(size_hint=(1, .3))
        self.add_widget(self.conf)

        with self.canvas:
            Line(points=(0, 388, 1980, 388))

        self.manager = ManagerWidget(size_hint=(1, .7))
        self.add_widget(self.manager)

class MainLabel(Label):
    def __init__(self, **kwargs):
        super(MainLabel, self).__init__(**kwargs)
        self.font_size = '20sp'
        self.text_size = (180, 20)
        self.size = (180, 20)
        self.size_hint = (None, None)
        self.halign = 'left'

class AboutLabel(Label):
    def __init__(self, **kwargs):
        super(AboutLabel, self).__init__(**kwargs)
        self.size = (300,30)
        self.size_hint = (None, None)
        self.halign = 'left'
        self.text_size = (300,30)
        self.font_size = '18sp'
    pass

class ManualWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ManualWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        self.instr_gen = [
            'Generator -> generate passwords',
            "   Uppercase   -> enable uppercase",
            "   Numeric       -> enable numeric",
            "   Separators  -> enable separators",
            "   Count           -> count of symbols",
            "   Generate     -> action"
            ]
        self.man_gen = BoxLayout(orientation='vertical', size_hint=(.5, 1))
        for x in self.instr_gen:
            self.man_gen.add_widget(AboutLabel(text=x))

        self.instr_man = [
            "Manager -> manage passwords",
            "    url               -> resourse",
            "    login           -> your login",
            "    password -> your password",
            "    Add             -> action",
            ""
        ]
        self.man_man = BoxLayout(orientation='vertical', size_hint=(.5, 1))
        for x in self.instr_man:
            self.man_man.add_widget(AboutLabel(text=x))

        self.add_widget(self.man_gen)
        self.add_widget(self.man_man)
    pass

class InformationWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(InformationWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.version = AnchorLayout(anchor_x='right', size_hint=(1, .3))
        self.author = AnchorLayout(anchor_x='right', size_hint=(1, .3))
        self.rights = AnchorLayout(anchor_x='right', size_hint=(1, .3))

        self.version.label = AboutLabel(text='version: 1.0')
        self.author.label = AboutLabel(text='Author: Nikolaj Vorobiev')
        self.rights.label = AboutLabel(text='All Rights Reserved')

        self.version.label.halign = 'right'
        self.author.label.halign = 'right'
        self.rights.label.halign = 'right'

        self.author.add_widget(self.author.label)
        self.version.add_widget(self.version.label)
        self.rights.add_widget(self.rights.label)

        self.add_widget(self.author)
        self.add_widget(self.version)
        self.add_widget(self.rights)

class AboutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(AboutWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(
            text='Password Generator',
            font_size = '26sp',
            size_hint=(1, .3)
        )

        self.man = ManualWidget(size_hint=(1, .3))
        self.information = InformationWidget(size_hint= (1, .15))

        self.add_widget(self.label)
        self.add_widget(self.man)
        self.add_widget(Widget(size_hint = (1, .25)))
        self.add_widget(self.information)

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
        self.about = Button(text='About')

        self.generator.bind(on_press=self.run_generator)
        self.manager.bind(on_press=self.run_manager)
        self.about.bind(on_press=self.run_about)
    
        self.add_widget(self.generator)
        self.add_widget(self.manager)
        self.add_widget(self.about)

    def run_generator(self, instance):
        self.parent.widg.clear_widgets()
        self.parent.widg.add_widget(PasswordGeneratorWidget())
    def run_manager(self, instance):
        self.parent.widg.clear_widgets()
        self.parent.widg.add_widget(PasswordManagerWidget())
    def run_about(self, instance):
        self.parent.widg.clear_widgets()
        self.parent.widg.add_widget(AboutWidget())

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 0, 10, 10]
        self.texture = Image('bg.jpg').texture
        with self.canvas:
            self.rect = Rectangle(texture=self.texture, size=self.size,
                                   pos=self.pos)

        def update_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size

        self.bind(pos=update_rect, size=update_rect)

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
