from typing import List
from db_routine.sqlite import SqliteInstance
import util.path as PATH

# sql data list to horse info data
def sql_data_to_horse_info(data: List):
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