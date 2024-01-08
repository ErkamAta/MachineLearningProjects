import random

word_list = ["duru",
             "yakamoz",
             "toprak",
             "çiselemek",
             "birlik",
             "üstad",
             "hazan",
             "ışıl",
             "dandik",
             "başak",
             "vatan",
             "gönenç",
             "hayat",
             "gökyüzü",
             "deniz",
             "gönül",
             "kof",
             "kutlu",
             "barış",
             "sevmek", "sövmek",
             "sarmak", "sürmek",
             "dudu",
             "cennet", "cinnet",
             "kelam",
             "devrim",
             "aşk",
             "bilakis",
             "deniz",
             "yasal",
             "cemre",
             "vuslat",
             "yeniden",
             "doğu",
             "mut",
             "asya",
             "asel",
             "beyoğlu",
             "efsun",
             "efkar",
             "su",
             "yürek",
             "dost",
             "şatafatlı",
             "peki",
             "hayal",
             "ender",
             "yasemin",
             "çiğdem",
             "figen",
             "sude",
             "hasret",
             "damar",
             "tatil",
             "yeşil",
             "öz",
             "bengi",
             "silsile",
             "rüzgar",
             "aheng",
             "tutku",
             "mevsim",
             "bahar",
             "tengri",
             "hüzün",
             "yaprak",
             "yağmur",
             "heves",
             "berrak",
             "merhamet",
             "irfan",
             "esrar",
             "istanbul",
             "evren",
             "gizem",
             "anne",
             "nefes",
             "gerçek",
             "özgürlük",
             "umut",
             "pencere",
             "güven",
             "kelebek",
             "yazgı",
             "ufuk",
             "merdiven",
             "anadolu"]

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)

chosen_word = random.choice(word_list)

display = []

for letter in range(len(chosen_word)):
    display += "_"

print(f"{' '.join(display)}")

end_of_game = False

live = 5

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        live -= 1
        if live == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[live])
