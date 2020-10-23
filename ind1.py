x = int(input("How much? "))
if x<50:
    a = 0.3*x
    print("Money :{0} ".format(a))
elif 50 <= x <= 75:
    a = 0.5*x
    print("Money :{0} ".format(a))
elif 75<x<=90:
    a = 0.65*x
    print("Money :{0} ".format(a))
else:
    a = (0.7*x)+20
    print("Money :{0} ".format(a))
