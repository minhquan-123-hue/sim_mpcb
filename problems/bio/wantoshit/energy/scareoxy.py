"""tế bào có thể thực hiện chuyển đổi dinh dưỡng theo cả kiểu
hiếu khí và kỵ khí , hoặc có cả loại chuyên biệt từng phương pháp"""

# tính E có ích
# tính Hieu suất
# cần bao nhiêu mol glucose để tạo 32 atp

energy_per_glucose = 686#kcal/mol
atp_created_per_glucose = 2#atp/glucose vì nó là tế bào kỵ khí
energy_per_atp = 7.3#kcal/mol

energy_huu_ich = atp_created_per_glucose * energy_per_atp
print(f"năng lượng hữu ích: {energy_huu_ich}kcal")

hieu_suat = energy_huu_ich / energy_per_glucose
print(f"hiệu suất: {hieu_suat:.2f}%")

# bởi vì 1mol glucose tạo 2mol atp
# để tạo ra 32 atp
glucose_in = 32 / atp_created_per_glucose
print(f"glucose cần nạp vào là: {glucose_in}mol")



