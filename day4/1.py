def solve(x):
    s = 0
    for l in x:
        if not "," in l:
            continue
        a,b = l.split(",")
        a = list(map(int,a.split("-")))
        b = list(map(int,b.split("-")))
        if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]): 
            s += 1
    print(s)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
     
