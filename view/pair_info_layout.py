from typing import List, Mapping

from kivy.clock import Clock
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.button import Button
from functools import partial

from model.horse_data import HorseData
from view.sub_view.parent_factor_info_layout import ParentFactorInfoLayout
import util.text as TEXT

class PairInfoLayout(GridLayout):
    def __init__(self, **kwargs):
        super(PairInfoLayout, self).__init__(cols=2, rows=2, **kwargs)
        self.left_parent_factor_info_layout = ParentFactorInfoLayout()
        self.right_parent_factor_info_layout = ParentFactorInfoLayout()

    @property
    def left_total_info(self):
        return self.left_parent_factor_info_layout.info

    @property
    def right_total_info(self):
        return self.right_parent_factor_info_layout.info

    def build(self):
        # TODO: Label
        self.add_widget(self.left_parent_factor_info_layout)
        self.add_widget(self.right_parent_factor_info_layout)

        select_left_parent_bt = Button(text=TEXT.BT_SELECT_LEFT_PARENT, size_hint=(1, .15))
        select_left_parent_bt.bind(on_press=self.press_select_left_parent_bt)

        select_right_parent_bt = Button(text=TEXT.BT_SELECT_RIGHT_PARENT, size_hint=(1, .15))
        select_right_parent_bt.bind(on_press=self.press_select_right_parent_bt)

        self.add_widget(select_left_parent_bt)
        self.add_widget(select_right_parent_bt)

        return self

    def press_select_left_parent_bt(self, arg):
        # TODO: select id
        Clock.schedule_once(partial(self.update_left_parent_factor_info_layout, HorseData(39)))


    def press_select_right_parent_bt(self, arg):
        # TODO: select id
        Clock.schedule_once(partial(self.update_right_parent_factor_info_layout, HorseData(36)))

    def update_left_parent_factor_info_layout(self, horse_data: HorseData, delta_time: float):
        self.left_parent_factor_info_layout.clear_widgets()
        self.left_parent_factor_info_layout.horse_info = horse_data.total_info
        self.left_parent_factor_info_layout.build()

    def update_right_parent_factor_info_layout(self, horse_data: HorseData, delta_time: float):
        self.right_parent_factor_info_layout.clear_widgets()
        self.right_parent_factor_info_layout.horse_info = horse_data.total_info
        self.right_parent_factor_info_layout.build()