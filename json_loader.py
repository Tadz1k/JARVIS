import json


class JsonLoader:
    def __init__(self):
        self.topics = self.load_topics()
        self.greetings = self.load_greetings()
        self.main_directory = {}
        self.loaded_json = {}

    def load_topics(self):
        with open('known_topics/topics.json', encoding='utf8') as json_file:
            self.loaded_json = json.load(json_file)
        return self.loaded_json

    def load_greetings(self):
        with open('known_topics/greetings.json', encoding='utf8') as json_file:
            self.loaded_json = json.load(json_file)
        return self.loaded_json

    def load_functions(self):
        with open('known_topics/functions.json', encoding='utf8') as json_file:
            self.loaded_json = json.load(json_file)
        return self.loaded_json

    def load_dialogs(self):
        with open('known_topics/dialog.json', encoding='utf8') as json_file:
            self.loaded_json = json.load(json_file)
        return self.loaded_json

    #DODATKOWE SLOWNIKI
    def load_introduces(self):
        with open('known_topics/introduces.json', encoding='utf8') as json_file:
            self.loaded_json = json.load(json_file)
        return self.loaded_json

    def reload_main(self):
        self.main_directory = {"topics": self.load_topics(),
                               "greetings": self.load_greetings(),
                               "functions": self.load_functions(),
                               "introduces": self.load_introduces(),
                               "dialog": self.load_dialogs()
                               }
        print("Przeładowano słowniki")
        return self.main_directory
