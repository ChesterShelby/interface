set1 = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2'] if i[1] == 'c'}
print(set1)
