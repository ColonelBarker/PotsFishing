import random

# Function to print player information
def print_player_info(money, pots):
    print(f"You have ${money} and {pots} pots.")

def weather_forecast():
    # Generate random percentages for the bay. This is magic code.
    bay_storm_percentage = random.randint(1, 50)
    bay_sunny_percentage = random.randint(1, 50)
    bay_clear_percentage = 100 - bay_storm_percentage - bay_sunny_percentage

    # Generate random percentages for the beach. This needs work.
    beach_storm_percentage = random.randint(1, 10)
    beach_sunny_percentage = random.randint(1, 60)
    beach_clear_percentage = 100 - beach_storm_percentage - beach_sunny_percentage

    print("\nWeather report. If there is a storm, you will lose your pots.")
    print("\nBAY")
    print(f"Storm {bay_storm_percentage}%")
    print(f"Sunny {bay_sunny_percentage}%")
    print(f"Clear {bay_clear_percentage}%")

    print("\nBEACH")
    print(f"Storm {beach_storm_percentage}%")
    print(f"Sunny {beach_sunny_percentage}%")
    print(f"Clear {beach_clear_percentage}%")

    bay_weather = (bay_storm_percentage, bay_sunny_percentage)
    beach_weather = (beach_storm_percentage, beach_sunny_percentage)

    return bay_weather, beach_weather

# Function for the fishing simulation
def fishing_simulation(pots_in_bay, pots_in_beach, bay_weather, beach_weather):
    dice_result = random.randint(1, 6)
    print(f"\nFishing simulation - Dice Result: {dice_result}")
    money_earned = 0    # Set money earned to zero
    returnpots = 0      # Declare this so there is something to return.
    dicepercent = dice_result * 100/6
 
    print("\nYou bring in the pots from the bay.")
    if bay_weather[0] > dicepercent:
        print("Oh no! It's a storm. You lose all pots in the bay.")
    elif (bay_weather[0] + bay_weather[1]  < dicepercent):
        print("Nice catch! You earn $10 for each pot in the bay.")
        money_earned = money_earned + (pots_in_bay * 10)
        returnpots += pots_in_bay
    else:
        print("Not a great catch. You earn $5 for each pot in the bay.")
        money_earned = money_earned + (pots_in_bay * 5)
        returnpots += pots_in_bay

    print("\nYou bring in the pots from the beach.")
    if beach_weather[0] > dicepercent:
        print("Oh no! It's a storm. You lose all pots in the beach.")
    elif (beach_weather[0] + bay_weather[1]  < dicepercent):
        print("Nice catch! You earn $20 for each pot in the beach.")
        money_earned = money_earned + (pots_in_beach * 20)
        returnpots += pots_in_beach
    else:
        print("Not a great catch. You lose your pots")

    return returnpots, money_earned

# Main game loop

#Initial variables
money = 50
pots = 0
day = 0

print("Welcome to the Fishing Dice Game!\n")
print("You are a fisherman trying to make a living by deploying pots in the bay and on the beach.")
print("Each day, you can choose to buy pots, check the weather forecast, and strategically place your pots.")
print("Roll the dice to simulate the fishing results and earn money based on the weather conditions.")
print("Be careful, as storms can be disastrous, but a sunny day can bring a great catch!\n")

while money >= 10 or pots > 0:
    print(f"\n-------- Day {day} --------")

    # 1. Purchase pots
    print_player_info(money, pots)
    buy_pots = int(input("\nHow many pots would you like to buy? They are $10 each: "))
    while buy_pots * 10 > money:
        print("Not enough money. Please choose a valid number of pots.")
        buy_pots = int(input("\nHow many pots would you like to buy? They are $10 each: "))
    money -= buy_pots * 10
    pots += buy_pots
    print_player_info(money, pots)

    # 2. Weather forecast
    bay_weather, beach_weather = weather_forecast()

    # 3. Putting pots on bay or beach
    pots_on_beach = int(input(f"\nHow many pots would you like to put on the beach? (max {pots}): "))
    while pots_on_beach > pots:
        print("Invalid input. You can't put more pots on the beach than you have.")
        pots_on_beach = int(input(f"\nHow many pots would you like to put on the beach? (max {pots}): "))

    pots -= pots_on_beach

    # Additional prompt for putting pots in the bay
    pots_on_bay = int(input(f"\nHow many pots would you like to put in the bay? (max {pots}): "))
    while pots_on_bay > pots:
        print("Invalid input. You can't put more pots in the bay than you have.")
        pots_on_bay = int(input(f"\nHow many pots would you like to put in the bay? (max {pots}): "))

    pots -= pots_on_bay
    print_player_info(money, pots)

    # 4. Fishing simulation
    pots, money_earned = fishing_simulation(pots_on_bay, pots_on_beach, bay_weather, beach_weather)
    money += money_earned

    # 5. Results
    print_player_info(money, pots)
    day += 1

    pots_on_bay = 0     # Resets pots.
    pots_on_beach = 0 

print("\nGame Over")
