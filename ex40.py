class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They ralley around tha family",
                        "With pockets full of shells",
                        "It's not very likely",
                        "That I will go to local prison cells"])
                        
double_boost_old_dead_meme = Song(["Together we can show the world what we can do",
                                   "You are next to me and I'm next to you",
                                   "Push me on through until the battle's won!",
                                   "No one's gonna give a thing to us",
                                   "Into each other we put our trust",
                                   "Standing united",
                                   "After the meme is dead!!!"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

double_boost_old_dead_meme.sing_me_a_song()
