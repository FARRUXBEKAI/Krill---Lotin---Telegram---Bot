#!/usr/bin/env python
# coding: utf-8

# # 09/09/2022
# 
# # Python asoslari
# 
# # Kril - lotin Telegram bot yaratish
# 
# # Muallif: Farrux Sotivoldiyev

# In[1]:


from transliterate import to_cyrillic,to_latin
import telebot

TOKEN = "5318382053:AAF8InhIF1Vp9hQkgLbNbnGnCmTm_tjT7Zw"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    ism = "Farruxbek"
    javob = f"Assalomu alaykum krill-lotin botiga xush kelibsiz.\nMatn kiriting: "
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    savol = message.text
    javob = to_cyrillic(savol) if savol.isascii() else to_latin(savol) 
    bot.reply_to(message, javob)   

bot.infinity_polling()


# In[ ]:




