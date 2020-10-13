def modExp(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r

def main():
    b = int(input("Enter b: "))
    e = int(input("Enter e: "))
    m = int(input("Enter m: "))
    r = modExp(b, e, m)
    print("{} ^ {} ≡ {} (mod {})".format(b, e, r, m))

if __name__ == '__main__':
    main()