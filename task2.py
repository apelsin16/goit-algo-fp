import turtle
import math

# Функція для малювання дерева Піфагора
def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        t.forward(branch_length)
        t.backward(branch_length)
        return
    
    t.forward(branch_length)
    t.left(45)
    draw_pythagoras_tree(t, branch_length / math.sqrt(2), level - 1)
    t.right(90)
    draw_pythagoras_tree(t, branch_length / math.sqrt(2), level - 1)
    t.left(45)
    t.backward(branch_length)

def main():
    # Запитати у користувача рівень рекурсії
    level = int(input("Введіть рівень рекурсії: "))
    
    # Налаштування turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)  # Найшвидша швидкість малювання
    t.left(90)  # Повернути черепашку вгору
    t.up()
    t.goto(0, -200)
    t.down()
    
    # Малювання дерева Піфагора
    draw_pythagoras_tree(t, 100, level)
    
    # Завершення роботи
    turtle.done()

if __name__ == "__main__":
    main()
