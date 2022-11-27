from kivy.base import runTouchApp

from model.horse_data import HorseData
from model.percentage import Percentage
from view.pair_info_layout import PairInfoLayout
from view.sub_view.inheritance_rate_layout import InheritanceRate

def testing_inheritance_rate_layout():
    left_horse_data = HorseData(34)
    right_horse_data = HorseData(31)

    # create
    # pair_info_layout = PairInfoLayout()
    # pair_info_layout.update_left_parent_factor_info_layout(left_horse_data)
    # pair_info_layout.update_right_parent_factor_info_layout(right_horse_data)

    percentage = Percentage(left_horse_data.total_info, right_horse_data.total_info)
    percentage.cal_percentage()
    inheritance_rate_layout = InheritanceRate(percentage=percentage)
    runTouchApp(inheritance_rate_layout.build())

if __name__ == '__main__':
    testing_inheritance_rate_layout()
