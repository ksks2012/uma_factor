from typing import List, Mapping
from kivy.uix.gridlayout  import GridLayout

from model.horse_data import HORSE_DATA
from view.sub_view.parent_factor_info_layout import ParentFactorInfoLayout

class PairInfoLayout(GridLayout):
    def __init__(self, **kwargs):
        super(PairInfoLayout, self).__init__(cols=2, rows=3, **kwargs)
        self.left_parent_factor_info_layout = ParentFactorInfoLayout()
        self.right_parent_factor_info_layout = ParentFactorInfoLayout()

    def build(self):
        # TODO: Label
        self.add_widget(self.left_parent_factor_info_layout)
        self.add_widget(self.right_parent_factor_info_layout)

        # TODO: select buttom
        # TODO: save data

        return self

    def update_left_parent_factor_info_layout(self, horse_data: HORSE_DATA):
        self.left_parent_factor_info_layout.clear_widgets()
        self.left_parent_factor_info_layout.horse_info = horse_data.total_info
        self.left_parent_factor_info_layout.build()

    def update_right_parent_factor_info_layout(self, horse_data: HORSE_DATA):
        self.right_parent_factor_info_layout.clear_widgets()
        self.right_parent_factor_info_layout.horse_info = horse_data.total_info
        self.right_parent_factor_info_layout.build()