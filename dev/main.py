from dev.algorithms.greedy import greedy_algorithm

pieces = [450, 444, 436, 430, 389, 389, 386, 375, 362, 362, 261, 261, 261]

result = greedy_algorithm(pieces)

for board in result:
    print ( board.contents )


