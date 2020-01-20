from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random


@listen_to('ライダータイム！')
def rider_time(messsage):
    rider_name_list = ['ジオウ', 'ゲイツ', 'ツクヨミ', 'バールクス', 'ザモナス', 'ゾンジス']
    rider_name = random.choice(rider_name_list)
    reply_name = 'ライダータイム！'

    if rider_name == 'ツクヨミ':
        reply_name += '仮面ライダーツクヨミ、ツ・ク・ヨ・ミ！'
    elif rider_name == 'ゲイツ':
        reply_name += '仮面ライダーゲイツ！'
        form = random.choice(['n', 'rg', 'rs'])

        if form == 'rs':
            reply_name += 'リバイリバイリバイ！リバイリバイリバイ！リバイブ疾風！疾風！'
        elif form == 'rg':
            reply_name += 'リ・バ・イ・ブ剛烈！'
    elif rider_name == 'ジオウ':
        form = random.choice(['n', 'II', 'tri', 'grand', 'king', 'ohma'])
        if form == 'ohma':
            reply_name = '最高！最善！最大！最強王！オーマジオウ！'
        elif form == 'king':
            reply_name = 'キングタイム！仮面ライダージオウ！オーマ！'
        elif form == 'II':
            reply_name += '仮面ライダー！ライダー！ジオウ！ジオウ！ジオウ！II!'
        else:
            reply_name += '仮面ライダー！ジオウ！'
            if form == 'tri':
                reply_name += 'トリニティタイム！3つの力！仮面ライダージオウ！ゲイツ！ウォズ！トリニティ！トリニティ！'
            elif form == 'grand':
                reply_name += 'グランドタイム！クウガアギト龍騎ファイズブレイド！'
                reply_name += '響鬼カブト電王キバディケイド！'
                reply_name += 'ダブル・オーズフォーゼ・ウィザード鎧武ドライブ！ゴースト！エグゼイド！ビルド！祝え！仮面ライダーグランド！ジオウ！'
    else:
        reply_name = '仮面ライダー！' + rider_name + '!'
    messsage.reply(reply_name)


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
