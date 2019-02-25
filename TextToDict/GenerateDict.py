import urllib.request


class GenerateDict:
    def __init__(self, url, is_online):
        self.url = url
        self.dice_word = {}
        self.is_online = is_online
        self.file_or_url()

    def file_or_url(self):
        if self.is_online:
            self.text_url_to_dict()
        elif self.is_online is False:
            self.text_file_to_dict()

    def text_file_to_dict(self):
        with open(self.url, "r") as file:
            data = file.read().split()
            self.dice_word = {data[i]: data[i + 1] for i in range(0, len(data), 2)}

    def text_url_to_dict(self):
        response = urllib.request.urlopen(self.url)
        data = response.read().decode('utf-8').split()
        self.dice_word = {data[i]: data[i + 1] for i in range(0, len(data), 2)}
