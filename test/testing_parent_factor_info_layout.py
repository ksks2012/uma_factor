from kivy.base import runTouchApp

from model.horse_data import Horse_DATA
from testing_data_processor import test_pair_factor
from view.sub_view.parent_factor_info_layout import ParentFactorInfoLayout

def testing_pair_info_layout():
    horse_data = Horse_DATA(0)
    # create
    runTouchApp(ParentFactorInfoLayout(horse_info=horse_data.total_info))

if __name__ == '__main__':
    testing_pair_info_layout()
