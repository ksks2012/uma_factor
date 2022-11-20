from kivy.base import runTouchApp

from model.horse_data import HorseData
from view.pair_info_layout import PairInfoLayout
from view.sub_view.parent_factor_info_layout import ParentFactorInfoLayout

def testing_pair_info_layout():
    left_horse_data = HorseData(0)
    right_horse_data = HorseData(3)

    # create
    pair_info_layout = PairInfoLayout()
    pair_info_layout.update_left_parent_factor_info_layout(left_horse_data)
    pair_info_layout.update_right_parent_factor_info_layout(right_horse_data)
    runTouchApp(pair_info_layout.build())

if __name__ == '__main__':
    testing_pair_info_layout()
