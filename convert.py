#Convert list of tuples to list of strings
test = [('G', 'E', 'E', 'K', 'S'), ('F', 'O', 'R'), ('G', 'E', 'E', 'K', 'S')]
output=[''.join(i) for i in test]
print(output)

