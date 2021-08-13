#!/usr/bin/python3

import sys
import os
import telebot
from utils import *
from covid import Covid
from math import floor

def getConfig(name: str):
    return os.environ[name]

# setup bot
bot = telebot.TeleBot(api_token)

# connect db
connection, curs = connectdb()

# create table in postgress if does not exist
create_table(connection, curs)


# get sudo users list
sudo_users = set()
if os.path.exists('sudo_users.txt'):
    with open('sudo_users.txt', 'r+') as f:
        lines = f.readlines()
        for line in lines:
            sudo_users.add(int(line.split()[0]))

# add owner to sudo user
sudo_users.add(owner_id)

# get authorized chats list local
authorized_chats_local = set()
if os.path.exists('authorized_chats.txt'):
    with open('authorized_chats.txt', 'r+') as f:
        lines = f.readlines()
        for line in lines:
            authorized_chats_local.add(int(line.split()[0]))


# get authorized chats from db
db_ids = list()


def get_chat_from_db():
    global db_ids
    curs.execute("SELECT id from ids")
    db_idsss = curs.fetchall()
    for row in db_idsss:
        var = int(row[0])
        db_ids.append(var)
    db_ids = set(db_ids)

get_chat_from_db()


# put all chats in authrized chats
authorized_chats = db_ids.union(authorized_chats_local)
authorized_chats = sudo_users.union(authorized_chats)


def adminfilter(message):
    return bool(message.chat.id in authorized_chats)


def sudoersfilter(message):
    return bool(message.from_user.id in sudo_users)


def updateAuthChatsCounter():
    global authorized_chats
    l1 = len(authorized_chats)
    return (l1)


def updateAuthChatsList():
    global authorized_chats
    global db_ids
    authorized_chats = set()
    db_ids = list()
    get_chat_from_db()
    authorized_chats = db_ids.union(authorized_chats_local)
    authorized_chats = sudo_users.union(authorized_chats)
    update_ids = list(authorized_chats)
    return (update_ids)


def doesExistDB(message):
    ex_db_ids = list(authorized_chats)
    return bool(message.chat.id in ex_db_ids)


def delAuthChat(auth_del):
    curs.execute("DELETE from IDS where ID=(%s)", [auth_del])
    connection.commit()


@bot.message_handler(commands=['start'])
def send_message(message):
    if adminfilter(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, """\
Hello, there! This bot can get you COVID update for Bangladesh.\nSee /help for command usage.\
    """, parse_mode='Markdown')
    else:
        pass


@bot.message_handler(commands=['help'])
def send_message_ex(message):
    if adminfilter(message) or doesExistDB(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, """\
*To get covid update for Bangladesh, send a message like this:*\n`/update`\
    """, parse_mode='Markdown')
    else:
        pass


@bot.message_handler(commands=['auth'])
def send_message_auth(message):
    if sudoersfilter(message):
        chat_id = message.chat
        if (message.reply_to_message == None):
            authID = message.text
            if authID[:6] == '/auth@':
                authID = authID[18:]
            else:
                authID = authID[6:]
            if (authID == ""):
                authID = message.chat.id
        else:
            authID = message.reply_to_message.from_user.id
        db_ids = list(authorized_chats)
        if int(authID) not in db_ids:
            curs.execute("INSERT INTO IDS (ID) VALUES (%s)", [authID])
            connection.commit()
            UserN = bot.get_chat(authID)
            if (UserN.username == None):
                displayName = "Supergroup " + UserN.title
            else:
                displayName = "["+"@" + str(UserN.username) + "](tg://user?id=" + \
                    str(authID)+")"
            show_ID = displayName + " added to authorized chats"
            bot.reply_to(message, show_ID, parse_mode='Markdown')
            updateAuthChatsList()
        else:
            show_ID = "Chat already authorized"
            bot.reply_to(message, show_ID, parse_mode='Markdown')
    else:
        pass


@ bot.message_handler(commands=['authlist'])
def send_message_authList(message):
    if sudoersfilter(message):
        chat_id = message.chat.id
        authLID = message.text
        if authLID[:10] == '/authlist@':
            authLID = authLID[22:]
        else:
            authLID = authLID[10:]
        send_auth_ = "Authorized Chats\n\n"
        global authorized_chats
        DB_listt = authorized_chats
        for id in DB_listt:
            UserN = bot.get_chat(id)
            if (UserN.username == None):
                displayName = UserN.title
            else:
                displayName = UserN.username
            send_auth_ = send_auth_ + "["+"@" + str(displayName) + "](tg://user?id=" + \
                str(id)+")" + " : " + "`"+str(id)+"`" + "\n"
        bot.send_message(chat_id, send_auth_, parse_mode='Markdown')
    else:
        pass


@ bot.message_handler(commands=['authdel'])
def send_message_authDel(message):
    if sudoersfilter(message):
        chat_id = message.chat.id
        authDID = message.text
        if authDID[:9] == '/authdel@':
            authDID = authDID[21:]
        else:
            authDID = authDID[9:]
        delAuthChat(authDID)
       # print(type(Au))
        send_authD_ = "User " + "["+str(authDID)+"](tg://user?id=" + \
            str(authDID)+")" + " deleted\n"
        bot.send_message(chat_id, send_authD_, parse_mode='Markdown')
        updateAuthChatsList()
    else:
        pass


@ bot.message_handler(commands=['stats'])
def send_message_stats(message):
    if sudoersfilter(message):
        chat_id = message.chat.id
        authID = message.text
        if authID[:7] == '/stats@':
            authID = authID[19:]
        else:
            authID = authID[7:]
        authcou = updateAuthChatsCounter()
        stats_msg = "System: " + sys.platform + "\nPython version: " + \
            sys.version[:5] + "\nAuthorized Chats: " + str(authcou)
        bot.send_message(chat_id, stats_msg, parse_mode='Markdown')
    else:
        pass


@ bot.message_handler(commands=['update'])

def echo_message(message):
    if adminfilter(message) or doesExistDB(message):
        covid_ = Covid("worldometers")
        data = covid_.get_status_by_country_name("Bangladesh")
        result = ""
        result += f"Covid Status for *{data['country']}*\n\n"
        result += f"*New Cases* : `{data['new_cases']}`\n"
        result += f"*New Deaths* : `{data['new_deaths']}`\n\n"
        result += f"**Critical** : `{data['critical']}`\n"
        result += f"**Active** : `{data['active']}`\n"
        result += f"**Confirmed** : `{data['confirmed']}`\n"
        result += f"**Deaths** : `{data['deaths']}`\n"
        result += f"**Recovered** : `{data['recovered']}`\n\n"
        result += f"**Total Tests** : `{data['total_tests']}`\n"
        po = data['population']
        tt = data['total_tests']
        ttpm = ( tt/po ) * 1000000
        ttpm = floor(ttpm)
        result += f"**Total Tests Per Million** : `{ttpm}`\n"
        result += f"**Total Cases Per Million** : `{data['total_cases_per_million']}`\n"
        result += (
            f"**Total deaths per million** : `{data['total_deaths_per_million']}`\n"
        )
        result += f"**Population** : `{data['population']}`\n"
        bot.reply_to(message, result, parse_mode='Markdown')
    else:
        pass


bot.polling(print("Bot started..."))