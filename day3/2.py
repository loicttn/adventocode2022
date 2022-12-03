def solve(x):
    pt = 0
    for ii in range(0, len(x), 3):
        c = {}
        for i in x[ii:ii+3]:
            for xx in list(set(i)):
                if not c.get(xx):
                    c[xx] = 1
                else:
                    c[xx] += 1
        for i in c:
            if c[i] != 3:
                continue
            if i.upper() == i:
                p = ord(i) - ord('A') + 27
            else:
                p = ord(i) - ord('a') + 1
            print(i, p)
            pt += p
            break
    print(pt)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
