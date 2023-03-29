def calc_cost(string):
    cost = 0
    for i in range(len(string) // 2):
        if string[i] != string[-i-1]:
            cost += 1
    return cost
print(calc_cost(input()))
