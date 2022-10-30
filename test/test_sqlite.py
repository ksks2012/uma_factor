from db_routine.sqlite import SqliteInstance

if __name__ == '__main__':
    sqlite_instance = SqliteInstance()
    sqlite_instance.connect("var/data.db3")
    print(sqlite_instance.is_table_exist("HorseData"))
    sqlite_instance.create_talbe()
    print(sqlite_instance.is_table_exist("HorseData"))
    print(sqlite_instance.list_horse_info())
    print(sqlite_instance.list_horse_info_with_factor())
    print(sqlite_instance.select_field("HorseData"))
    print(sqlite_instance.paging_horse_info_with_factor(10, 10))
