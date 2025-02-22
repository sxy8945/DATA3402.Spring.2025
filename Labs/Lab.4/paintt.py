class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[' '] * width for _ in range(height)]

    def set_pixel(self, row, col, **kargs):
        char = kargs.get('char', '*')
        if 0 <= row < self.height and 0 <= col < self.width:
            self.data[row][col] = char

    def get_pixel(self, row, col):
        return self.data[row][col]

    def clear_canvas(self):
        self.data = [[' '] * self.width for _ in range(self.height)]

    def v_line(self, x, y, w, **kargs):
        for i in range(x, x + w):
            self.set_pixel(i, y, **kargs)

    def h_line(self, x, y, h, **kargs):
        for i in range(y, y + h):
            self.set_pixel(x, i, **kargs)

    def line(self, x1, y1, x2, y2, **kargs):
        slope = (y2 - y1) / (x2 - x1) if x2 != x1 else 0
        for y in range(y1, y2 + 1):
            x = int(x1 + (y - y1) / slope) if slope else x1
            self.set_pixel(x, y, **kargs)

    def display(self):
        print("\n".join(["".join(row) for row in self.data]))


class Rectangle:
    def __init__(self, x, y, width, height, **kargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.kargs = kargs  # Store drawing properties

    def draw(self, canvas, **kargs):
        draw_kargs = {**self.kargs, **kargs}  # Merge class and function args
        canvas.h_line(self.x, self.y, self.width, **draw_kargs)
        canvas.h_line(self.x + self.height - 1, self.y, self.width, **draw_kargs)
        canvas.v_line(self.x, self.y, self.height, **draw_kargs)
        canvas.v_line(self.x, self.y + self.width - 1, self.height, **draw_kargs)


class Circle:
    def __init__(self, x, y, radius, **kargs):
        self.x = x
        self.y = y
        self.radius = radius
        self.kargs = kargs

    def draw(self, canvas, **kargs):
        draw_kargs = {**self.kargs, **kargs}
        for i in range(-self.radius, self.radius + 1):
            for j in range(-self.radius, self.radius + 1):
                if i**2 + j**2 <= self.radius**2:
                    canvas.set_pixel(self.x + i, self.y + j, **draw_kargs)


class CompoundShape:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw(self, canvas, **kargs):
        for shape in self.shapes:
            shape.draw(canvas, **kargs)
