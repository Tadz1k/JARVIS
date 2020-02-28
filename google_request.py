from gtts import gTTS
import os
import pygame.mixer
from time import sleep


class Google:
    def __init__(self):
        self.translate = None
        self.patch_name = None

    def request(self, text):
        self.translate = gTTS(text, 'pl')
        self.translate.save('last_reply.wav')
        pygame.mixer.init()
        path_name = os.path.realpath('last_reply.wav')
        real_path = path_name.replace('\\', '\\\\')
        pygame.mixer.music.load(open(real_path, "rb"))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            sleep(1)
