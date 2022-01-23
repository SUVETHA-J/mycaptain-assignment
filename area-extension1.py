#area of circle
r=int(input("enter a radius"))
area=3.14*pow(r,2)
print("area of a circle",area)
#extension of file
filename=input("enter a filename")
file=filename.split(".")
print("the extension of file",repr(file[-1]))
