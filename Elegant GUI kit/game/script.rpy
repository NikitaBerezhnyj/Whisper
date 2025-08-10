# The script of the game goes in this file.

## CTC (click to continue) animation. Feel free to delete this
## if you don't like it. Or you can edit its position.
image ctc:
    align (0.82, 0.9)
    "gui/ctc.png"
    subpixel True
    easein 1.0 ypos 0.89
    pause 0.4
    easein 1.0 ypos 0.9
    pause 0.4
    repeat

default nvl = False ## Make sure to change this to TRUE if you're using NVL mode.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define m = Character('Martha', ctc="ctc", ctc_position="fixed", kind=adv)
define m_nvl = Character('Martha', ctc="ctc", ctc_position="fixed", kind=nvl)
define narrator = nvl_narrator
define n = Character(None, ctc="ctc", ctc_position="fixed", kind=adv)


transform centered:
    xalign 0.5
    ypos -100


# The game starts here.

label start:

    scene black

    $ quick_menu = False

    menu:
        n "Do you want to try NVL mode?"

        "Yes":
            $ quick_menu = True
            $ nvl = True
            jump nvl

        "No":
            $ quick_menu = True
            jump adv

    label adv:
        # Show a background. This uses a placeholder by default, but you can
        # add a file (named either "bg room.png" or "bg room.jpg") to the
        # images directory to show it.

        scene bg shrine

        # This shows a character sprite. A placeholder is used, but you can
        # replace it by adding a file named "eileen happy.png" to the images
        # directory.

        show martha n at centered

        # These display lines of dialogue.

        m "Greetings, I'm Martha."

        m "I wanted to thank you for downloading the 'Elegant GUI kit'."

        n "You can use it for personal, non-commercial projects."

        n "Which means your game must be free to play, just as this kit is free to download."

        n "All I ask is to put my name in the credits."

        m "The theme is simple enough to be used in most types of visual novels."

        m "But also has an elegant feel to it."

        menu:
            n "Don't you agree?"

            "Definitely!":

                show martha smile

                $ renpy.notify("Thank you!")

                m "I see you have good taste."

                m "If you appreciate my work, consider tipping me on Ko-fi."

                m "You don't have to, but it will help me create more content."
                

            "Not really":

                m "Fair enough."

                m "Perhaps you will find something else that suits your tastes in my account."

                m "And if not, I may create it in the future so feel free to give me a follow."


        m "You can take a look around and familiarize with the UI."

        m "Share your thoughts in the comments, as well as your game, if you used this GUI kit."

        show martha smile

        m "I'm a curious person, after all."

        m "I believe this is all, have fun creating your game!"

        return

    label nvl:
        # Show a background. This uses a placeholder by default, but you can
        # add a file (named either "bg room.png" or "bg room.jpg") to the
        # images directory to show it.

        scene bg shrine

        # This shows a character sprite. A placeholder is used, but you can
        # replace it by adding a file named "eileen happy.png" to the images
        # directory.

        show martha n at centered

        # These display lines of dialogue.

        m_nvl "Greetings, I'm Martha."

        m_nvl "I wanted to thank you for downloading the 'Elegant GUI kit'."

        narrator "You can use it for personal, non-commercial projects."

        narrator "Which means your game must be free to play, just as this kit is free to download."

        narrator "All I ask is to put my name in the credits."

        if renpy.variant("small"):
            nvl clear

        m_nvl "The theme is simple enough to be used in most types of visual novels."

        if not renpy.variant("small"):
            nvl clear

        m_nvl "But also has an elegant feel to it."

        menu (nvl=True):
            "Don't you agree?"

            "Definitely!":

                nvl clear

                show martha smile

                $ renpy.notify("Thank you!")

                m_nvl "I see you have good taste."

                m_nvl "If you appreciate my work, consider tipping me on Ko-fi."

                m_nvl "You don't have to, but it will help me create more content."
                

            "Not really":

                nvl clear

                m_nvl "Fair enough."

                m_nvl "Perhaps you will find something else that suits your tastes in my account."

                m_nvl "And if not, I may create it in the future so feel free to give me a follow."


        m_nvl "You can take a look around and familiarize with the UI."

        if renpy.variant("small"):
            nvl clear

        m_nvl "Share your thoughts in the comments, as well as your game, if you used this GUI kit."

        show martha smile

        if not renpy.variant("small"):
            nvl clear

        m_nvl "I'm a curious person, after all."

        m_nvl "I believe this is all, have fun creating your game!"
    # This ends the game.

    return
