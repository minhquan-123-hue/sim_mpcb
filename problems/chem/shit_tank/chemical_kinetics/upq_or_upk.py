"""tang vi khuan xu ly chat thai , hay tang toc do rua troi"""

V = 500#L
q = 25#L/h , qin = qout
C = 20#mg/L
k = 0.03#h^-1

# 0 = qin * Cin - qout * C - k * V * C
# qin * Cin = qout * C + k * V * C
# qin * Cin = C * (qout + k * V)
# C = qin * Cin / (qout + k * V)
# C = (qin / V) * Cin / (qout / V + k)

toc_do_rua_troi = q / V
tong_toc_do = toc_do_rua_troi + k
C = (toc_do_rua_troi * C) / tong_toc_do
print("nong do chat thai trong be chua = ", C, "mg/L")
# Cin = qin * Cin => 25 * 20 = 500
# Cout = qout * C => 25 * 12.5 = 312.5
# Cbe = k * V * C => 0.03 * 500 * 12.5 = 187.5

# tai thiet lap lai chi so khoi luong chat thai
C = 20#mg/L

# neu bay gio tang qout len 50 L/h
q = 50#L/h , qin = qout
toc_do_rua_troi = q / V
print(toc_do_rua_troi)
tong_toc_do = toc_do_rua_troi + k
print(tong_toc_do)
C = (toc_do_rua_troi * C) / tong_toc_do
print("nong do chat thai trong be chua = ", C, "mg/L")
# Cin = qin * Cin => 50 * 20 = 1000
# Cout = qout * C => 50 * 15.4 ~ 770
# Cbe = k * V * C => 0.03 * 500 * 15.4 ~ 231
# ta co the thay khi tang luu luong chay ra , thi chat thai khong duoc xu ly ma chay ra nhieu hon 

# tai thiet lap lai chi so khoi luong chat thai
C = 20#mg/L

q = 25
k = k * 2
toc_do_rua_troi = q / V
tong_toc_do = toc_do_rua_troi + k
C = (toc_do_rua_troi * C) / tong_toc_do
print("nong do chat thai trong be chua = ", C, "mg/L")
# Cin = qin * Cin => 25 * 20 = 500
# Cout = quot * C => 25 * 4.4 = 88
# Cbe = k * V * C => 0.06 * 500 * 20 = 1
# mot lan nua toi van chua biet tai sao ve mat toan hoc toi lai chung minh sai mot lan nua la phan vao != ra + phan huy , nhung ma ta co the thay la sai me het roi

# copilot work
def better():
    V = 500
    Cin = 20

    for q, k in ((25, 0.03), (50, 0.03), (25, 0.06)):
        C = q * Cin / (q + k * V)
        vao = q * Cin
        ra = q * C
        phan_huy = k * V * C
        print(C, vao, ra, phan_huy, ra + phan_huy)
