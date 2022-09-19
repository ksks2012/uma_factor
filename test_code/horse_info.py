# -*- coding: utf-8 -*-

from typing import Mapping
from kivy.app import App
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.boxlayout  import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.text import LabelBase
import kivy

import os

kivy.resources.resource_add_path(os.path.abspath('./font/msjh.ttc'))
LabelBase.register('zh_font', './font/msjh.ttc')

class HorseInfoApp(App):
    horse_info = {'horse_name': '神鷹☆Numero1', 'blue': {'智力': 2}, 'red': {'中距離': 1}, 'white': {'路況差勁': 1, '彎道靈巧': 1, 'URA劇本': 1, '陰天': 1, '集中力': 1}}
    def build(self):
        count = len(self.horse_info) - 1 + len(self.horse_info.get("white", {}))
        horse_info_grid = GridLayout(cols=2, rows=count//2+1)

        # TODO: background
        # TODO: stars
        horse_info_grid.add_widget(Label(text=self.horse_info["horse_name"]))
        horse_info_grid.add_widget(Label(text=list(self.horse_info["blue"].keys())[0]))
        horse_info_grid.add_widget(Label(text=list(self.horse_info["red"].keys())[0]))
        if self.horse_info.get("green") is not None:
            horse_info_grid.add_widget(Label(text=list(self.horse_info["green"].keys())[0]))
        # TODO: check if horse_info had missing value
        for key, value in self.horse_info.get("white", {}).items():
            l = Label(text=str(key))
            horse_info_grid.add_widget(l)
        return horse_info_grid

    @classmethod
    def show_horse_info(horse_info: Mapping):
        # TODO: implement to return horse info grid layout
        return

if __name__ == '__main__':
    HorseInfoApp().run()