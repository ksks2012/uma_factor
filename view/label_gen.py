from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Quad

class RGB():
    R = 0
    G = 0
    B = 0
    def __init__(self, color='black') -> None:
        if color == 'white':
            self.R = 1
            self.B = 1
            self.G = 1
        elif color == 'red':
            self.R = 1
        elif color == 'green':
            self.G = 1
        elif color == 'blue':
            self.B = 1


class LabelGen(Label):
    def __init__(self, text, backgroud_color, **kwargs):
        super(LabelGen, self).__init__(**kwargs)
        if text == "":
            return
        self.text=text
        color = RGB(backgroud_color)
        with self.canvas.before:
            Color(color.R, color.G, color.B,)
            self.rect = Rectangle(size=self.size,pos=self.pos)

        self.bind(size=self.adjust_size)
        self.bind(pos=self.adjust_pos)

    def adjust_pos(self, instance, new_pos):
        self.rect.pos = new_pos

    def adjust_size(self, instance, new_size):
        self.rect.size = new_size