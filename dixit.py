# ==========================================================
#  DIXIT PERSONAL CLI — FINAL MASTER VERSION
#  Author : Bismaya Dikshit
# ==========================================================

from colorama import Fore, Style, init
import datetime
import random
import os
import time
import requests

# ---------- INIT ----------
init(autoreset=True)

# ---------- READLINE (Auto-complete + History) ----------
try:
    import readline
    readline.parse_and_bind("tab: complete")
except ImportError:
    readline = None

# ---------- GLOBALS ----------
LOG_FILE = "dixit_logs.txt"

COMMANDS = [
    "about", "skills", "projects", "contact", "social",
    "github", "ask", "theme", "quote", "game",
    "time", "date", "birthday",
    "clear", "help", "exit"
]

THEMES = {
    "dark": Fore.WHITE,
    "neon": Fore.LIGHTCYAN_EX,
    "matrix": Fore.GREEN
}

THEME_COLOR = Fore.LIGHTCYAN_EX

# ---------- COMPLETER ----------
def completer(text, state):
    options = [cmd for cmd in COMMANDS if cmd.startswith(text)]
    return options[state] if state < len(options) else None

if readline:
    readline.set_completer(completer)

# ---------- UTILITIES ----------
def log_command(cmd):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} ➜ {cmd}\n")

def type_print(text, color=Fore.WHITE, delay=0.015):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()

def startup_sound():
    print("\a", end="")

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    startup_sound()
    banner()
    command_box()

# ---------- UI ----------
def banner():
    type_print("╔══════════════════════════════════════════════╗", Fore.CYAN, 0.002)
    type_print("║        D I X I T   P E R S O N A L           ║", Fore.LIGHTCYAN_EX, 0.002)
    type_print("║                C L I                         ║", Fore.LIGHTBLUE_EX, 0.002)
    type_print("╚══════════════════════════════════════════════╝", Fore.CYAN, 0.002)

def command_box():
    print(THEME_COLOR + Style.BRIGHT + """
╔══════════════════ AVAILABLE COMMANDS ══════════════════╗
║ about      skills      projects    contact             ║
║ social     github     ask         theme                ║
║ quote      game       time        date                 ║
║ birthday   clear      help        exit                 ║
╚════════════════════════════════════════════════════════╝
""")

def prompt():
    return input(Style.BRIGHT + THEME_COLOR + "DixitCLI ➜ ").lower()

# ---------- SECTIONS ----------
def about():
    type_print("""
👤 Name      : Bismaya Dikshit
🎓 Degree    : Bachelor of Computer Applications (BCA)
📍 Location  : Odisha, India
💡 Interests : Programming, Data Science, Machine Learning
""", THEME_COLOR)

def skills():
    type_print("""
🛠️ SKILLS

• Programming Languages:
  C, C++, Java (Basic), Python (Basic), R

• Web Technologies:
  HTML, CSS, JavaScript

• Database:
  MySQL, PostgreSQL

• Data & AI:
  Data Science, Machine Learning, GitHub

• Tools & Platforms:
  Git, VS Code, Windows / Linux / Unix

• Other:
  MS Word, Excel, PowerPoint, Canva
""", THEME_COLOR)

def projects():
    type_print("""
📂 PROJECTS
1️⃣ UPI Scam Detection using Data Mining
2️⃣ Movie Hit/Flop Prediction App
3️⃣ Product Price Prediction Project
4️⃣ Lost and Found Application
""", THEME_COLOR)

def contact():
    type_print("""
📞 CONTACT
📱 Phone : 8984971764
""", THEME_COLOR)

def social():
    type_print("""
🌐 SOCIAL LINKS
• GitHub    : https://github.com/bismayadixit
• LinkedIn  : https://www.linkedin.com/in/bismaya-dixit-4143aa32b/
• Instagram : https://www.instagram.com/bismaya._.dixit/
""", THEME_COLOR)

# ---------- GITHUB STATS ----------
def github():
    username = "bismayadixit"
    url = f"https://api.github.com/users/{username}"
    try:
        r = requests.get(url, timeout=5)
        data = r.json()
        type_print(f"""
🌐 GitHub Stats
• Username  : {data['login']}
• Repos     : {data['public_repos']}
• Followers : {data['followers']}
• Following : {data['following']}
""", THEME_COLOR)
    except:
        type_print("⚠ Unable to fetch GitHub stats", Fore.RED)

# ---------- AI COMMAND ----------
def ask():
    try:
        from openai import OpenAI
        import os

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        q = input("🤖 Ask Dixit AI ➜ ")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": q}]
        )

        type_print("\n" + response.choices[0].message.content, THEME_COLOR)
    except:
        type_print("⚠ AI not configured (API key missing)", Fore.RED)

# ---------- THEME ----------
def theme():
    global THEME_COLOR
    print("🎨 Themes: dark | neon | matrix")
    choice = input("Choose theme ➜ ").lower()

    if choice in THEMES:
        THEME_COLOR = THEMES[choice]
        type_print(f"✅ Theme switched to {choice.upper()}", THEME_COLOR)
    else:
        type_print("❌ Invalid theme", Fore.RED)

# ---------- OTHER ----------
def quote():
    type_print("""
"Work hard in silence, let success make the noise."
""", Fore.LIGHTRED_EX)

def show_time():
    type_print(f"⏰ Time : {datetime.datetime.now().strftime('%H:%M:%S')}", Fore.YELLOW)

def show_date():
    type_print(f"📅 Date : {datetime.datetime.now().strftime('%d-%m-%Y')}", Fore.YELLOW)

def birthday():
    type_print("🎂 Birthday : 31 / 08 / 2005", Fore.GREEN)

def game():
    type_print("🎮 Guess the Number (1–10)", Fore.LIGHTYELLOW_EX)
    num = random.randint(1, 10)
    guess = input("Your guess ➜ ")

    if guess.isdigit() and int(guess) == num:
        type_print("🎉 Correct! You Win!", Fore.GREEN)
    else:
        type_print(f"❌ Wrong! Number was {num}", Fore.RED)

# ---------- MAIN LOOP ----------
def main():
    clear()

    while True:
        cmd = prompt()
        log_command(cmd)

        if cmd == "about": about()
        elif cmd == "skills": skills()
        elif cmd == "projects": projects()
        elif cmd == "contact": contact()
        elif cmd == "social": social()
        elif cmd == "github": github()
        elif cmd == "ask": ask()
        elif cmd == "theme": theme()
        elif cmd == "quote": quote()
        elif cmd == "time": show_time()
        elif cmd == "date": show_date()
        elif cmd == "birthday": birthday()
        elif cmd == "game": game()
        elif cmd == "clear": clear()
        elif cmd == "help": command_box()
        elif cmd == "exit":
            type_print("👋 Goodbye Mr. Dixit — Keep Building 🚀", Fore.GREEN)
            break
        else:
            type_print("❌ Unknown command. Type 'help'.", Fore.RED)

# ---------- ENTRY ----------
if __name__ == "__main__":
    main()
