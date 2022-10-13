from sys import argv

with open(argv[1]) as f:
    lines = f.readlines()
    line1 = lines[1].split()[0]
    line2 = lines[0].split()[0]

def calc_len_of_runs(l):
    m, cur, i, runs = 0, 1, 1, 1
    # print(l)
    while i < len(l):
        
        if l[i-1] != l[i]:
            runs += 1
            m = m if m > cur else cur
            cur = 1
        else:
            cur += 1
            
        i+=1 
    m = m if m > cur else cur    
    return (m, runs)

tup = []
ret = []
for s in [line2, line1]:
    mat = []
    for i in range(len(s)):
        s = s[1:]+s[0]
        mat.append(s)
    mat = sorted(mat)

    fin = []

    for k in mat:
        fin.append(k[-1])    

    l = "".join(fin)
    tup.append(calc_len_of_runs(l))
    ret.append([l, calc_len_of_runs(l)[1], calc_len_of_runs(l)[0]])
    
with open(argv[2], "w") as f:
    f.write(f"{ret[0][0]} {ret[0][1]} {ret[0][2]}" if int(tup[0][1]) < int(tup[1][1]) else f"{ret[1][0]} {ret[1][1]} {ret[1][2]}")
