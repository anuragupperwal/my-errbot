import logging
import token

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r'/Users/anurag/Documents/Coding/errbot/data'
BOT_EXTRA_PLUGIN_DIR = r'/Users/anurag/Documents/Coding/errbot/plugins'
BOT_IDENTITY = { 'token': 'xoxb-976506867619-1044986979235-G04bE4pOqxB0dlo3o281aU5W'}
BOT_LOG_FILE = r'/Users/anurag/Documents/Coding/errbot/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@CHANGE_ME', )  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!