import random
import sys
import time
import threading
import core

#clements - broken arm - dysentary - Bitten

distance = 0

health = [100,100,100,100,100]

pStatus = {
        "head": ["","","","",""],
        "torso": ["","","","",""],
        "right arm": ["","","","",""],
        "left arm": ["","","","",""],
        "right leg": ["","","","",""],
        "left leg": ["","","","",""],
        "health status": ["","","","",""],
        "infected": [False,False,False,False,False]
        }
cond = {            ## Possible health conditions ##
        "head": ["Healthy","One-eyed","Bleeding","Decapitated"],                                                            ## 0 - Possible head injuries
        "torso": ["Healthy","Bruised","Lacerated","Broken Ribs","Broken Back"],                  ## 1 - Possible torso injuries
        "arm": ["Healthy","Bruised","Lacerated","Broken","Amputated"],                           ## 2 - Possible arm injuries
        "leg": ["Healthy","Bruised","Lacerated","Broken","Amputated"],                           ## 3 - Possible leg injuries
        "status": ["Stable","Critical","Unconcious"],                                            ## 4 - Possible overall health conditions
        "disease": ["Healthy","fever","Cholera","Dysentery","Typhoid","Covid-19","Bone-exploditis","Infected"]      ## 5 - Possible diseases
        }

def hBar(names,health):
    charIndex = 0
    for n in names:
        bar = n + ":\t\t|"
        for i in range(0,100):
            if(health[charIndex] >= i):
                bar += "█"
            else:
                bar += "-"
        charIndex += 1
        bar += "|"
        print(bar)

def clemFace():
    core.clear()
    print("""                   .,'..   .
                  .;clll:,;:,'.
               ..,loodddddoddoc;'
               ':lodddkOOxdxdddo:..
               .,lddodk000OOOkkdc,..
               .:xxxdx000OOOOOOOx:.
            ...,lxkxdk000 ddxk kd,
     ...'''',,,;cdxddxO000kkOOxxd'
    .'.......',,:okxddk00000OOOOd.
   ......'.. .',;cxxddxkkk___kkxc.
  .'.......'. .,,;ldddddkO00Okl'.
  .... .......,,...;llolloddo;.
    .'......':l:......,:cc;,,,.
  ..',,,'..  .cl,.....,oKKo,,od'
..,,,,,'.     ,ol,. ..,:odc,,c:...
',,,,,,.      .loc.   .,,,,','.....     \n\n""")


clemFace()

core.SPrint(0.025,"""Well then, it looks like
I just saved your bacon.

I recon we stand a
better chance out there
if we stick together.

My name is Clements. I
used to be a priest. Not
much use for those
nowadays.

What's your name,
partner?\n\n""")

leader = input("Your Name : ")

clemFace()

core.SPrint(0.025,"""\nThe pleasure's all mine
""" + leader + """\n
Listen. Even with the two
of us, we won't survive
very long. Everyone I
trusted died a while
back.

Do you know anyone we
could count on in a
pinch?\n\n""")

pNames = [leader,input("Party Member 1 : "),input("Party Member 2 : "),input("Party Member 3 : "),input("Party Member 4 : ")]

clemFace()

core.SPrint(0.025,"""There's a good chance if
they're still alive they
will be at the shelter
setup in D.C. If they
have any sense that is.

We're going to need a way
to get around. I saw an
old station wagon a few
blocks back.

those things might not be
very reliable but you'd
be surprised how roomy
they are.

Anyway, lets get moving.""")

input("- Press Enter to continue -")

hBar(pNames,health)
