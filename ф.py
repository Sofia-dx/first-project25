import pygame
import random

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600 # ширина и высота окна.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Анимация фигур_Лукина_СЕ_МиКН23-1') # заголовок окна

# Функция случайного цвета
def random_color():
    return [random.randint(0, 255) for _ in range(3)]
#Генерируем список из трёх случайных в диапазоне 0–255.
# цвет будет исп. для заливки фигур.
WHITE = (255, 255, 255) # будет использоваться для очистки экрана для каждого  кадра

# Список фигур с их параметрами
figures = [
    {'type': 'rect', 'pos': [500, 500], 'size': [90, 60], 'color': random_color(), 'speed': 3},  # Прямоугольник
    {'type': 'square', 'pos': [200, 200], 'size': 60, 'color': random_color(), 'speed': 4},  # Квадрат
    {'type': 'circle', 'pos': [100, 100], 'radius': 40, 'color': random_color(), 'speed': 5},  # Круг
    {'type': 'triangle', 'pos': [350, 350], 'size': [70, 70], 'color': random_color(), 'speed': 6}  # Треугольник
]

running = True  # флаг  определяет работает ли программа.
clock = pygame.time.Clock() # ограничивает время

while running:
    screen.fill(WHITE)  # очищаем экран

    # Обрабатывает события (клик мыши, выход)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = e.pos
#pygame.event.get() получает список всех событий мышки
# Если  нажимаем на  крестик(QUIT), программа завершит работу.
# Если нажата мышь(MOUSEBUTTONDOWN), получаем координаты  mouse_x, mouse_y.
            for figur in figures:
                if figur['type'] == 'rect':# если клик попадает  меняет  цвет
                    x, y = figur['pos']
                    w, h = figur['size']
                    if x <= m_x <= x + w and y <= m_y <= y + h:
                        figur['color'] = random_color()
                elif figur['type'] == 'square':# если клик попадает  меняет  цвет
                    x, y = figur['pos']
                    size = figur['size']
                    if x <= m_x <= x + size and y <= m_y <= y + size:
                        figur['color'] = random_color()
                elif figur['type'] == 'circle':# если клик попадает  меняет  цвет
                    cx, cy = figur['pos']
                    r = figur['radius']
                    if (m_x - cx) ** 2 + (m_y - cy) ** 2 <= r ** 2:  # Проверка попадания в круг
                        figur['color'] = random_color()
                elif figur['type'] == 'triangle':# если клик попадает  меняет  цвет
                    x, y = figur['pos']
                    w, h = figur['size']
                    if x <= m_x <= x + w and y - h <= m_y <= y:
                        figur['color'] = random_color()

    # Обновление позиций и обработка столкновений
    for figur in figures:
        figur['pos'][0] += figur['speed']  # Увеличиваем x-координату на  speed двигая фигуру вправо.

        # Проверка столкновения с границами
        #Если фигура достигла правого края(x + ширина >= WIDTH) или левой границы(x <= 0)
        # Меняется направление движения(speed=-speed).
        # Меняется цвет
        if figur['type'] == 'rect':  # Прямоугольник
            if figur['pos'][0] + figur['size'][0] >= WIDTH or figur['pos'][0] <= 0:
                figur['speed'] = -figur['speed']
                figur['color'] = random_color()

        elif figur['type'] == 'square':  # Квадрат
            if figur['pos'][0] + figur['size'] >= WIDTH or figur['pos'][0] <= 0:
                figur['speed'] = -figur['speed']
                figur['color'] = random_color()

        elif figur['type'] == 'circle':  # Круг
            if figur['pos'][0] + figur['radius'] >= WIDTH or figur['pos'][0] - figur['radius'] <= 0:
                figur['speed'] = -figur['speed']
                figur['color'] = random_color()

        elif figur['type'] == 'triangle':  # Треугольник
            if figur['pos'][0] + figur['size'][0] >= WIDTH or figur['pos'][0] <= 0:
                figur['speed'] = -figur['speed']
                figur['color'] = random_color()

    # Рисуем фигуры
    for figur in figures:
        if figur['type'] == 'rect':
            pygame.draw.rect(screen, figur['color'], (*figur['pos'], *figur['size']))
        elif figur['type'] == 'square':
            pygame.draw.rect(screen, figur['color'], (*figur['pos'], figur['size'], figur['size']))
        elif figur['type'] == 'circle':
            pygame.draw.circle(screen, figur['color'], figur['pos'], figur['radius'])
        elif figur['type'] == 'triangle':
            x, y = figur['pos']
            w, h = figur['size']
            pygame.draw.polygon(screen, figur['color'], [(x, y), (x + w, y), (x + w // 2, y - h)])

    pygame.display.flip()
    clock.tick(30) #30 кадров в секунду

pygame.quit()
