#!/usr/bin/python3
for i in range(10):
    for y in range(i + 1, 10):
        print("{}{}".format(i, y), end="")
        if int(str(i) + str(y)) < 89:
            print(", ", end="")

print("")
