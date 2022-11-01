class ThisIsTriangle():
    def is_triangle(x, y, z):
        if (x + y > z and x + z > y and z + y > x):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    x, y, z = map(int, input('Enter the stick lengths: ').split())
    ThisIsTriangle.is_triangle(x,y,z)
