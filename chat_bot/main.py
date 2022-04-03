def create_bot(name):
    from chatterbot import ChatBot
    Bot = ChatBot(name=name,
                  read_only=False,
                  logic_adapters=["chatterbot.logic.BestMatch"],
                  storage_adapter="chatterbot.storage.SQLStorageAdapter")
    return Bot


def train_all_data(Bot):
    from chatterbot.trainers import ChatterBotCorpusTrainer
    corpus_trainer = ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")
