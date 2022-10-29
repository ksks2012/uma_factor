import os
from typing import List, Mapping

import kivy
from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.core.text import LabelBase
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from util.common import read_static_data

kivy.resources.resource_add_path(os.path.abspath('./font/msjh.ttc'))
LabelBase.register('zh_font', './font/msjh.ttc')

class InputWithSpinner(TextInput):
    def __init__(self, all_of_data = [], **kwargs):
        super().__init__(**kwargs)
        for idx, data in enumerate(all_of_data):
            if type(data) is not str:
                all_of_data[idx] = str(data)
        self.all_of_data = all_of_data
        self.init_spinner()
        # self.bind(on_text_validate=self.on_enter)

    def init_spinner(self):
        self.spinner = Spinner(
            # default value shown
            text='>',
            # available values
            values=self.all_of_data,
            # just for positioning in our example
            size_hint=(None, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5})
        # self.spinner.is_open=BooleanProperty(True)

    def insert_text(self, substring, from_undo=False):
        # s = substring.upper()
        update_value = []
        for v in self.all_of_data:
            if substring in v:
                update_value.append(v)
        self.spinner.values = update_value
        return super().insert_text(substring, from_undo=from_undo)

class FieldLayout(GridLayout):
    def __init__(self, **kwargs):
        super(FieldLayout, self).__init__(cols=1, rows=2, **kwargs)
        self.horse_name_dict, self.blue_list, self.red_list, self.green_list, self.factor_list = read_static_data()
        self.build()
    
    def build(self):
        # label

        # text
        textinput = InputWithSpinner(all_of_data=self.factor_list ,text='', multiline=False)
        # textinput = InputWithSpinner(all_of_data=["a", "b", "c"] ,text='', multiline=False)

        self.add_widget(textinput)
        self.add_widget(textinput.spinner)
        return self

class HorseInfoFilterLayout(GridLayout):
    def __init__(self, **kwargs):
        super(HorseInfoFilterLayout, self).__init__(cols=5, rows=1, **kwargs)
        self.horse_name_dict, self.blue_list, self.red_list, self.green_list, self.factor_list = read_static_data()
        self.build()

    def build(self):
        return self.create_filter()

    def create_filter(self):
        # label + text
        # typing and searching
        pass

class HorseInfoFilterApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return HorseInfoFilterLayout()

    @classmethod
    def show_horse_info(horse_info: Mapping):
        # TODO: implement to return horse info grid layout
        return

    def show_field():
        return FieldLayout()

if __name__ == '__main__':
    HorseInfoFilterApp().run()