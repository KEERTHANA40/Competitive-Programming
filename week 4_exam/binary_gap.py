def binary_gap(n):
	z = "{0:b}".format(n)
	k = [i for i, e in enumerate(list(z)) if e == "1"]
	m = 0

	for i in range(len(k)-1):
		if (k[i+1] - k[i]) >0:
			if m < k[i+1] - k[i]:
				m = k[i+1] - k[i]
	print(m)

binary_gap(0)
binary_gap(55)
binary_gap(-5)
binary_gap(12354)
binary_gap(6)
binary_gap(256)