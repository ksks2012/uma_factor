import json
from typing import List, Mapping
from db_routine.sqlite import SqliteInstance
import util.path as PATH

# sql data list to horse info data
def sql_data_to_horse_info(data: List) -> List:
    sqlite_instance = SqliteInstance()
    sqlite_instance.connect(PATH.DB_PATH)
    horse_data_field = sqlite_instance.select_field("HorseData")
    result = []
    for info in data:
        tmp = {}

        for i in range(len(info)):
            tmp[horse_data_field[i]] = info[i]
        
        result.append(tmp)

    return result

PARENT_NAME = {0: "parent_one_id", 1: "parent_two_id"}

def check_parents(parent_number: int, parent_id: int, child_id: int):
    sqlite_instance = SqliteInstance()
    sqlite_instance.connect(PATH.DB_PATH)
    # child exist
    sql_cmd = f"SELECT * from HorseData where horse_id={child_id}"
    result = sqlite_instance.search_horse(sql_cmd)
    if len(result) == 0:
        print("check_parents: missing child")
        return 

    # child == parent
    if parent_id == child_id:
        print("check_parents: same id")
        return

    # repeat
    sql_cmd = f"SELECT {PARENT_NAME[not parent_number]} from HorseData where horse_id='{child_id}'"
    result = sqlite_instance.search_horse(sql_cmd)
    if result[0][0] is not None and int(result[0][0]) == parent_id:
        print("check_parents: repeat parent id")
        return
    
    sqlite_instance.set_parents(PARENT_NAME[parent_id], parent_id, child_id)
    print("check_parents: success")

def _store_factor(total_factor: Mapping, horse_info: Mapping) -> Mapping:
    """
        total_factor
            $store_key
                $factor_name
                    count
                    stars
    """

    store_key = ['blue_factor', 'red_factor', 'green_factor', 'white_factor']

    for key, value in horse_info.items():
        if key in store_key:
            if total_factor.get(key) is None:
                total_factor[key] = {}
            for factor_name, factor_stars in json.loads(value).items():
                if factor_name in total_factor.get(key):
                    total_factor[key][factor_name]['count'] += 1
                    total_factor[key][factor_name]['stars'] += factor_stars
                else:
                    if total_factor[key].get(factor_name) is None:
                        total_factor[key][factor_name] = {}
                    total_factor[key][factor_name]['count'] = 1
                    total_factor[key][factor_name]['stars'] = factor_stars

    return total_factor

def total_factor(horse_info: Mapping, parent_one_info: Mapping, parent_two_info: Mapping) -> Mapping:
    # merge child and two parent
    total_factor = {}

    total_factor = _store_factor(total_factor, horse_info)
    total_factor = _store_factor(total_factor, parent_one_info)
    total_factor = _store_factor(total_factor, parent_two_info)

    return total_factor