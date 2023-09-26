# This file was created by: Carson Bleh

'''
Goals - create working rock, paper, scissors game with images 

'''

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
import winsound
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint
from time import sleep
# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
sounds_folder = os.path.join(game_folder, 'sounds')


# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

player_choice = ""

cpu_choice = ""

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()
# rock_instance.hideturtle()

cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
cpu_rock_instance = turtle.Turtle()
# cpu_rock_instance.hideturtle()

paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
# paper_instance.hideturtle()

cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
cpu_paper_instance = turtle.Turtle()
# cpu_paper_instance.hideturtle()

scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
# scissors_instance.hideturtle()

cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
cpu_scissors_instance = turtle.Turtle()
# cpu_scissors_instance.hideturtle()

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

# setting up the all of the images
def cpu_show_rock(x,y):
    screen.addshape(cpu_rock_image)
    cpu_rock_instance.shape(cpu_rock_image)
    cpu_rock_instance.penup()
    cpu_rock_instance.setpos(x,y)

def cpu_show_paper(x,y):
    screen.addshape(cpu_paper_image)
    cpu_paper_instance.shape(cpu_paper_image)
    cpu_paper_instance.penup()
    cpu_paper_instance.setpos(x,y)

def cpu_show_scissors(x,y):
    screen.addshape(cpu_scissors_image)
    cpu_scissors_instance.shape(cpu_scissors_image)
    cpu_scissors_instance.penup()
    cpu_scissors_instance.setpos(x,y)

def show_paper(x,y):
    screen.addshape(paper_image)
    paper_instance.shape(paper_image)
    paper_instance.penup()
    paper_instance.setpos(x,y)

def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

# turtle for writing text
text = turtle.Turtle()
def write_text(message, x, y):
    text.hideturtle()
    text.color('red')
    text.penup()
    text.clear()
    text.setpos(x,y)
    text.write(message, False, "center", ("Arial", 24, "normal"))
    # for i in message:
    #     text.setpos(x,y)
    #     text.write(i, False, "center", ("Arial", 24, "normal"))    
    #     x += 17
    #     sleep(.01)
        
# getting computers random choice 
def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]

# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# getting images up on screen to begin
show_rock(-300,0)
show_paper(0,0)
show_scissors(300,0)

# function that passes through wn onlick
def mouse_pos(x, y):
    print(cpu_select())
    cpu_picked = cpu_select()
    # have cpu select
    # set instance for when user chooses rock
    if collide(x,y,rock_instance,rock_w,rock_h):
        write_text("You picked rock!", 0, 150 )
        if cpu_picked == "rock":
            write_text("The computer chose rock too...", 0, 150)
            # remove other choices from screen
            show_scissors(2000,0)
            show_paper(2000,0)
            cpu_show_rock(300,0)
            # show user choice and computer choice
            show_rock(-300,0)
            write_text("It's a tie!", 0, 150 )
            # show result
        if cpu_picked == "scissors":
            write_text("The computer chose scissors...", 0, 150)
            # same as above but with scissors choice instead
            show_scissors(2000,0)
            show_paper(2000,0)
            cpu_show_scissors(300,0)
            show_rock(-300,0)
            write_text("You win!", 0, 150)
            # show result
        if cpu_picked == "paper":
            write_text("The computer chose paper...", 0, 150)
            # same as above but with paper choice
            show_scissors(2000,0)
            show_paper(2000,0)
            cpu_show_paper(300,0)
            show_rock(-300,0)
            write_text("You lose!", 0, 150)
            # show result
    # set instance for when user chooses paper
    elif collide(x,y,paper_instance,paper_w,paper_h):
        write_text("You picked paper!", 0, 150)
        if cpu_picked == "rock":
            write_text("The computer chose rock...", 0, 150)
            show_scissors(2000,0)
            show_rock(2000,0)
            cpu_show_rock(300,0)
            show_paper(-300,0)
            write_text("You win!", 0, 150 )
        if cpu_picked == "scissors":
            write_text("The computer chose scissors...", 0, 150)
            show_scissors(2000,0)
            show_rock(2000,0)
            cpu_show_scissors(300,0)
            show_paper(-300,0)
            write_text("You lose!", 0, 150)
        if cpu_picked == "paper":
            write_text("The computer chose paper tooo...", 0, 150)
            show_scissors(2000,0)
            show_rock(2000,0)
            cpu_show_paper(300,0)
            show_paper(-300,0)
            write_text("It's a tie!", 0, 150)
    # set instance for when user chooses scissors
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        write_text("You picked scissors!", 0, 150)
        if cpu_picked == "rock":
            write_text("The computer chose rock...", 0, 150)
            show_rock(2000,0)
            show_paper(2000,0)
            cpu_show_rock(300,0)
            show_scissors(-300,0)
            write_text("You lose!", 0, 150 )
        if cpu_picked == "scissors":
            write_text("The computer chose scissors too...", 0, 150)
            show_rock(2000,0)
            show_paper(2000,0)
            cpu_show_scissors(300,0)
            show_scissors(-300,0)
            write_text("It's a tie!", 0, 150)
        if cpu_picked == "paper":
            write_text("The computer chose paper...", 0, 150)
            show_rock(2000,0)
            show_paper(2000,0)
            cpu_show_paper(300,0)
            show_scissors(-300,0)
            write_text("You win", 0, 150)
    else:
        write_text("Choose something...", 0, 150)
        # for if player does not click on a viable choice

# user this to get mouse position
screen.onclick(mouse_pos)
write_text("Let's play rock paper scissors...", 0, 150 )

# runs mainloop for turtle, has to be last
screen.mainloop()

