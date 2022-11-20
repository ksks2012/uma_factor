from typing import List

from tkinter import Image
from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.gridlayout  import GridLayout
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

class ShowHorsesApp(App):
    def __init__(self, horse_info_list=[], **kwargs):
        self.sqlite_instance = SqliteInstance()
        self.sqlite_instance.connect(PATH.DB_PATH)
        self.horse_info_list = horse_info_list
        super().__init__(**kwargs)
        self.page_cache = {}
        self.take_screen_shot = 0
        self.use_google_api = 1
        self.page = 1
        self.is_popup = True

    def build(self):
        self.take_screen_shot = 0
        self.use_google_api = 1
        self.page = 1
        self.is_popup = False
        self._cache_horse_info()
        self.create_show_horse_view()

        return self.show_horses_layout

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
        # last page
        if len(self.page_cache[self.page]) < DEFINE.NUM_OF_HORSE_INFO_IN_PAGE:
            return
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

        self.update_horse_list(0)

        self.pre_page_bt = Button(text=TEXT.BT_ENTER_PRE_PAGE)
        self.next_page_bt = Button(text=TEXT.BT_ENTER_NEXT_PAGE)
        self.enter_filter_bt = Button(text=TEXT.BT_ENTER_FILTER)
        self.content_bt = Button(text=TEXT.BT_CONTEXT_TEXT)
        

        self._bind_button()

        button_layout = GridLayout(cols=4, rows=1)
        button_layout.add_widget(self.pre_page_bt)
        button_layout.add_widget(self.next_page_bt)
        button_layout.add_widget(self.enter_filter_bt)
        button_layout.add_widget(self.content_bt)

        self.show_horses_layout = GridLayout(cols=1)
        self.show_horses_layout.add_widget(filter_layout)
        self.show_horses_layout.add_widget(self.horse_list)
        self.show_horses_layout.add_widget(button_layout)

        # when App is popup window
        if self.is_popup is True:
            print("popup")
            popup = Popup(title=TEXT.TITLE_SHOW_HORSES, content=self.show_horses_layout, auto_dismiss=False)
            self.content_bt.bind(on_press=popup.dismiss)        
            popup.open()

if __name__ == '__main__':
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./.credentials/google_cred.json"
    ShowHorsesApp().run()