import turtle


num_pts = 5 #number sides to your drawing!
for i in range(num_pts):
    turtle.left(360/num_pts)
    turtle.forward(100)

turtle.mainloop()

result = []
for count in range(1, n):
    if count % 3 ==0:
         result.append("fizz")
    else:
        result.append(count)

        
