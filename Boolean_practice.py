"""
Checks to see if it's a triangle 
by if length is less than 0 on all sides 
and if 2 sides will always be greater than the third"""
def is_triangle(lengthA, lengthB, lengthC):
    if lengthA <= 0 or lengthB <= 0 or lengthC <= 0:
        return False
    return (lengthA + lengthB > lengthC and
            lengthB + lengthC > lengthA and
            lengthA + lengthC > lengthB)

###Returns true if all sides are equal to eachother
def equilateral(lengthA, lengthB, lengthC):
    if is_triangle(lengthA, lengthB, lengthC):
        return lengthA == lengthB == lengthC
    return False

###Returns true if 2 sides are equal to eachother
def isosceles(lengthA, lengthB, lengthC):
    if is_triangle(lengthA, lengthB, lengthC):
        return (lengthA == lengthB or
                lengthB == lengthC or
                lengthA == lengthC)
    return False

###Returns true if all sides are not equal to eachother
def scalene(lengthA, lengthB, lengthC):
    if is_triangle(lengthA, lengthB, lengthC):
        return (lengthA != lengthB and
                lengthB != lengthC and
                lengthA != lengthC)
    return False

#is triangle checks
print("### Is it a triangle? ###")
print(is_triangle(3,3,4)) #<- True
print(is_triangle(1,1,4)) #<- False
print(is_triangle(3,3,4)) #<- True
print(is_triangle(4,3,5)) #<- True

print("------")

#is equilateral checks
print("### Is it an equilateral? ###")
print(equilateral(3,3,3)) #<- True
print(equilateral(7,7,7)) #<- True
print(equilateral(9,9,9)) #<- True
print(equilateral(1,2,3)) #<- False

print("------")

#is isosceles checks
print("### Is it an isosceles? ###")
print(isosceles(2,2,3)) #<- True
print(isosceles(2,3,3)) #<- True
print(isosceles(5,4,3)) #<- False
print(isosceles(1,1,3)) #<- False

#is scalene checks
print("------")
print("### Is it a scalene? ###")
print(scalene(2,3,4)) #<- True
print(scalene(6,4,10)) #<- False
print(scalene(4,4,8)) #<- False
print(isosceles(1,1,3)) #<- False