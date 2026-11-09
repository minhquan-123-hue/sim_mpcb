"""giam luong H^+ de Al^3+ bien thanh dang ran it tan"""

# tính tổng lớp đất canh tác 2ha
# tính tổng điện tích (H^+ và Al^3+) bị keo đất giữ để thay thế bằng Ca^2+
# tính khối lượng vôi CaCO3 đổ vào đất

# dữ liệu mà ta có
S = 20000 #m^2
D = 0.25 #m
density = 1.2 #tons/m^3
CEC = 20#meq/100g đất , Cation exchange capacity
C_CaCO3 = 100#g/mol 

# tổng khối lượng đất
tt_mass = ((S*D) * density) * 1000 * 1000
print(tt_mass / 1000 / 1000,"tons")


# tổng điện tích
tt_charge = 20 * tt_mass / 100
print(tt_charge,"charge +")

# khối lượng vôi phải rắc lên đất
Ca2plus_mol = (tt_charge / 2) / 1000
print(Ca2plus_mol,"mol")

# CaCO3 => Ca^2+ + CO3^-
# ty le la 1:1:1
CaCO3_mass = Ca2plus_mol * C_CaCO3
print(CaCO3_mass / 1000 / 1000,"tons")