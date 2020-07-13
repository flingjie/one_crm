# from django.shortcuts import render
from .bot_helper import bot


async def get_bot_response(text):
    return bot.get_response(text)
