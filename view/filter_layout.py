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
import util.text as TEXT

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

    def init_spinner(self):
        self.spinner = Spinner(
            # default value shown
            # text='>',
            # available values
            values=self.all_of_data,
            # just for positioning in our example
            # size_hint=(None, None),
            # size=(100, 44),
            # pos_hint={'center_x': .5, 'center_y': .5}
        )

    def insert_text(self, substring, from_undo=False):
        update_value = []
        for v in self.all_of_data:
            if substring in v:
                update_value.append(v)
        self.spinner.values = update_value
        return super().insert_text(substring, from_undo=from_undo)

class FieldLayout(GridLayout):
    def __init__(self, label_name="", spin_data=[], **kwargs):
        super(FieldLayout, self).__init__(cols=1, rows=3, **kwargs)
        self.label_name = label_name
        self.spin_data = spin_data
        self.build()
    
    def build(self):
        # label
        label = Label(text=self.label_name)
        # text
        textinput = InputWithSpinner(all_of_data=self.spin_data ,text='', multiline=False)

        self.add_widget(label)
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

    def _process_horse_name(self) -> List:
        horse_name_list = []

        for key, value in self.horse_name_dict.items():
            tmp = f"{key} - {value}"
            horse_name_list.append(tmp)
    
        return horse_name_list

    def create_filter(self) -> GridLayout:
        # label + text
        # typing and searching
        self.horse_name_filter = FieldLayout(label_name=TEXT.HORSE_FILTER_LABEL_NAME, spin_data=self._process_horse_name())
        self.blue_filter = FieldLayout(label_name=TEXT.BLUE_FILTER_LABEL_NAME, spin_data=self.blue_list)
        self.red_filter = FieldLayout(label_name=TEXT.RED_FILTER_LABEL_NAME, spin_data=self.red_list)
        self.green_filter = FieldLayout(label_name=TEXT.GREEN_FILTER_LABEL_NAME, spin_data=self.green_list)
        self.factor_filter = FieldLayout(label_name=TEXT.WHITE_FILTER_LABEL_NAME, spin_data=self.factor_list)

        self.add_widget(self.horse_name_filter)
        self.add_widget(self.blue_filter)
        self.add_widget(self.red_filter)
        self.add_widget(self.green_filter)
        self.add_widget(self.factor_filter)

        return self

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