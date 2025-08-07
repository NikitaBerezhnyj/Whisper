label day2:
    window hide
    show screen show_day(get_day())
    pause 2
    hide screen show_day
    window show

    call friends_meeting_scene

    scene black
    $ next_day()
    jump day3
    return
