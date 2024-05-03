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
    print(Fore.LIGHTBLUE_EX + f'Logged in as {bot.user}!' + Style.RESET_ALL)
    await start_interaction()

async def start_interaction():
    server_id = int(colored_input(Fore.LIGHTBLUE_EX, "serveur ID: "))
    message_content = colored_input(Fore.LIGHTBLUE_EX, "entré le message a envoyer a tout le monde: ")
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
                    print(Fore.LIGHTBLUE_EX + f"Message Sent to {member.name} ({member.id})" + Style.RESET_ALL)
                    members_sent += 1
                except Exception as e:
                    print(Fore.RED + f"Can't send message to {member.name}: {e}" + Style.RESET_ALL)
                    members_fail += 1
        end_time_total = time.time()
        print(Fore.BLUE + f"DM All - {members_sent} messages sent, {members_fail} messages failed - Total Time taken: {end_time_total - start_time_total:.2f} seconds" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Guild not found." + Style.RESET_ALL)

if __name__ == "__main__":
    bot_token = colored_input(Fore.CYAN, "Entré le token du bot: ")
    bot.run(bot_token)
