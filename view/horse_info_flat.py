# -*- coding: utf-8 -*-

from cProfile import label
from typing import List, Mapping
from kivy.app import App
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.boxlayout  import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.text import LabelBase
import kivy

import os
from view.label_gen import LabelGen

kivy.resources.resource_add_path(os.path.abspath('./font/msjh.ttc'))
LabelBase.register('zh_font', './font/msjh.ttc')

class HorseInfoFlatLayout(GridLayout):
    def __init__(self, horse_info={}, **kwargs):
        self.horse_info = horse_info
        # count = len(self.horse_info) - 1 + len(self.horse_info.get("white", {}))
        super(HorseInfoFlatLayout, self).__init__(cols=5, rows=1, **kwargs)
        self.build()

    def _info_to_lable(self, info: Mapping) -> List:
        if len(info) == 0:
            return ""
        
        info_keys = list(info.keys())
        if len(info_keys) == 0:
            return ""

        return info_keys[0]

    def build(self):
        # TODO: background
        # TODO: stars
        self.add_widget(Label(text=self.horse_info.get("horse_name", "")))
        self.add_widget(LabelGen(text=self._info_to_lable(self.horse_info.get("blue", {})), backgroud_color='blue'))
        self.add_widget(LabelGen(text=self._info_to_lable(self.horse_info.get("red", {})), backgroud_color='red'))
        if self.horse_info.get("green") is not None:
            self.add_widget(LabelGen(text=self._info_to_lable(self.horse_info.get("green", {})), backgroud_color='green'))

        # TODO: check if horse_info had missing value
        white_factor_count = len(self.horse_info.get("white", {}).items())
        white_label = LabelGen(text=str(white_factor_count), backgroud_color='balck')
        self.add_widget(white_label)
        print(self.horse_info)
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