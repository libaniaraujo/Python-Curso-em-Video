# Tocando um MP3

import pygame
pygame.init()
pygame.mixer.music.load('exe20.mp3')
pygame.mixer.music.play()
pygame.event.wait()