def solve(d):
    x = d[0]
    i = 0
    while i < len(x):
        buff = x[i:i+4]
        if "".join(sorted(buff)) == "".join(sorted(list(set(buff)))):
            print(i + 4)
            break
        i += 1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
    with open("ex.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
       
