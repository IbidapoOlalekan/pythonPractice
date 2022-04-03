from functions import *

# create chatbot

bot = create_bot("Alexa")

# train all data
train_all_data(bot)

# train chatbot with your custom data

house_owner = [
    "Who is the owner of the house?",
    "Olumide Ibidapo"
]

my_name = [
    "What is my Name?",
    "Ibidapo Olalekan"
]

custom_train(bot, house_owner)
custom_train(bot, my_name)

# start chatbot
start_chatbot(bot)
