import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen.fill((255, 255, 255))  # белый фон
pygame.display.set_caption("Первая программа Лукиной Софии МиКН23-1")

# создание кругов разными способами задания цвета
pygame.draw.circle(screen, 'red', (200, 100), 30, width=0)
pygame.draw.circle(screen, (255, 135, 143), (100, 400), 50, width=15)
pygame.draw.circle(screen, '#FFE5B4', (400, 300), 100, width=5)

# создание прямоугольника
pygame.draw.rect(screen, 'yellow', (400, 20, 300, 200), 0)

# создание пяти случайных по размеру и положению прямоугольников
for i in range(5):
    top = random.randint(50, 700)
    left = random.randint(50, 100)
    w = random.randint(10, 200)
    h = random.randint(10, 200)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(screen, color, (top, left, w, h), 4)

# создание произвольной фигуры из линий
dots = [
    (221, 432), (225, 331), (133, 342), (141, 310),
    (51, 230), (74, 217), (58, 153), (114, 164),
    (123, 135), (176, 190), (159, 77), (193, 93),
    (230, 28), (267, 93), (301, 77), (284, 190),
    (327, 135), (336, 164), (402, 153), (386, 217),
    (409, 230), (319, 310), (327, 342), (233, 331)
]
pygame.draw.lines(screen, 'green', True, dots, 2)  # closed=True соединяет первую и последнюю точку

# Рисуем домик линиями
house_width = 200
house_height = 150
roof_height = 100

house_x = 400 - house_width // 2
house_y = 300

# Стены домика
pygame.draw.line(screen, 'yellow', (house_x, house_y), (house_x + house_width, house_y), 2)  # верх
pygame.draw.line(screen, 'black', (house_x, house_y), (house_x, house_y + house_height), 2)  # левый бок
pygame.draw.line(screen, 'lime', (house_x + house_width, house_y), (house_x + house_width, house_y + house_height), 2)  # правый бок
pygame.draw.line(screen, 'black', (house_x, house_y + house_height), (house_x + house_width, house_y + house_height), 2)
# Крыша
roof_top = (house_x + house_width // 2, house_y - roof_height)
pygame.draw.line(screen, 'magenta', (house_x, house_y), roof_top, 2)  # левая сторона крыши
pygame.draw.line(screen, 'orange', roof_top, (house_x + house_width, house_y), 2)  # правая сторона крыши

# Дверь
door_x = house_x + 75
door_y = house_y + 75
door_width = 50
door_height = 75

pygame.draw.line(screen, 'crimson', (door_x, door_y), (door_x + door_width, door_y), 2)  # верх двери
pygame.draw.line(screen, 'indigo', (door_x, door_y), (door_x, door_y + door_height), 2)  # левая сторона двери
pygame.draw.line(screen, 'indigo', (door_x + door_width, door_y), (door_x + door_width, door_y + door_height), 2)  # правая сторона двери
pygame.draw.line(screen, 'crimson', (door_x, door_y + door_height), (door_x + door_width, door_y + door_height), 2)  # низ двери

#
window_size = 30
window1_x = house_x + 15
window1_y = house_y + 30


pygame.draw.rect(screen, 'red', (window1_x, window1_y, window_size, window_size), 2)


# яблоко на экране
apple = pygame.image.load("D:/Users/SofaF/Downloads/apple.png")
screen.blit(apple, (450, 500))  # копирование пикселей с растр. изображения (блитинг)
pygame.display.flip()  # обновление монитора

# передвигаем изображение в новые координаты
pygame.time.delay(3000)  #
screen.fill('white', (450, 500, 100, 100))  # стираем старое яблоко
screen.blit(apple, (600, 450))  # копирование пикселей с растр. изображения (блитинг)

pygame.display.flip()  # обновление монитора

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # проверка нажатия на крестик
            running = False

pygame.quit()  # закрытие окна
