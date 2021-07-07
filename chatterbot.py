from chatterbot import ChatBot

chatbot = ChatBot('My Chatbot')
# Train the chatbot with a few responses
from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings")