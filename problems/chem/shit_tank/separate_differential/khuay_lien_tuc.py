"""tim luu luong can thiet trong he thong de co duoc luong chat thai trong be phot on dinh"""

from math import log

# q = k_rua_troi . V

V = 400#l
t = 2#hour
k_phan_huy = 0.1#hour^-1
Co = 80#mg/L
Ct = 20#mg/L

K = (log(Ct / Co) / t) * (-1)
print("tong toc do:", K)

k_rua_troi = K - k_phan_huy
print("k_rua_troi: ",k_rua_troi)

q  = k_rua_troi * V
print("luu luong can thiet: ",q,"L/h")
