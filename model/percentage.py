import copy
from typing import Mapping

from util.inheritance import get_inheritance

class Percentage():
    def __init__(self, left_parent_data: Mapping, right_parent_data: Mapping) -> None:
        self.inheritance_rate = get_inheritance()
        
        self.left_parent_data = left_parent_data
        self.right_parent_data = right_parent_data

        self.rate = {}

    def _fetch_count(self, parent_data: Mapping):
        for key, value in parent_data.get("white_factor").items():
            count = value.get("count", 0)
            if key in self.rate:
                self.rate[key] = self.rate[key] + count
            else:
                self.rate[key] = count



    def cal_percentage(self):
        self._fetch_count(self.left_parent_data)
        self._fetch_count(self.right_parent_data)

        for key, value in self.rate.items():
            self.rate[key] = self.inheritance_rate.get(value, 0)
