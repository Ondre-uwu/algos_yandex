def solution (a, b, c):
	if a == 0:
		if b == c**2:
			return "MANY SOLUTIONS"
		return "NO SOLUTION"
	if ((c * c - b) % a) != 0:
		return "NO SOLUTION"
	x = (c * c - b) // a
	if c < 0 or abs(x) < (-b/a):
		 return 'NO SOLUTION'
	return x

print(solution(*[int(input()) for i in range(3)]))