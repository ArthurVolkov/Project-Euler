# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# Moti Version:

def multiples():
    num = 1
    total = []

    while num < 1000:
        if num % 3 == 0:
            total.append(num)
        elif num % 5 == 0:
            total.append(num)
        num += 1

    print(sum(total))


if __name__ == '__main__':
    multiples()

    
# Arthur version:


def mult_3_5():
    total = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    print(total)


if __name__ == '__main__':
    mult_3_5()
