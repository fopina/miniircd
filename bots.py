from irc.bot import SingleServerIRCBot
import threading


def join(c, e):
    c.join('#test')


def newbot(nick):
    c = SingleServerIRCBot([('localhost', 6667)], nick, nick)
    c.connection.add_global_handler('endofmotd', join)
    c.start()


for i in xrange(100):
    threading.Thread(target=newbot, args=('botbotbotbotbotbot%d' % i,)).start()
