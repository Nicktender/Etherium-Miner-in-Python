import os
import random
playing = False
import time
from colorama import init, Fore, Back, Style
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '_', '=', '?', '/', '|', '\\', ':', ';', '"', "'", ',', '.', '<', '>', '(', ')', '{', '}']
Base_Temp = 60
Temp = 0
def load():
  global SaveLoad
  print(Fore.RED+"Sorry, this doesn't work yet. I plan to add it in the future, thats why it's here.")
  SaveLoad = 1
  return SaveLoad
def save():
  global SaveLoad
  print(Fore.RED+"Sorry, this doesn't work yet. I plan to add it in the future, thats why it's here.")
  SaveLoad = 1
  return SaveLoad
def clear_screen():
    print(Fore.WHITE)
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
        choice = input(Fore.RED + "Invalid input! Please choose Heads or Tails: ").lower()
    result = random.choice(("heads", "tails"))
    print("You landed on... ", result)
    if choice == result:
        print(Fore.GREEN + "Congratulations! You won!")
        ETH += random.randint(1,20)
    else:
        print(Fore.RED +"Sorry, you lost!")
    input(Fore.WHITE+"Press Enter to continue...")

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
        print(Fore.GREEN + "Congratulations! You won",Fore.BLUE + result, Fore.GREEN + "ETH!")
    input("Press Enter to continue...")
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
        result = random.randint(20,25)
        print(Fore.GREEN + "Congratulations! You won",Fore.BLUE + result, Fore.GREEN + "ETH!")
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
              print(Fore.RED + "Invalid input! Please choose 1, 2, 3, or 4.")
              input("Press Enter to continue...")
          playing = False


    else:
      print("Try to reach a milestone first!")
      input("Press Enter to continue...")
# Initialize the colorama module
init()
# Sets the colors
print(Fore.WHITE + Back.BLACK + Style.BRIGHT + " ")
target = 1


clicks = 0
ETH = 0
multiplier = 1
started = 0
milestones = 0
cool_factor = 0
program = 0
sus = 0
gain=True
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
    SaveLoad = 0
    started = 1
  elif SaveLoad == "2":
    load()
    input("Press Enter to continue...")
    SaveLoad = 0
  else: 
    print(Fore.RED + "Invalid option. Please enter 1 or 2.")
    input("Press Enter to continue...")
Temp += Base_Temp
def add_ETH():
    global ETH
    global Temp
    global Base_Temp
    global cool_factor
    global program
    if gain==True:
      Temp += (PC)*(multiplier + 1.5)//(cool_factor+1)
      ETH += multiplier
      global clicks
      clicks += 1
    else:
      ETH += 0.5
    return clicks
    return Temp
    return ETH
Temp_Color = Fore.GREEN
def check_temp():
    global Temp
    global Temp_Color
    if Temp >= Base_Temp + 40:
        Temp_Color = Fore.RED
    elif Temp <= Base_Temp - 20:
        Temp_Color = Fore.BLUE
    else:
        Temp_Color = Fore.GREEN
    return Temp_Color
    return Temp
while started == 1:
  if Temp >= 115:
    gain=False
  else:
    gain=True
    
  PC = program+1
  milestone = (clicks // 20)
  if milestone > 0 and clicks % 20 == 0:
    print(f"Milestone unlocked: {milestone}")
    input("Press Enter to continue...")
  clear_screen()
  print(f"PC count: {PC}")
  print("Milestone", milestone, Fore.BLUE)
  print(ETH, "Ethereum mined", Fore.WHITE)
  check_temp()
  print(f"{Temp_Color}The current temperature is {Temp}°C{Fore.RESET}")
  print(Fore.WHITE + "Overclock level of ", multiplier)
  print("____________________________")
  if auto == True:
    print("Type auto to afk with earnings. You need to buy it again to use it again!")
  print("Type help to for actions.")
  print("Type mine to mine!")
  user_input = input("")
  if user_input == "mine":
    add_ETH()
  else:
    if user_input == "save":
      save()
      input("Press Enter to continue...")
    elif user_input == "help":
      print("Press enter to mine.")
      if auto:
        print("Type auto to afk with earnings!")
      print("Type help for actions.")
      print("Type shop to buy upgrades!")
      print("Type chance to play minigames!")
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
                print("You have", Fore.BLUE + ETH, "Etherium.")
                print("Automating... (do not press any keys)")
                time.sleep(0.2)
            input("Press Enter to continue...")
            auto=False
        else:
          print(Fore.RED+"You need more PCs to do that!")
    elif user_input == "shop":
      clear_screen()
      print("SHOP")
      print("1. Overclock")
      print("   Every piece of Ethereum mined gets you more!")
      cost_multiplier = (multiplier + 1) * 20
      print(Fore.YELLOW)
      print(f"   Cost: 💰 {cost_multiplier}")
      print(Fore.WHITE)
      print("")
      print("2. Buy PCs")
      print("   They help you find Ethereum!")
      PC_price = (program + 1) * 30
      print(Fore.YELLOW)
      print(f"   Cost: 💰 {PC_price}")
      print(Fore.WHITE)
      print("")
      print("3. Buy Fan")
      print("   A fan is helpful for cooling your rigs!")
      print(Fore.YELLOW)
      print("   Cost: 💰 15")
      print(Fore.WHITE)
      print("")
      print("4. Buy Cooling Rig")
      print("   The Cooling Rig cools your PCs down dramatically")
      cool_rig_price = (cool_factor + 1) * 50
      print(Fore.YELLOW)
      print(f"   Cost: 💰 {cool_rig_price}")
      print(Fore.WHITE)
      
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
              print("You don't have enough Ethereum!")
              input("Press Enter to continue...")
      elif bought == "3":
          if 15 <= ETH:
              Temp -= 15
              ETH -= 15
              input("Press Enter to continue...")
          else:
              print("You don't have enough Ethereum!")
              input("Press Enter to continue...")
      elif bought == "4":
          if cool_rig_price <= ETH:
              cool_factor += 1.5
              Temp -= cool_factor
              ETH -= cool_rig_price
              print(f"You now have a cooling rate of {cool_factor}!")
              input("Press Enter to continue...")
          else:
              print("You don't have enough Ethereum!")
              input("Press Enter to continue...")

      else:
          print(Fore.RED + "Invalid option. Please enter 1 or 2")
          input("Press Enter to continue...")

    else:
      print(Fore.RED + "Invalid choice. Type help for a list of actions.")
      input("Press enter to continue...")


