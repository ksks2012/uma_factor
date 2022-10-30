from view.filter_layout import HorseInfoFilterApp, FieldLayout
from kivy.base import runTouchApp

from util.common import read_static_data
import os
from typing import List, Mapping

import kivy
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from util.common import read_static_data

kivy.resources.resource_add_path(os.path.abspath('./font/msjh.ttc'))
LabelBase.register('zh_font', './font/msjh.ttc')


def testing_filter_layout():
    HorseInfoFilterApp().run()

def testing_field_layout():
    runTouchApp(FieldLayout())

def test_input_with_spinner():
    pass

if __name__ == '__main__':
    horse_name_dict, blue_list, red_list, green_list, factor_list = read_static_data()

    # testing_filter_layout()
    testing_field_layout()
    