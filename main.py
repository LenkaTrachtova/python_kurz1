import re
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

link = colored_text ("-", 125) * 45

#hlavička
print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lenka Trachtová
email: lenkatrachtova@email.cz""")
print(link)

#vstup uživatele
name = input("username:")
password = input("password:")
#ANSI obarvení hesla
import sys
#přesunutí kurzoru o 2 řádky a obarvení výstupu
sys.stdout.write("\033[F\033[K")
print(f"username: {name}")
sys.stdout.write("\033[F\033[K")
print(f"password: {colored_text(password, 214)}")
print(link)

#podmínky přihlášení
registred = user.get(name) == password
    
if registred:
        print (f'''Welcome to the app{colored_text(",", 203)} {name}
We have {colored_text("3", 214)} texts to be analyzed.''')
else:
    print(f"unregistered user{colored_text(",", 125)} " +
          f"terminating the program{colored_text("..", 125)}")
    quit()

print(link)
#výběr textu
try:
    select = int(input(f"Enter a number btw{colored_text(".", 125)} " +
                   f"{colored_text("1", 214)} {colored_text("and", 125)} " +
                   f"{colored_text("3", 214)} to select:"))
#obarvení výstupu
    sys.stdout.write("\033[F\033[K")
    print(f"Enter a number btw{colored_text(".", 125)} " +
          f"{colored_text("1", 214)} {colored_text("and", 125)} " +
          f"{colored_text("3", 214)} to select: {colored_text(select, 214)}")
    print(link)

    if 1 <= select <= len(TEXTS):
          select_text = TEXTS[select -1]
#analýza textu          
          words = re.findall(r'\b\w+\b', select_text)
          total_words = len(words)
          capitalized_words = sum(1 for w in words if w[0].isupper() and w[1:].islower())
          uppercase_words = sum(1 for w in words if w.isupper())
          lowercase_words = sum(1 for w in words if w.islower())
          numbers = [int(w) for w in words if w.isdigit()]
          number_count = len(numbers)
          number_sum = sum(numbers)
#výstup
          print(
             f"There are {colored_text(str(total_words), 214)} words " +
             f"{colored_text("in", 125)} the selected text{colored_text(".", 125)}\n"
             f"There are {colored_text(str(capitalized_words), 214)} " +
             f"{colored_text("titlecase", 12)} words{colored_text(".", 125)}\n"
             f"{colored_text("There", 11)} are {colored_text(str(uppercase_words), 214)} " +
             f"uppercase words{colored_text(".", 125)}\n"
             f"There are {colored_text(str(lowercase_words), 214)} {colored_text("lowercase", 12)} " +
             f"words{colored_text(".", 125)}\n"
             f"{colored_text("There", 11)} are {colored_text(number_count, 214)} " +
             f"numeric strings{colored_text(".", 125)}\n"
             f"The sum of all the numbers {colored_text(number_sum, 214)}"
               ) 
          print(link)
        
#četnost délky slov
          print(f"{'LEN'.rjust(3)}{colored_text('|', 125)}{'OCCURRENCES'.center(35)}{colored_text('|', 125)}" +
                f"{'NR.'.rjust(3)}")
          print(link)
          
          lengths = {}
          for word in words:
            length = len(word)
            lengths[length] = lengths.get(length, 0) + 1
#sloupcový graf   
          for length in sorted(lengths):
               count = lengths[length]
               stars = "*" * count
            #    gap = " " * (12 - len(stars))
            #    num_gap = " " * (4 - len(str(length)))
               print(f"{colored_text(str(length).rjust(3), 214)}" +
                     f"{colored_text("|", 125)}" +
                     f"{colored_text(stars.ljust(35), 125)}{colored_text("|", 125)}" +
                     f"{colored_text(str(count).rjust(3), 214)}"
                     )
#ukončení
    else:
          print(f"Invalid number{colored_text(",", 125)} " +
                f"program termination{colored_text("..", 125)}")
          quit()
except ValueError:
      print(f"Incorrect format{colored_text(",", 125)} " +
            f"program termination{colored_text("..", 125)}")          
                    
print(link)




    














