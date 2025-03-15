from dda import *

def accept_points():
    x1 = accept_x1()
    x2 = accept_x2()
    y1 = accept_y1()
    y2 = accept_y2()

    return x1, x2, y1, y2

def find_step(x1,x2,y1,y2):
    dx = find_dx(x1, x2)
    dy = find_dy(y1, y2)
    x_inc, y_inc = check_d(dx, dy)

    validate_pixel(x_inc, y_inc, x1)

def main():
    x1, x2, y1, y2 = accept_points()
    find_step(x1,x2,y1,y2)

main()