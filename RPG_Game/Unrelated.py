# Test time :boggers:

weights = [1.75, 0.75, 2, 1.75, 2, 1.75]

scores = [19/20, 6/10, 6/20, 171/232, 12/16, 17/20]
tot = 0
for i in range(len(weights)):
	tot += (weights[i] * scores[i])
print(tot)