import requests
from telegram.ext import Updater, CommandHandler

def short_url(bot, update, args):
  # get the long URL from the user's message
  long_url = args[0]

  # use the shorturllink.in API to shorten the URL
  api_key = "fff6414a990cb0295f487d3a5f1d1651864c1bf6"
  response = requests.post(f"https://shorturllink.in/api/v1/shorten?api={api_key}&url={long_url}")
  short_url = response.json()["short_url"]

  # send the shortened URL back to the user
  update.message.reply_text(short_url)

def main():
  # create the bot and attach the /shorten command
  updater = Updater("5851423202:AAFTfgPEwlnqumitPvPlhiKkEneGj2F1xxA")
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("shorten", short_url, pass_args=True))

  # start the bot
  updater.start_polling()
  updater.idle()

if __name__ == '__main__':
  main()
