"""xác định lượng glucose và o2 mà khi chưa biết số mol atp"""

# câu 1: tính hiệu suất chuyến hóa năng lượng ?
# câu 2: để bóp tống phân cần x ATP mỗi phút
# tính mass glu và vol o2 để cơ thể phân giải trong ti thể
# đáp ứng đủ lượng ATP đó ?

#datas
#phương trình cân bằng: C?H?O? + 6O2 => 6CO2 + 6H20 + 32ATP
# 1mol của glu tạo ra 32 mol atp 
# 6mol của o2 tạo ra 32 mol atp 
# 1mol của glu = 180g
# 1mol của o2 chiếm 22.4 lít
epm_atp = 7.3#kcal
epm_glu = 686#kcal

# câu 1:
E_tong = epm_glu
E_co_ich = 32 * 7.3
hieu_suat = (E_co_ich / E_tong) * 100

# câu 2:
# mol atp gấp mol glu 32 lần
# mol atp gâp mol o2 6 lần
# ta có mol ATP = x
# => mol của glu = x/32
# => mol của o2 = x/6
# glu_mass = 180 * x/32 (tổng khối lượng)
# o2_volume = 22.4 * x/6 (tổng không gian chiếm)

