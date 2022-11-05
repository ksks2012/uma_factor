from functools import partial
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

from view.screen_shot import ScreenShotApp
import util.text as TEXT


LabelBase.register(
 name='SiyuanHeiti',
 fn_regular='./font/msjh.ttc'
)


class UMA_factor(App):

    def on_start(self):
        self.screen_shot_view = ScreenShotApp(take_screen_shot=1)
        # self.screen_shot_view.build()
        return super().on_start()

    def on_stop(self):
        return super().on_stop()

    def build(self): 
        layout = GridLayout(cols=1)

        screen_shot_bt = Button(text=TEXT.BT_SCREEN_SHOT)
        screen_shot_bt.bind(on_press=self.press_screen_shot_bt)
        layout.add_widget(screen_shot_bt)

        show_horses_bt = Button(text=TEXT.BT_SHOW_HORSE)
        show_horses_bt.bind(on_press=self.press_show_horses_bt)
        layout.add_widget(show_horses_bt)

        auto_calculate_bt = Button(text=TEXT.BT_CALCULATE)
        auto_calculate_bt.bind(on_press=self.press_auto_calculate_bt)
        layout.add_widget(auto_calculate_bt)

        return layout

    def press_screen_shot_bt(self, *args, **kwargs):
        self.screen_shot_view.create_screen_shot_view()

    def press_show_horses_bt(self, arg):
        print("press_show_horses_bt")

    def press_auto_calculate_bt(self, arg):
        print("press_auto_calculate_bt")

if __name__ == '__main__':
    UMA_factor().run()