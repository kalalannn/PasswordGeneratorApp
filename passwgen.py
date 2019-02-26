import random
LOWCASE = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE = LOWCASE.upper()
NUMERIC = '0123456789'
SEPR = '_-'
class Password(object):
    label = ''
    def __init__(self, count=8, upperCase=False, numeric=False, sepr=False):
        self.count = count
        self.upperCase = upperCase
        self.numeric = numeric
        self.sepr = sepr

    def gen_passwd(self):
        gen = LOWCASE
        if self.upperCase:
            gen += UPPERCASE
        if self.numeric:
            gen += NUMERIC
        if self.sepr:
            gen += SEPR
        gen = list(gen)
        random.shuffle(gen)
        return  ''.join([random.choice(gen) for x in range(self.count)])
