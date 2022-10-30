import json
from typing import List, Mapping

from kivy.uix.gridlayout  import GridLayout

from util.common import read_static_data

class HorseInfoLayout(GridLayout):
    def __init__(self, horse_info=None, **kwargs):
        self.horse_info = horse_info
        super(HorseInfoLayout, self).__init__(**kwargs)
        self.horse_name_dict, self.blue_list, self.red_list, self.green_list, self.factor_list = read_static_data()
        if horse_info is None:
            return self
        self.build()

    def _info_to_label(self, info: str) -> List:
        print(info)
        info = json.loads(info)
        if len(info) == 0:
            return None, None
        
        info_keys = list(info.keys())
        info_value = list(info.values())
        if len(info_keys) == 0:
            return None, None

        return int(info_keys[0]), int(info_value[0])

    def gen_star_with_info(self, num_star):        
        star = " "
        for i in range(num_star):
            star += "★"
        return star
        
    # callback function for update self widget
    def update_horse_info(self, info: Mapping, delta_time: float):
        if info != self.horse_info:
            self.horse_info = info
            self.clear_widgets()
            self.build()
