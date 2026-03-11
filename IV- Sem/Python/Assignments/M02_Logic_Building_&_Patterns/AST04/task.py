def right_triangle(n: int) -> str:
    res = ""
    for i in range(1, n + 1):
        res += "*" * i
        if i != n:
            res += "\n"
    return res

if __name__ == "__main__":
    n = int(input())
    print(right_triangle(n))