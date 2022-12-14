from view.show_horses import ShowHorsesApp
from util.data_processor import sql_data_to_horse_info
from db_routine.sqlite import SqliteInstance
import util.define as DEFINE

HORSE_INFO = {'horse_name': '神鷹☆Numero1', 'blue': {'智力': 2}, 'red': {'中距離': 1}, 'white': {'路況差勁': 1, '彎道靈巧': 1, 'URA劇本': 1, '陰天': 1, '集中力': 1}}
HORSE_INFO_IDX = [(1, '低語溪流 - 超級小溪', None, None, None, '{"2": 1}', '{"5": 2}', '{}', '{"3": 1, "16": 1, "31": 2, "86": 1, "98": 2, "141": 1, "183": 1, "15": 1, "24": 3, "47": 2, "87": 3, "140": 2, "168": 2, "0": 2}')]

def testing_show_horse():
    sqlite_instance = SqliteInstance()
    sqlite_instance.connect("var/data.db3")
    offset = 0 * DEFINE.NUM_OF_HORSE_INFO_IN_PAGE
    ShowHorsesApp(horse_info_list=sql_data_to_horse_info(sqlite_instance.paging_horse_info_with_factor(DEFINE.NUM_OF_HORSE_INFO_IN_PAGE, offset))).run()
    
if __name__ == '__main__':
    testing_show_horse()