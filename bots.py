from irc.bot import SingleServerIRCBot
import threading
import time
import string
import random


def join(c, e):
    c.join('#test')


class A(SingleServerIRCBot):
    def on_welcome(self, c, e):
        c.join('#test')

    def on_error(self, c, e):
        print('ERROR:', repr(e))


def newbot(nick):
    c = A([('127.0.0.1', 6667)], nick, nick)
    c.start()

for i in xrange(200):
    threading.Thread(target=newbot, args=('%s%d' % (
        ''.join(random.choice(string.letters) for _ in xrange(17)),
        i
    ),)).start()
    time.sleep(0.1)
