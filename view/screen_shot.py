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

from input.fetch import HorseFetcher
from view.horse_info import HorseInfoDetailLayout
import util.text as TEXT
import util.path as PATH

class ScreenShotApp(App):
    def __init__(self, take_screen_shot=0, **kwargs):
        super().__init__(**kwargs)
        self.take_screen_shot = take_screen_shot
        self.use_google_api = 1
        self.img = None

    def build(self):
        self.take_screen_shot = 1
        self.use_google_api = 1
        return self.create_screen_shot_view()

    def create_screen_shot_view(self):
        print("press_screen_shot_bt")

        if self.take_screen_shot == 1:
            # screen shot
            image = ImageGrab.grab(bbox=(1350, 100, 1920, 800))

            # save image
            image.save(PATH.SOURCE_FILE_NAME)

            # reload image
            self.img = Image(source=PATH.SOURCE_FILE_NAME)
            self.img.reload()

        analysis_bt = Button(text=TEXT.BT_ANALYSIS_TEXT, size_hint=(1, .15))
        analysis_bt.bind(on_press=self.press_analysis_bt)

        content_bt = Button(text=TEXT.BT_CONTEXT_TEXT, size_hint=(1, .15))

        self.save_bt = Button(text=TEXT.BT_SAVE_TEXT, size_hint=(1, .15))
        self.save_bt.bind(on_press=self.press_save_bt)
        self.save_bt.disabled = True

        self.horse_info_layout = HorseInfoDetailLayout()

        self.screen_shot_layout = GridLayout(cols=2)
        self.screen_shot_layout.add_widget(self.img)
        self.screen_shot_layout.add_widget(self.horse_info_layout)
        self.screen_shot_layout.add_widget(analysis_bt)
        self.screen_shot_layout.add_widget(content_bt)
        self.screen_shot_layout.add_widget(self.save_bt)

        # when App is popup window
        popup = Popup(title=TEXT.TITLE_SCREENSHOT, content=self.screen_shot_layout, auto_dismiss=False)
        content_bt.bind(on_press=popup.dismiss)        
        popup.open()

        return self.screen_shot_layout

    def press_analysis_bt(self, arg):
        # TODO: charactor label 
        self.horse_fetcher = HorseFetcher(use_api=self.use_google_api)
        self.horse_fetcher.fetch_screen()
        Clock.schedule_once(partial(self.horse_info_layout.update_horse_info, self.horse_fetcher.horse_info))
        self.save_bt.disabled = False

    def press_save_bt(self, arg):
        self.horse_fetcher.save_horse_info_idx_in_db()

if __name__ == '__main__':
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./.credentials/google_cred.json"
    ScreenShotApp().run()