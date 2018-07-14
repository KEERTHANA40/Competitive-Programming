def hamming_distance(x,y):
	output=bin(x^y).count('1')
	print(output)



hamming_distance(25,30)
hamming_distance(1,4)
hamming_distance(25,30)
hamming_distance(100,250)
hamming_distance(1,30)
hamming_distance(0,255)