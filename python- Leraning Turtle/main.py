from turtle import*

getscreen()
bgcolor("blue")

pencolor("red")
pensize(1)
shape("turtle")

speed(5)

init_size = 30

for i in range(36):
  for i in range(4):
    forward(init_size)
    left(360/4)
  left(10)
  
done()