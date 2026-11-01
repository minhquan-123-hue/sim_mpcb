"""tinh phan chat thai di vao = di ra + phan huy"""

V = 500 #L, day la the tich cua be chua chat thai
q_in = 25 #L/hour
q_out = q_in #L/hour 
C_in = 20 #mg/L, nong do chat thai di vao be chua
k = 0.03 #hour^-1,hang so phan huy

# hieu suat chat thai di ra
# hay con goi la toc do rua troi
# q/V 
toc_do_rua_troi = q_out/V #hour^-1
print("toc do rua troi = ", toc_do_rua_troi, "hour^-1")
# suy giam nong do chat thai trong be chua
# sau khi duoc dua vao be no se tra ve mot phan chat thai di ra va mot phan bi phan huy
# va hieu suat chat thai di ra + hieu suat chat thai bi phan huy = tong hieu suat chat thai bi suy giam
tong_toc_do = toc_do_rua_troi + k
print("tong toc do = ", tong_toc_do, "hour^-1")

#tinh nong do chat thai trong trang thai bi phan huy
#va chay ra ngoai
#qCin = qC + kVC
#qCin = C(q + kV)
#C = qCin/(q + kV)
#C = (qCin / V) / (q + kV) / V
#C = (q/V).Cin / (q/V + k)
C = (toc_do_rua_troi * C_in) / tong_toc_do
print("nong do chat thai trong be chua = ", C, "mg/L")

