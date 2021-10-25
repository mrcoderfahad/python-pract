course = "python programing"
print(len(course))
print(course[0])
print(course[-1])
print(course[1:3])

# Escape Sequence

course = "python \''programing"
print(course)

#  Formatted Strings

first = "Fahad"
last = "Rifat"
full = first + " " + last
full = f"{len(first)} {5 + 5}"
print(full)

# String Methods
course = "python programing"
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())
print(course.lstrip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("ggg" in course)
print("hfhfh" not in course)

# Numbers
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x+3
x += 3

# Working with Numbers
import math
print(round(2.9))
print(abs(-2.8))
print(math.ceil(2.4))
print(math.copysign(2.67 , -7.8))

# Type Conversion
x = input("x: ")
y = int(x) + 2
print(f"x: {x}, y: {y}")
