def solve(x):
    l = []
    c = 0
    print(x)
    for i in x:
        if len(i):
            c += int(i)
        else:
            l.append(c)
            c = 0
    l.sort()
    print(sum(l[::-1][:3]))


if __name__ == "__main__":
    with open("input1.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
