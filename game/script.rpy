# The script of the game goes in this file.

init:
    image bg origins:
        "images/bg_origins.jpg"
    image astolfo happy:
        "images/astolfo_happy.jpg"
        zoom 5.0
    image astolfo horny:
        "images/astolfo_horny.jpg"
        zoom 1.2
    image astolfo profile:
        "images/astolfo_profile.jpg"
        zoom 1.2
    image beanstolfo:
        "images/beanstolfo.jpg"
        zoom 2.5
    image astolfo angry:
        "images/astolfo_angry.jpg"
        zoom 7.0
    image astolfo shocked:
        "images/astolfo_shocked.jpg"
        zoom 5.0
    image astolfo nice:
        "images/astolfo_nice.jpg"
    image zeb:
        "images/zeb_culoh.jpg"
        zoom 1.2
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define AR = Character("Astolfo", color="#ff00ea")
define Z= Character("Zeb", color="#000000")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg origins

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show astolfo profile

    # These display lines of dialogue.

    AR "Ciao!"

    hide astolfo profile

    show astolfo horny

    AR "E mi piacciono i cazzi"

    hide astolfo horny

    show astolfo happy

    AR "Ma non solo..."

    hide astolfo happy

    show beanstolfo 

    AR "Anche i fagioli"

    hide beanstolfo

    "doveva essere 'mi piace anche hitler' ma il compilatore ha deciso di fare il funny"

    show zeb

    Z "Culoh"

    hide zeb

    show astolfo shocked #non funzia, adesso che ho modificato forse funzia

    AR "Oh no! è quello youtuber che ha perso rilevanza perchè è più testardo di un toro ma manipolato dalla sua fidanzata!"

    hide astolfo shocked

    show zeb

    Z "Ciao ragazzi ciao a tutti! Sono Zeb89 e oggi andremo a cacciare bambini nei territori di un certo 'Flavio Digo', non so chi sia questa feccia ma verrà schiacciato dalla grandezza dell'impero 89"

    hide zeb

    show astolfo angry 

    AR "Guarda che hai 69 spettatori di picco..."

    hide astolfo angry

    show beanstolfo

    menu: 

        AR "Comunque, ho bisogno di aiuto contro Zeb! Da solo non ce la farò mai, mi aiuterai?"

        "Ovvio":

            hide beanstolfo

            show zeb

            Z "Bastardi finocchi! Lo sapevo che eravate inferiori ma non pensavo a tal punto da andare 2vs1 contro di me! Il grande Zeb89!"

            Z "Vabeh, vuol dire che tornerò a fare i video di minecraft e di robaccia"

            hide zeb

            "Anche qui volevo mettere tipo 'adesso andrò a fottermi i piccioni' ma ancora una volta il compilatore ha creato una frase ancora più stupida e divertente"

            "E nel mentre che scrivo, sempre il compilatore, si insulta pure da solo!"

            "Comunque"

            "Torniamo al gioco"

            show astolfo nice

            AR "Grazie dell'aiuto, almeno così Flavio riuscirà a cacciare i bambini in tranquillità"

        "Ma Zeb89 ha il piccione, è carino :3":

            AR "vabeh, cercherò di non colpire il piccione"

            hide beanstolfo

            "La battaglia impervia e Astolfo per poco esce vincitore"

            show zeb

            Z "Maledetto, tornerò e mi vendicherò frociazzi!"

            hide zeb

            "ti avvicini a Astolfo per medicarlo"

            show astolfo angry

            AR "Grazie per le cure, anche se avrei preferito un aiuto in battaglia"

            "L'episodio finisce con il sium"



    # This ends the game.
    return
