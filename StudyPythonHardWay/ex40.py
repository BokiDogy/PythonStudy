class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for l in self.lyrics:
            print(l)


happy_bday = Song(["Happy birthday to you",
                   "I don't wang to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song({"s":"They rally around tha family",
                        "y":"With pockets full of shells"})

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
