import discord
import time
from colorama import Fore, Style

intents = discord.Intents.default()
intents.members = True  
bot = discord.Client(intents=intents)

def colored_input(color, prompt):
    print(color + prompt + Style.RESET_ALL, end='')
    return input()

@bot.event
async def on_ready():
    print(Fore.LIGHTBLUE_EX + f'Connecté en tant que {bot.user}!' + Style.RESET_ALL)
    await start_interaction()

async def start_interaction():
    server_id = int(colored_input(Fore.LIGHTBLUE_EX, "ID du serveur: "))
    message_content = colored_input(Fore.LIGHTBLUE_EX, "Entre le message à envoyer à tout le monde: ")
    await dm_all(server_id, message_content)

async def dm_all(server_id, message_content):
    guild = bot.get_guild(server_id)
    if guild:
        members_sent = 0
        members_fail = 0
        start_time_total = time.time()
        for member in guild.members:
            if not member.bot:
                try:
                    await member.send(message_content)
                    print(Fore.LIGHTBLUE_EX + f"Message envoyé à {member.name} ({member.id})" + Style.RESET_ALL)
                    members_sent += 1
                except Exception as e:
                    print(Fore.RED + f"Impossible d'envoyer le message à  {member.name}: {e}" + Style.RESET_ALL)
                    members_fail += 1
        end_time_total = time.time()
        print(Fore.BLUE + f"DM All - {members_sent} mmessages envoyés, {members_fail} messages non envoyés - Temps total pour l'envoie: {end_time_total - start_time_total:.2f} seconds" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Discord introuvable." + Style.RESET_ALL)

if __name__ == "__main__":
    bot_token = colored_input(Fore.CYAN, "Token du bot: ")
    bot.run(bot_token)
