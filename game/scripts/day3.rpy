label day3:
    window hide
    show screen show_day(get_day())
    pause 2
    hide screen show_day
    window show

    call family_dinner_scene

    $ next_day()
    jump day4
    return
