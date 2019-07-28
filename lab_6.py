import turtle
x = 0
while x<300:
    y = x**2/300 #x**2 is the same as x*x
    turtle.goto(x,y)
    x = x + 100

turtle.mainloop()


total = 0
for number in range(1, 10 + 1):
    print (number)
    total = total + number
print(total)

def add_number():
    for number in range(3, 13 + 2):
        print(number)
        add_number = add_number + number
print(add_number)


