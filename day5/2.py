def solve(d):
    stacks = {}
    yy = 0
    for l in d:
        if l == "":
            break
        i = 0
        x = l
        while i < len(x):
            if x[i] == "":
                i += 1
                continue
            if x[i] == "[":
                xx = x[i+1]
                if not stacks.get(int(i/4)):
                    stacks[int(i/4)] = [xx]
                else:
                    stacks[int(i/4)].append(xx)
                i += 1
            i += 1
        yy += 1
    for l in d[yy+1:]:
        xx = l.split(" ")
        if xx == [""]:
            continue
        nb = int(xx[1])
        f = int(xx[3])-1
        t = int(xx[5])-1
        stacks[t] = stacks[f][:nb] + stacks[t]
        for u in range(nb):
            stacks[f].remove(stacks[f][0])
    s = ''
    for x in range(len(stacks)):
        s += stacks[x][0]
    print(s)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
    with open("ex.txt", "r") as f:
        c = f.read().split("\n")
        solve(c)
      
