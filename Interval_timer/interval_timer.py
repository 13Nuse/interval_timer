import time
import winsound
# from threading import Timer
# Need a timer to show overall time
# need a timer for warmups and cooldowns
# remaining time and elapse time


class SoundChimes:
    def __init__(self):
        # audio
        self.high = winsound.Beep(3500, 500)


class Main:
    def __init__(self):
        self.sets_done: int = 0
        self.starting_countdown: int = int(input('Countdown: '))
        self.number_of_sets: int = int(input('number of sets: '))
        self.seconds_per_set: int = int(input('Seconds: '))
        self.seconds_of_rest: int = int(input('Rest: '))
        self.elapsed_time = self.sets_done * self.seconds_per_set + self.seconds_of_rest
        self.remaining_time = (self.seconds_per_set + self.seconds_of_rest) * self.number_of_sets / self.elapsed_time

    def start_countdown(self):
        # Simple starting countdown will need to test for other use case statements and value errors
        for number in reversed(range(0, self.starting_countdown)):
            time.sleep(1)
            if number > 0:
                print(f'Countdown: {number}', end='\r')
                SoundChimes()
            else:
                print('\nGO!')

    def work_rest(self):
        # Looping through the number of sets within the workout
        for sets in range(self.number_of_sets):
            print('\nEXERCISE')
            print(f'SETS: ', self.sets_done)
            SoundChimes()
            for number in range(self.seconds_per_set):
                # doing this to account for our 0 index
                time.sleep(1)
                print(f'{number + 1}', end='\r')

            self.sets_done += 1

            if sets + 1 == self.number_of_sets:
                print('\nDONE')
                SoundChimes()
                break
            else:
                print('\nREST')
                SoundChimes()
                for number in range(self.seconds_of_rest):
                    time.sleep(1)
                    print(f'{number + 1}', end='\r')


class Warmup:
    '''Warm up class'''


class Cooldown:
    '''Cooldown phase'''


if __name__ == '__main__':
    it = Main()
    it.start_countdown()
    it.work_rest()
