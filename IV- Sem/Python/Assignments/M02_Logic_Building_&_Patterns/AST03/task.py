def sum_of_digits(n: int) -> int:
    s = 0
    n = abs(n)
    while n > 0:
        s += n % 10
        n //= 10
    return s

if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))