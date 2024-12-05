import random


DECODER_LINK = "https://skalkuluj.pl/rot47-koder-dekoder-online"
TEMPLATE_FOR_SANTA_ROW = """
wyslij do {sender_number} wiadomosc:
\t{reciever_desire} dla {reciever_name}
"""

class Person:
    def __init__(self, name, desire, number):
        self.name = name
        self.desire = desire
        self.number = number


DETAILS = [ # YOU FILL THIS ONLY
    Person("alutka", "maszyna", "+alutka nr"),
    Person("michal", "komputer", "+michal nr"),
    Person("cezar", "mysz", "+cezar nr"),
    Person("tosia", "kosc", "+tosia nr"),
]

def rot47(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)


def gen_message_to_santa():
    context = ""
    l = list(range(len(DETAILS)))
    random.shuffle(l)

    for cur_i, next_i in zip(l, l[1:] + l[:1]):
        context += TEMPLATE_FOR_SANTA_ROW.format(
            sender_number=DETAILS[cur_i].number,
            reciever_desire=DETAILS[next_i].desire,
            reciever_name=DETAILS[next_i].name,
        )
    return DECODER_LINK + '\n\n' + rot47(context)

if __name__ == "__main__":
    print(gen_message_to_santa())


