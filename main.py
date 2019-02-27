# Author: Nikolaj Vorobiev
from passwgen import Password
from kivy import app
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
            size = (100,40),
            size_hint = (None,None),
            valign = 'center',
            halign = 'left',
            text_size=(100,40),
            font_size = '20sp'
        )
        self.text_input = TextInput(
            multiline=False,
            size=(200, 40),
            size_hint = (None,None),
            font_size = '20sp'
        )
        self.add_widget(self.label)
        self.add_widget(self.text_input)

class MainLabel(Label):
    def __init__(self, **kwargs):
        super(MainLabel, self).__init__(**kwargs)
        self.font_size = '20sp'
        self.text_size = (160, 20)
        self.size = (160, 20)
        self.halign = 'center'
        self.valign = 'center'

class AboutLabel(Label):
    def __init__(self, **kwargs):
        super(AboutLabel, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.halign = 'left'
        #self.text_size = (200,30)
        self.text_size = (400,30)
        self.size = (400,30)
        self.font_size = '18sp'
    pass

class InformationWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(InformationWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.version = AnchorLayout(anchor_x='right', size_hint=(1, .3))
        self.author = AnchorLayout(anchor_x='right', size_hint=(1, .3))
        self.rights = AnchorLayout(anchor_x='right', size_hint=(1, .3))

        self.version.label = AboutLabel(text='version: 1.2')
        self.author.label = AboutLabel(text='Author: Nikolaj Vorobiev')
        self.rights.label = AboutLabel(text='License: GNU GPLv3')

        self.version.label.size = (100, 30)
        self.author.label.size = (100, 30)
        self.rights.label.size = (100, 30)

        self.author.add_widget(self.author.label)
        self.version.add_widget(self.version.label)
        self.rights.add_widget(self.rights.label)

        self.add_widget(self.author)
        self.add_widget(self.version)
        self.add_widget(self.rights)

class ManualWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ManualWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        self.instr_gen = [
            'Generator -> generate passwords',
            "   Uppercase -> enable uppercase",
            "   Numeric -> enable numeric",
            "   Separators -> enable separators",
            "   Count -> count of symbols",
            "   Generate -> action"
        ]
        self.man_gen = BoxLayout(orientation='vertical', size_hint=(.5, 1))
        for x in self.instr_gen:
            self.man_gen.add_widget(AboutLabel(text=x))

        self.instr_man = [
            "Manager -> manage passwords",
            "    url -> resourse",
            "    login -> your login",
            "    password -> your password",
            "    Add -> action",
            ""
        ]
        self.man_man = BoxLayout(orientation='vertical', size_hint=(.5, 1))
        for x in self.instr_man:
            self.man_man.add_widget(AboutLabel(text=x))

        self.add_widget(self.man_gen)
        self.add_widget(self.man_man)

class AboutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(AboutWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(
            text='Password Generator',
            font_size = '26sp',
            size_hint=(1, .4)
        )

        self.man = ManualWidget(size_hint=(1, .3))
        self.information = InformationWidget(size_hint= (1, .15))

        self.add_widget(self.label)
        self.add_widget(self.man)
        self.add_widget(Widget(size_hint = (1, .25)))
        self.add_widget(self.information)

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

    def add_account(self, url_text, login_text, password_text):
        self.url = MainLabel(text = url_text)
        self.login = MainLabel(text = login_text)
        self.password = MainLabel(text = password_text)

        self.layout = AnchorLayout(anchor_x='center', anchor_y='center')
        self.layout.btn = Button(text='del', size=(30, 30), size_hint=(None, None))

        self.layout.btn.bind(on_press=self.delete_account)

        self.layout.add_widget(self.layout.btn)

        self.item = BoxLayout(orientation='horizontal')

        self.item.add_widget(self.url)
        self.item.add_widget(self.login)
        self.item.add_widget(self.password)
        self.item.add_widget(self.layout)

        self.body.box.add_widget(self.item)

    def delete_account(self, instance):
        item = instance.parent.parent
        instance.parent.parent.parent.remove_widget(item)
        pass

class ConfigurationManagerWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ConfigurationManagerWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.url_input = LabelInputWidget()
        self.login_input = LabelInputWidget()
        self.password_input = LabelInputWidget()

        self.url_input.label.text = 'url: '
        self.url_input.text_input.text = 'default'

        self.login_input.label.text = 'login: '
        self.login_input.text_input.text = 'default'

        self.password_input.label.text = 'password: '
        self.password_input.text_input.text = 'default'

        self.add_widget(self.url_input)
        self.add_widget(self.login_input)
        self.add_widget(self.password_input)


        self.layout_0 = AnchorLayout(anchor_x='right')
        self.layout = AnchorLayout(anchor_x='right')

        self.layout_0.btn = Button(text='Delete All', size_hint=(.2, 1))
        self.layout.btn = Button(text='Add', size_hint = (.2, 1))

        self.layout_0.btn.bind(on_press=self.delete_all)
        self.layout.btn.bind(on_press=self.add_account)

        self.layout_0.add_widget(self.layout_0.btn)
        self.layout.add_widget(self.layout.btn)

        self.add_widget(self.layout)
        self.add_widget(self.layout_0)
    def add_account(self, instance):
        self.parent.manager.add_account(
            self.url_input.text_input.text,
            self.login_input.text_input.text,
            self.password_input.text_input.text,
        )
    def delete_all(self, instance):
        self.parent.manager.body.box.clear_widgets()
        pass

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

class OutputWidget(GridLayout):
    def __init__(self, **kwargs):
        super(OutputWidget, self).__init__(**kwargs)
        self.rows = 5
        self.cols = 3
        self.password = Password()
        self.labels = []
        self.create_all()

    def generate_all(self):
        self.labels.clear()
        for x in range(15):
            self.password.generate_password()
            self.labels.append(self.password.label)

    def create_all(self):
        self.generate_all()
        for x in self.labels:
            self.label = TextInput(
                    text = x,
                    font_size = '17sp',
                    size = (207, 50),
                    size_hint = (None, None),
                    multiline = False
                    )
            self.add_widget(self.label)

    def update(self):
        self.generate_all()
        a=0
        for label in self.children:
            label.text = self.labels[a]
            a += 1

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
        self.box.count_layout.input.text_input.size = (80, 40)
        self.box.count_layout.input.text_input.text = '8'

        self.box.generator_layout.generate = Button(
            text = 'Generate',
            size_hint = (.4, 1)
        )

        self.box.generator_layout.generate.bind(on_press=self.generate)
        self.box.count_layout.input.text_input.bind(text=self.enter_input)

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
    def enter_input(self, instance, some):
        int_input = self.box.count_layout.input.text_input.text
        if int_input.isdigit():
            int_input = int(int_input)
            self.parent.output.password.count = int_input

class MenuWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.cols = 3

        self.generator = Button(text='Generator')
        self.manager = Button(text='Manager')
        self.about = Button(text='About')
        self.exit_btn = Button(text='Exit')

        self.generator.bind(on_press=self.run_generator)
        self.manager.bind(on_press=self.run_manager)
        self.about.bind(on_press=self.run_about)
        self.exit_btn.bind(on_press=self.exit)
    
        self.add_widget(self.generator)
        self.add_widget(self.manager)
        self.add_widget(self.about)
        self.add_widget(self.exit_btn)

    def run_generator(self, instance):
        self.parent.widg.clear_widgets()
        self.parent.widg.add_widget(PasswordGeneratorWidget())
    def run_manager(self, instance):
        self.parent.widg.clear_widgets()
        self.parent.widg.add_widget(PasswordManagerWidget())
    def run_about(self, instance):
        self.parent.widg.clear_widgets()
        self.parent.widg.add_widget(AboutWidget())
    def exit(self, instance):
        app.App.get_running_app().stop()

class PasswordGeneratorWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(PasswordGeneratorWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.conf = ConfigurationWidget(size_hint=(1, .35))
        self.output = OutputWidget(size_hint=(1, .65))

        self.add_widget(self.conf)
        self.add_widget(self.output)

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
    def __init__(self, **kwargs):
        super(PasswordGeneratorApp, self).__init__(**kwargs)
    def build(self):
        root = RootWidget()
        return self.root

def __main__():
    root = PasswordGeneratorApp()
    root.run()

if __name__ == '__main__':
    __main__()
