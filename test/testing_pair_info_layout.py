from kivy.base import runTouchApp
from testing_data_processor import test_pair_factor
from view.pair_info_layout import PairInfoLayout

def testing_pair_info_layout():
    pair_info = test_pair_factor()
    # create
    runTouchApp(PairInfoLayout(horse_info=pair_info))

if __name__ == '__main__':
    testing_pair_info_layout()
