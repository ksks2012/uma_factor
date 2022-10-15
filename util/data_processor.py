from typing import List
from db_routine.sqlite import SqliteInstance

# sql data list to horse info data
def sql_data_to_horse_info(data: List):
    sqlite_instance = SqliteInstance()
    sqlite_instance.connect("var/data.db3")
    horse_data_field = sqlite_instance.select_field("HorseData")
    result = {}
    if len(horse_data_field) != len(data):
        return result

    for i in range(len(data)):
        result[horse_data_field[i]] = data[i]

    return result