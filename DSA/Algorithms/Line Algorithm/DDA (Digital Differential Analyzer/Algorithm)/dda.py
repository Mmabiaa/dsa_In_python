# Algorithm for DDA line Algorithm
def accept_x2():
    x2 = int(input('Enter x2: '))
    return x2
def accept_x1():
    x1 = int(input('Enter x1: '))
    
    return x1

def accept_y2():
    y2 = int(input('Enter y2: '))
    return y2
def accept_y1():
    y1 = int(input('Enter y1: '))
    return y1,

def find_dx(x1,x2):
    dx = x2-x1
    return dx

def find_dy(y1,y2):
    dy = y2-y1
    return dy

def check_d(dx, dy):
    step = dy/dx
    if dx > dy:
        step = dx
    else:
        x1 = accept_x1()
        y1 = accept_y1()
        x_inc = dx/step
        y_inc = dy/step
        x = x1
        y = y1
    return x_inc, y_inc

def validate_pixel(x_inc, y_inc, x):
    pixel =  [x, y]
    x = x + x_inc
    y = y + y_inc

    x = round(x)
    y = round(y)
    pixel.clear()
    pixel = [x, y]
    x2 = accept_x2()
    if x == x2:
        return pixel
    else:
        return validate_pixel(x, y)

