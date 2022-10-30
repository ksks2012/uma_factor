from view.horse_info_flat import HorseInfoFlatApp
from util.data_processor import sql_data_to_horse_info

HORSE_INFO = {'horse_name': '低語溪流 - 超級小溪', 'blue_factor': '{"2": 1}', 'red_factor': '{"5": 2}', 'green_factor': '{}', 'white_factor': '{"3": 1, "16": 1, "31": 2, "86": 1, "98": 2, "141": 1, "183": 1, "15": 1, "24": 3, "47": 2, "87": 3, "140": 2, "168": 2, "0": 2}'}
HORSE_INFO_IDX = [(1, '低語溪流 - 超級小溪', None, None, None, '{"2": 1}', '{"5": 2}', '{}', '{"3": 1, "16": 1, "31": 2, "86": 1, "98": 2, "141": 1, "183": 1, "15": 1, "24": 3, "47": 2, "87": 3, "140": 2, "168": 2, "0": 2}')]

def testing_horse_info_flat_layout():
    HorseInfoFlatApp(horse_info=HORSE_INFO).run()

if __name__ == '__main__':
    testing_horse_info_flat_layout()