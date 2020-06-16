"""
Sample Parrot Bot

This bot responds to any message by repeated what was said to it.

See ./all-config.py for all config available
"""
__name__ = 'localConfig'
__package__ = 'ringcentral_bot_framework'

import copy
import time

def botJoinPrivateChatAction(bot, groupId, user, dbAction):
  """
  This is invoked when the bot is added to a private group. 
  """
  bot.sendMessage(
    groupId,
    {
      'text': f'Hello, I am a BOT Poly, I will repeat your message as requested. Please reply "![:Person]({bot.id}) the-message-you-want-me-to-say" if you want me to say anything.'
    }
  )

def botGotPostAddAction(
  bot,
  groupId,
  creatorId,
  user,
  text,
  dbAction,
  handledByExtension,
  event
):
  """
  This is invoked when the user sends a message to the bot.
  """
  st = f'![:Person]({bot.id}) '
  if not st in text or handledByExtension:
    return
  ntxt = text.replace(st, '', 1)
  if f'![:Person]({bot.id})' in text:
    bot.sendMessage(
      groupId,
      {
        'text': ntxt
      }
    )

