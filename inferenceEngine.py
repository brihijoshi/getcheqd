# 	This is a simulation of the algorithm we shall use to give to rank the diseases in 
#	order of their probability on the basis of the data collected. Each parameter that we collect 
#	has weights for different diseases and the final result is calculated on the basis of those weights
#	and the data collected.
#	 _____________________________________________________________________________________________
#	|	Disease			|	Weight 1	  |		Weight 2	|	Weight 3		|	Weight 4	  |
# 	|___________________|_________________|_________________|___________________|_________________|	
# 	|					|				  |					|					|				  |
# 	|					|				  |					|					|				  |
# 	|		A			|		2		  |			3		|		0			|		0		  |
# 	|		B			|		1		  |			4		|		1			|		2		  |
# 	|		C			|		2		  |			1		|		0			|		3		  |
# 	|		D			|		2		  |			1		|		3			|		0		  |
# 	|					|				  |					|					|				  |
# 	|___________________|_________________|_________________|___________________|_________________|

diseases = ["A","B","C","D"]

ranks = []


d1 = 3
d2 = 4
d3 = 5
d4 = 6

for i in range(4):

	if i==1:

		w1 = 2
		w2 = 3
		w3 = 0
		w4 = 0

		resA = w1*d1 + w2*d3 + w3*d3 + w4*d4
		ranks.append((resA,"A"))

	if i==2:

		w1 = 1
		w2 = 4
		w3 = 1
		w4 = 2

		resB = w1*d1 + w2*d3 + w3*d3 + w4*d4
		ranks.append((resB,"B"))

	if i==3:

		w1 = 2
		w2 = 1
		w3 = 0
		w4 = 3

		resC = w1*d1 + w2*d3 + w3*d3 + w4*d4
		ranks.append((resC,"C"))

	if i==4:

		w1 = 2
		w2 = 1
		w3 = 3
		w4 = 0

		resD = w1*d1 + w2*d3 + w3*d3 + w4*d4
		ranks.append((resD,"D"))


ranks.sort(reverse=True)
for i in ranks:
	print(i[1])




