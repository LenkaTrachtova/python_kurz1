import re
from collections import Counter

#hlavička
print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lenka Trachtová
email: lenkatrachtova@email.cz""")

TEXTS =  [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
#uživatelé
user = {"bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"}
#obarvení výstupu
def colored_text(text, color_code):
      return f"\033[38;5;{color_code}m{text}\033[0m"

link = colored_text ('-', 125) * 45
print(link)

#vstup uživatele
name = input("username:")
password = input("password:")
print(link)

#podmínky přihlášení
registred = user.get(name) == password
if registred:
        print (f'''Welcome to the app, {name}
We have {colored_text('3', 214)} texts to be analyzed.''')
else:
    print(f"unregistered user, terminating the program..")
    quit()
print(link)

#výběr textu
try:
    select = int(input(f"Enter a number btw. {colored_text('1', 214)}and {colored_text('3', 214)} to select:"))
    print(link)
    if 1 <= select <= len(TEXTS):
          select_text = TEXTS[select -1]
#analýza textu          
          words = re.findall(r'\b\w+\b', select_text)
          total_words = len(words)
          title_case = sum(1 for w in words if w[0].isupper() and w[1:].islower())
          uppercase_words = sum(1 for w in words if w.isupper())
          lowercase_words = sum(1 for w in words if w.islower())
          numbers = [int(w) for w in words if w.isdigit()]
          number_count = len(numbers)
          number_sum = sum(numbers)
#výstup
          print(
             f"There are {colored_text(str(total_words), 214)} words in the selected text.\n"
             f"There are {colored_text(str(title_case), 214)} titlecase words.\n"
             f"There are {colored_text(str(uppercase_words), 214)} uppercase words.\n"
             f"There are {colored_text(str(lowercase_words), 214)} lowercase words.\n"
             f"There are {colored_text(number_count, 214)} numeric strings.\n"
             f"The sum of all the numbers {colored_text(number_sum, 214)}"
               ) 
          print(link)
        
#četnost délky slov
          print(f"{'LEN'.rjust(3)}{colored_text('|', 125)}{'OCCURRENCES'.center(35)}{colored_text('|', 125)}{'NR.'.rjust(3)}")
          print(link)
          lengths = Counter(len(word) for word in words)
#sloupcový graf   
          for length in sorted(lengths):
               count = lengths[length]
               stars = "*" * count
               print(f"{colored_text(str(length).rjust(3), 214)}{colored_text('|', 125)}{colored_text(stars.ljust(35), 125)}" +
                     f"{colored_text('|', 125)}{colored_text(str(count).rjust(3), 214)}"
                     )
#ukončení
    else:
          print("Invalid number, program termination..")
          quit()
except ValueError:
      print(f"Incorrect format, program termination..")
      quit()          
print(link)