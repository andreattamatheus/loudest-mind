import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex01.mp3')
pygame.mixer.music.play()
#porque do INPUT
input()
pygame.event.wait()
