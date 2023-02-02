#######################
# LANDSCAPER LAB
#######################
game = {"tool":0, "money": 0}

## Player
player = {
    'money': 0,
    'tools': [],
    'current_tool': {
        'name': "Teeth",
        'cost': 0,
        'profit': 1
    }
}

## Tools
tools = [
    {
        'name': 'teeth',
        'cost': 0,
        'profit': 1
    },
    {
        'name': 'rusty scissors',
        'cost': 5,
        'profit': 5 
    },
    {
        'name': 'push lawnmower',
        'cost': 25,
        'profit': 50
    },
    {
        'name': 'electric lawnmower',
        'cost': 250,
        'profit': 100
    },
    {
        'name': 'team of students',
        'cost': 500,
        'profit': 250
    }
]

## Functions
def upgrade():
    if (game["tool"] >= len(tools) -1):
        print("no more upgrades available")
        return 0
    buy_tool = tools[game["tool"]+1]
    if (buy_tool == None):
        print("There is no more tools")
        return 0
    if (game["money"] < buy_tool["cost"]):
        print("Not enough money to buy tool")
        return 0
    print("You have upgraded your tool")
    game["money"] -= buy_tool["cost"]
    game["tool"] += 1

def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have {game['money']} dollars and are using a {tool['name']}")
            
def mow_lawn():
    tool = tools[game["tool"]]
    print(f"You mow a lawn with your {tool['name']} and make {tool['profit']} dollars")  
    game["money"] += tool["profit"]  
    
def win_check():
    if(game["tool"] == 4 and game["money"] >=  1000):
        print("YOU WIN!")
        return True
    return False
          
while(True):
    player_choice = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [Q] Quit")
    player_choice = int(player_choice)
    
    if (player_choice == 1):
        mow_lawn()
    
    if (player_choice == 2):
        check_stats()
        
    if (player_choice == 3):
        upgrade()   
             
    if(player_choice == "Q"):
        print("You've quit the game")
        break  
    
    if(win_check()):
        break        

    