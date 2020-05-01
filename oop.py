class Point:
    def __init__(self,x,y):
        #super().__init__()
        self.x=x
        self.y=y
        
    def move(self):
        print("move")

    def draw(self):
        print("draw")

#point1 = Point()
#point2 = Point()
#point1.x=10
#point2.x=1
#print(point1.x)
#print(point2.x)
#point1.draw()

point = Point(10,20)
print(point.x)
