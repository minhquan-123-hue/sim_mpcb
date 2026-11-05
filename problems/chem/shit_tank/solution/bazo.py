"""dung dung dich bazo de can bang luong ion H+ trong dung dich axit"""

# ta co 2 loai bazo de thuc hien giam ion H+ 
# KOH hoac Ba(OH)2

KOH = 0.5 #mol/l
BaOH2 = 171 #g/mol

# phan li 1 nac cua KOH -> K^+ + OH^- , ty le la 1:1:1
# phan li 1 nac cua Ba(OH)2 -> Ba^2+ + 2OH^- , ty le la 1:1:2

# TINH THE TICH CUA KOH DE CAN BANG ION H+ TRONG DUNG DICH AXIT H2SO4
# Vi co 120 mol H+ trong dung dich axit H2SO4, ta can 120 mol OH^- de trung hoa
# Vi 1 mol KOH tao ra 1 mol OH^-, nen can 120 mol KOH de trung hoa 120 mol H+
# The tich KOH can dung = 120 mol / 0.5 mol/l = 240 l

KOH_volume = 120 / KOH # l
print(f"The volume of KOH needed to neutralize the H+ ions in the acid solution is: {KOH_volume} liters")

# TINH KHOI LUONG CUA Ba(OH)2 DE CAN BANG ION H+ TRONG DUNG DICH AXIT
# Vi co 120 mol H+ trong dung dich axit H2SO4, ta can 120 mol OH^- de trung hoa
# Vi 1 mol Ba(OH)2 tao ra 2 mol OH^-, nen can 60 mol Ba(OH)2 de trung hoa 120 mol H+
# Khoi luong Ba(OH)2 can dung = 60 mol * 171 g/mol = 10260 g = 10.26 kg
BAOH2_mass = (120 / 2) * BaOH2 # g
print(f"The mass of Ba(OH)2 needed to neutralize the H+ ions in the acid solution is: {BAOH2_mass} grams or {BAOH2_mass /1000} kilograms")