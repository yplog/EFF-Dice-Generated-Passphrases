import os
from Dice import Dice
from TextToDict import GenerateDict


class LongWordList:
    def __init__(self, is_online):
        self.eff_long_word_list_url = 'https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.eff_long_word_list_path = os.path.join(dir_path, "offline/eff_large_wordlist.txt")
        self.is_online = is_online
        self.dice = Dice.Dice(5)
        self.dice_list = ''
        self.generated_password = ''
        self.generated_password_list = ''
        self.online_or_offline()

    def online_or_offline(self):
        self.dice_list = ' '.join(self.dice.dice_list)
        if self.is_online:
            self.online()
        elif self.is_online is False:
            self.offline()

    def online(self):
        generated_dict = GenerateDict.GenerateDict(self.eff_long_word_list_url, True)
        for i in self.dice.dice_list:
            self.generated_password += generated_dict.dice_word[i]
            self.generated_password_list += generated_dict.dice_word[i] + ' '

    def offline(self):
        generated_dict = GenerateDict.GenerateDict(self.eff_long_word_list_path, False)
        for i in self.dice.dice_list:
            self.generated_password += generated_dict.dice_word[i]
            self.generated_password_list += generated_dict.dice_word[i] + ' '

    def __str__(self):
        return 'Dice Series: {0}\nPassword Words: {1} \nPassword: {2}'\
            .format(self.dice_list, self.generated_password_list, self.generated_password)
