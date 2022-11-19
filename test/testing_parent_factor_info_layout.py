from kivy.base import runTouchApp

from model.horse_data import HORSE_DATA
from testing_data_processor import test_pair_factor
from view.sub_view.parent_factor_info_layout import ParentFactorInfoLayout

def testing_parent_factor_info_layout():
    horse_data = HORSE_DATA(0)
    # create
    runTouchApp(ParentFactorInfoLayout(horse_info=horse_data.total_info))
    # runTouchApp(ParentFactorInfoLayout())

if __name__ == '__main__':
    testing_parent_factor_info_layout()
