from random import choice
import string

# Standard Caesar Cipher: Maps commonly used characters to Chinese counterparts.

charset1 = [i for i in string.ascii_uppercase] + [i for i in string.ascii_lowercase] + list(map(str, range(10))) + "` ~ ! @ # $ % ^ & * ( ) - = _ + [ ] \\ { } | ; ' \" , . / < > ?".split()
# Set of commonly used English characters.

charset2 = ['安', '被', '产', '豆', '意', '方', '高', '河', '你', '种', '康','里', '满', '脑', '哦', '苹', '清', '认', '所', '她', '吴', '万', '网', '星', '用', '咋', '啊', '把', '从', '到', '饿', '发', '个', '好', '以', '中', '开', '力', '买', '内', '我', '平', '区', '人', '送', '他', '无', '完', '王', '行', '勇', '早', '十', '一', '二', '三', '四', '五', '六', '七', '八', '九'] + "` ~ ！ @ # $ % ^ & * （ ） - = _ + 【 】 \\ ｛ ｝ | ； ’ “ ， 。 / < > ？".split()
# Set of Chinese characters that share a common index with their English counterparts.

cs2_spaces = ['和', '那', '这', '啥', '咋', '些', '的', '得', '地']
# Multiple characters are used as a substitute for space because of " " occurs too frequently in text.

def encode(inpt):
    out = []
    for i in inpt:
        if i == " ":
            out.append(choice(cs2_spaces))
        else:
            out.append(charset2[charset1.index(i)])
    return "".join(out)

def decode(inpt):
    out = []
    for i in inpt:
        if i in cs2_spaces:
            out.append(" ")
        else:
            out.append(charset1[charset2.index(i)])
    return "".join(out)
