#! python3

# models.py
# create all models here


# import os
import time
# import kivy
from kivy.core.audio import SoundLoader


class UserInputModel:
    def user_input(self,
                   starting_countdown,
                   number_of_sets,
                   seconds_per_sets,
                   seconds_of_rest,
                   sets_finished):
        self.starting_countdown = int(input('countdown: '))
        self.number_of_sets = int(input('number of sets: '))
        self.seconds_per_set = int(input('Seconds: '))
        self.seconds_of_rest = int(input('Rest: '))
        self.sets_finished = 0

    def countdown(self):
        for number in reversed(range(1, self.starting_countdown)):
            time.sleep(1)
            if number > 0:
                print(f'Timer will start in {number}')
            else:
                print('GO!')

    def interval_timer(self):
        for sets in range(self.number_of_sets):
            for number in range(self.seconds_per_set):
                # doing this to account for our 0 index
                time.sleep(1)
                print(f'exercise {number + 1}')
                print(self.sets_finished)

            self.sets_finished = self.sets_finished + 1

            if sets + 1 == self.number_of_sets:
                print('Done')
                break
            else:
                print('Rest')
                for number in range(self.seconds_of_rest):
                    time.sleep(1)
                    print(f'rest: {number + 1}')


class Settings(UserInputModel):
    def __init__(self, sound, elapsed_time, remaining_time):
        self.sound = SoundLoader.load('''audio.mp3''')
        if self.sound:
            sound.volume = 0.1
            sound.play()

        self.elapsed_time = self.seconds_per_set + self.seconds_of_rest * self.sets_finished
        self.remaining_time = (self.seconds_per_set + self.seconds_of_rest) * self.number_of_sets / elapsed_time
