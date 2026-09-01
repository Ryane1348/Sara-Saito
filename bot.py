from fbchat import Client
from fbchat.models import *
import os
import time
import random
import requests
from datetime import datetime

cookies = {
    "email": os.getenv("BOT_EMAIL"),
    "password": os.getenv("BOT_PASSWORD"),
    "c_user": os.getenv("C_USER")
}

PREFIX = "#"
START_TIME = time.time()
ADMIN_IDS = [cookies['c_user']] # انت الادمين

MENU = """━━━☠️ 𝗡𝗲𝗼𝗞𝗘𝗫 𝗔𝗜 V5 ☠️━━━

╭──『 ADMIN 』
× addadmin × deladmin × ban × unban × kick × mute × unmute × warn × promote × demote × delete × onlyadmin × broadcast
╰────────────◊

╭──『 AI 』
× ai × gpt × meta × prompt × imagine
╰────────────◊

╭──『 FUN 』
× bonk × burn × clown × gay × jail × slap × wanted × rip × punch × kiss × hug × ship × roast
╰────────────◊

╭──『 GAME 』
× coinflip × rps × 8ball × dice × ttt × truth × dare
╰────────────◊

╭──『 INFO 』
× uid × tid × ping × uptime × stats × info × botinfo × weather
╰────────────◊

╭──『 BOX CHAT 』
× gcinfo × all × setname × setavatar × rules × refresh × leave
╰────────────◊

╭──『 MEDIA 』
× meme × quote × joke × fact × song × yt × tiktok × img
╰────────────◊

╭──『 SETTINGS 』
× prefix × setlang × restart × help
╰────────────◊

➥ Use: #help for all commands
➥ Admin Only: #kick #ban #delete"""

banned_users = []
muted_users = []
admin_list = ADMIN_IDS

class NeoKexBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        if author_id == self.uid: return
        if author_id in banned_users: return

        msg = message_object.text
        if not msg or not msg.startswith(PREFIX): return

        parts = msg[len(PREFIX):].split()
        command = parts[0].lower()
        args = " ".join(parts[1:])
        is_admin = author_id in admin_list

        if command == "help":
            self.send(Message(text=MENU), thread_id=thread_id, thread_type=thread_type)
        elif command == "ping":
            ms = int((time.time() - START_TIME)*1000)
            self.send(Message(text=f"Pong! {ms}ms ☠️"), thread_id=thread_id, thread_type=thread_type)
        else:
            self.send(Message(text=f"Command '{command}' not found. Use #help"), thread_id=thread_id, thread_type=thread_type)

bot = NeoKexBot(cookies=cookies)
print("NeoKEX AI V5 Online ☠️")
bot.listen()
