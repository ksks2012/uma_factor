# -*- coding: utf-8 -*-
import json
import os

from typing import List, Mapping
import kivy
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.label import Label

from view.label_gen import LabelGen
from view.layout import HorseInfoLayout
from util.common import read_static_data

kivy.resources.resource_add_path(os.path.abspath('./font/msjh.ttc'))
LabelBase.register('zh_font', './font/msjh.ttc')

class HorseInfoFlatLayout(HorseInfoLayout):
    def __init__(self, horse_info=None, **kwargs):
        super(HorseInfoFlatLayout, self).__init__(horse_info=horse_info, cols=5, rows=1, **kwargs)


    def build(self):
        self.add_widget(Label(text=self.horse_info.get("horse_name", "")))
        blue_idx, stars = self._info_to_label(self.horse_info.get("blue_factor", '{}'))
        self.add_widget(LabelGen(text=self.blue_list[blue_idx] + self.gen_star_with_info(stars), backgroud_color='blue'))
        red_idx, stars = self._info_to_label(self.horse_info.get("red_factor", '{}'))
        self.add_widget(LabelGen(text=self.red_list[red_idx] + self.gen_star_with_info(stars), backgroud_color='red'))
        green_idx, stars = self._info_to_label(self.horse_info.get("green_factor", '{}'))
        if type(green_idx) is not int:
            self.add_widget(LabelGen(text="-", backgroud_color='green'))
        else:
            self.add_widget(LabelGen(text=self.green_list[green_idx] + self.gen_star_with_info(stars), backgroud_color='green'))

        # TODO: check if horse_info had missing value
        # TODO: button to all white factor
        white_factor_count = len(json.loads(self.horse_info.get("white_factor", '{}')).items())
        white_label = LabelGen(text=str(white_factor_count), backgroud_color='balck')
        self.add_widget(white_label)
        return self
    
    # callback function for update self widget
    def update_horse_info(self, info: Mapping, delta_time: float):
        if info != self.horse_info:
            self.horse_info = info
            self.clear_widgets()
            self.build()

class HorseInfoFlatApp(App):
    def __init__(self, horse_info={}, **kwargs):
        super().__init__(**kwargs)
        self.horse_info = horse_info

    def build(self):
        return HorseInfoFlatLayout(horse_info=self.horse_info)

    @classmethod
    def show_horse_info(horse_info: Mapping):
        # TODO: implement to return horse info grid layout
        return

if __name__ == '__main__':
    HorseInfoFlatApp().run()