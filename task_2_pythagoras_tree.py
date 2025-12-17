import turtle

def draw_tree(branch_len: float, level: int):
    if level == 0:
        return

    turtle.forward(branch_len)
    turtle.left(45)
    draw_tree(branch_len * 0.7, level - 1)
    turtle.right(90)
    draw_tree(branch_len * 0.7, level - 1)
    turtle.left(45)
    turtle.backward(branch_len)

def main():
    level = int(input("Введіть рівень рекурсії (наприклад 8-12): ").strip())

    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()

    draw_tree(140, level)
    turtle.done()

if __name__ == "__main__":
    main()
