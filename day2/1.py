def solve(x):
    s = 0
    for l in x:
        p = l.split(" ")
        if p[0] == "A" and p[1] == "Y":
            s += 6 + 2
        elif p[0] == "B" and p[1] == "Z":
            s += 6 + 3
        elif p[0] == "C" and p[1] == "X":
            s += 6 + 1
        elif p[0] == "A" and p[1] == "X":
            s += 3 + 1
        elif p[0] == "B" and p[1] == "Y":
            s += 3 + 2
        elif p[0] == "C" and p[1] == "Z":
            s += 3 + 3
        elif p[1] == "X":
            s += 1
        elif p[1] == "Y":
            s += 2
        elif p[1] == "Z":
            s += 3

    print(s)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
