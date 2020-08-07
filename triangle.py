def checkTriangle(a, b, c):
    # returns information if triangle is equilateral / isosceles / scalene
    if not allPositive(a, b, c):
        return "Negative integer(s) found"
    if not checkValidity(a, b, c):
        return "Triangle not valid"
    if isEquilateral(a, b, c):
        return "Equilateral"
    if isIsosceles(a, b, c):
        return "Isosceles"
    if isScalene(a, b, c):
        return "Scalene"


def allPositive(a, b, c):
    # check if all a,b,c are positive integers
    return a > 0 and b > 0 and c > 0


def checkValidity(a, b, c):
    # check if triangle is valid
    return a + b > c and a + c > b and b + c > a


def isEquilateral(a, b, c):
    # check if triangle is equilateral
    if a == b == c:
        return True
    return False


def isIsosceles(a, b, c):
    # check if triangle is isosceles
    if a == b or b == c or a == c:
        return True
    return False


def isScalene(a, b, c):
    # check if triangle is scalene
    if a != b and b != c and a != c:
        return True
    return False


def main():
    print("Provide 3 integers (defining triangle)")
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
    except ValueError:
        print("all provided numbers should be integers")
        exit()
    print(checkTriangle(a, b, c))


main()
