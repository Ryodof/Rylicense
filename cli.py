import colorama
from rich import print
from questionary import Style
import questionary


print("[bold cyan] License Generator[/bold cyan]" )

options = ["MIT", "Apache", "Custom", "Exit"]

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
        print(f"Вы выбрали: {choice}")