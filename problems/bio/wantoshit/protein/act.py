"""tính năng lượng cần thiết cho myosin và actin protein quân lính chuyển động hoạt động được"""

# cách chuyển đổi qua lại giữa cal và J
# tính hiệu suất (hao tổn == thành nhiệt)

#datas
atp_in = 0.002
J = 4184 #1kcal = 4184J
kcal_per_atp = 7.3 #kcal/mol
J_per_atp = J * kcal_per_atp 
print(J_per_atp)

# ta có cách tính hiệu suất: in * efficiecy = out
Joule_in =  atp_in * J_per_atp
Joule_out = Joule_in * (40/100)
print(Joule_out)


