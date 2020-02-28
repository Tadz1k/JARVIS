import functions


class Interpreter:
    def __init__(self):
        self.main_dict = {}
        from google_request import Google
        self.jarvis = Google()
        self.loader = None
        self.light_function = False
        self.keywords = {'pogoda': 'functions', 'godzina': 'functions', 'data': 'functions'}
        self.light_output = ""

    def reload(self):
        from json_loader import JsonLoader
        self.loader = JsonLoader()
        self.main_dict = self.loader.reload_main()

    def get_dictionary(self, text):
        for key, value in self.main_dict['topics']:
            if key == text:
                return value

    def set_response(self, text):
        dictionary = None
        print("recognized text: {}".format(text))
        split = text.split()

        if 'ile kosztuje' in text:
            self.light_function = True
            find = ""
            for i in range(2, len(split)):
                find = find+' '+split[i]
            try:
                dictionary = 'functions'
                self.jarvis.request(functions.price_checker(find))
            except:
                self.jarvis.request("Nie udało mi się wyszukać przedmiotu.")
        if 'dzisiaj' in text and 'pogoda' in text:
            dictionary = self.get_dictionary("jaka jest pogoda")
            self.light_function = False
            text = 'jaka jest pogoda'

        if 'który dzisiaj' in text:
            dictionary = self.get_dictionary("data")
            self.light_function = False
            text = 'data'
            #self.jarvis.request(functions.select_function("data"))
        if 'co to jest' in text:
            self.light_function = True
            wiki_ask = ''
            for i in range(0, len(split)):
                if i > 2:
                    wiki_ask = wiki_ask+' '+split[i]
            try:
                output = functions.wiki_search(wiki_ask)
            except:
                self.jarvis.request("Nie udało mi się znaleźć frazy.")
            if self.light_function is False:
                dictionary = self.get_dictionary(text)
            else:
                print("Sprawdzam")
                dictionary = 'functions'
                self.jarvis.request(functions.wiki_search(wiki_ask))

        if dictionary == None :
            self.jarvis.request("Nie rozumiem. Czy wyszukać informacji w wikipedii?")
            response = functions.get_input()
            splitted_response = response.split()
            if splitted_response[0] == 'tak' or splitted_response[0] == 'poproszę':
                try:
                    self.jarvis.request(functions.wiki_search(text))
                except:
                    self.jarvis.request("Nie udało mi się wyszukać informacji.")
            else:
                self.jarvis.request("Spróbuj inaczej wydać polecenie")

        else:
            if dictionary == 'functions' and self.light_function is False:
                self.jarvis.request(functions.select_function(text))
            if dictionary == 'functions' and self.light_function is True:
                print("Wykonano")
            else:
                print('Wynik: {}'.format(dictionary))
                response = self.main_dict[dictionary]
                responses = len(response)
                #Tutaj wsadzamy odpowiedzi wybierane pseudolosowo
                import random
                number = random.randint(0, responses-1)
                for k, val in response:
                    if int(k) == number:
                        self.light_function = False
                        self.jarvis.request(val)
                        break



