import os
from EffWordList import WordList


class ShortWordList1(WordList.WordList):
    def __init__(self, is_online, dice):
        super().__init__(is_online, dice)
        self.eff_long_word_list_url = 'https://www.eff.org/files/2016/09/08/eff_short_wordlist_1.txt'
        self.eff_long_word_list_path = os.path.join(self.dir_path, "offline/eff_short_wordlist_1.txt")
        self.online_or_offline()
