import os
from EffWordList import WordList


class LongWordList(WordList.WordList):

    def __init__(self, is_online, dice):
        super().__init__(is_online, dice)
        self.eff_long_word_list_url = 'https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt'
        self.eff_long_word_list_path = os.path.join(self.dir_path, "offline/eff_large_wordlist.txt")
        self.online_or_offline()
