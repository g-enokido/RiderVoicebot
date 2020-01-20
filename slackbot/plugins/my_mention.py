from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply


@respond_to('ウンババウバッホラオラオハー')
def mention_func(message):
    message.reply('アーッハッハ！私の勝ちだ！')


@listen_to('ウンババウバッホラオラオハー')
def listen_func(message):
    message.send('ダンダンズガンダン！僕ら遮二無二進化中！')
    message.reply('ウンババウバッホラオラオハー')


@default_reply()
def default_func(message):
    global count
    count += 1
    message.reply('%d 回目のデフォルトの返事です。' % count)
