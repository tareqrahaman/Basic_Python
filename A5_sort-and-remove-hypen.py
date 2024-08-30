def sortIt(names):
    s = ''
    l = names.split("-")
    l.sort()
    for i in l:
        s = s+'-'+i
    return s[1:]

names = "green-red-yellow-black-white"
res = sortIt(names)
print(res)