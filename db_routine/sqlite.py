from operator import truediv
import os

import sqlite3
from typing import List

from util.common import read_static_data

class SqliteInstance():
    def __init__(self) -> None:
        self.connection = None

    def connect(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.create_talbe()

    def get_all_horse_data(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * from HorseData')
        self.connection.commit()

        return cursor.fetchall()
    
    def is_table_exist(self, table_name: str) -> bool:
        try:
            sql_cmd = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
            cursor = self.connection.cursor()
            cursor.execute(sql_cmd)
            self.connection.commit()
        except:
            return False

        return len(cursor.fetchall()) != 0

    def create_talbe(self):
        # create table
        if self.is_table_exist("HorseData") is True:
            return
            
        _, blue_list, red_list, green_list, factor_list = read_static_data()
        db_field_list = []
        db_field_list.extend(blue_list)
        db_field_list.extend(red_list)
        db_field_list.extend(green_list)
        db_field_list.extend(factor_list)

        sql_cmd = f"CREATE TABLE HorseData('horse_id' INTEGER PRIMARY KEY AUTOINCREMENT, 'horse_name', 'parent_one_id', 'parent_two_id', 'is_owner'"
        count = 0
        for field in db_field_list:
            sql_cmd += f",'{field}'"
        sql_cmd += ")"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_cmd)
            self.connection.commit()
        except Exception as e:
            print(f"create_talbe error: {e}")

    def search_horse(self, cmd) -> List:
        try:
            cursor = self.connection.cursor()
            cursor.execute(cmd)
            self.connection.commit()
        except:
            return []

        return cursor.fetchall()


    def run_sql_cmd(self, sql_cmd: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_cmd)
        except Exception as e:
            print("run_sql_cmd error: %s", e)
        self.connection.commit()