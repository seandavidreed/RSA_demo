def euclidean(phi, e, show_calc=False):
    a, b, rem = phi, e, 1
    rem_dict = {}
    rem = 1

    while rem > 0:
        div = a // b
        rem = a % b

        if show_calc:
            print(f'{a} = {b}({div}) + {rem}')

        rem_dict[rem] = (a, b, div * -1)

        a, b = b, rem

    return rem_dict

def extended_euclidean(phi, e, show_calc=False):
    rem_dict = euclidean(phi, e, show_calc=show_calc)

    if not rem_dict.get(1, False):
        print("e is not coprime with phi! Private key not generated. Terminating...")
        exit()

    a, b, t = rem_dict[1]
    s = 1

    while True:
        if show_calc:
            print()
            print(f'1 = {a}({s}) + {b}({t})', end='')
        
        if a == phi:
            break

        a1, b1, t1 = rem_dict[b]

        if show_calc:
            print(f' => {a}({s}) + [{a1} + {b1}({t1})]({t})')

        temp = t
        t = (t * t1) + s
        s = temp

        b, a = a, a1

    return t % phi

# DRIVER CODE FOR TESTING
# def main():
#     phi = 159900
#     e = 65537
#     result = extended_euclidean(phi, e)
#     print(f'\nModular Multiplicative Inverse: {result}')

# if __name__=="__main__":
#     main()
