import re
import sys
from typing import Mapping
from unittest.util import strclass

import cv2
import pyscreenshot as ImageGrab
from db_routine.sqlite import SqliteInstance

from input import image_processing
from util.common import read_static_data

SOURCE_FILE_NAME = "./var/fullscreen.png"

TEST_STR = ['「持有因子', '速度', '寶塚紀念', '晴天○', '放學的樂趣', '因子一覽', '關閉', '[火紅鬥爭]', '黃金船', '中距離', '希望S', '深呼吸']

# fix error by google API response
# TODO: middleware by language 
def fix_text(test_str):
    for i in range(len(test_str)):
        test_str[i] = re.sub("\||\[|\]|\●|\ ", "", test_str[i])
        test_str[i] = re.sub("◎|〇|○", "o", test_str[i])
        test_str[i] = re.sub("營道|警道", "彎道", test_str[i])
        test_str[i] = re.sub("皐", "皋", test_str[i])
        test_str[i] = re.sub("（", "(", test_str[i])
        test_str[i] = re.sub("）", ")", test_str[i])
        if(len(test_str[i]) > 1 and (test_str[i][-1] != 'o' and test_str[i][-1] != 'O')):
            continue 
        test_str[i] = re.sub("o|O", "", test_str[i])
        print(test_str[i])

class HorseFetcher():
    def __init__(self, use_api = False, screen_shot = False) -> None:
        # processing args
        self.use_api = 0
        self.screen_shot = 0
        print(sys.argv)
        try:
            self.use_api = use_api
            self.screen_shot = screen_shot
        except:
            print("No input arg")

        self.horse_name = ""
        self.blue = ""
        self.red = ""
        self.green = ""

        self.factor = None
        self.exist_factor_idx = []

        self.stars = {}

        self._horse_info = {}
        
        self.white_factor_count = 0

        self.sqlite_instance = SqliteInstance()
        self.sqlite_instance.connect("var/data.db3")

        self.horse_name_dict, self.blue_list, self.red_list, self.green_list, self.factor_list = read_static_data()

    # img to text
    def fetch_screen(self):
        if self.screen_shot == 1:
            # screen shot
            image = ImageGrab.grab(bbox=(1350, 100, 1920, 800))

            # save image
            image.save(SOURCE_FILE_NAME)

        image = cv2.imread('./var/fullscreen.png')

        # use google API to trans image to text
        if self.use_api == 1:
            test_str, text_allocate_list = image_processing.detect_text(SOURCE_FILE_NAME)
            text_allocate_list = image_processing.merge_text_allocate_list(text_allocate_list)
            # cut_text(image, text_allocate_list)
            print(text_allocate_list)
        else:
            test_str = TEST_STR
            print("No google api support")
            return

        # fix text
        fix_text(test_str)

        self.factor = [0] * len(self.factor_list)


        # mapping factor
        ## get horse name
        ## get blue/red factor
        ## get white factor
        print("List of white factor:")

        for i in range(len(test_str)):
            x1 = text_allocate_list[i + 1][0][0] + 60
            y1 = text_allocate_list[i + 1][0][1]
            x2 = text_allocate_list[i + 1][0][0] + 130
            y2 = text_allocate_list[i + 1][0][1] + 30

            if len(self.horse_name) == 0 and test_str[i] in self.horse_name_dict.keys():
                self.horse_name = f"{test_str[i]} - {self.horse_name_dict[test_str[i]]}"
                continue
            ### TODO: judge the number of star
            if len(self.blue) == 0 and test_str[i] in self.blue_list:
                self.blue = test_str[i]
                try:
                    self.stars[self.blue] = image_processing.star_tracker(image[y1 : y2, x1: x2], "blue")
                except Exception as e:
                    print("error when blue factor use star_tracker()", e)
                continue
            if len(self.red) == 0 and test_str[i] in self.red_list:
                self.red = test_str[i]
                try:
                    self.stars[self.red] = image_processing.star_tracker(image[y1 : y2, x1: x2], "red")
                except:
                    print("error when red factor use star_tracker()")
                continue
            if len(self.green) == 0 and test_str[i] in self.green_list:
                self.green = test_str[i]
                try:
                    self.stars[self.green] = image_processing.star_tracker(image[y1 : y2, x1: x2], "green")
                except:
                    print("error when green factor use star_tracker()")
                continue
            ###
            idx = -1
            try:
                idx = self.factor_list.index(test_str[i])
                print(test_str[i])
                self.white_factor_count += 1
            except:
                pass
            if(idx != -1):
                try:
                    self.factor[idx] = image_processing.star_tracker(image[y1 : y2, x1: x2], str(idx))
                    self.stars[self.factor_list[idx]] = self.factor[idx]
                    self.exist_factor_idx.append(idx)
                except:
                    self.factor[idx] = 1
                    print("error when white factor use star_tracker()")

        # # gen _horse_info
        # self._gen_horse_info_in_index()

    def _gen_horse_info_in_text(self):
        self._horse_info["horse_name"] = self.horse_name
        self._horse_info["blue"] = {self.blue: self.stars[self.blue]}
        self._horse_info["red"] = {self.red: self.stars[self.red]}
        if len(self.green) != 0: 
            self._horse_info["green"] = {self.green: self.stars[self.green]}
        exist_white_factor = {}
        for idx in self.exist_factor_idx:
            exist_white_factor[self.factor_list[idx]] = self.stars[self.factor_list[idx]]

        self._horse_info["white"] = exist_white_factor

    def _gen_horse_info_in_index(self):
        self._horse_info["horse_name"] = self.horse_name
        self._horse_info["blue"] = {self.blue_list.index(self.blue): self.stars[self.blue]}
        self._horse_info["red"] = {self.red_list.index(self.red): self.stars[self.red]}
        if len(self.green) != 0: 
            self._horse_info["green"] = {self.green_list.index(self.green): self.stars[self.green]}
        exist_white_factor = {}
        for idx in self.exist_factor_idx:
            exist_white_factor[idx] = self.stars[self.factor_list[idx]]

        self._horse_info["white"] = exist_white_factor

    def trans_csv(self, path = 'output.txt'):
        ## trans to csv row
        # TODO: save in DB
        # TODO: change value by number of star
        csv_result = f"{self.horse_name}\t{self.blue} {self.stars[self.blue]}\t{self.red} {self.stars[self.red]}"
        if(self.green != ""):
            csv_result += f"\t{self.stars[self.green]}"
        else:
            csv_result += "\t0"

        for v in self.factor:
            csv_result += f"\t{v}"

        print("================================")
        print(csv_result)
        print("================================")
        f = open(path, 'w', encoding='utf8')
        f.write(csv_result)

        print(f"白因子{self.white_factor_count}")

    def gen_sql_col_cmd(self) -> str:
        col_cmd = ""
        col_cmd += "'horse_name'"
        col_cmd += f", '{self.blue}'"
        col_cmd += f", '{self.red}'"
        if len(self.green) != 0:
            col_cmd += f", '{self.green}'"

        for idx in self.exist_factor_idx:
            col_cmd += f", '{self.factor_list[idx]}'"

        return col_cmd

    def gen_sql_value_cmd(self) -> str:
        value_cmd = ""
        value_cmd += f"'{self.horse_name}'"
        value_cmd += f", {self.stars[self.blue]}"
        value_cmd += f", {self.stars[self.red]}"
        if len(self.green) != 0:
            value_cmd += f", {self.stars[self.green]}"

        for idx in self.exist_factor_idx:
            value_cmd += f", {self.stars[self.factor_list[idx]]}"

        return value_cmd

    def gen_sql_col_cmd2(self) -> str:
        col_cmd = ""
        col_cmd += '"horse_name"'
        col_cmd += f', "{self.blue}"'
        col_cmd += f', "{self.red}"'
        if len(self.green) != 0:
            col_cmd += f', "{self.green}"'

        for idx in self.exist_factor_idx:
            col_cmd += f', "{self.factor_list[idx]}"'
        
        return col_cmd

    def gen_sql_condition_cmd(self) -> str:
        col_cmd = ""
        col_cmd += f'"horse_name" = "{self.horse_name}"'
        col_cmd += f' AND "{self.blue}" = {self.stars[self.blue]}'
        col_cmd += f' AND "{self.red}" = {self.stars[self.red]}'
        if len(self.green) != 0:
            col_cmd += f' AND "{self.green}" = {self.stars[self.green]}'

        for idx in self.exist_factor_idx:
            col_cmd += f' AND "{self.factor_list[idx]}" = {self.stars[self.factor_list[idx]]}'

        return col_cmd   

    def trans_sql_cmd(self) -> str:
        # insert data from input.screen
        col_cmd = self.gen_sql_col_cmd()
        value_cmd = self.gen_sql_value_cmd()
        sql_cmd = f"INSERT INTO HorseData ({col_cmd}) VALUES ({value_cmd})"
        return sql_cmd
    
    def trans_search_cmd(self) -> str:
        col_cmd = self.gen_sql_col_cmd2()
        condition_cmd = self.gen_sql_condition_cmd()
        sql_cmd = f"SELECT {col_cmd} FROM HorseData WHERE {condition_cmd}"
        print(sql_cmd)
        # self.sqlite_instance.search_horse(sql_cmd)
        return sql_cmd
    
    def check_horse_exist(self) -> bool:
        print(len(self.sqlite_instance.search_horse(self.trans_search_cmd())))
        if len(self.sqlite_instance.search_horse(self.trans_search_cmd())) != 0:
            print("\nFind repeat horse!\n")
            return True
        return False

    def save_horse_info_in_db(self):
        if len(self.horse_info) != 0 and self.check_horse_exist() is False:
            self.sqlite_instance.run_sql_cmd(self.trans_sql_cmd())

    @property
    def horse_info(self) -> Mapping:
        return self._horse_info

if __name__ == '__main__':
    horse_fetcher = HorseFetcher(int(sys.argv[1]), int(sys.argv[2]))
    horse_fetcher.fetch_screen()
    horse_fetcher.trans_csv()
    key_in = sys.stdin.readline()
    if key_in == 'y\n' or key_in == "\n":
        horse_fetcher.save_horse_info_in_db()