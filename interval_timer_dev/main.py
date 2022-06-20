#! python3

import time
from models import Settings
from models import UserInputModel
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty


class TimerPage(BoxLayout, UserInputModel):
    count = time.strftime('%M:%S:')
    total = 0
    elapsed_time = StringProperty(f'{time.strftime("%H:%M:%S:")}')
    count_enabled = BooleanProperty(False)
    my_visual_data = StringProperty(f'{time.strftime("%S:")}')
    user_input_str = StringProperty(f'{time.strftime("%M:%S")}')

    def on_start_click(self):
        print('button start clicked')
        if self.count_enabled is True:
            self.count += 1
            self.my_visual_data = str(self.count)

    def on_cancel_click(self):
        print('button cancel clicked')

    def start_counter(self):
        pass

    def on_text_validate(self, widget):
        self.user_input_str = widget.text


class IntervalApp(App):
    pass


if __name__ == '__main__':
    interval = IntervalApp()
    interval.run()
