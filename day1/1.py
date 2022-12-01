def solve(x):
    m = 0
    c = 0
    print(x)
    for i in x:
        if len(i):
            c += int(i)
        else:
            if c > m:
                m = c
            c = 0
    print(m)


if __name__ == "__main__":
    with open("input1.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
