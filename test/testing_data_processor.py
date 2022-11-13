from db_routine.sqlite import SqliteInstance
from util.data_processor import sql_data_to_horse_info, check_parents, total_factor

HORSE_INFO_IDX = [1, '低語溪流 - 超級小溪', None, None, None, '{"2": 1}', '{"5": 2}', '{}', '{"3": 1, "16": 1, "31": 2, "86": 1, "98": 2, "141": 1, "183": 1, "15": 1, "24": 3, "47": 2, "87": 3, "140": 2, "168": 2, "0": 2}']
HORSE_INFO_IDX_RESULT = {'horse_id': 1, 'horse_name': '低語溪流 - 超級小溪', 'parent_one_id': None, 'parent_two_id': None, 'is_owner': None, 'blue_factor': '{"2": 1}', 'red_factor': '{"5": 2}', 'green_factor': '{}', 'white_factor': '{"3": 1, "16": 1, "31": 2, "86": 1, "98": 2, "141": 1, "183": 1, "15": 1, "24": 3, "47": 2, "87": 3, "140": 2, "168": 2, "0": 2}'}

TOTAL_FACTOR_RESULT = {'blue_factor': {'0': {'count': 2, 'stars': 5}, '4': {'count': 1, 'stars': 2}}, 'red_factor': {'5': {'count': 1, 'stars': 3}, '4': {'count': 2, 'stars': 3}}, 'green_factor': {'0': {'count': 1, 'stars': 1}, '15': {'count': 1, 'stars': 2}}, 'white_factor': {'23': {'count': 1, 'stars': 3}, '63': {'count': 1, 'stars': 1}, '12': {'count': 1, 'stars': 1}, '45': {'count': 1, 'stars': 1}, '15': {'count': 1, 'stars': 2}, '36': {'count': 1, 'stars': 1}, '10': {'count': 1, 'stars': 2}, '24': {'count': 1, 'stars': 2}, '67': {'count': 2, 'stars': 3}, '46': {'count': 1, 'stars': 1}, '61': {'count': 1, 'stars': 1}, '0': {'count': 1, 'stars': 1}, '52': {'count': 1, 'stars': 1}}}

def testing_sql_data_to_horse_info():
    result = sql_data_to_horse_info(HORSE_INFO_IDX)
    print("testing_sql_data_to_horse_info: ", result == HORSE_INFO_IDX_RESULT)

def testing_check_parent():
    check_parents(1, 1, 10)
    check_parents(0, 1, 1)
    check_parents(0, 1, 2)
    check_parents(0, 1, 2)
    check_parents(1, 1, 2)

def test_total_factor():
    sqlite_instance = SqliteInstance()
    sqlite_instance.connect("var/data.db3")
    horse_id = 0
    horse_info = {}
    parent_one_info = {}
    parent_two_info = {}
    try:
        horse_info = sqlite_instance.select_horse_by_id(horse_id)
        horse_info = sql_data_to_horse_info(horse_info)[0]
        print(horse_info)
        parent_one_info = sqlite_instance.select_horse_by_id(horse_info['parent_one_id'])
        parent_one_info = sql_data_to_horse_info(parent_one_info)[0]
        print(parent_one_info)
        parent_two_info = sqlite_instance.select_horse_by_id(horse_info['parent_two_id'])
        parent_two_info = sql_data_to_horse_info(parent_two_info)[0]
        print(parent_two_info)
    except Exception as e:
        print("test_total_factor fail %s" % e)
    total_result = total_factor(horse_info, parent_one_info, parent_two_info)
    print(total_result == TOTAL_FACTOR_RESULT)

if __name__ == '__main__':
    # testing_sql_data_to_horse_info()
    # testing_check_parent()
    test_total_factor()  