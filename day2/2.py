def solve(x):
    s = 0
    for l in x:
        p = l.split(" ")
        if p[1] == "Y":
            s += 3
            if p[0] == "A":
                s += 1
            if p[0] == "B":
                s += 2
            if p[0] == "C":
                s += 3
        elif p[1] == "Z":
            s += 6
            if p[0] == "A":
                s += 2
            if p[0] == "B":
                s += 3
            if p[0] == "C":
                s += 1
        else:
            if p[0] == "A":
                s += 3
            if p[0] == "B":
                s += 1
            if p[0] == "C":
                s += 2

    print(s)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
