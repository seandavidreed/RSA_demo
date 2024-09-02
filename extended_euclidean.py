def eEuclidean(phi, e, show_calc=False):
    original = phi
    rem_dict = {
        e: (phi, phi % e, phi // e)
    }

    while True:
        remainder = phi % e
        divisor = phi // e

        if show_calc:
            print(f'{phi} = {e}({divisor}) + {remainder}')

        rem_dict[remainder] = (phi, e, divisor * -1)

        phi = e
        e = remainder

        if remainder == 1:
            break

    a = rem_dict[e][0]
    b = phi
    s = 1
    t = rem_dict[e][2]

    while True:
        if show_calc:
            print()
            print(f'{e} = {a}({s}) + {b}({t})')
        
        if a == original:
            break

        a1, b1, t1 = rem_dict[b]

        if show_calc:
            print(f'{e} = {a}({s}) + [{a1} + {b1}({t1})]({t})')

        temp = t
        t = (t * t1) + s
        s = temp

        b = a
        a = a1

    return t % original

def main():
    phi = 159900
    e = 65537
    result = eEuclidean(phi, e)
    print(f'Modular Multiplicative Inverse: {result}')

if __name__=="__main__":
    main()
