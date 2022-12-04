# program to find whether a triangle is a right angled triange or not ?
# Also find the area of the triangle using the heron's formula

# taking the inputs / 3 sides of the triangle
a = int(input("Enter the first side of the triangle\n"))
b = int(input("Enter the second side of the triangle\n"))
c = int(input("Enter the third side of the triangle\n"))

# we know that the pythagorean theorem states that the 

'''if the sum of squares of the 2 sides of a triangle is eqaual
to the square of the third side of the triangle then the given
triangle is a right angled triangle'''

# so we find if the  the sum of squares of the 2 sides of a triangle is eqaual
# to the square of the third side of the triangle using a defined function
# as below
def right_angled_triangle_or_not(a,b,c):
    if(a*a+b*b==c*c)or(b*b + c*c == a*a)or(a*a + c*c == b*b):
        print("The Given sides form a right angled traingle")
    else:
        print("Not a right angled triangle")


# we know that the heron's formulae to find area of a given triangle is 
#  if a, b, and c are the lengths of the sides: Area = Square root 
# of √s(s - a)(s - b)(s - c) where s is half the perimeter, or (a + b + c)/2.


def area_of_the_triangle_using_herons_formula(a,b,c):
    s = (a + b + c) / 2  
  
    # calculate the area  
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
    print('The area of the triangle is %0.2f' %area + 'm2 or cms2') 


# calling the functions
right_angled_triangle_or_not(a,b,c)
area_of_the_triangle_using_herons_formula(a,b,c)
