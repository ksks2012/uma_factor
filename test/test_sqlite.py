from db_routine.sqlite import SqliteInstance

if __name__ == '__main__':
    sqlite_instance = SqliteInstance()
    sqlite_instance.connect("var/data.db3")
    print(sqlite_instance.is_table_exist("HorseData"))
    sqlite_instance.create_talbe()
    print(sqlite_instance.is_table_exist("HorseData"))
