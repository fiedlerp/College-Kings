# SCENE 24: Mc goes to bed
# Locations: Hotel Room
# Characters: MC (Outfit: 11)
# Time: Night
# Phone Images: None

label v12_simplr_convo:
    scene v12sic1 # TPP. Show MC waking up in the middle of the night slightly confused, mouth closed, looking at the ceiling
    with dissolve

    pause 0.75

    play music "music/v12/Scene 24/Track Scene 24.mp3" fadein 2

    if v12_msrose_sex:
        scene v12sic1a # TPP. Same as v12sic1, MC awake, looking at the ceiling, slight smile, mouth closed
        with dissolve

        u "(Oh shit, how the fuck did I get back here? Damn, that was crazy!)"

        scene v12sic1b # TPP. Same as v12sic1a, MC in a different pose
        with dissolve

        u "(I need to sleep this off, but I'm kind of wide awake right now. I'll just check out my phone.)"

    else:
        scene v12sic1c # TPP. Same as v12sic1, MC awake, looking at the ceiling, neutral expression, mouth closed
        with dissolve

        u "(Randomly waking up in the middle of the night, with nothing to do except stare at the wall, yayyy.)"

        scene v12sic1d # TPP. Same as v12sic1c, MC different pose
        with dissolve

        u "(Guess I can check out my phone.)"

    scene v12sic1e # TPP. Same as v12sic1, MC on his phone, looking at it, neutral expression, mouth closed
    with dissolve

    u "(Haven't checked out Simplr in a while.)"

    if simplr_Emmy in simplr_contacts:

        $ v12s24_emmymatch = True

        $ simplr_Emmy.newMessage("Hey handsome, I was hoping I'd match with you. Where are you from?", queue=False)
        $ simplr_Emmy.addReply("I'm actually in Paris right now, but I'm from California. Wbu?")
        $ simplr_Emmy.newMessage("Wow, my distance settings are way off. I'm from Amsterdam.")
        $ simplr_Emmy.addReply("Haha, call it a coincidence, but I'm actually headed to Amsterdam here soon.")
        $ simplr_Emmy.newMessage("Wowww, guess I got a headstart on all the other Amsterdam chicks huh?")
        $ simplr_Emmy.addReply("Ha, I'm thinking I'm the lucky one.")
        $ simplr_Emmy.newMessage("There's actually a Simplr event they do regularly here, you should stop by when you come and maybe we'll run into each other.")
        $ simplr_Emmy.addReply("I'll definitely look into that.")
        $ simplr_Emmy.newMessage("Good, I know it's late so goodnight handsome ;)")
        $ simplr_Emmy.addReply("Goodnight ;)")

        call screen phone

        scene v12sic1a
        with dissolve

        u "(Very interesting... *Chuckles* Now, I need to sleep.)"
    
    else:
        scene v12sic1c
        with dissolve

        u "(Well, no matches, I'm just gonna take my sorry ass to sleep.)"

    scene v12sic1f # TPP. Show MC sleeping again
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v12_julia_call #scene 25