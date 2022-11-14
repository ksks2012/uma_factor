import json

from typing import List, Mapping
from view.layout import HorseInfoLayout
from view.label_gen import LabelGen

class PairInfoLayout(HorseInfoLayout):
    def __init__(self, horse_info=None, **kwargs):
        super(PairInfoLayout, self).__init__(horse_info=horse_info, cols=2, rows=30, **kwargs)

    def _info_to_label(self):
        pass

    def _add_info(self, factor_list, info: Mapping, color: str):
        for factor_idx, values in info.items():
            count = values.get("count", 0)
            stars = values.get("stars", 0)
            self.add_widget(LabelGen(text=f"{factor_list[int(factor_idx)]} {stars}★ *{count}", backgroud_color=color))

    def build(self):
        self._add_info(self.blue_list, self.horse_info.get("blue_factor", '{}'), 'blue')
        self._add_info(self.red_list, self.horse_info.get("red_factor", '{}'), 'red')
        self._add_info(self.green_list, self.horse_info.get("green_factor", '{}'), 'green')
        self._add_info(self.factor_list, self.horse_info.get("white_factor", '{}'), 'balck')

        return self