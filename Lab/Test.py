values = [1, 2, 3, 4, 5, 123, 456]
limit = 100
pos = None

for i in range(len(values)):
    if values[i] > limit:
        pos = i
        break

if pos is not None:
    print("Found at position: ", pos)
else:
    print("Not found")
