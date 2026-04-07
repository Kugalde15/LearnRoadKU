list = [12, 13, 17, 20, 5, 90, 14, 77]
pairs = []
for value in list: 
  if value % 2 == 0:
    pairs.append(value)
print('Lista de pares', pairs)