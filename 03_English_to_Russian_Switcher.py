#  This small program was made for people who accidentally typed english letters,
#  but they wanted to type russian words.

# This program will change your english characters to russian


text = input("Enter: ")
final = ''
characters = {
    "q": "й",
    "w": "ц",
    "e": "у",
    "r": "к",
    "t": "е",
    "z": "н",
    "u": "г",
    "i": "ш",
    "o": "щ",
    "p": "з",
    "ü": "х",
    "a": "ф",
    "s": "ы",
    "d": "в",
    "f": "а",
    "g": "п",
    "h": "р",
    "j": "о",
    "k": "л",
    "l": "д",
    "ö": "ж",
    "ä": "э",
    "y": "я",
    "x": "ч",
    "c": "с",
    "v": "м",
    "b": "и",
    "n": "т",
    "m": "ь",
    "^": "ё",
    "Q": "Й",
    "W": "Ц",
    "E": "У",
    "R": "К",
    "T": "Е",
    "Z": "Н",
    "U": "Г",
    "I": "Ш",
    "O": "Щ",
    "P": "З",
    "Ü": "Х",
    "A": "Ф",
    "S": "Ы",
    "D": "В",
    "F": "А",
    "G": "П",
    "H": "Р",
    "J": "О",
    "K": "Л",
    "L": "Д",
    "Ö": "Ж",
    "Ä": "Э",
    "Y": "Я",
    "X": "Ч",
    "C": "С",
    "V": "М",
    "B": "И",
    "N": "Т",
    "M": "Ь",
    "°": "Ё",
    "/": "?",
    "-": ".",
    "_": ","
}

for editor in list(text):
    for editor2 in list(editor):
        final += characters.get(editor, editor)

print(final)
