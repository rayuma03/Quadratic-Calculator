import math

def find_roots(d):
    if d < 0: #imaginary roots
        print("no real solution")
    elif d == 0: #one real root
        one_root = float((-1*b / 2*a))
        print(one_root)
    else: #2 real roots
        d_temp = float(math.sqrt(d))
        f_root = float((-1*b + d_temp) / (2*a))
        s_root = float((-1*b - d_temp) / (2*a))
        print(format(f_root,".2f"))
        print(format(s_root,".2f"))

def count_roots(d):
    if d < 0: #imaginary roots
        print("no real solution")
    elif d == 0: #one real root
        print("one_root")
    else: #2 real roots
       print("two roots")


##############################################
if __name__ == '__main__':
    a = int(input("enter the value of a: "))
    b = int(input("enter the value of b: "))
    c= int(input("enter the value of c: "))
    d= int((b*b - (4*a*c))) 

    find_roots(d)
    #count_roots(d)


