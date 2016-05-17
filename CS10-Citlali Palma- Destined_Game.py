# -*- coding: utf-8 -*-
# DESTINED


#import pickle;fore player to save game progress
#-----------------------------------------------------------------------
#at the end where everything is defined, def,put:
#def save():
    #global player_name,node, something, something, something
    #with open('savegame.dat', 'wb') as f:
        #pickle.dump([player_name, something, something, something],f, protocol=2)
        #These are your variablesthat you want to save, inside the list above
    #print "Game successfully saved"
#----------------------------------------------------------------------------
#load function
#def load():
    #global name, player_name,node, something, somehting
    #with open('savegame.dat','wb') as f:
        #name, player, =pickle.load(f)
    #print "Game was successfully loaded"
#-----------------------------------------------------------------------
#ends game
    #if command in quit:
        #break
#-----------------------------------------------------------------------
#save/load game
    #elif command in ["save"]:
        #save()
    #elif command is ["load"]
        #load()
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
    
#hello
print """
Hello there! 
~Press enter to continue 
"""
raw_input()

#Welcome
print"""
-------------------------------------------------
Welcome to DESTINED *Created by Citlali Palma:)*
-------------------------------------------------

~Press enter to continue
"""
raw_input()

#player objective
print"""
The objective of this game is for the player to pass all 30 levels using 
their memory, knowledge of culture, creativity, and thinking skills.

~Press enter to continue
"""
raw_input()

#introduce who they are
print "Greetings. You are a little baby in a world of nothing"

print "You literally have nothing. You have nothing to call yours."

print "~Press enter to continue"
raw_input()
#Gives player hope
print """But wait!! Don\'t lose hope yet..."""
print """There is a way you can survive in this world of nothing and become 
something you would never imagine."""
print "~Press enter to continue"
raw_input()
print "First, I must ask one question"

#ASKS FOR PLAYER NAME
#Player must put it in quotations
player_name = input("What is your name? Please put in 'quotes' >")

print "Hello, " +player_name+ "."

#Introduce Lali the fairy
print"Allow me to introduce myself. ~Press enter to continue"
raw_input()
#Lali purpose
print """My name is Lali. I am your assigned fairy. Almost like a fairygod mother, 
but much cooler"""
print "~Press enter to continue"
raw_input()
print """My job is to help little helpless babies like you become something in the world.
~Press enter to continue
"""
raw_input()

#Tells player about supernatural power
print"""
By the end of this journey, you will have a miraculous supernatural power of some sort. 
For good, or for evil. That\'s up to you. ~Press enter to continue
"""
raw_input()

#RULES
print"Would you like to see the rules?"

rules = """Here are the rules:)
RULES: 
1.Answer the Lali 
2.Protect Lali from monsters
3.Correctly solve riddles.
4.There are 30 questions 
6.You have only 3 tries per question 
7.If you got 15 questions wrong, the game will end and you lose
8.The more questions you get right, the closer you'\ll be to getting 
supernatural powers
9.Be mature
10.HAVE FUN!
    """
#Background
#needs to be edited    
background = """Well here's a quick background. Hope you like reading. The small 
organism is called a Lali and will help the baby expand the box so that the player 
can move, and give them a world with resources.That’s only if they answer the Lali 
correctly and solve riddles. They can have whatever they want in their world only
if they solve the riddles and obey the Lali. The Lali will give the baby 30 different 
tasks/questions and 3 tries for each one. The player has a limit of 15 questions to 
get wrong. If they reach their 15 question wrong, the Lali will not help the baby 
anymore and the game is over. The more questions the player gets wrong, the smaller
their world will get and the number of items they have decrease. The more they do 
right/good your world will be better with space and resources. The further the 
playergets in the game, the harder the questions and riddles. There will be times 
where the baby will have to fight monsters to protect the Lali. Which means they 
will have to use weapon. The Lali is the baby’s only chance to expanding their 
world. If theLali dies, the game is over. If the player gets 15 questions wrong, 
the game is over. Once the player reaches the final question and answers it correctly, 
theLali will let the player choose a supernatural power and what they're gonna do 
with it, and they are free from the box and are free in the world. Whatever 
supernatural power the player chooses will determine their future which will 
already be explained for them in a description. The Lali will leave and wish 
the player good luck in the world and in the story it’ll say that they’re are 
off to a new baby.That is the end of the game.
"""
#asks if player wants to see rules
something = raw_input("Enter (y)es or (n)o: ") 
if something == "yes" or something == "y": 
    print rules 
#player says no #recieves background info
elif something == "no" or something == "n": 
    print "Okay "+player_name+ "."
    print
    raw_input()
if something == "no" or something == "n":
    print "Would you like to read the background of DESTINED? "
    print raw_input("yes or no?")
if something == "yes" or something == "y":
    print background
elif something == "no" or something == "n":
    print "Alrighty then "+player_name


print "~Press enter to continue"
raw_input()

#continues game
print "Now, it\'s time to figure out which supernatural power is destined to be yours!"
print "Press enter to continue"
raw_input()

#Player ready to play
print "Are you ready to begin?"
something_else = raw_input("Enter (y)es or (n)o: ") 
if something_else == "yes" or something_else == "y": 
    print "Sweet! Let\'s begin" 
elif something_else == "no" or something_else == "n": 
    print "Ummmm well okay then" 

print"Press enter to continue"
raw_input()

#QUESTION TEMPLATE
#print "question"
#"~Press enter to continue"
#raw_input()
#print "The question?"
#answer = raw_input(">") 
#if answer == "answer" or answer == "other answer": 
#    print "CORRECT" 
#elif something_else == "" or something_else == "": 
#    print "Ehh!!! Wrong" 
#raw_input()

#starts questions
#Question 1
print "Okay here is the first question"
"~Press enter to continue"
raw_input()
print "    1. Who lives in a pineapple under the sea?"
answer = raw_input(">") 
if answer == "spongebob" or answer == "spongebob squarepants": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()

#player tries again
#3 tries per question


#Make thing for when person gets it wrong
#Make a true or false statement for when the person gets it right, they can
#be asked if they want to add an item to their "items"


#dialogue saying : Congrats your first question is complete. You have moved closer
#towards your destined supernatural power. It shall be granted to you once you have completed
#/answered all of the questions i will ask you. Since you got the first question right, I will
#give you anything you desire to have with you as we go along your questions. What would you like?
# raw_input() "I want to have a "chicken/hug/sword/blanket"

#COMPLETED LEVEL 1 DIALOGUE
print "Congrats, " +player_name+ ".You have completed the first question of your journey!"
print 
raw_input()
print "You can have any item you want because you are a SMART BABY!"
#player adds items to items list after correctly answering a question right
#needs a way to subtract items 
#needs a way to add to current list
#needs a way to record how many items the player has
print "What item or thing in the world do you wish to have?"
player_items = raw_input(">")
print
print [player_items]
print "You have added, "+player_items+", to your items"

print "Would you like to see what items you have?"
see_items = raw_input("Enter (y)es or (n)o: ") 
if see_items == "yes" or see_items == "y": 
    print [player_items] 
elif see_items == "no" or see_items == "n": 
    print "okay"

print "Would you like to add to your list?"
add_items = raw_input("Enter (y)es or (n)o: ")
if add_items == "yes" or add_items == "y":
    player_added = input("What would you like to add? Please put in 'quotes' >")
    print player_added
    print "You added, [" +player_added+ "]."
elif add_items == "no" or add_items == "n":
    print "Alrighty then"
print "~Press enter to continue"
raw_input()


#Question 2
print "Question 2"
"~Press enter to continue"
raw_input()
print "    2. What is the biggest state in state in the U.S.?"
answer = raw_input(">") 
if answer == "texas" or answer == "Texas": 
    print "Howdy partner! You are CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input() 

#All questions need a thing for the player to retry the question
#All questions need to show how many tries are left
#All questions need something that prints something when they get it wrong

#Question 3
print "Question 3"
raw_input()
print "    3. Can you name an animal with stripes?"
answer = raw_input(">") 
if answer == 'tiger' or answer == 'zebra': 
    print "CORRECT!" 
elif something_else == "" or something_else == "": 
    print "Ummm...they have stripes?!" 
raw_input()

#Question 4
print "Question 4"
"~Press enter to continue"
raw_input()
print "    4. What color is shrek?"
answer = raw_input(">") 
if answer == "green" or answer == "shrek color": 
    print "CORRECT! Shrek is life" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong color" 
raw_input()

#Question 5
print "Question 5"
"~Press enter to continue"
raw_input()
print "    5. How many continents are on Earth?"
answer = raw_input(">") 
if answer == "seven" or answer == "7": 
    print "That\'s CORRECT! Antartica, North America, South America, Austrailia, Asia, Africa, and Europe!" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong number"
raw_input() 

#Question 6
print "Question 6"
"~Press enter to continue"
raw_input()
print "    6. Who sings the song Thriller?"
answer = raw_input(">") 
if answer == "michael jackson" or answer == "Michael Jackson": 
    print "CORRECT!!" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()

#Question 7
print "Question 7"
"~Press enter to continue"
raw_input()
print "    7. What word rhymes with orange?"
answer = raw_input(">") 
if answer == "nothing" or answer == "orange": 
    print "Don\'t take that question seriously. I just really want orange juice sorry" 
elif something_else == "" or something_else == "": 
    print "Does it?" 
raw_input()

#Question 8
print "Question 8"
"~Press enter to continue"
raw_input()
print "    8. What is 'hello', in spanish?"
answer = raw_input(">") 
if answer == "hola" or answer == "Hola": 
    print "Si! Tu es CORRECTO! Muy bien! " 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()

#Question 9
print "Question 9"
"~Press enter to continue"
raw_input()
print "    9. Is an avacado a fruit, or a vegetable?"
answer = raw_input(">") 
if answer == "fruit" or answer == "Fruit": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Nope"
raw_input() 
    
#Question 10
print "Question 10"
"~Press enter to continue"
raw_input()
print "    10. What is the name of the little girl from Monsters Inc.?"
answer = raw_input(">") 
if answer == "boo" or answer == "Boo": 
    print "CORRECT! '2319!'" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong. That/'s not the right name." 
raw_input()
    
#Question 11
print "Question 11"
"~Press enter to continue"
raw_input()
print """    11. If a man bought six carrots for his rabbit, and his rabbit ate four 
of them and ran away, how many carrots does the man have left?"""
answer = raw_input(">") 
if answer == "2" or answer == "two": 
    print "CORRECT! Carrots are yummy" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 12
print "Question 12"
"~Press enter to continue"
raw_input()
print "    12. Can you finsh the lyrics?"
raw_input()
print "Do you ever feel, like a plastic ___, ________ _______ ___ ____, wanting to start again?"
answer = raw_input(">") 
if answer == "bag, drifting through the wind" or answer == "bag, drifting through the wind": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Sorry that\'s not how the song goes" 
raw_input()
    
#Question 13
print "Question 13"
"~Press enter to continue"
raw_input()
print "    13. What sound does a cow make?"
answer = raw_input(">") 
if answer == "moo" or answer == "MOO": 
    print "CORRECT! You are moosome" 
elif something_else == "" or something_else == "": 
    print "A cow makes that noise? I belive you\'re wrong" 
raw_input()
    
#Question 14
print "Question 14"
"~Press enter to continue"
raw_input()
print "    14. What fast food chain has a clown?"
answer = raw_input(">") 
if answer == "McDonalds" or answer == "mcdonalds": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()

#FIX SO THAT YOU CAN GET IF IT'S CORRECT OR NOT    
#Question 15
print "Question 15"
"~Press enter to continue"
raw_input()
print "    15. What are the three R\'s of recycling?"
answer = raw_input(">") 
if answer == ["reduce", "reuse", "recycle"] or answer == ["Reduce","Reuse", "Recycle"]: 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input() 
    
#Question 16
print "Question 16"
"~Press enter to continue"
raw_input()
print "    16. What is the biggest country in the world?"
answer = raw_input(">") 
if answer == "russia" or answer == "Russia": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input() 
    
#Question 17
print "Question 17"
"~Press enter to continue"
raw_input()
print "    17. What animal is Arthur?"
answer = raw_input(">") 
if answer == "ardvark" or answer == "Ardvark": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
    
#Question 18
print "Question 18"
"~Press enter to continue"
raw_input()
print "    18. What country was Miss Universe 2016 from?"
answer = raw_input(">") 
if answer == "philipines" or answer == "Philipines": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
    
#Question 19
print "Question 19"
"~Press enter to continue"
raw_input()
print "    19. What animal does wool come from?"
answer = raw_input(">") 
if answer == "sheep" or answer == "Sheep": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 20
print "Question 20"
"~Press enter to continue"
raw_input()
print "    20. Who was the first black president of the United States?"
answer = raw_input(">") 
if answer == "obama" or answer == "barack obama": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 21
print "Question 21"
"~Press enter to continue"
raw_input()
print "    What is the name of Phineas\'s and Candace\'s brother?"
answer = raw_input(">") 
if answer == "ferb" or answer == "Ferb": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 22
print "Question 22"
"~Press enter to continue"
raw_input()
print "    What two colors make the color purple?"
answer = raw_input(">") 
if answer == "blue and red" or answer == "Blue and Red": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 23
print "Question 23"
"~Press enter to continue"
raw_input()
print "Which celebrity gained fame through YouTube and sings the song, 'Baby'?  "
answer = raw_input(">") 
if answer == "justin bieber" or answer == "Justin Bieber ": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong person!" 
raw_input()

#Question 24
print "Question 24"
"~Press enter to continue"
raw_input()
print "What is the name of the dad from Family Guy?"
answer = raw_input(">") 
if answer == "Peter" or answer == "peter griffin": 
    print "CORRECT! Heeheheehe shut up Meg" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 25
print "Question 25"
"~Press enter to continue"
raw_input()
print "Prince Charming is to Cinderella, as in Fiona is to _ _ _ _ _"
answer = raw_input(">") 
if answer == "shrek" or answer == "Shrek": 
    print "CORRECT! It\'s never orgor!" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 26
print "Question 26"
"~Press enter to continue"
raw_input()
print "What shape has four equal sides?"
answer = raw_input(">") 
if answer == "Square" or answer == "square": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 27
print "Question 27"
"~Press enter to continue"
raw_input()
print "What country is Paris in?"
answer = raw_input(">") 
if answer == "France" or answer == "france": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 28
print "Question 28"
"~Press enter to continue"
raw_input()
print "What is H2O?"
answer = raw_input(">") 
if answer == "Water" or answer == "water": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 29
print "Question 29"
"~Press enter to continue"
raw_input()
print "Who is the author of 'Green Eggs And Ham'?"
answer = raw_input(">") 
if answer == "Dr. Suess" or answer == "dr.suess": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong" 
raw_input()
    
#Question 30
print "Question 30"
"~Press enter to continue"
raw_input()
print "If you had five pillows, and gave 3 pillows away, then bought 2 more, how many pillows would you have?"
answer = raw_input(">") 
if answer == "4" or answer == "four": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()     

#Question 31
print "Question 31"
"~Press enter to continue"
raw_input()
print "What animal is the mascot of Geico?"
answer = raw_input(">") 
if answer == "Lizard" or answer == "lizard": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()  

#Question 32
print "Question 32"
"~Press enter to continue"
raw_input()
print "How many stars are on the American flag?"
answer = raw_input(">") 
if answer == "50" or answer == "fifty": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()  

#Question 33
print "Question 33"
"~Press enter to continue"
raw_input()
print "What country did Hitler rule?"
answer = raw_input(">") 
if answer == "Germany" or answer == "germany": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()  

#Question 34
print "Question 34"
"~Press enter to continue"
raw_input()
print "What is 14 x 9"
answer = raw_input(">") 
if answer == "126" or answer == "one hundred and twenty six": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()  

#Question 35
print "Question 35"
"~Press enter to continue"
raw_input()
print "Who said this line, 'Mama said life was like a box of chocolates. You never know what your gonna get.'?"
answer = raw_input(">") 
if answer == "Forrest Gump" or answer == "forrest gump": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()  

#Question 36
print "Question 36"
"~Press enter to continue"
raw_input()
print "Head, shoulders, knees, and....?"
answer = raw_input(">") 
if answer == "toes" or answer == "Toes": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()  

#Question 37
print "Question 37"
"~Press enter to continue"
raw_input()
print "Name a bird that can'\t fly?"
answer = raw_input(">") 
if answer ==  ["penguin", "ostrich", "kiwi", "emu", "cassowary", "rhea"]: 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()  

#Question 38
print "Question 38"
"~Press enter to continue"
raw_input()
print "How many inches are in a foot?"
answer = raw_input(">") 
if answer == "12" or answer == "twelve": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()  

#Question 39
print "Question 39"
"~Press enter to continue"
raw_input()
print "What weighs more? A horse or a bull?"
answer = raw_input(">") 
if answer == "bull" or answer == "Bull": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()  

#Question 40
print "Question 40"
"~Press enter to continue"
raw_input()
print "What comics does the Green Latern belong to??"
answer = raw_input(">") 
if answer == "DC" or answer == "dc": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()  

#Question 41
print "Question 41"
"~Press enter to continue"
raw_input()
print "Name a founder of Google"
answer = raw_input(">") 
if answer == ["Larry Page", "Sergey Brin"]: 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()

#Question 42
print "Okay here is the first question"
"~Press enter to continue"
raw_input()
print "Who lives in a pineapple under the sea?"
answer = raw_input(">") 
if answer == "spongebob" or answer == "spongebob squarepants": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()

#Question 43
print "Okay here is the first question"
"~Press enter to continue"
raw_input()
print "Who lives in a pineapple under the sea?"
answer = raw_input(">") 
if answer == "spongebob" or answer == "spongebob squarepants": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()

#Question 44
print "Okay here is the first question"
"~Press enter to continue"
raw_input()
print "Who lives in a pineapple under the sea?"
answer = raw_input(">") 
if answer == "spongebob" or answer == "spongebob squarepants": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()

#Question 45
print "Okay here is the first question"
"~Press enter to continue"
raw_input()
print "Who lives in a pineapple under the sea?"
answer = raw_input(">") 
if answer == "spongebob" or answer == "spongebob squarepants": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()

#Question 46
print "Okay here is the first question"
"~Press enter to continue"
raw_input()
print "Who lives in a pineapple under the sea?"
answer = raw_input(">") 
if answer == "spongebob" or answer == "spongebob squarepants": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()

#Question 47
print "Okay here is the first question"
"~Press enter to continue"
raw_input()
print "Who lives in a pineapple under the sea?"
answer = raw_input(">") 
if answer == "spongebob" or answer == "spongebob squarepants": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()

#Question 48
print "Okay here is the first question"
"~Press enter to continue"
raw_input()
print "Who lives in a pineapple under the sea?"
answer = raw_input(">") 
if answer == "spongebob" or answer == "spongebob squarepants": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()

#Question 49
print "Okay here is the first question"
"~Press enter to continue"
raw_input()
print "Who lives in a pineapple under the sea?"
answer = raw_input(">") 
if answer == "spongebob" or answer == "spongebob squarepants": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()

#Question 50
print "Okay here is the first question"
"~Press enter to continue"
raw_input()
print "Who lives in a pineapple under the sea?"
answer = raw_input(">") 
if answer == "spongebob" or answer == "spongebob squarepants": 
    print "CORRECT" 
elif something_else == "" or something_else == "": 
    print "Ehh!!! Wrong"
raw_input()

#needs more questions
#needs fighting
#needs points
#needs way for player to go when wrong
#needs to count right/wrong
#


#SUPERNATURAL POWERS FOR PLAYER
#RANDOMLY GIVEN TO PLAYER
import random
superpower = ('Breath Underwater', 'Fire Breathing', 'Duplication', 'Invisibility',
'Sonic Scream','Superhuman Strength', 'Night Vision', 'X-Ray Vision', 'Wallcrawling',
'Telepathy', 'Gravity Manipulation', 'Imortality', 'Time Manipulation', 'Superhuman Speed',
'Time Travel', 'Teleportation','Animal Morphing', 'Elasticity', 'Size Shifting',
'Flying', 'Echolocation', 'Matter ingestion', 'Vortex breath' , 'Air Manipulation',)

#When the player reaches the end
#CONGRATS
print "Congratualtions " +player_name+ "!" " You have completed the last level of DESTINED."
print "Now you will be granted with a supernatural power."
print "Fate will decide what that power will be."
raw_input()

#player recieves Supernatural power
print "Ready " +player_name+ "?"
useransw = raw_input("Enter (y)es or (n)o: ") 
if useransw == "yes" or useransw == "y": 
    print "Okay here it is!!"
    print("Your super natural power is " + str(random.choice(superpower)) + " when you grow up!")
    print "Yay" 
elif useransw == "no" or useransw == "n": 
    print "Are u sure you don\'t want to find out your supernatural power " +player_name+ "?"
userresp = raw_input("Enter (y)es or (n)o: ") 
if userresp == "yes" or userresp == "y":
    print "Okay...ummm.." "Peace out "+player_name+ "!!!" "Hope you had fun playing DESTINED:)"
if userresp == "no" or userresp == "n":
    print "That\'s what I thought"
    raw_input()
    print ("Your super natural power is " + str(random.choice(superpower)) + " when you grow up!")
#Explain what their supernatural does and how they can use it
#Have an option for the user to be asked what they will use thier power for

#END AND THANKS
print """
Thank you for playing DESTINED! This is incomplete becuase this is all I could get to work.
Better will be coming soon! Goodbye :)
"""


#Have level 10, 20, 25, 30, 40, and level 49 be levels where they must protect/defend the Lali
#Have the health of the Lali available so they can see if im alive and not dying
#
