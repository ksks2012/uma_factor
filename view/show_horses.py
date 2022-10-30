from typing import List

from tkinter import Image
from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.boxlayout  import BoxLayout
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.image import Image
from kivy.app import App
from kivy.clock import Clock

from functools import partial
import pyscreenshot as ImageGrab

from db_routine.sqlite import SqliteInstance
from input.fetch import HorseFetcher
from view.horse_info import HorseInfoDetailLayout
from view.horse_info_flat import HorseInfoFlatLayout
from util.data_processor import sql_data_to_horse_info
import util.text as TEXT
import util.path as PATH
import util.define as DEFINE
from view.filter_layout import HorseInfoFilterLayout

SOURCE_FILE_NAME = "./var/fullscreen.png"

ANALYSIS_BT_TEXT = 'Analysis'
CONTEXT_BT_TEXT = 'Close me!'
SAVE_BT_TEXT = 'Save'

class ShowHorsesApp(App):
    def __init__(self, horse_info_list=[], **kwargs):
        self.sqlite_instance = SqliteInstance()
        self.sqlite_instance.connect(PATH.DB_PATH)
        self.horse_info_list = horse_info_list
        super().__init__(**kwargs)
        self.page_cache = {}
        self.build()

    def build(self):
        self.take_screen_shot = 0
        self.use_google_api = 1
        self.page = 1
        self._cache_horse_info()
        return self.create_show_horse_view()

    def _cache_horse_info(self):
        if self.page_cache.get(self.page, None) is not None:
            self.horse_info_list = self.page_cache[self.page]
            return
        offset = (self.page - 1) * DEFINE.NUM_OF_HORSE_INFO_IN_PAGE
        self.horse_info_list = sql_data_to_horse_info(self.sqlite_instance.paging_horse_info_with_factor(DEFINE.NUM_OF_HORSE_INFO_IN_PAGE, offset))
        self.page_cache[self.page] = self.horse_info_list

    # callback function for update self horse list
    def update_horse_list(self, delta_time: float):
        self.horse_list.clear_widgets()
        for horse_info in self.horse_info_list:
            horse_info_flat_layout = HorseInfoFlatLayout(horse_info=horse_info)
            self.horse_list.add_widget(horse_info_flat_layout)

    def update_horse_info_flat_layout(self):
        self._cache_horse_info()
        Clock.schedule_once(partial(self.update_horse_list))

    def _press_pre_page_bt(self, arg):
        if self.page == 1:
            return

        self.page = self.page - 1
        self.update_horse_info_flat_layout()


    def _press_next_page_bt(self, arg):
        self.page = self.page + 1
        self.update_horse_info_flat_layout()

    def _press_enter_filter_bt(self, arg):
        # TODO: rebuild layout
        pass

    def _bind_button(self):
        self.pre_page_bt.bind(on_press=self._press_pre_page_bt)
        self.next_page_bt.bind(on_press=self._press_next_page_bt)
        self.enter_filter_bt.bind(on_press=self._press_pre_page_bt)

    def create_show_horse_view(self):
        filter_layout = HorseInfoFilterLayout()
        self.horse_list = GridLayout(cols=1, rows=10)

        for horse_info in self.horse_info_list:
            horse_info_flat_layout = HorseInfoFlatLayout(horse_info=horse_info)
            self.horse_list.add_widget(horse_info_flat_layout)

        self.pre_page_bt = Button(text=TEXT.ENTER_PRE_PAGE)
        self.next_page_bt = Button(text=TEXT.ENTER_NEXT_PAGE)
        self.enter_filter_bt = Button(text=TEXT.ENTER_FILTER_BT)

        self._bind_button()

        button_layout = GridLayout(cols=3, rows=1)
        button_layout.add_widget(self.pre_page_bt)
        button_layout.add_widget(self.next_page_bt)
        button_layout.add_widget(self.enter_filter_bt)

        self.root = GridLayout(cols=1)
        self.root.add_widget(filter_layout)
        self.root.add_widget(self.horse_list)
        self.root.add_widget(button_layout)
        return self.root


if __name__ == '__main__':
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./.credentials/google_cred.json"
    ShowHorsesApp().run()