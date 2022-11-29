from kivy.app import App 
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.gridlayout  import GridLayout
from functools import partial

from model.percentage import Percentage
from view.sub_view.inheritance_rate_layout import InheritanceRate
from view.pair_info_layout import PairInfoLayout
import util.text as TEXT

class CalculateView(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.pair_info_layout = PairInfoLayout()

        calculate_rate_bt = Button(text=TEXT.BT_CALCULATE_RATE, size_hint=(1, .15))
        calculate_rate_bt.bind(on_press=self.press_calculate_rate_bt)

        save_bt = Button(text=TEXT.BT_SAVE_RATE_TEXT, size_hint=(1, .15))
        save_bt.bind(on_press=self.press_save_bt)

        content_bt = Button(text=TEXT.BT_CONTEXT_TEXT, size_hint=(1, .15))

        self.inheritance_rate = InheritanceRate(Percentage())

        self.root = GridLayout(cols=2, rows=3)
        self.root.add_widget(self.pair_info_layout.build())
        self.root.add_widget(self.inheritance_rate.build())
        self.root.add_widget(content_bt)
        self.root.add_widget(calculate_rate_bt)
        self.root.add_widget(save_bt)
    
    def press_save_bt(self, arg):
        pass

    def press_calculate_rate_bt(self, arg):
        left_total_info = self.pair_info_layout.left_total_info
        right_total_info = self.pair_info_layout.right_total_info
        Clock.schedule_once(partial(self.inheritance_rate.update, Percentage(left_total_info, right_total_info)))

if __name__ == '__main__':
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./.credentials/google_cred.json"
    CalculateView().run()