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