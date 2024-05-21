import pygame
from settings import *
from meteor import Meteor
from random import randint

class MeteorManager:
    def __init__(self):
        filename_list = ["big_zmea1.jpg", "lit_zmea1.jpg"]
##        filename_list2 = ["big_zmea2.jpg", "lit_zmea2.jpg"]
        
        self.meteors = []
        for filename in filename_list:
            meteor = Meteor("images\\meteors\\" + filename)
            meteor.random_position()
            if filename.find("big"):
                meteor.set_damage(50)
                meteor.set_score(5)
                meteor.set_anim_size("big")
            elif filename.find("lit"):
                meteor.set_damage(30)
                meteor.set_score(15)
                meteor.set_anim_size("lit")
            #elif filename.find("2") > 0:
                #meteor.set_speedx(-2)
                #meteor.rect.x = 800
                #meteor.rect.x = 10  
            #elif filename.find("1") > 0:
                #meteor.set_speedx(2)
                #meteor.rect.x = 0
                #meteor.rect.y = 10  

    def update(self):
        for meteor in self.meteors:
            meteor.update()

    def draw(self, screen):
        for meteor in self.meteors:
            meteor.draw(screen)
