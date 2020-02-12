import random


def OOO():
    medal = {
        'head': ['タカ', 'クワガタ', 'ライオン', 'サイ', 'シャチ', 'プテラ', 'コブラ'],
        'body': ['クジャク', 'カマキリ', 'トラ', 'ゴリラ', 'ウナギ', 'カメ'],
        'leg': ['コンドル', 'バッタ', 'チーター', 'ゾウ', 'タコ', 'ワニ'],
    }

    form = random.choice(medal['head']) + '！'
    if form == 'プテラ！':
        return 'プテラ！トリケラ！ティラノ！プトティラノザウルース！'
    else:
        form += random.choice(medal['body']) + '！'
        form += random.choice(medal['leg']) + '！'

    if form == 'タカ！トラ！バッタ！':
        form += 'タ!ト!バ！タトバ！タトバ！'
    elif form == 'クワガタ':
        form += 'ガータガキリバ！ガタキリバ！'
    elif form == 'ライオン！トラ！チーター！':
        form += 'ラタラタ！ラトラーター！'
    elif form == 'サイ！ゴリラ！ゾウ！':
        form += 'サゴーゾ……サゴーゾ！'
    elif form == 'シャチ！ウナギ！タコ！':
        form += 'シャシャシャウタ！シャシャシャウタ！'
    elif form == 'タカ！クジャク！コンドル！':
        form += 'タ～ジャドル～ドル～！'
    elif form == 'コブラ！カメ！ワニ！':
        form += 'ブラカ～ワニ！'

    return form
