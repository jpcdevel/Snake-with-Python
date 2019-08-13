import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food

pygame.init()
window = pygame.display.set_mode((441, 441))
pygame.display.set_caption('Snake')
control = Control()
snake = Snake()
gui = Gui()
food = Food()
gui.init_field()
food.get_food_position(gui)

head = [45, 45]
var_speed = 0

while control.flag_game:
    gui.check_win_lose()
    control.control()
    window.fill(pygame.Color("Black"))
    if gui.game == "GAME":
        food.draw_food(window)
        gui.draw_indicator(window)

    elif gui.game == "WIN":
        gui.draw_win(window)

    elif gui.game == "LOSE":
        gui.draw_lose(window)

    snake.draw_snake(window)
    gui.draw_level(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_game = False

    if var_speed % 4 == 0 and control.flag_pause and gui.game == "GAME":
        snake.move(control)
        snake.check_barrier(gui)
        snake.eat(food, gui)
        snake.check_end_window()
        snake.animation()

    var_speed += 1
    pygame.display.flip()


