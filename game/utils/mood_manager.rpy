default mood = 0

init python:
    def get_mood():
        return mood

    def set_mood(val):
        global mood
        mood = val

    def inc_mood(val=1):
        global mood
        mood += val

    def dec_mood(val=1):
        global mood
        mood -= val