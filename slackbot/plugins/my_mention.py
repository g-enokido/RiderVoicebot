from slackbot.bot import respond_to
# from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random
from zikudriver import rider_time
from RiderDriver.ooo import OOO


@respond_to('変身！')
def random_Driver(message):
    rider = random.choice([2010, 2013, 2015, 2016, 2017, 2018])
    change = ''
    if rider == 2010:
        change = OOO()
    elif rider == 2013:
        change = open('./RiderDriver/Gaim.txt', encoding="utf-8").readlines()
        change = random.choice(change)
    elif rider == 2015:
        change = open('./RiderDriver/Ghost.txt', encoding="utf-8").readlines()
        change = random.choice(change)
    elif rider == 2016:
        change = open('./RiderDriver/Exaid.txt', encoding="utf-8").readlines()
        change = random.choice(change)
    elif rider == 2017:
        change = open('./RiderDriver/Build.txt', encoding="utf-8").readlines()
        change = random.choice(change)
    elif rider == 2018:
        change = rider_time

    message.reply(change)


@respond_to('アナザータイム！')
def another_time(message):
    name = ['君が', 'あなたが', 'お前が']
    reply_message = ''
    riders = ['クウガ', 'アギト', '龍騎', 'ファイズ', '剣',
              '響鬼', 'カブト', '電王', 'キバ', 'ディケイド',
              'W', 'オーズ', 'フォーゼ', 'ウィザード', '鎧武',
              'ゴースト', 'エグゼイド', 'ビルド', 'ジオウ', 'ジオウII',
              'シノビ', 'クイズ', 'キカイ', 'ゼロワン', '1号']
    your = random.choice(name)
    if your == '君が' or your == 'あなたが':
        reply_message += 'おめでとう。'

    rider = '仮面ライダー' + random.choice(riders)
    reply_message += '歴史が変わって、今日から' + your + rider
    if your == 'あなたが':
        reply_message += 'よ'
    else:
        reply_message += 'だ'
    message.reply(reply_message)


@default_reply()
def default_func(message):
    global count
    count += 1
    message.reply('%d 回目のデフォルトの返事です。' % count)
