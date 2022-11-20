from kivy.uix.gridlayout  import GridLayout

from model.percentage import Percentage
from view.label_gen import LabelGen
from util.common import read_static_data

class InheritanceRate(GridLayout):
    def __init__(self, percentage: Percentage, **kwargs):
        super().__init__(cols=2, rows=20, **kwargs)
        self.horse_name_dict, self.blue_list, self.red_list, self.green_list, self.factor_list = read_static_data()
        self.percentage = percentage

    def build(self):
        print(self.percentage.rate)
        for key, value in self.percentage.rate.items():
            self.add_widget(LabelGen(text=f"{self.factor_list[int(key)]} {value * 100}%"))

        return self

    def update(self):
        self.clear_widgets()
        self.build()
