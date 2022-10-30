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

kivy.resources.resource_add_path(os.path.abspath('./font/msjh.ttc'))
LabelBase.register('zh_font', './font/msjh.ttc')

class HorseInfoDetailLayout(HorseInfoLayout):
    def __init__(self, horse_info={}, **kwargs):
    #     self.horse_info = horse_info
    #     # count = len(self.horse_info) - 1 + len(self.horse_info.get("white", {}))
        super(HorseInfoDetailLayout, self).__init__(horse_info=horse_info, cols=2, rows=20, **kwargs)
    #     self.horse_name_dict, self.blue_list, self.red_list, self.green_list, self.factor_list = read_static_data()
    #     self.build()

    def build(self):
        # TODO: background
        # TODO: stars
        self.add_widget(Label(text=self.horse_info.get("horse_name", "")))
        blue_idx, stars = self._info_to_label(self.horse_info.get("blue_factor", '{}'))
        self.add_widget(LabelGen(text=self.blue_list[blue_idx] + self.gen_star_with_info(stars), backgroud_color='blue'))
        red_idx, stars = self._info_to_label(self.horse_info.get("red_factor", '{}'))
        self.add_widget(LabelGen(text=self.red_list[red_idx] + self.gen_star_with_info(stars), backgroud_color='red'))
        green_idx, stars = self._info_to_label(self.horse_info.get("green_factor", '{}'))
        if type(green_idx) is not int:
            self.add_widget(LabelGen(text="-", backgroud_color='green'))
        else:
            self.add_widget(LabelGen(text=self.green_list[green_idx], backgroud_color='green'))
        
        # TODO: check if horse_info had missing value
        for key, value in json.loads(self.horse_info.get("white_factor", '{}')).items():
            label = LabelGen(text=self.factor_list[int(key)] + self.gen_star_with_info(value), backgroud_color='balck')
            self.add_widget(label)
        print(self.horse_info)
        return self
    
class HorseInfoApp(App):
    def __init__(self, horse_info={}, **kwargs):
        super().__init__(**kwargs)
        self.horse_info = horse_info

    def build(self):
        return HorseInfoDetailLayout(horse_info=self.horse_info)

    @classmethod
    def show_horse_info(horse_info: Mapping):
        # TODO: implement to return horse info grid layout
        return

if __name__ == '__main__':
    HorseInfoApp().run()