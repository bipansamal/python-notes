# import turtle as tur
# import colorsys as cs

# tur.setup(800,800)
# tur.speed(0)
# tur.tracer(10)
# tur.width(2)
# tur.bgcolor("black")
# for j in range(25):
#     for i in range(15):
#         tur.color(cs.hsv_to_rgb(i/15,j/25,1))
#         tur.right(90)
#         tur.circle(200-j*4,90)
#         tur.left(90)
#         tur.circle(200-j*4,90)
#         tur.right(180)
#         tur.circle(50,24)
# tur.hideturtle()
# tur.done()

i = 1
n = input("enter your number")
while i <= 10:
    print(i*n)
    i += 1

i = 1
n = int(input("enter the number"))
while i <= 10:
    print(i*n)
    i += 1