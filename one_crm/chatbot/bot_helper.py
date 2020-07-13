# -*- encoding: utf-8 -*-
"""
@File    :   bot.py
@Time    :   2020/07/13 20:53:48
@Author  :   Fan Lingjie
@Version :   1.0
@Contact :   fanlingjie@laiye.com
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def get_bot():
    chatbot = ChatBot("Bot")
    trainer = ChatterBotCorpusTrainer(chatbot)
    # 使用中文语料库训练它
    trainer.train("chatterbot.corpus.chinese")
    return chatbot


bot = get_bot()


if __name__ == "__main__":
    print(bot.get_response("你好"))
