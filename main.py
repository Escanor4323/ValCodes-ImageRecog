import math

import PIL
import pygame, sys
from operator import sub
from tkinter import messagebox
from tkinter import *

from PIL import Image, ImageChops
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
import numpy as np

# cropping frop mouse box
import agent
from agent import *
import ability


def displayImage(screen, px, topleft):
    screen.blit(px, px.get_rect())
    if topleft:
        pygame.draw.rect(screen, (128, 128, 128),
                         pygame.Rect(topleft[0], topleft[1], pygame.mouse.get_pos()[0] - topleft[0],
                                     pygame.mouse.get_pos()[1] - topleft[1]))
    pygame.display.flip()


def setup(path):
    px = pygame.image.load(path)
    screen = pygame.display.set_mode(px.get_rect()[2:])
    screen.blit(px, px.get_rect())
    pygame.display.flip()
    return screen, px


def mainLoop(screen, px):
    topleft = None
    bottomright = None
    n = 0
    while n != 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if not topleft:
                    topleft = event.pos
                else:
                    bottomright = event.pos
                    n = 1
        displayImage(screen, px, topleft)
    return (topleft + bottomright)


# ending of section


def matchImagesW_MSE(image1, image2):
    MSE = mean_squared_error(image1, image2)
    # return the MSE, the lower the error, the more "similar"
    PSNR = 10 * math.log10(256 * 256 / MSE)
    return PSNR


def getImage(path="img1.png"):
    return Image.open(path)


def cropAbility(path="img1.png", crop=(0, 0, 0, 0), blackNwhite=""):
    im = Image.open(path)
    try:
        return im.crop(box=crop).convert(blackNwhite)
    except:
        print(f"should be a box {crop[0], crop[2]} compared to: {im.size} <Original Image returned>")
        return im.convert(blackNwhite)


def matchSizes(arr1, size_to):
    return np.resize(arr1, size_to)


def dictionary_abilities(agent_name, ability_name, image) -> dict:
    ability_dict = {agent_name: []}
    ability_dict[agent_name].append([ability_name, image])
    return ability_dict


def display_box(title="def_Title", message="def.Message_Message not defined enter the message:", size="200x200"):
    top = Tk()
    if message == "def.Message_Message not defined enter the message:":
        message = input("...")
    if title == "def_Title":
        title = input("Enter title")
    top.geometry(size)
    messagebox.showinfo(title, message)
    top.mainloop()


def createBox_crop(input_loc=None):
    if input_loc is None:
        print("Error 2: Nothing was sent, be sure to sent a type PIL image")
        return None
    else:
        screen, px = setup(img1)
        left, upper, right, lower = mainLoop(screen, px)
        im = Image.open(input_loc)
        im = im.crop((left, upper, right, lower))
        # Gettign the ability to the dictionary
        pygame.display.quit()
        return im


if __name__ == '__main__':
    # Image declaration:
    img1, img2, img3 = "img1.png", "img2.png", "img3.jpg"

    # displaying the box with info
    # display_box(title="How to use the box feature", message="1. Only clicking alowed (not dragging)\n2. Select a "
    # "valid cordinate being\n1. +---+\n     |      |\n    +---+ "
    # "2.\n3. enjoy!")
    # cropped_Image = createBox_crop(img1)
    # cropped_Image.save("croppedIm.png")
    # Do the matching to state names and Agent
    # Better idea to create a new dictionary to fill whole Valorant roaster and abilities for every agent

    # dict_data_agent_ability = dictionary_abilities("Jett", "Blade Storm", cropped_Image)
    # print(dict_data_agent_ability["Jett"][0][1].show())
    abilities = ability.ability(name_abilityStr="Blade Storm")
    agntJett = agent.newAgent(name="Jett", ability_list=None, ability_image=None)
