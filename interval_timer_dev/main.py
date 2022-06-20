#! python3

import time
import models
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty


class TimerPage(BoxLayout):
    count = 0
    count_enabled = BooleanProperty(False)
    my_visual_data = StringProperty('0')
    user_input_str = StringProperty('00')

    def on_button_click(self):
        print('button clicked')
        if self.count_enabled is True:
            self.count += 1
            self.my_visual_data = str(self.count)


class IntervalApp(App):
    pass


if __name__ == '__main__':
    interval = IntervalApp()
    interval.run()
