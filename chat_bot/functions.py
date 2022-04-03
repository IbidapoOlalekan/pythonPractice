def create_bot(name):
    from chatterbot import ChatBot
    Bot = ChatBot(name=name,
                  read_only=False,
                  logic_adapters=["chatterbot.logic.BestMatch"],
                  storage_adapter="chatterbot.storage.SQLStorageAdapter")
    return Bot


# function to train the bot with a variety of topics
# language chosen is English
# todo bot would be trained with other languages also

def train_all_data(Bot):
    from chatterbot.trainers import ChatterBotCorpusTrainer
    corpus_trainer = ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")


# function to train the bot with custom data
# it uses ListTrainer to train data from lists

def custom_train(Bot, conversation):
    from chatterbot.trainers import ListTrainer
    trainer = ListTrainer(Bot)
    trainer.train(conversation)


# function to start and take responses from the chatbot
# the chatbot stays running unless a word is typed from the bye_lists

def start_chatbot(Bot):
    print('\033c')
