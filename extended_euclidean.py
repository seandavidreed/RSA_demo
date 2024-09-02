def euclidean(phi, e, show_calc=False):
    x = phi
    y = e
    rem_dict = {
        y: (x, x % y, x // y)
    }

    while True:
        remainder = x % y
        divisor = x // y

        if show_calc:
            print(f'{x} = {y}({divisor}) + {remainder}')

        rem_dict[remainder] = (x, y, divisor * -1)

        x = y
        y = remainder

        if remainder == 1:
            break

    return x, y, rem_dict

def extendedEuclidean(phi, e, show_calc=False):
    x, y, rem_dict = euclidean(phi, e, show_calc=show_calc)
    a = rem_dict[y][0]
    b = x
    s = 1
    t = rem_dict[y][2]

    while True:
        if show_calc:
            print()
            print(f'{y} = {a}({s}) + {b}({t})')
        
        if a == phi:
            break

        a1, b1, t1 = rem_dict[b]

        if show_calc:
            print(f'{y} = {a}({s}) + [{a1} + {b1}({t1})]({t})')

        temp = t
        t = (t * t1) + s
        s = temp

        b = a
        a = a1

    return t % phi

def main():
    phi = 159900
    e = 65537
    result = extendedEuclidean(phi, e, show_calc=True)
    print(f'Modular Multiplicative Inverse: {result}')

if __name__=="__main__":
    main()
