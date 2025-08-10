label day4:
    window hide
    show screen show_day(get_day())
    pause 2
    hide screen show_day
    window show

    call ending_scene

    if get_mood() >= 7:
        call merge_ending_scene
    else:
        call rejection_ending_scene

    return
