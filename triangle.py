class Triangle:
    def Logic(a, b, c):
        if (a > 0 and b > 0 and c > 0):
            if (a + b > c and b + c > a and c + a > b):
                if (a == b and a == c and c == b):
                    print("Equilateral tiangle") # Side A = Side B ond Side A = Side C -- equilateral tiangle
                elif (a == b) or (a == c) or (c == b):
                    print("Isosceles triange") # side a = side b or side b = side c or side a = side c -- isosceles triange
                else: 
                    print("Versatile triangle") # Versatile Triangle  
            else:
                print("Theres no triangle like this")
        else:
            print("Theres no triangle like this")

Triangle.Logic(33, 0, 0)