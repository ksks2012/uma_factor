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

from input.fetch import HorseFetcher
from view.horse_info import HorseInfoLayout
from view.horse_info_flat import HorseInfoFlatLayout

SOURCE_FILE_NAME = "./var/fullscreen.png"

ANALYSIS_BT_TEXT = 'Analysis'
CONTEXT_BT_TEXT = 'Close me!'
SAVE_BT_TEXT = 'Save'

class ShowHorsesApp(App):
    def __init__(self, horse_info_list=[], **kwargs):
        self.horse_info_list = horse_info_list
        super().__init__(**kwargs)
        self.build()

    def build(self):
        self.take_screen_shot = 0
        self.use_google_api = 1
        return self.create_show_horse_view()

    def create_show_horse_view(self):
        filter_layout = GridLayout(cols=1, rows=10)
        horse_list = GridLayout(cols=1, rows=10)

        for horse_info in self.horse_info_list:
            horse_info_flat_layout = HorseInfoFlatLayout(horse_info=horse_info)
            horse_list.add_widget(horse_info_flat_layout)

        self.root = GridLayout(cols=1)
        self.root.add_widget(filter_layout)
        self.root.add_widget(horse_list)
        return self.root


if __name__ == '__main__':
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./.credentials/google_cred.json"
    ShowHorsesApp().run()