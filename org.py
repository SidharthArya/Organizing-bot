import datetime
import json
import subprocess

from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext, PollAnswerHandler, PollHandler
import pickle

updater = Updater(token='1681500274:AAFcyNowy0v-e4RiowAS0_3sfCd5NC1enyA', use_context=True)

dispatcher = updater.dispatcher

def notify(title, body):
    Notification = Gio.Notification.new(title)
    Notification.set_body(body)
    Icon = Gio.ThemedIcon.new("dialog-information")
    Notification.set_icon(Icon)
    Application.send_notification(None, Notification)
    
try:
    import gi
    from gi.repository import Gio
    Application = Gio.Application.new("organizer.personal", Gio.ApplicationFlags.FLAGS_NONE)
    Application.register()
except:
    pass

with open("/home/arya/Documents/Org/Bots/Telegram/org", "rb") as f:
    variables = pickle.load(f)


def save_variables():
    with open("/home/arya/Documents/Org/Bots/Telegram/org", "wb") as f:
        pickle.dump(variables, f)

exercises = [x[:100] for x in subprocess.check_output(["/home/arya/.emacs.d/scripts/exercises"]).decode('utf-8').strip("()").strip().split("TODO ")[1:]]
if len(exercises) == 1:
    exercises = [exercises[0], exercises[0]]
notify("Exercises", str(exercises))
polls = int(len(exercises)/10)
for i in range(polls):
    dispatcher.bot.send_poll(chat_id=variables["Allowed"][0], question="Exercises", options=exercises[i*10:i*10+10], allows_multiple_answers=True)
print(exercises[polls*10:])
dispatcher.bot.send_poll(chat_id=variables["Allowed"][0], question="Exercises", options=exercises[polls*10:], allows_multiple_answers=True)

habit = [x[:100] for x in subprocess.check_output(["/home/arya/.emacs.d/scripts/habit"]).decode('utf-8').strip("()").strip().split("TODO ")][1:]
if len(habit) == 1:
    habit = [habit[0], habit[0]]
notify("Habit", str(habit))
polls = int(len(habit)/10)
for i in range(polls):
    dispatcher.bot.send_poll(chat_id=variables["Allowed"][0], question="Habit", options=habit[i*10:i*10+10], allows_multiple_answers=True)
dispatcher.bot.send_poll(chat_id=variables["Allowed"][0], question="Habit", options=habit[polls*10:], allows_multiple_answers=True)

diet = subprocess.check_output(["/home/arya/.emacs.d/scripts/diet"]).decode('utf-8').strip("()").strip().split("\n")
if len(diet) == 1:
    diet = [diet[0], diet[0]]
notify("Diet", str(diet))
polls = int(len(diet)/10)
for i in range(polls):
    dispatcher.bot.send_poll(chat_id=variables["Allowed"][0], question="Diet", options=diet[i*10:i*10+10], allows_multiple_answers=True)
dispatcher.bot.send_poll(chat_id=variables["Allowed"][0], question="Diet", options=diet[polls*10:], allows_multiple_answers=True)

scheduled = [x[:100] for x in subprocess.check_output(["/home/arya/.emacs.d/scripts/scheduled"]).decode('utf-8').strip("()").strip().split("TODO ")[1:]]
if len(scheduled) == 1:
    diet = [scheduled[0], scheduled[0]]
print(scheduled)
notify("Scheduled", str(scheduled))
polls = int(len(scheduled)/10)
for i in range(polls):
    dispatcher.bot.send_poll(chat_id=variables["Allowed"][0], question="Scheduled", options=scheduled[i*10:i*10+10], allows_multiple_answers=True)
dispatcher.bot.send_poll(chat_id=variables["Allowed"][0], question="Scheduled", options=scheduled[polls*10:], allows_multiple_answers=True)


deadline = [x[:100] for x in subprocess.check_output(["/home/arya/.emacs.d/scripts/deadline"]).decode('utf-8').strip("()").strip().split("TODO ")[1:]]
if len(deadline) == 1:
    diet = [deadline[0], deadline[0]]
print(deadline)
notify("Deadline", str(deadline))
polls = int(len(deadline)/10)
for i in range(polls):
    dispatcher.bot.send_poll(chat_id=variables["Allowed"][0], question="Deadline", options=deadline[i*10:i*10+10], allows_multiple_answers=True)
dispatcher.bot.send_poll(chat_id=variables["Allowed"][0], question="Deadline", options=deadline[polls*10:], allows_multiple_answers=True)
