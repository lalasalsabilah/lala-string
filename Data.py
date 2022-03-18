from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
hallo {}
━━━━━━━━━━━━━━━━━━━━━━━━
jika kamu tidak percaya bot ini, 
1. gausah baca pesan ini
2. blokir bot atau delete chat
━━━━━━━━━━━━━━━━━━━━━━━━
bot ini membantu kamu mendapatkan
string session via bot
━━━━━━━━━━━━━━━━━━━━━━━━
managed by @lalanashirah
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ​", callback_data="generate")],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ​", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
       
      
          
            InlineKeyboardButton("ᴀʙᴏᴜᴛ​", callback_data="about")
        
        
    ]

    # Help Message
    HELP = """
 TENTANG BOT INI :

/about - tentang bot ini
/help - bantuan
/start - mulai bot
/generate - mulai generating session
/cancel - membatalkan process
/restart - process membatalkan
"""

    # About Message
    ABOUT = """
 
 bot untuk mengambil pyrogram dan telethon
  string session by @lalastringbot

CHANNEL : [join](https://t.me/mmwrld)

developer : @lalanashirah
    """
