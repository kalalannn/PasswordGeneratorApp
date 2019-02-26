import random
LOWCASE = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE = LOWCASE.upper()
NUMERIC = '0123456789'
SEPR = '_-'
class Password(object):
    label = ''
    def __init__(self, count=8, uppercase=False, numeric=False, sepr=False):
        self.count = count
        self.uppercase = uppercase
        self.numeric = numeric
        self.sepr = sepr

    def generate_password(self):
        gen = LOWCASE
        if self.uppercase:
            gen += UPPERCASE
        if self.numeric:
            gen += NUMERIC
        if self.sepr:
            gen += SEPR
        gen = list(gen)
        random.shuffle(gen)
        self.label =  ''.join([random.choice(gen) for x in range(self.count)])
