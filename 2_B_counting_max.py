maximum = int(input())
counter = 0
new = maximum
while new != 0:
    if new > maximum:
        maximum = new
        counter = 1
    elif new == maximum:
        counter += 1
    new = int(input())
print(counter)
