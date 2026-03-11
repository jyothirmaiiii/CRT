def number_triangle(n: int) -> str:
    res = ""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            res += str(j)
        if i != n:
            res += "\n"
    return res

if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))