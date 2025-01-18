import telebot
import os
from telebot import types

API_TOKEN = "7347901122:AAGPo8b_ur82gRxYfTBjf3JP1tWgTYAFkpU"
bot = telebot.TeleBot(API_TOKEN)

user = {}
course = {"spring": ["ccna","mcsa","python for beginner","photoshop"],
          "summer":["ccna","mcsa","python for beginner","python for advanced"],
          "autumn":["icdl","seller"],
          "winter":["photoshop","c"]}

@bot.message_handler(commands=["start"])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,input_field_placeholder="place celect one of our options")
    markup.add(
        types.KeyboardButton("Courses"),
        types.KeyboardButton("home"),
        types.KeyboardButton("call with ac"),
    )
    user = {}
    bot.send_message(message.chat.id,"select one our options",reply_markup=markup)#

def see_course_season(message):
    
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,input_field_placeholder="place celect one season",row_width=4)
    markup.add(types.KeyboardButton("spring"),
        types.KeyboardButton("summer"),
        types.KeyboardButton("autumn"),
        types.KeyboardButton("winter")
        
    )
    bot.reply_to(message,"selecte option",reply_markup=markup)


def call_with_ac(message):
    bot.reply_to(message,"for call to ac give this nummber 09123456789")

def home(message):
    bot.reply_to(message,"place celect one of our options")

def spring_courses(message):
    markup = types.InlineKeyboardMarkup()
    for cr in course["spring"]:
        markup.add(types.InlineKeyboardButton(cr , callback_data=cr))
    bot.send_message(message.chat.id,"for register course click on it",reply_markup=markup)#

def summer_courses(message):
    markup = types.InlineKeyboardMarkup()
    for cr in course["summer"]:
        markup.add(types.InlineKeyboardButton(cr , callback_data=cr))
    bot.send_message(message.chat.id,"for register course click on it",reply_markup=markup)#

def autumn_courses(message):
    markup = types.InlineKeyboardMarkup()
    for cr in course["autumn"]:
        markup.add(types.InlineKeyboardButton(cr , callback_data=cr))
    bot.send_message(message.chat.id,"for register course click on it",reply_markup=markup)#

def winter_courses(message):
    markup = types.InlineKeyboardMarkup()
    for cr in course["winter"]:
        markup.add(types.InlineKeyboardButton(cr , callback_data=cr))
    bot.send_message(message.chat.id,"for register course click on it",reply_markup=markup)#
@bot.callback_query_handler(func=lambda call:True)
def handler_register_course(call):
    user["course"]=call.data
    message=call.message
    text="""
    place insert your name and family
    """
    bot.reply_to(message,text)
    bot.register_next_step_handler(message,insert_basic_info)#
def insert_basic_info(message):
    user["info"]=message.text
    text="""
    place insert your phone number
    """

    bot.reply_to(message,text)
    bot.register_next_step_handler(message,insert_phone_number)#
def insert_phone_number(message):
    user["phone"]=message.text
    text="""
    pre_register complete successfully
    """
    bot.reply_to(message,text)
    with open("./export/register.txt","a") as file:
        
        file.write(f"{user['season']}\n========\n{user['info']}\n===========\n{user['phone']}\n============\n{user['course']}\n===========\n" )
        start_message(message)
@bot.message_handler(func=lambda message:True)
def call_back(message):
    if message.text == "call with ac":
        call_with_ac(message)
    elif message.text == "Courses":
        see_course_season(message)
    elif message.text == "home":
        home(message)
    elif message.text == "spring":
        user["season"]=message.text
        spring_courses(message)
    elif message.text == "summer":
        user["season"]=message.text
        summer_courses(message)
    elif message.text == "autumn":
        user["season"]=message.text
        autumn_courses(message)
    elif message.text == "winter":
        user["season"]=message.text
        winter_courses(message)




bot.infinity_polling()