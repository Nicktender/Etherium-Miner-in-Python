import os
import random
playing = False
import time
from colorama import init, Fore, Back, Style
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '_', '=', '?', '/', '|', '\\', ':', ';', '"', "'", ',', '.', '<', '>', '(', ')', '{', '}']
def clear_screen():
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Unix-based systems
        os.system('clear')
def coin_toss():
    clear_screen()
    global ETH
    print("Welcome to Coin Toss!")
    choice = input("Heads or Tails? ").lower()
    while choice not in ("heads", "tails"):
        choice = input("Invalid input! Please choose Heads or Tails: ").lower()
    result = random.choice(("heads", "tails"))
    print("You landed on... ", result)
    if choice == result:
        print("Congratulations! You won!")
        ETH += random.randint(1,20)
    else:
        print("Sorry, you lost!")
    input("Press Enter to continue...")

def wheel():
    global ETH
    clear_screen()
    print("Welcome to the Wheel of Randomness!")
    prizes = ["100", "50", "25", "10", "5", "0"]
    input("Press enter to spin the wheel!")
    result = random.choice(prizes)
    print("Spinning...")
    print("You landed on:", result, "ETH")
    ETH += int(result)
    if result == "0":
        print("Better luck next time!")
    else:
        print("Congratulations! You won", result)
    input("Press Enter to continue...")
    return ETH
def rps():
    global ETH
    clear_screen()
    print("Welcome to Rock Paper Scissors!")
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    while player_choice not in choices:
        player_choice = input("Invalid input! Please choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    print("You chose", player_choice)
    print("The computer chose", computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
        input("Press Enter to continue...")
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        result = random.randint(20,25)
        print(f"Congratulations! You won {result}ETH!")
        ETH += result
        return ETH
        input("Press Enter to continue...")
    else:
        print("Sorry, you lose!")
        input("Press Enter to continue...")

def surprise():
    clear_screen()
    print("Welcome to the Surprise Game!")
    games = [coin_toss, wheel, rps]
    game = random.choice(games)
    game()

def play_game():
    random_choice = ""
    if milestone > 0:
      playing = True
      while playing:
          clear_screen()
          print("Welcome to the chance spot!")
          print("What would you like to do?")
          print("1. Coin Toss")
          print("2. Wheel of Randomness")
          print("3. Rock Paper Scissors")
          print("4. Surprise me!")
          random_choice = input("")
          if random_choice == "1":
              coin_toss()
          elif random_choice == "2":
              wheel()
          elif random_choice == "3":
              rps()
          elif random_choice == "4":
              surprise()
          else:
              print("Invalid input! Please choose 1, 2, 3, or 4.")
              input("Press Enter to continue...")
          playing = False


    else:
      print("Try to reach a milestone first!")
      input("Press Enter to continue...")
# Initialize the colorama module
init()
# Print colored and styled text
print(Fore.WHITE + Back.BLACK + Style.BRIGHT + " ")
target = 1


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


while started == 0:
  clear_screen()
  while not Named:
    clear_screen()
    Username = input("Username: ")
    if len(Username) >= 3 and len(Username) <= 10 and not any(symbol in Username for symbol in symbols):
        input("Press Enter to continue...")
        Named = True
    else: 
        print("Invalid username! You entered", Username, ".")
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
    SaveLoad = 0
    started = 1
  elif SaveLoad == "2":
    load()
    input("Press Enter to continue...")
    SaveLoad = 0
  else: 
    print("Invalid option. Please enter 1 or 2.")
    input("Press Enter to continue...")
    
while started == 1:
  milestone = (clicks // 20)
  if milestone > 0 and clicks % 20 == 0:
    print(f"Milestone unlocked: {milestone}")
    input("Press Enter to continue...")
  clear_screen()
  print(milestone)
  print(f"{ETH} Ethereum found")
  print(f"{multiplier} multiplier")
  print("____________________________")
  if auto == True:
    print("Type auto to afk with earnings. You need to buy it again to use it again!")
  print("Type help to for actions.")
  print("Press Enter to mine!")
  user_input = input("")
  if user_input == "":
    ETH += (multiplier)
    clicks += 1
  else:
    if user_input == "save":
      save()
      input("Press Enter to continue...")
    elif user_input == "help":
      print("Press enter to mine.")
      print("Type help for actions.")
      print("Type shop to buy upgrades!")
      if auto == True:
        print("Type auto to afk with earnings!")
      print("Type save to save your progress.")
      input("Press enter to close")
    elif user_input.lower() == "chance":
        play_game()
    elif user_input == "auto":
        if auto:
            while sus < 25 * program:
                auto = False
                ETH += program
                sus += 1
                clear_screen()
                print("You have", ETH, "Etherium.")
                print("Automating... (do not press any keys)")
                time.sleep(0.2)
        else:
          print("You need more PCs to do that!")
    elif user_input == "shop":
      clear_screen()
      print("SHOP")
      print("1. Upgrade multiplier")
      print("   Every piece of Ethereum mined gets you more!")
      cost_multiplier = (multiplier + 1) * 20
      print(f"   Cost: 💰 {cost_multiplier}")
      print("")
      print("2. Buy PCs")
      print("   They help you find Ethereum!")
      PC_price = (program + 1) * 30
      print(f"   Cost: 💰 {PC_price}")
      bought = input("What would you like to buy? ")
      if bought == "1":
          if cost_multiplier <= ETH:
              multiplier += 1
              ETH -= cost_multiplier
              print(f"You now have a {multiplier}x multiplier!")
              input("Press Enter to continue...")
          else:
              print("You don't have enough Ethereum!")
              input("Press Enter to continue...")
      elif bought == "2":
          if PC_price <= ETH:
              program += 1
              ETH -= PC_price
              print(f"You now have {program} PCs!")
              auto = True
              input("Press Enter to continue...")
          else:
              print("You don't have enough Etherium!")
              input("Press Enter to continue...")
      else:
          print("Invalid option. Please enter 1 or 2")
          input("Press Enter to continue...")

    else:
      print("Invalid choice. Type help for a list of actions.")
      input("Press enter to continue...")
