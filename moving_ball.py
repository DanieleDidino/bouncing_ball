# import modules
import pygame
import numpy as np
import os

# Setting
ball_img = os.path.join('.\intro_ball.gif')
size = width, height = 512, 512  # window size
speed = np.random.randint(low=1, high=20, size=2)  # speed of the ball
col_back = 125, 100, 255  # background color

# define a main function
def main():
    # initialize the pygame module
    pygame.init()

    # initialize clock object
    clock = pygame.time.Clock()

    # create a surface on screen
    screen = pygame.display.set_mode(size)

    # load image
    ball = pygame.image.load(ball_img)
    ballrect = ball.get_rect()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        clock.tick(30)

        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        ballrect = ballrect.move(speed)

        pygame.display.update()
        screen.fill(col_back)
        screen.blit(ball, ballrect)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
