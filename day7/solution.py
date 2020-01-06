holding = {}
weights = {}

for i in contents:
    name = i.split()[0]
    weights[name] = int(i.split()[1].strip('()'))
    held = i.split()[3:]
    held = [x.strip(',') for x in held]
    holding[name] = set(held)

for i in holding.keys():
    found = False
    for j in holding.values():
        if i in j:
            found = True
            break

    if not found:
        print("Part One:", i)
        break