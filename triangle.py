class Triangle:
    def Logic(a, b, c):
        if (a > 0 and b > 0 and c > 0):
            if (a + b > c or b + c > a or c + a > b):
                if (a == b and a == c and c == b):
                    return ("Equilateral tiangle") # Side A = Side B ond Side A = Side C -- equilateral tiangle
                if (a == b) or (a == c) or (c == b):
                    return("Isosceles triange") # side a = side b or side b = side c or side a = side c -- isosceles triange
                else: 
                    return("Versatile triangle") # Versatile Triangle
            
        else:
            return("Theres no triangle like this")

