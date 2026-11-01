"""he thong: o trong chiec lon khong co loi ra , chat doc chat thai tu phan huy"""

#remember this: you can't prove everything
#but use the things that proved
#choose it as a axiom

#de tinh duoc su anh huong cua vi phan thoi len su thay doi mol ta co: dC/dt = -k.C 
#-k.C chinh la dao ham ta tinh duoc tu ham so goc Co.e^-kt

#tu giai thich: khi ma ta biet su anh huong cua 1 bien len dau ra
#ta co khoi phuc ham ban dau bang nguyen ham(doi hoi mot so ket noi nhanh toan hoc khac)
#va hien tai chua can hoc voi de chung minh no , va khi khoi phuc ham so ban 
#dau ta se biet "ham do" tinh cai gi

V_be = 2000#m^3 
q = 0#L/s

Co = 50#mg/L
k = 0.02#ngay^-1

e = 2.71828
t = 30#ngay

#de tinh duoc so mol hien sau 30 ngay lien tuc "phan ung"
#ta da co ham so Co.e^-kt

Ct = Co*e**(-k*t)
print("Ct: ",Ct,"mg/L")

tt_C_before = V_be * 1000 * Co
print("tt_C_before: ", tt_C_before,"mg")

print("sau 30 ngay chi con lai")
tt_C_after = V_be * 1000 * Ct
print("tt_C_after: ", tt_C_after,"mg")

