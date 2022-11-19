from db_routine.sqlite import SqliteInstance
from util.data_processor import sql_data_to_horse_info, total_factor
import util.path as PATH

class HORSE_DATA():
    def __init__(self, child) -> None:
        self.sqlite_instance = SqliteInstance()
        self.sqlite_instance.connect(PATH.DB_PATH)

        self.child_id = child
        self.parent_one_id = -1
        self.parent_two_id = -1
        self.update_parent_id()

    def update_parent_id(self):
        child_info = self.sqlite_instance.select_horse_by_id(self.child_id)
        self.child_info = sql_data_to_horse_info(child_info)[0]
        self.parent_one_id = self.child_info.get("parent_one_id", -1)
        self.parent_two_id = self.child_info.get("parent_two_id", -1)

        parent_one_info = self.sqlite_instance.select_horse_by_id(self.parent_one_id)
        self.parent_one_info = sql_data_to_horse_info(parent_one_info)[0]
        parent_two_info = self.sqlite_instance.select_horse_by_id(self.parent_two_id)
        self.parent_two_info = sql_data_to_horse_info(parent_two_info)[0]
        self.total_info = total_factor(self.child_info, self.parent_one_info, self.parent_two_info)
