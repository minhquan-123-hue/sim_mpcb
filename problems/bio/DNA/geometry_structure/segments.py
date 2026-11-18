"""tổng số lượng hydrogens bond  ở cả 2 đoạn và đoán xem cái nào dùng nhiều nhiệt hơn khi tách ra thành 2 mảnh rời, tập form linear equation"""

#datas
# G - A = 150
# G + A = 2500
# Seg X have A = 600
# Seg Y have G = 700
# A need 2 Hydrogen to bond with T
# G need 3 Hydrogen to bond with C
# Both have 2000 Neucleotides 

N_both = 2000

#Seg X
A = 600
T = A
G = (N_both - (A+T)) / 2
C = G

H_bond_seg_X = A * 2 + G * 3
print(H_bond_seg_X)

#Seg Y
G = 700
C = G
A = (N_both - (G+C)) / 2
T = A

H_bond_seg_Y = A * 2 + G * 3
print(H_bond_seg_Y)

result = H_bond_seg_Y > H_bond_seg_X
print("seg_y need more heat energy to separate: ",result)

# solve linear equations
# G - A = 150
# A + G = 2500
# G = 150 + A
# A + G = 2500
# G = 150 + A
# A + 150 + A = 2500
# G = 150 + A
# 2A = 2350
# G = 150 + A
# A = 1175
# G = 1320
