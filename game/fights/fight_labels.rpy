label fightTutorialLabel:
    scene tomstancekick
    with dissolve

    show screen fightTutorialKeys

    tut "In every fight, you'll have positions from which you can attack and positions from which you'll need to defend."
    tut "In attacking positions you'll have a set of offensive actions, as shown on the left."
    tut "Since you're new to fighting, you only have 3 simple attacks:"

    show screen fightTutorialKeys(highlight='q')

    tut "{b}Q{/b}: a quick, left-handed jab to create distance and attack the opponent's face from the front."

    show screen fightTutorialKeys(highlight='w')

    tut "{b}W{/b}: a strong, right-handed hook to attack the opponent's head from the side."

    show screen fightTutorialKeys(highlight='r')

    tut "And {b}R{/b}: a right-footed kick to attack the opponent's legs."

    show screen fightTutorialKeys

    tut "As you learn more about fighting, you'll gain new attack moves."

    tut "When attacking, look at the opponent's stance and try to identify possible points of attack."

    show targets

    tut "With your three actions, there are three possible points of attack."

    show screen fightTutorialKeys(highlight='r')

    tut "Since Tom has his guard up and could probably block both a jab and a hook, try to kick him by pressing {b}R{/b} in the upcoming screen."

    hide screen fightTutorialKeys
    hide targets
    with dissolve

label fight:
    if fight_type == "simWin":
        $ mc.health = 1000

    $ players = allies + enemies

    $ attacker = getCurrentAttacker()
    $ defender = getCurrentDefender()

    jump healthCheck

label healthCheck:

    $ print("Attacker: MC {} : Defender: Lars {}".format(mc.health, lars.health))
    if defender.health <= 0:
        scene youfinishmovie
        pause 1

        play sound "sounds/fall.mp3"

        $ attacker.reset()

        scene youfinish
        with vpunch
        pause

        jump youfinish
    else:
        python:
            for player in allies + enemies:
                player.selectDefence()

        $ attacker = getCurrentAttacker()
        $ defender = getCurrentDefender()

        jump startAttack

label startAttack:
    if attacker in enemies:
        pass
        

    # if fight_type.startswith("sim"):
    #     $ attacker.attack(defender)
    #     jump healthCheck
    # else:
    #     call screen noramlAttack
