clicks = 0
ETH = 0
multiplier = 1
started = 0
milestones = 0
program = 0
sus = 0
level = 1
auto = False
Named = False
import signal

def signal_handler(signal, frame):
    pass

import os
import random
playing = False
import time
from colorama import init, Fore, Back, Style
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '_', '=', '?', '/', '|', '\\', ':', ';', '"', "'", ',', '.', '<', '>', '(', ')', '{', '}']
import json

def encrypt_binary(data):
    json_str = json.dumps(data)
    binary_str = ''.join(['!' if bit == '1' else '|' for bit in ''.join(format(ord(char), '08b') for char in json_str)])
    return binary_str.encode()

def decrypt_binary(binary_str):
    binary_str = binary_str.decode()
    json_str = ''.join([chr(int(binary_str[i:i+8].replace('!', '1').replace('|', '0'), 2)) for i in range(0, len(binary_str), 8)])
    data = json.loads(json_str)
    return data


def save(Username, data):
    encrypted_data = encrypt_binary(data)
    with open(f"{Username}.Nicktender", "wb") as f:
        f.write(encrypted_data)
    print("This is your save file.")
    print("Highlight the data, then press CRTL + SHIFT + C to copy.")
    with open(f"{Username}.Nicktender", "rb") as file:
      # Read the data
        data = file.read()
        print("")
        print(data)
def load(Username):
        loading = True
        clear_screen()
        while loading:
          try:
            encrypted_data = input("Save File Data: ")
            data = decrypt_binary(encrypted_data.encode())
            global clicks, ETH, multiplier, started, milestones, program, sus, level, auto, Named
            clicks = data['clicks']
            ETH = data['ETH']
            multiplier = data['multiplier']
            started = data['started']
            milestones = data['milestones']
            program = data['program']
            sus = data['sus']
            level = data['level']
            auto = data['auto']
            Named = data['Named']
            loading = False
            print(f"{Fore.GREEN}Succesfully loaded save!")
            input(f"{Fore.WHITE}Press Enter to continue...")
          except:
            clear_screen()
            print(f"{Fore.RED}Error loading data! Your file may be corrupted.{Fore.WHITE}")
            input("Press Enter to continue...")
            clear_screen()

            
                    
def clear_screen():
    print(Back.BLACK, Fore.WHITE)
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Unix-based systems
        os.system('clear')
#in Replit, this would always be linux  becasue the console is a linux VM, but if your running it locally, this is useful for windows users.

def coin_toss():
    clear_screen()
    global ETH
    print("Welcome to the Coin Toss!")
    choice = input("Heads or Tails? ").lower()
    while choice not in ("heads", "tails"):
        choice = input(Fore.RED + "Invalid input! Please choose Heads or Tails: ").lower()
    result = random.choice(("heads", "tails"))
    print("It landed on... ", result)
    if choice == result:
        print(Fore.GREEN + "Congratulations! You won!")
        ETH += random.randint(60,70)
    else:
        print(Fore.RED +"Sorry, you lost!")
        ETH -= ETH*0.15
    input ("Press Enter to continue...")
    return ETH
def rps():
    global ETH
    clear_screen()
    print("Welcome to Rock Paper Scissors!")
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    while player_choice not in choices:
        player_choice = input(Fore.RED + "Invalid input! Please choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    print("You chose", player_choice)
    print("The computer chose", computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
        input("Press Enter to continue...")
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        result = random.randint(50,65)
        print(f"{Fore.GREEN} Congratulations! You won {Fore.BLUE} {result} Etherium!")
        ETH += result
        return ETH
        input("Press Enter to continue...")
    else:
        print("Sorry, you lose!")
        ETH -= ETH*0.10
        input("Press Enter to continue...")

def surprise():
    clear_screen()
    games = [coin_toss, rps]
    game = random.choice(games)
    game()

def play_game():
    random_choice = ""
    if milestone > 0:
      playing = True
      while playing:
          clear_screen()
          print("What would you like to do?")
          print("1. Coin Toss")
          print("2. Rock Paper Scissors")
          print("3. Surprise me!")
          random_choice = input("")
          if random_choice == "1":
              coin_toss()
              playing = False
          elif random_choice == "2":
              rps()
              playing = False

          elif random_choice == "3":
              surprise()
              playing = False
          else:
              print(Fore.RED + "Invalid input! Please choose 1, 2, or 3")
              input("Press Enter to continue...")
              playing = True
init()
# Sets the colors
print(Fore.WHITE + Back.BLACK + Style.BRIGHT + " ")
target = 1
color = print(Fore.WHITE + Back.BLACK + Style.BRIGHT + " ")

# Set the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)


started = 0
Named = False
while started == 0:
  clear_screen()
  while not Named:
    clear_screen()
    Username = input("Username: ")
    if len(Username) >= 3 and len(Username) <= 10 and not any(symbol in Username for symbol in symbols):
        input("Press Enter to continue...")
        Named = True
    else: 
        print(Fore.RED + "Invalid username! You entered", Username, ".")
        print("Name must be 3 to 10 characters long. It may not contain symbols.")
        input("Press Enter to continue...")
        Named = False
  clear_screen()
  print("Pick an option.")
  print("1. New save")
  print("2. Load save")
  SaveLoad = input("")
  if SaveLoad == "1":
    print("Starting new save...")
    input("Press Enter to continue...")
    clicks = 0
    ETH = 0
    multiplier = 1
    started = 1
    milestones = 0
    milestone = 0
    program = 0
    sus = 0
    level = 1
    auto = False
    if Username == "Admin0409":
      clicks = 69420
      ETH = 10000000
      multiplier = 100
      started = 1
      milestone = 15
      milestones = 15
  elif SaveLoad == "2":
    load(Username)
    input("Press Enter to continue...")
    started = 1
  else: 
    print(Fore.RED + "Invalid option. Please enter 1 or 2." + Fore.WHITE)
    input("Press Enter to continue...")

def add_ETH():
    global ETH
    ETH += multiplier
    global clicks
    clicks += 1
while started == 1:
  color
  ETH = round(ETH)
  if ETH < 1:
    ETH = 0
  milestone = (clicks // 20)
  if milestone > 0 and clicks % 20 == 0:
    print(f"Milestone unlocked: {milestone}")
    input("Press Enter to continue...")
  clear_screen()
  if Username == "Admin0409":
    print(f"{Fore.GREEN}Admin{Fore.WHITE}")
    milestone = 69
  print("Milestone:", milestone, Fore.BLUE)
  print(ETH, "Ethereum", Fore.WHITE)
  print(f"{multiplier} GPUs")
  print("____________________________")
  if auto == True:
    print("Type investigate to check for Etherium.")
  print("Type help to for actions.")
  print("Type mine to mine!")
  user_input = input("")
  if user_input == "mine":
    add_ETH()
  else:
    if user_input == "save":
      data = {
      "clicks": clicks,
      "ETH": ETH,
      "multiplier": multiplier,
      "started": started,
      "milestones": milestones,
      "program": program,
      "sus": sus,
      "level": level,
      "auto": auto,
      "Named": Named,
      }
      save(Username, data)
      input("Press Enter to continue...")
    elif user_input == "help":
      print("Press enter to mine.")
      if auto:
        print("Type 'investigate' to afk with earnings!")
      print("Type 'help' for actions.")
      print("Type 'shop' to buy upgrades!")
      if auto == True:
        print("Type 'investigate' to afk with earnings!")
      print("Type 'save' to save your progress.")
      input("Press Enter to close")
    elif user_input.lower() == "investigate":
        if auto:
          amount = random.randint(100,130)
          if random.randint(0,10) < 3:
            input("Press Enter to start looking...")

            while sus < amount:
                auto = False
                ETH += 1
                sus += 1
                clear_screen()
                print(f"You found {sus} {Fore.BLUE}Etherium!{Fore.WHITE}")
                print(f"You have {Fore.BLUE}{ETH} Etherium.{Fore.WHITE}")
                time.sleep(0.15)
            input("Press Enter to continue...")
            auto=False
          else:
            print("You did not find any Etherium!")
            auto = False
            input("Press Enter to continue...")
        else:
          print(Fore.RED+"You need a Hard Drive to do that!")
          input("Press Enter to continue...")
    elif user_input == "shop":
      shopping = True
      while shopping:
        clear_screen()
        print("SHOP")
        print("1. New GPU")
        print("   Every piece of Ethereum mined gets you more!")
        cost_multiplier = (multiplier + 1) * 20
        print(f"{Fore.YELLOW}   Cost: 💰 {cost_multiplier}")
        print("   Requirement: Reach Milestone 5")
        print(Fore.WHITE)
        print("")
        print("2. Buy Hard Drive")
        print("   Maybe you will find some etherium!")
        print(f"{Fore.YELLOW}   Cost: 💰 100")
        print(Fore.WHITE)
        print("3. Make a Bet")
        print("   Arrange a bet with someone, you are betting on etherium!")
        cost_multiplier = (multiplier + 1) * 20
        print(f"{Fore.YELLOW}   Cost: 💰 50")
        print("   Requirement: Reach milestone 10")
        print(Fore.WHITE)
        bought = input("What would you like to buy? ")
        if bought == "1":
          if milestone >= 5:
            if cost_multiplier <= ETH:
                multiplier += 1
                ETH -= cost_multiplier
                print(f"You now have {multiplier} GPUs!")
                input("Press Enter to continue...")
            else:
                print(f"{Fore.RED}You don't have enough Ethereum!{Fore.WHITE}")
                input("Press Enter to continue...")
          else:
            print(f"{Fore.RED}You don't meet the rquirement!{Fore.WHITE}")
            input ("Press Enter to continue...")
        elif bought == "2":
            if auto == False:
              if 100 <= ETH:
                  ETH -= 100
                  print(f"You now have a new Hard Drive to look through.")
                  auto = True
                  input("Press Enter to continue...")
              else:
                  print(f"{Fore.RED}You don't have enough Etherium!{Fore.WHITE}")
                  input("Press Enter to continue...")
            else:
              print(f"{Fore.RED}Try looking through the Hard Drive you already have!{Fore.WHITE}")
              input("Press Enter to continue...")

        
        elif bought == "3":
          if milestone >= 10:
            if ETH >=50:
              ETH -= 50
              play_game()
            else:
              print("You have insufficient Etherium!")
              input("Press Enter to continue...")
          else:
            print("You need to get to milestone 10!")
            input("Press Enter to continue...")
        elif bought == "close":
          shopping = False
        else:
            print(Fore.RED + "Invalid option. Please enter 1, 2,3, or close")
            input("Press Enter to continue...")
        
  
    else:
      print(Fore.RED + "Invalid choice.  help for a list of actions.")
      input("Press enter to continue...")
