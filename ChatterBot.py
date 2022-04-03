from chatterbot import Chatbot

Bot = Chatbot(name='calculator',
              read_only=True,
              logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
              storage_adapter="chatterbot.storage.SQLStorageAdapter")

# clear the screen and start the calculator
print('\033c')
print('Hello! I am a calculator. How can i help you')
while True:
    user_input = input('me: ')

    if user_input.lower() == 'quit':
        print("Exiting")
        break
