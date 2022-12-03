def solve(x):
    pt = 0
    for i in x:
        a = i[:len(i) // 2]
        b = i[len(i) // 2:]
        p = 0
        for x in a:
            for y in b:
                if x == y:
                    if x.upper() == x:
                        p = ord(x) - ord('A') + 27
                    else:
                        p = ord(x) - ord('a') + 1
                    print(x, p)
                    break
            if p:
                break
        pt += p
    print(pt)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
