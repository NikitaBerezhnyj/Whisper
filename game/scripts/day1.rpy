label day1:
    window hide
    show screen show_day(get_day()) with fade
    pause 2
    hide screen show_day with fade
    window show

    call awakening_scene
    call street_scene
    call shop_scene

    scene black
    $ next_day()
    jump day2
    return
