from kivy.base import runTouchApp
from testing_data_processor import test_pair_factor
from view.sub_view.parent_factor_info_layout import ParentFactorInfoLayout

def testing_pair_info_layout():
    pair_info = test_pair_factor()
    # create
    runTouchApp(ParentFactorInfoLayout(horse_info=pair_info))

if __name__ == '__main__':
    testing_pair_info_layout()
