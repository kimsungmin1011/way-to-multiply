def div(value):
    value = value // 2
    return value

def mul(value):
    value = value * 2
    return value

if __name__ == '__main__':
    n = int(input("숫자를 입력하세요: "))
    m = int(input("숫자를 입력하세요: "))

    value1 = n
    value2 = m

    sum = 0
    while (n > 1):
        n = div(n)
        m = mul(m)

        if (n % 2 == 1):
            sum += m

    print(str(value1) + " x " + str(value2) + " = " + str(sum))

