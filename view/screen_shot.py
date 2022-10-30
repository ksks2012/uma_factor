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
from view.horse_info import HorseInfoDetailLayout
import util.text as TEXT

SOURCE_FILE_NAME = "./var/fullscreen.png"

class ScreenShotApp(App):
    def __init__(self, take_screen_shot=0, **kwargs):
        super().__init__(**kwargs)
        self.take_screen_shot = take_screen_shot

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
            image.save(SOURCE_FILE_NAME)
        
        box = BoxLayout(spacing=10)

        analysis_bt = Button(text=TEXT.ANALYSIS_BT_TEXT, size_hint=(1, .15))
        analysis_bt.bind(on_press=self.press_analysis_bt)

        content_bt = Button(text=TEXT.CONTEXT_BT_TEXT, size_hint=(1, .15))
        # FIXME: when App is popup window
        # popup = Popup(title='Test popup', content_bt=box, size_hint=(None, None), size=(620, 1000), auto_dismiss=False)
        # content_bt.bind(on_press=popup.dismiss)        
        # popup.open()

        self.save_bt = Button(text=TEXT.SAVE_BT_TEXT, size_hint=(1, .15))
        self.save_bt.bind(on_press=self.press_save_bt)
        self.save_bt.disabled = True

        self.build_figure(box)
        self.horse_info_layout = HorseInfoDetailLayout()

        self.root = GridLayout(cols=2)
        self.root.add_widget(box)
        self.root.add_widget(self.horse_info_layout)
        self.root.add_widget(analysis_bt)
        self.root.add_widget(content_bt)
        self.root.add_widget(self.save_bt)

        return self.root

    def press_analysis_bt(self, arg):
        # TODO: charactor label 
        self.horse_fetcher = HorseFetcher(use_api=self.use_google_api)
        self.horse_fetcher.fetch_screen()
        Clock.schedule_once(partial(self.horse_info_layout.update_horse_info, self.horse_fetcher.horse_info))
        self.save_bt.disabled = False

    def press_save_bt(self, arg):
        self.horse_fetcher.save_horse_info_idx_in_db()

    def build_figure(self, box: GridLayout):
        try:
            # load the image
            img = Image(source=SOURCE_FILE_NAME)
            # add to the main field
            box.add_widget(img)
        except Exception as e:
            Logger.exception('Pictures: Unable to load <%s>' % SOURCE_FILE_NAME)


if __name__ == '__main__':
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./.credentials/google_cred.json"
    ScreenShotApp().run()