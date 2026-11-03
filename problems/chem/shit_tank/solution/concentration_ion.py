"""tinh so luong mol cua ion trong dung dich"""

# theo gia thiet thi H2SO4 phan ly 2 nac hoan toan
# sinh ra ty le: 1H2S04 -> 2H^+ + SO4^2-

V = 2500#L
pH = 1.5

# ta biet rang mol cua H^+ = 10^-pH
# tinh so luong mol cua H^+ trong dung dich
# va sau do tinh tong so luong mol cua chung
n_H_plus = 10**(-pH)
print("So luong mol cua H^+ trong 1L dung dich: ", n_H_plus, "mol/L")

tt_n_H_plus = n_H_plus * V
print("So luong mol cua H^+ trong dung dich: ", tt_n_H_plus, "mol")

# theo ty le phan ly thi so luong mol cua SO4^2- = 1/2 * so luong mol cua H^+
tt_n_SO4_2_minus = 0.5 * tt_n_H_plus
print("So luong mol cua SO4^2- trong dung dich: ", tt_n_SO4_2_minus, "mol")
