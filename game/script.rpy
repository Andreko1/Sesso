# The script of the game goes in this file.

init:
    image bg origins = Image("images/bg_origins.jpg")
    image astolfo happy = Image("images/astolfo_happy.jpg")
    image astolfo horny = Image("images/astolfo_horny.jpg")
    image astolfo profile = Image("images/astolfo_profile.jpg")
    image beanstolfo = Image("images/beanstolfo.jpg")
    image zeb = Image("images/zeb_culoh.jpg")
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define AR = Character("Astolfo", color="#ff00ea")
define Z= Character("Zeb", color="#000000")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg origins at Zoom((800, 600), (0, 0, 800, 600), (225, 150, 400, 300), 1.0)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show astolfo profile

    # These display lines of dialogue.

    AR "Ciao!"

    show astolfo horny

    AR "E mi piacciono i cazzi"

    show astolfo happy

    AR "Ma non solo..."

    show beanstolfo 

    AR "Anche i fagioli"

    "doveva essere 'mi piace anche hitler' ma il compilatore ha deciso di fare il funny"

    show zeb

    Z "Culoh"

    # This ends the game.
    return
