def well_formed_parenthesis(n):
	if n <= 0:
		print('[]')
	elif n == 1:
		print('["()"]')
	paren = [[] for _ in range(n + 1)]
	paren[0].append('')
	for i in range(1, n + 1):
		for j in range(i):
			for x in paren[j]:
				for y in paren[i - j - 1]:
					paren[i].append('(' + x + ')' + y)

	print(paren[-1])




well_formed_parenthesis(2)
print()
well_formed_parenthesis(3)
print()
well_formed_parenthesis(5)
print()
well_formed_parenthesis(4)
print()
well_formed_parenthesis(1)
print()
well_formed_parenthesis(6)
