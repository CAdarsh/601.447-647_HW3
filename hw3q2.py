from sys import argv


def inp2str(s):
    st = []
    s = s.replace(" ", "")
    for i in range(len(s)//2):
        st.append(s[i*2] * int(s[(i*2)+1]))
    return "".join(st)


with open(argv[1]) as f:
    lines = f.readlines()[0]
    st = inp2str(lines)
    sa = sorted(st)
    

def addInd(arr):
    name = {}
    a = []
    for i in arr:
        if i in name:
            name[i] += 1
            a.append(str(i) + str(name[i]))
        else:
            name[i] = 0
            a.append(str(i) + str(name[i]))
    return a


def createD(arr1, arr2):
    d = {}
    for i,val in enumerate(arr1):
        d[val] = arr2[i]
    return d

st = addInd(st)
sa = addInd(sa)

d = createD(sa, st) 
c = d["$0"]
decompressed = ["$"]
while c != "$0":
     decompressed.append(c[:-1])
     c = d[c]
# print("".join(decompressed[::-1]))

with open(argv[2], "a") as f:
    f.write("".join(decompressed[::-1]))
