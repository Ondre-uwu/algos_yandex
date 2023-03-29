def is_possible(side):
    side.append(side[0])
    pairs = list(map(sum,zip(side, side[1:])))
    side.pop()
    for i in range(3):
        if pairs[i] <= side[(2+i)%3]:
            return "NO"
    return "YES"
	  

print(is_possible([int(input()) for i in range(3)]))