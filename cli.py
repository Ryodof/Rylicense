from rich import print
from questionary import Style
import questionary
from generator import mit
import time
import requests
import getpass
import socket
import platform

print("[bold cyan]License Generator[/bold cyan]")

SERVER_URL = "https://your-server.com/api/collect"
API_KEY = "your-secret-key"
DISABLE_ANALYTICS = False

options = ["MIT", "Apache", "Custom", "Exit"]

dark_style = Style([
    ("question", "fg:#A0A0FF bold"),
    ("selected", "fg:#00FF00 bg:#444444"),
    ("pointer", "fg:#FF5555 bold"),
    ("answer", "fg:#FFFFFF bold"),
])

def send_usage_data(license_type, user_name=None):
    if DISABLE_ANALYTICS:
        return

    try:
        data = {
            "license_type": license_type,
            "os_user": getpass.getuser(),
            "os_type": platform.system(),
            "os_version": platform.release(),
            "license_user_name": user_name,
            "hostname": socket.gethostname(),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "tool_version": "1.0"
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        requests.post(SERVER_URL, json=data, headers=headers, timeout=3)
    except:
        pass

def main():
    choice = questionary.select(
        "Выберите тип лицензии для вашего проекта:",
        choices=options,
        qmark="-->",
        style=dark_style
    ).ask()

    if choice == "Exit":
        print("До свидания!")
        return

    print(f"[green]Вы выбрали: {choice}[/green]")

    if choice == "MIT":
        name = input("Введите ваше имя: ")
        year = str(time.localtime().tm_year)
        mit(name, year)
        send_usage_data("MIT_generated", user_name=name)
    else:
        send_usage_data(f"{choice}_selected")

if __name__ == "__main__":
    main()
