import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

# Data tambahan untuk generasi nama profesional
SUFFIXES = ["FC", "United", "City", "Athletic", "Club", "Atletico", "SC", "Rovers", "Wanderers", "Dynamo", "Alliance"]
EMOJIS = {
    'animal': {
        'lion': '🦁', 'eagle': '🦅', 'wolf': '🐺', 'bear': '🐻', 'shark': '🦈', 'dragon': '🐉',
        'tiger': '🐅', 'phoenix': '🕊️', 'panther': '🐆', 'bull': '🐂', 'falcon': '🦅',
        'horse': '🐎', 'rhino': '🦏', 'cobra': '🐍', 'elephant': '🐘', 'cheetah': '🐆'
    },
    'symbol': ['⚡', '🔥', '🌪', '🌌', '🌀', '💎', '🌟', '🌈', '🚀', '✨', '⚔️', '🏹']
}


def animate_text(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def display_welcome_animation():
    print(f"{Fore.MAGENTA}{'⚽':^80}")
    print(f"{Fore.YELLOW}{'🚀 WELCOME TO THE ULTIMATE FOOTBALL CLUB NAME GENERATOR 🚀':^80}")
    print(f"{Fore.MAGENTA}{'⚽':^80}")
    time.sleep(1)
    animate_text(f"{Fore.CYAN}Let’s create a professional, powerful, and stylish football club name for you!")


def validate_input(input_str):
    return input_str.strip() != ''


def get_style_choice():
    styles = {
        '1': 'Modern',
        '2': 'Classic',
        '3': 'Mythical',
        '4': 'Futuristic'
    }
    print(f"\n{Fore.CYAN}Choose name style:")
    for key, value in styles.items():
        print(f"{Fore.YELLOW}{key}. {value}")
    while True:
        choice = input(f"{Fore.GREEN}Enter style number (1-4): ")
        if choice in styles:
            return styles[choice]
        print(f"{Fore.RED}Invalid choice. Please try again.")


def generate_name(user_inputs, style):
    # Format dasar
    formats = [
        f"{user_inputs['city']} {user_inputs['color']} {user_inputs['animal']}",
        f"{user_inputs['city']} {user_inputs['powerful_word']}",
        f"{user_inputs['color']} {user_inputs['animal']} {random.choice(SUFFIXES)}",
        f"{user_inputs['powerful_word']} {user_inputs['city']} {random.choice(SUFFIXES)}",
        f"{user_inputs['animal']} {user_inputs['powerful_word']} FC"
    ]

    # Penyesuaian gaya
    if style == 'Classic':
        base = random.choice(formats[:2])
        return f"{base} {random.choice(['FC', 'United', 'City'])}"
    elif style == 'Modern':
        return f"{user_inputs['city']} {random.choice(['Ultra', 'Prime', 'Nova'])} {user_inputs['powerful_word']}"
    elif style == 'Mythical':
        return f"{random.choice(['Ancient', 'Royal', 'Celestial'])} {user_inputs['animal']} {random.choice(SUFFIXES)}"
    elif style == 'Futuristic':
        return f"{user_inputs['powerful_word']} {random.choice(['Cyber', 'Neon', 'Quantum'])} {random.choice(SUFFIXES)}"

    return random.choice(formats)


def add_emojis(name, animal):
    for key, emoji in EMOJIS['animal'].items():
        if key in animal.lower():
            return f"{emoji} {name} {emoji}"
    return f"{random.choice(EMOJIS['symbol'])} {name} {random.choice(EMOJIS['symbol'])}"


def main():
    # Animasi pembuka
    display_welcome_animation()

    # Input pengguna dengan validasi
    user_inputs = {}
    while True:
        user_inputs['city'] = input(f"\n{Fore.CYAN}🏠 Enter city name: {Style.RESET_ALL}")
        if validate_input(user_inputs['city']): break

    while True:
        user_inputs['color'] = input(f"{Fore.BLUE}🎨 Enter primary color: {Style.RESET_ALL}")
        if validate_input(user_inputs['color']): break

    while True:
        user_inputs['animal'] = input(f"{Fore.GREEN}🐅 Enter mascot (animal/symbol): {Style.RESET_ALL}")
        if validate_input(user_inputs['animal']): break

    while True:
        user_inputs['powerful_word'] = input(f"{Fore.RED}💥 Enter powerful word: {Style.RESET_ALL}")
        if validate_input(user_inputs['powerful_word']): break

    # Pemilihan gaya
    style = get_style_choice()

    # Generasi nama
    print(f"\n{Fore.MAGENTA}🌀 Generating Football Club names...")
    time.sleep(1)

    names = []
    while len(names) < 5:
        new_name = generate_name(user_inputs, style)
        styled_name = add_emojis(new_name, user_inputs['animal'])
        if styled_name not in names:
            names.append(styled_name)

    # Menampilkan hasil dengan animasi
    print(f"\n{Fore.GREEN}✨ Top 5 Professional Club Names ✨")
    for i, name in enumerate(names, 1):
        time.sleep(0.5)
        print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{name}")

    # Fitur tambahan: Simpan favorit
    favorites = []
    choice = input(f"\n{Fore.CYAN}💾 Save any names to favorites? (y/n): ").lower()
    if choice == 'y':
        while True:
            try:
                nums = input("Enter numbers to save (e.g., 1 3 5): ").split()
                favorites = [names[int(n) - 1] for n in nums if 1 <= int(n) <= len(names)]
                break
            except (ValueError, IndexError):
                print(f"{Fore.RED}Invalid input. Please try again.")

    # Penutup
    print(f"\n{Fore.MAGENTA}🎉 Generation complete!")
    if favorites:
        print(f"{Fore.CYAN}⭐ Your favorite Football Club Names: {', '.join(favorites)}")
    print(f"{Fore.YELLOW}⚽ Thank you for using Football Club Name Generator! ⚽")


if __name__ == "__main__":
    main()
