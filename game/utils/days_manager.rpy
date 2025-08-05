default current_day = 1

init python:
    def next_day():
        global current_day
        current_day += 1

    def get_day():
        return current_day