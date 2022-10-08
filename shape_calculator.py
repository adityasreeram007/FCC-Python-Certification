class Rectangle:
    height,width=0,0
    def __init__(self,w,h) -> None:
        self.height=h
        self.width=w
    def set_height(self,h):
        self.height=h
    def set_width(self,w):
        self.width=w
    def get_area(self):
        return self.height*self.width
    def get_perimeter(self):
        return 2*self.height+2*self.width
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_amount_inside(self,poly):
        if hasattr(poly, 'side'):
            return int((self.height*self.width)/(poly.side**2))
        else:
            return int((self.height*self.width)/(poly.height*poly.width))
    def __str__(self) -> str:
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
        
    def get_picture(self):
        image=""
        for h in range(self.height):
            for w in range(self.width):
                image+="*"
            image+="\n"
        # print(image)
        return image



class Square:
    side=0
    def __init__(self,side) -> None:
        self.side=side
    def set_side(self,side):
        self.side=side
    def get_area(self):
        return self.side**2
    def get_perimeter(self):
        return 4*(self.side)
    def get_diagonal(self):
        return ((2) ** .5)*self.side
    def get_amount_inside(self,poly):
        if hasattr(poly, 'side'):
            return int((self.side**2)/(poly.side**2))
        else:
            return int((self.side**2)/(poly.height*poly.width))
    def __str__(self) -> str:
        return "Square(side="+str(self.side)+")"
        
    def get_picture(self):
        image=""
        for h in range(self.side):
            for w in range(self.side):
                image+="*"
            image+="\n"
        # print(image)
        return image

# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))