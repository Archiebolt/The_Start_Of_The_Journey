text = """
Für einen Blog benötigen Sie eine Plattform, die bestimmte Voraussetzungen erfüllt. Einige Anbieter verfügen über entsprechend eingerichtete Server
und stellen diese zur Verfügung. Hier bekommen Sie eine eigene Internetadresse für Ihren Blog zugeteilt. Über den Administrationsbereich richten Sie
ihn Ihren Vorstellungen entsprechend ein und füllen ihn mit Inhalten. In verschiedenen Details unterscheiden sich die Anbieter jedoch.
Diese gilt es zunächst zu vergleichen, um von Anfang an die richtige Entscheidung zu treffen: Stellt sich später heraus, dass Sie mit der Wahl
unzufrieden sind, weil der Blog nicht die gewünschten Möglichkeiten bietet, waren Ihre Bemühungen umsonst. Sie müssen auf einer geeigneteren Plattform von vorne beginnen.
"""  # You can paste pretty much any text you want
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