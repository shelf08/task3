def get_circle_points(x, y, r):
    return [(x + r * i, y) for i in range(-r, r+1)] + [(x, y + r * i) for i in range(-r, r+1)]

# Функция для проверки пересечения двух окружностей
def do_circles_overlap(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance < abs(r2 - r1)

circles = []
output_circles = []

# Чтение координат из файла
with open("input01.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        x, y, r = map(int, line.strip().split())
        circles.append((x, y, r))

# Находим окружности, которые не пересекаются с другими окружностями
for circle in circles:
    is_overlapping = False
    for other_circle in circles:
        if circle != other_circle and do_circles_overlap(circle, other_circle):
            is_overlapping = True
            break
    if not is_overlapping:
        output_circles.append(circle)

# Выводим результат
for circle in output_circles:
    print(f"Окружности с координтами центра ({circle[0]}, {circle[1]}) и радиусом {circle[2]} не пересекаются с другими окружностями.")