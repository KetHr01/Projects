def count_ad_bc(x, y):
    ad_bc_number = []

    def karatsuba(x, y):
        if int(x) < 10 or int(y) < 10:
            return x * y
        n = max(len(str(x)), len(str(y)))
        n_2 = n // 2
        a, b = divmod(int(x), 10 ** n_2)
        c, d = divmod(int(y), 10 ** n_2)
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_bc = karatsuba(a + b, c + d) - ac - bd
        ad_bc_number.append(ad_bc)
        result = ac * 10 ** (n_2 * 2) + ad_bc * 10 ** n_2 + bd
        return result

    res = karatsuba(x, y)
    num = len(ad_bc_number)
    return "Result:", res, "Number of 'ad+bc':", num


x = input("Enter x:")
y = input("Enter y:")

print(count_ad_bc(x, y))
