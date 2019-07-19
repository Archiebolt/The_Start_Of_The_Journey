#  First you need to put text into a "text" variable
#  Then by turning this code on, it will ask what you searching for
#  if you, for example, type the letter "a" - it will close all a's into () in the text.


text = """
The Elder Scrolls V: Skyrim is an action role-playing game, playable from either a first or third-person perspective.
The player may freely roam over the land of Skyrim which is an open world environment consisting of wilderness expanses,
dungeons, cities, towns, fortresses, and villages. Players may navigate the game world more quickly by riding horses or
by utilizing a fast-travel system which allows them to warp to previously discovered locations. The game's main
quest can be completed or ignored at the player's preference after the first stage of the quest is finished. However,
some quests rely on the main storyline being at least partially completed. Non-player characters (NPCs) populate
the world and can be interacted with in a number of ways: the player may engage them in conversation, marry an eligible
NPC, kill them or engage in a nonlethal "brawl". As in previous The Elder Scrolls games, killing certain NPCs can make
some quests or items unobtainable. Some NPCs cannot be killed due to their importance in later story-lines. If witnessed,
crimes like murder and theft accrue the player a bounty which is tracked independently in each of Skyrim's nine holds.
"""  # You can paste pretty much any text you want / Right now this is just some random text of the elder scrolls game
print(text)  # Just shows the text to user
final_text_words = ''
final_text_characters = ''
final = ''

command = input("What are you searching for?: ")  # Gives user chance to type symbol he wants to search in the text

for storage in text.split():
    if storage == command.upper() or storage == command.lower() or storage == command:
        final_text_words += f'({storage}) '
    else:
        final_text_words += storage + " "

final_text_list = list(final_text_words)  # imports text into list of symbols

for storage_characters in final_text_list:
     if storage_characters == command.upper() or storage_characters == command.lower() or storage_characters == command:
         final += f'({storage_characters})'
     else:
         final += storage_characters

final.replace("  ", " ")

print(final)