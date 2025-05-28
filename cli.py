from rich import print
from questionary import Style
import questionary
from generator import mit
import time


print("[bold cyan] License Generator[/bold cyan]" )

options = ["MIT", "Apache", "Custom", "Exit"]

commands = {
    "exit":"exit()",
    "MIT":"mit()",
    "Apache":"apache()",
    "Custom":"cst()",
}

dark_style = Style([
    ("question", "fg:#A0A0FF bold"),      
    ("selected", "fg:#00FF00 bg:#444444"),
    ("pointer", "fg:#FF5555 bold"),       
    ("answer", "fg:#FFFFFF bold"),        
])
    
choice = questionary.select(
    "Выберите тип лицензии для вашего проекта: ",
    choices=options,
    qmark="-->", 
    style= dark_style, 
).ask()

if choice == "Exit":
    print("До свидания!")
    exit()
else:
    if choice != "Exit":
        print(f"[green] Вы выбрали: {choice}[/green]")
    if choice == "MIT":
        name = input("Type your name:  ")
        year = str(time.localtime().tm_year)
        mit(name, year)